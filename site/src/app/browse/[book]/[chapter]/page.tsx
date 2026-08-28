import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import { CrossDivider } from "@/components/decorations";
import { TextReader } from "./text-reader";

// DDC's structure is flat — 2 books, ~50 chapters, no distinctio/articulus/
// quaestio nesting like the Sentences. A simpler two-level route
// (/browse/[book]/[chapter]) is more honest to the source than force-fitting
// Bonaventure's 4-level URL scheme.
export function generateStaticParams() {
  const books = loadAllContent();
  const params: { book: string; chapter: string }[] = [];
  for (const book of books) {
    // Iterate CHAPTERS, not chunks — a chapter transcribed in three parts is one
    // page, and iterating chunks emitted the same param three times (§8d).
    for (const ch of book.chapters) {
      params.push({ book: String(book.id), chapter: String(ch.chapter) });
    }
  }
  return params;
}

export default async function ChapterPage({
  params,
}: {
  params: Promise<{ book: string; chapter: string }>;
}) {
  const { book: bookParam, chapter: chapterParam } = await params;
  const books = loadAllContent();
  const book = books.find((b) => b.id === parseInt(bookParam));
  if (!book) return <p>Book not found.</p>;
  const chapter = book.chapters.find((c) => c.chapter === parseInt(chapterParam));
  if (!chapter) return <p>Chapter not found.</p>;

  // ⚠ Neighbours are computed over CHAPTERS. Over chunks, II.iv's three parts all
  // carry chapter 4, so "next" linked the page to itself.
  const idx = book.chapters.findIndex((c) => c.chapter === chapter.chapter);
  const prev = idx > 0 ? book.chapters[idx - 1] : null;
  const next = idx < book.chapters.length - 1 ? book.chapters[idx + 1] : null;

  // Prefer the Latin title if present, else whatever title comes first.
  const primaryTitle =
    chapter.titles["la"] ?? Object.values(chapter.titles)[0] ?? chapter.parts[0].id;
  const secondaryTitle = Object.entries(chapter.titles).find(([k]) => k !== "la")?.[1];

  return (
    <div>
      <Link href={`/browse/${book.id}`} className="back-link">
        &larr; Back to {book.title}
      </Link>

      <h2 className="h2" style={{ fontSize: "22px", marginBottom: "0.25rem" }}>
        Cap. {chapter.chapter}. {primaryTitle}
      </h2>
      {secondaryTitle && (
        <p
          style={{
            fontSize: "13px",
            color: "#8B6914",
            fontFamily: "var(--font-cinzel), serif",
            letterSpacing: "0.08em",
            marginBottom: "0.5rem",
          }}
        >
          {secondaryTitle}
        </p>
      )}

      <CrossDivider />

      {/* Every part of the chapter, in order. Each keeps its own reader, because each
          restarts its {¶N} numbering at 1 and carries its own apparatus. */}
      {chapter.parts.map((part, i) => (
        <section key={part.id} id={part.id}>
          {chapter.parts.length > 1 && (
            <div className="section-title" style={{ fontSize: "12px", marginTop: i ? "2.5rem" : 0 }}>
              Part {String.fromCharCode(97 + i)}
            </div>
          )}
          {part.headnote && (
            <div className="headnote-block">
              {part.headnote.split(/\n{2,}/).map((para, j) => (
                <p key={j}>{renderHeadnoteInline(para)}</p>
              ))}
            </div>
          )}
          <TextReader chunkId={part.id} texts={part.texts} apparatus={part.apparatus} />
        </section>
      ))}

      {(prev || next) && (
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginTop: "2rem",
            paddingTop: "1rem",
            borderTop: "1px solid rgba(139,105,20,0.2)",
          }}
        >
          {prev ? (
            <Link href={`/browse/${book.id}/${prev.chapter}`} className="back-link">
              &larr; Cap. {prev.chapter}
            </Link>
          ) : (
            <span />
          )}
          {next && (
            <Link href={`/browse/${book.id}/${next.chapter}`} className="back-link">
              Cap. {next.chapter} &rarr;
            </Link>
          )}
        </div>
      )}
    </div>
  );
}

// Headnote is stored as raw markdown (M2 scope decision — structured parse
// deferred). Renders **bold labels** and *italics* as plain React nodes
// (no dangerouslySetInnerHTML) — small, self-contained, no sanitizer needed.
function renderHeadnoteInline(text: string): React.ReactNode[] {
  const tokens: React.ReactNode[] = [];
  const regex = /\*\*([^*]+)\*\*|\*([^*]+)\*/g;
  let lastIndex = 0;
  let m: RegExpExecArray | null;
  let key = 0;
  while ((m = regex.exec(text)) !== null) {
    if (m.index > lastIndex) tokens.push(text.slice(lastIndex, m.index));
    if (m[1] !== undefined) tokens.push(<strong key={key++}>{m[1]}</strong>);
    else if (m[2] !== undefined) tokens.push(<em key={key++}>{m[2]}</em>);
    lastIndex = regex.lastIndex;
  }
  if (lastIndex < text.length) tokens.push(text.slice(lastIndex));
  return tokens;
}
