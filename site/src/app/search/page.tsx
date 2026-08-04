import { loadAllContent } from "@/lib/content";
import { SearchClient } from "./search-client";

// M2 SIMPLIFICATION: search is "search everything" — one flat index across
// all discovered languages, no per-language mode toggle. The pilot has one
// chunk; a language-aware search UI (mirroring the reader's language array)
// is worth building once there's a corpus to search. See PLAN.md M4 notes.
export default function SearchPage() {
  const books = loadAllContent();

  const searchIndex = books.flatMap((book) =>
    book.chunks.map((chunk) => {
      const title = chunk.titles["la"] ?? Object.values(chunk.titles)[0] ?? chunk.id;
      // First 300 chars of each language, concatenated — keeps the index
      // compact while still surfacing a snippet from any language.
      const preview = chunk.texts.map((t) => t.body.substring(0, 300)).join(" • ");
      return {
        id: chunk.id,
        title,
        bookId: book.id,
        bookTitle: book.title,
        chapter: chunk.chapter,
        preview,
      };
    })
  );

  return <SearchClient searchIndex={searchIndex} />;
}
