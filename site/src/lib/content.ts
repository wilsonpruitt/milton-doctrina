import contentData from "@/data/content.json";

// --- Language-array types ----------------------------------------------------
// This is the load-bearing generalization (see PLAN.md §5.3 / CLAUDE.md):
// a chunk carries an ARRAY of language texts, not a fixed Latin/English pair.
// Keys are plain strings ("la", "en-sumner", later "en-wp") so this ports
// cleanly to a 3-language (Greek/Latin/English) reader for Andrewes without
// re-architecting. Never hardcode a language count or a fixed key anywhere
// that consumes this shape.

export type LangKey = string;

export interface LangText {
  key: LangKey;
  label: string; // display label, e.g. "Latin" or "English (Sumner, 1825)"
  body: string;
  scholion?: string;
}

export interface ApparatusEntry {
  id: string;
  entries: Record<LangKey, string>;
  page?: string;
  anchor?: string;
}

export interface Chunk {
  id: string;
  book: number;
  chapter: number;
  titles: Record<LangKey, string>;
  texts: LangText[]; // in frontmatter/discovery order
  apparatus: ApparatusEntry[];
  headnote?: string; // raw markdown, rendered as-is for M2 (structured parse deferred)
  pagesByLang?: Record<LangKey, string>;
  status?: string;
}

// ⚠ A CHAPTER IS NOT A CHUNK. Long chapters are transcribed in parts
// (`ddc-2-04-a/-b/-c`), all carrying the same `chapter` number — CONVENTIONS §8d.
// That convention arrived in M3, after M2 built this site against a one-chunk-per-
// chapter assumption, and every `chunks.find(c => c.chapter === n)` written under the
// old assumption silently returns ONLY THE FIRST PART. Group by chapter and iterate
// the parts; never `.find()` a chapter.
export interface ChapterMeta {
  chapter: number;
  parts: Chunk[];
  titles: Record<LangKey, string>;
}

export interface BookMeta {
  id: number;
  title: string;
  chunks: Chunk[];      // every part, flat — for search, which wants them all
  chapters: ChapterMeta[]; // parts grouped, in order — for browsing and counting
}

// DDC has only 2 books, no distinctio/articulus/quaestio nesting — this is
// deliberately flatter than the Bonaventure Sentences data model.
const BOOK_TITLES: Record<number, string> = {
  1: "Liber I: De Cognitione Dei",
  2: "Liber II: De Dei Cultu",
};

export function loadAllContent(): BookMeta[] {
  const chunks = contentData as Chunk[];
  const bookMap = new Map<number, Chunk[]>();
  for (const c of chunks) {
    if (!bookMap.has(c.book)) bookMap.set(c.book, []);
    bookMap.get(c.book)!.push(c);
  }
  const books: BookMeta[] = [];
  for (const [id, list] of [...bookMap.entries()].sort((a, b) => a[0] - b[0])) {
    list.sort((a, b) => a.chapter - b.chapter || a.id.localeCompare(b.id));
    const byChapter = new Map<number, Chunk[]>();
    for (const c of list) {
      if (!byChapter.has(c.chapter)) byChapter.set(c.chapter, []);
      byChapter.get(c.chapter)!.push(c);
    }
    const chapters: ChapterMeta[] = [...byChapter.entries()]
      .sort((a, b) => a[0] - b[0])
      .map(([chapter, parts]) => ({
        chapter,
        parts,
        // The parts of one chapter share a heading; the first part carries it.
        titles: parts[0].titles,
      }));
    books.push({ id, title: BOOK_TITLES[id] || `Liber ${id}`, chunks: list, chapters });
  }
  return books;
}

/** All parts of a chapter, in order. Empty if the chapter is not transcribed. */
export function findChapter(book: number, chapter: number): ChapterMeta | undefined {
  return loadAllContent().find((x) => x.id === book)
    ?.chapters.find((c) => c.chapter === chapter);
}

export function totalChunkCount(): number {
  return (contentData as Chunk[]).length;
}
