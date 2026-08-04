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
    for (const chunk of book.chunks) {
      params.push({ book: String(book.id), chapter: String(chunk.chapter) });
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
  const chunk = book.chunks.find((c) => c.chapter === parseInt(chapterParam));
  if (!chunk) return <p>Chapter not found.</p>;

  const idx = book.chunks.findIndex((c) => c.id === chunk.id);
  const prev = idx > 0 ? book.chunks[idx - 1] : null;
  const next = idx < book.chunks.length - 1 ? book.chunks[idx + 1] : null;

  // Prefer the Latin title if present, else whatever title comes first.
  const primaryTitle = chunk.titles["la"] ?? Object.values(chunk.titles)[0] ?? chunk.id;
  const secondaryTitle = Object.entries(chunk.titles).find(([k]) => k !== "la")?.[1];

  return (
    <div>
      <Link href={`/browse/${book.id}`} className="back-link">
        &larr; Back to {book.title}
      </Link>

      <h2 className="h2" style={{ fontSize: "22px", marginBottom: "0.25rem" }}>
        Cap. {chunk.chapter}. {primaryTitle}
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

      {chunk.headnote && (
        <div className="headnote-block">
          {chunk.headnote.split(/\n{2,}/).map((para, i) => (
            <p key={i}>{renderHeadnoteInline(para)}</p>
          ))}
        </div>
      )}

      <TextReader texts={chunk.texts} apparatus={chunk.apparatus} />

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
