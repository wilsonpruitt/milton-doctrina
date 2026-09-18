/**
 * Shared helpers for the open-corpus reading layer (siblings + export).
 * See ~/open-corpus/PLAN.md §3/§4/Appendix E for the contract this implements.
 *
 * Canonical unit here is the CHAPTER PAGE (/browse/<book>/<chapter>), which
 * bundles one or more transcription "parts" sharing that chapter number —
 * mirrors src/lib/content.ts's loadAllContent() grouping exactly, since these
 * scripts run as plain Node and can't import the TS module directly.
 *
 * Sibling URL scheme deviates from the plain `.txt`/`.json` convention used
 * on the other sites: Next's static export already writes a `<slug>.txt` RSC
 * prefetch payload next to every `<slug>.html` page (same issue as
 * bonaventure-sentences), so the plain-text sibling lives at
 * `<slug>.plain.txt` instead. `.json` was free and is unchanged.
 */

const SITE_URL = "https://milton.wrootpress.com";
const AUTHOR = "John Milton";
const LICENSE_SOURCE = "Public Domain Mark 1.0";
const LICENSE_STRUCTURE = "CC BY-NC 4.0";
const SOURCE_EDITION_TITLE = "De Doctrina Christiana (Sumner editio princeps)";
const SOURCE_EDITION_EDITOR = "Charles Richard Sumner";
const SOURCE_EDITION_YEAR = "1825";

const BOOK_TITLES = {
  1: "Liber I: De Cognitione Dei",
  2: "Liber II: De Dei Cultu",
};

/** Group flat chunks by book, then by chapter — mirrors src/lib/content.ts. */
export function groupByBookAndChapter(chunks) {
  const bookMap = new Map();
  for (const c of chunks) {
    if (!bookMap.has(c.book)) bookMap.set(c.book, []);
    bookMap.get(c.book).push(c);
  }
  const books = [];
  for (const [id, list] of [...bookMap.entries()].sort((a, b) => a[0] - b[0])) {
    list.sort((a, b) => a.chapter - b.chapter || a.id.localeCompare(b.id));
    const byChapter = new Map();
    for (const c of list) {
      if (!byChapter.has(c.chapter)) byChapter.set(c.chapter, []);
      byChapter.get(c.chapter).push(c);
    }
    const chapters = [...byChapter.entries()]
      .sort((a, b) => a[0] - b[0])
      .map(([chapter, parts]) => ({ chapter, parts, titles: parts[0].titles }));
    books.push({ id, title: BOOK_TITLES[id] || `Liber ${id}`, chapters });
  }
  return books;
}

export function chapterUrl(bookId, chapter) {
  return `${SITE_URL}/browse/${bookId}/${chapter}`;
}

function partText(part, key) {
  const t = part.texts.find((x) => x && x.key === key);
  return t ? t.body : null;
}

// Strip page-break comments for the plain-text sibling; keep them in the
// JSON's language bodies since they're real pagination information.
export function toPlainText(md) {
  if (!md) return "";
  return md
    .replace(/<!--\s*p\.?\s*[\d-]+\s*-->/gi, "")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

// One record per chapter page, shared by the .json sibling and the bulk export.
export function buildRecord({ book, chapter }) {
  const parts = chapter.parts;
  const primaryTitle = chapter.titles["la"] ?? Object.values(chapter.titles)[0] ?? parts[0].id;
  const secondaryTitle = Object.entries(chapter.titles).find(([k]) => k !== "la")?.[1] ?? null;

  const laBody = parts.map((p) => partText(p, "la")).filter(Boolean).join("\n\n");
  const enBody = parts.map((p) => partText(p, "en-sumner")).filter(Boolean).join("\n\n");

  return {
    id: `${book.id}-${chapter.chapter}`,
    url: chapterUrl(book.id, chapter.chapter),
    site: "milton-doctrina",
    collection: book.title,
    title: primaryTitle,
    title_alt: secondaryTitle ? [secondaryTitle] : [],
    author: AUTHOR,
    languages: ["en", "la"],
    source_edition: {
      title: SOURCE_EDITION_TITLE,
      editor: SOURCE_EDITION_EDITOR,
      year: SOURCE_EDITION_YEAR,
      book: book.id,
      chapter: chapter.chapter,
      pages: parts.map((p) => p.pagesByLang ?? null),
    },
    source_text: laBody || null,
    english: enBody || null,
    apparatus: {
      notes: parts.flatMap((p) => p.apparatus || []),
      headnotes: parts.map((p) => p.headnote || null).filter(Boolean),
    },
    parts: parts.map((p) => ({ id: p.id, status: p.status || null })),
    // A chapter is complete only when every one of its parts is "verified" —
    // ddc-1-10-b is "la-verified" (English transcription in progress), and
    // its truncated English must not be read as the finished chapter.
    status: parts.every((p) => p.status === "verified") ? "verified" : "in_progress",
    provenance: {
      method:
        "Transcription of C. R. Sumner's 1825 edition and translation, verified against the printed plates. No fresh translation — both languages are Sumner's own 1825 text.",
      corrected_against_scan: true,
    },
    license_source: LICENSE_SOURCE,
    license_structure: LICENSE_STRUCTURE,
    generated: new Date().toISOString().slice(0, 10),
  };
}

export function plainTextSibling(record) {
  const statusNote =
    record.status === "verified"
      ? ""
      : "\nNOTE: this chapter's transcription is IN PROGRESS — the English below may be incomplete.\n";
  const lines = [
    record.title,
    `by ${record.author}`,
    `Source text: ${record.license_source}. Structured corpus (addressing, index, notes): ${record.license_structure}, Wroot Press.`,
    record.url,
    statusNote,
    "-".repeat(40),
    "",
    toPlainText(record.english || ""),
  ];
  return lines.filter((l) => l !== "").join("\n");
}

export { SITE_URL, AUTHOR, LICENSE_SOURCE, LICENSE_STRUCTURE };
