/**
 * Bulk export: aggregates every chapter into one JSONL file, both languages
 * inline, plus a manifest and README. Builds locally into export/ at the
 * repo root (not the site/ deploy root) — hosting is the shared Cloudflare
 * R2 bucket `wroot-corpus-export`, prefix `milton/`, per
 * ~/open-corpus/PLAN.md item 8. Not wired to R2 yet — see status log.
 *
 * Run: node scripts/build-export.mjs
 */

import fs from "fs";
import path from "path";
import zlib from "zlib";
import { fileURLToPath } from "url";
import { groupByBookAndChapter, buildRecord, toPlainText } from "./lib/reading-layer.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_DIR = path.resolve(__dirname, "..");
const REPO_ROOT = path.resolve(SITE_DIR, "..");
const CONTENT_FILE = path.join(SITE_DIR, "src", "data", "content.json");
const EXPORT_DIR = path.join(REPO_ROOT, "export");

const chunks = JSON.parse(fs.readFileSync(CONTENT_FILE, "utf-8"));
const books = groupByBookAndChapter(chunks);
const today = new Date().toISOString().slice(0, 10);

const records = [];
for (const book of books) {
  for (const chapter of book.chapters) {
    records.push(buildRecord({ book, chapter }));
  }
}

const complete = records.filter((r) => r.status === "verified");
const inProgress = records.filter((r) => r.status !== "verified");

fs.mkdirSync(EXPORT_DIR, { recursive: true });

// jsonl.gz — one JSON object per chapter, full text inline. In-progress
// chapters are INCLUDED (their status field says so) rather than silently
// dropped — disclosed in the manifest and README, not omitted.
const jsonlName = `milton-doctrina-${today}.jsonl.gz`;
const jsonlLines = records.map((r) => JSON.stringify(r)).join("\n") + "\n";
const jsonlGz = zlib.gzipSync(Buffer.from(jsonlLines, "utf-8"));
fs.writeFileSync(path.join(EXPORT_DIR, jsonlName), jsonlGz);

// Plain-text mirror, one file per chapter, tarred.
const txtDir = path.join(EXPORT_DIR, "_txt-staging");
fs.rmSync(txtDir, { recursive: true, force: true });
fs.mkdirSync(txtDir, { recursive: true });
for (const r of records) {
  const header = [
    r.title,
    `by ${r.author}`,
    `Source text: ${r.license_source}. Structured corpus (addressing, index, notes): ${r.license_structure}, Wroot Press.`,
    r.url,
    "-".repeat(40),
    "",
  ].join("\n");
  fs.writeFileSync(path.join(txtDir, `${r.id}.txt`), header + toPlainText(r.english || ""));
}

const { execFileSync } = await import("child_process");
const txtTarName = `milton-doctrina-txt-${today}.tar.gz`;
execFileSync("tar", ["-czf", path.join(EXPORT_DIR, txtTarName), "-C", txtDir, "."]);
fs.rmSync(txtDir, { recursive: true, force: true });

// README.md
const totalWords = complete.reduce(
  (s, r) => s + (r.english || "").split(/\s+/).filter(Boolean).length,
  0
);
const readme = `# De Doctrina Christiana — bulk export

Generated ${today}. ${records.length} chapters (${complete.length} complete,
${inProgress.length} in progress), ~${totalWords.toLocaleString()} words of
English across the complete chapters.

## Files

- \`${jsonlName}\` — one JSON object per chapter, full English text inline in
  the \`english\` field, the Latin source text in \`source_text\`, apparatus
  notes, source-edition citation, license fields. **Every record carries a
  \`status\` field** (\`verified\` or \`in_progress\`) and a per-part status
  breakdown — an in-progress chapter's English may be a partial
  transcription; check \`status\` before treating it as finished.
- \`${txtTarName}\` — plain-text mirror of each chapter as \`<id>.txt\`
  (English only, headered), one file per chapter inside the archive.

## In-progress chapters (disclosed, not dropped)

${inProgress.length ? inProgress.map((r) => `- ${r.id}: ${r.title}`).join("\n") : "(none)"}

## License

**The source text.** Both C. R. Sumner's 1825 Latin edition and his own
English translation of it are public domain — no claim is made over either,
and this has never required permission.

**The structured corpus** (addressing, paragraph alignment, citation index,
Junius-Tremellius division data, notes) is
[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), attribution
"milton.wrootpress.com (Wilson Pruitt, Wroot Press)". Full terms:
https://milton.wrootpress.com/rights — including the explicit
machine-learning-use permission (§3a of LICENSE), which covers commercial
model training.

## Hosting

Served from the shared Cloudflare R2 bucket \`wroot-corpus-export\`
(prefix \`milton/\`), not baked into any deploy — see
\`~/open-corpus/PLAN.md\` item 8.
`;
fs.writeFileSync(path.join(EXPORT_DIR, "README.md"), readme);

// manifest.json
const manifest = {
  generated: today,
  chapters: records.length,
  chapters_complete: complete.length,
  chapters_in_progress: inProgress.length,
  words: totalWords,
  files: [
    {
      name: jsonlName,
      description: "One JSON object per chapter, full text inline, status field per record.",
      size_bytes: fs.statSync(path.join(EXPORT_DIR, jsonlName)).size,
    },
    {
      name: txtTarName,
      description: "Plain-text mirror of each chapter, one file per chapter inside the archive.",
      size_bytes: fs.statSync(path.join(EXPORT_DIR, txtTarName)).size,
    },
    {
      name: "README.md",
      description: "Schema, license, and changelog.",
      size_bytes: fs.statSync(path.join(EXPORT_DIR, "README.md")).size,
    },
  ],
};
fs.writeFileSync(path.join(EXPORT_DIR, "manifest.json"), JSON.stringify(manifest, null, 2));

// Copy for the /export page to import at Next build time (same reason
// content.json is pre-built — see build-content.mjs).
fs.writeFileSync(
  path.join(SITE_DIR, "src", "data", "export-manifest.json"),
  JSON.stringify(manifest, null, 2)
);

console.log(
  `Built export: ${records.length} chapters (${complete.length} complete, ${inProgress.length} in progress), ~${totalWords.toLocaleString()} words -> ${EXPORT_DIR}`
);
