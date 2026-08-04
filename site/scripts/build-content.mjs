/**
 * Pre-build script: reads Milton *De Doctrina Christiana* chunks from
 * ~/milton-doctrina/chunks/*.md and outputs src/data/content.json, which the
 * Next.js app imports at build time.
 *
 * Milton's chunk format is NOT Bonaventure's. Frontmatter is flat (book,
 * chapter, no distinctio/articulus/quaestio nesting). Language sections are
 * h2 headers named by their language KEY directly (`## la`, `## en-sumner`,
 * later `## en-wp`) rather than fixed `## Latin` / `## English` headers — so
 * language sections are DISCOVERED, not hardcoded. See CONVENTIONS.md §1, §7.
 *
 * MARKUP CHOICE (documented once, applies throughout): paragraph markers
 * (`{¶N}`, `{¶2–3}`) and page-break comments (`<!-- p.NNN -->`) are kept
 * INLINE in the stored body text rather than parsed into structured paragraph
 * objects at build time. The build script stays a pure text-extraction pass;
 * all markup interpretation (bold-caps -> small-caps, italics, footnote
 * links, paragraph/page markers) happens in one shared inline renderer on the
 * client, same precedent as Bonaventure's page-marker handling.
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_DIR = path.resolve(__dirname, "..");
const REPO_ROOT = path.resolve(SITE_DIR, "..");
const CHUNKS_DIR = path.join(REPO_ROOT, "chunks");
const OUT_FILE = path.join(SITE_DIR, "src", "data", "content.json");

// Section names that are NOT language sections, matched case-insensitively
// against a bare h2 heading. Any other h2 is treated as a language-key
// section (`la`, `en-sumner`, `en-wp`, a future `grc`, ...).
const APPARATUS_PREFIX = "apparatus-";
const HEADNOTE_HEADER = "headnote";
const NOTES_HEADER = "notes"; // editorial QA — not parsed/rendered in M2

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!match) return { meta: {}, body: content };
  const meta = {};
  for (const line of match[1].split("\n")) {
    const m = line.match(/^(\w[\w-]*):\s*"?([^"]*)"?\s*$/);
    if (m) meta[m[1]] = m[2];
  }
  return { meta, body: match[2] };
}

// Split the body into an ordered list of { header, raw } sections at each
// top-level `## <header>` line. Header text is captured verbatim (case and
// all); classification happens in the caller.
function splitSections(body) {
  const lines = body.split("\n");
  const sections = [];
  let current = null;
  for (const line of lines) {
    const m = line.match(/^##\s+(\S.*?)\s*$/);
    if (m) {
      if (current) sections.push(current);
      current = { header: m[1], lines: [] };
    } else if (current) {
      current.lines.push(line);
    }
  }
  if (current) sections.push(current);
  return sections.map((s) => ({ header: s.header, raw: s.lines.join("\n") }));
}

function cleanBody(text) {
  return text.replace(/\n{3,}/g, "\n\n").trim();
}

// Title / pages lookups are keyed by langKey with a family fallback, e.g.
// "en-sumner" tries `title_en-sumner` then `title_en`. This is what lets a
// future `en-wp` per-chapter title slot in without changing this function.
function metaLookup(meta, prefix, langKey) {
  const family = langKey.split("-")[0];
  return meta[`${prefix}_${langKey}`] ?? meta[`${prefix}_${family}`] ?? "";
}

// Human-readable panel label for a language KEY (distinct from a chunk's
// per-language chapter TITLE, which comes from title_<key> in frontmatter).
// Known keys get a proper label; anything undiscovered falls back to a
// generic title-cased rendering of the key so a new key never breaks the
// build — it just looks a little plain until this map is extended.
const LANG_LABELS = {
  la: "Latin",
  "en-sumner": "English (Sumner, 1825)",
  "en-wp": "English (Wroot Press)",
};
function langLabel(key) {
  if (LANG_LABELS[key]) return LANG_LABELS[key];
  return key
    .split("-")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
    .join(" ");
}

// Parse a `## apparatus-<suffix>` section into entries. Frozen shape
// (CONVENTIONS.md §5):
//   [^sN]: (printed p. NNN, anchored after <anchor text>) <note body>
// Entries are matched to a discovered language key by substring (the
// "sumner" suffix matches the "en-sumner" language key); if no language key
// contains the suffix, the suffix itself is used as the entries' key so the
// data still round-trips.
function parseApparatusSection(raw, suffix, langKeys) {
  const matchKey = langKeys.find((k) => k.includes(suffix) || suffix.includes(k)) ?? suffix;
  const text = raw + "\n[^__SENTINEL__]:";
  const entries = [];
  const re = /\[\^([^\]]+)\]:\s*([\s\S]*?)(?=\n\[\^[^\]]+\]:)/g;
  let m;
  while ((m = re.exec(text)) !== null) {
    if (m[1] === "__SENTINEL__") break;
    const id = m[1];
    let content = m[2].trim();
    let page, anchor;
    const paren = content.match(
      /^\(printed\s+p\.\s*(\d+)[^,]*,\s*anchored after\s*([\s\S]*?)\)\s*([\s\S]*)$/i
    );
    if (paren) {
      page = paren[1];
      anchor = paren[2].trim();
      content = paren[3].trim();
    }
    entries.push({
      id,
      entries: { [matchKey]: content.replace(/\s+/g, " ").trim() },
      ...(page ? { page } : {}),
      ...(anchor ? { anchor } : {}),
    });
  }
  return entries;
}

function processChunkFile(file) {
  const content = fs.readFileSync(file, "utf-8");
  const { meta, body } = parseFrontmatter(content);
  if (!meta.id) return null;

  const sections = splitSections(body);

  const langSections = sections.filter((s) => {
    const h = s.header.toLowerCase();
    return !h.startsWith(APPARATUS_PREFIX) && h !== HEADNOTE_HEADER && h !== NOTES_HEADER;
  });
  const langKeys = langSections.map((s) => s.header);

  const texts = langSections.map((s) => ({
    key: s.header,
    label: langLabel(s.header),
    body: cleanBody(s.raw),
  }));

  const titles = {};
  const pagesByLang = {};
  for (const key of langKeys) {
    const t = metaLookup(meta, "title", key);
    if (t) titles[key] = t;
    const p = metaLookup(meta, "pages", key);
    if (p) pagesByLang[key] = p;
  }

  const apparatusSections = sections.filter((s) => s.header.toLowerCase().startsWith(APPARATUS_PREFIX));
  let apparatus = [];
  for (const s of apparatusSections) {
    const suffix = s.header.slice(APPARATUS_PREFIX.length).toLowerCase();
    apparatus = apparatus.concat(parseApparatusSection(s.raw, suffix, langKeys));
  }

  const headnoteSection = sections.find((s) => s.header.toLowerCase() === HEADNOTE_HEADER);
  const headnote = headnoteSection ? cleanBody(headnoteSection.raw) : undefined;

  return {
    id: meta.id,
    book: parseInt(meta.book) || 0,
    chapter: parseInt(meta.chapter) || 0,
    titles,
    texts,
    apparatus,
    ...(headnote ? { headnote } : {}),
    ...(Object.keys(pagesByLang).length ? { pagesByLang } : {}),
    ...(meta.status ? { status: meta.status } : {}),
  };
}

// Main
if (!fs.existsSync(CHUNKS_DIR)) {
  console.error(`No chunks dir at ${CHUNKS_DIR}`);
  process.exit(1);
}

const files = fs
  .readdirSync(CHUNKS_DIR)
  .filter((f) => f.endsWith(".md"))
  .map((f) => path.join(CHUNKS_DIR, f));

const chunks = [];
for (const file of files) {
  const chunk = processChunkFile(file);
  if (chunk) chunks.push(chunk);
  else console.warn(`SKIP ${file}: no id in frontmatter`);
}

chunks.sort((a, b) => a.book - b.book || a.chapter - b.chapter || a.id.localeCompare(b.id));

fs.mkdirSync(path.dirname(OUT_FILE), { recursive: true });
fs.writeFileSync(OUT_FILE, JSON.stringify(chunks, null, 0));

console.log(`Built content.json: ${chunks.length} chunk(s) from ${files.length} file(s)`);
