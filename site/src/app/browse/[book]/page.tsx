import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import { Illumination, CrossDivider } from "@/components/decorations";

export function generateStaticParams() {
  const books = loadAllContent();
  return books.map((b) => ({ book: String(b.id) }));
}

export default async function BookPage({ params }: { params: Promise<{ book: string }> }) {
  const { book: bookParam } = await params;
  const books = loadAllContent();
  const book = books.find((b) => b.id === parseInt(bookParam));
  if (!book) return <p>Book not found.</p>;

  return (
    <div>
      <Link href="/browse" className="back-link">
        &larr; Back to Browse
      </Link>

      <div style={{ textAlign: "center", margin: "1.5rem 0 2rem" }}>
        <Illumination size={60} letter={String(book.id)} />
        <h2 className="h2" style={{ fontSize: "22px", marginTop: "1rem" }}>
          {book.title}
        </h2>
      </div>

      <CrossDivider />

      {/* One card per CHAPTER. Listing chunks made II.iv appear three times. */}
      {book.chapters.map((ch) => {
        const title =
          ch.titles["la"] ?? Object.values(ch.titles)[0] ?? ch.parts[0].id;
        const status = ch.parts[0].status;
        return (
          <Link key={ch.chapter} href={`/browse/${book.id}/${ch.chapter}`} className="card-link">
            <div className="card">
              <h3 className="card-title">
                Cap. {ch.chapter}. {title}
              </h3>
              {status && (
                <p className="card-meta">
                  {status}
                  {ch.parts.length > 1 && ` · ${ch.parts.length} parts`}
                </p>
              )}
            </div>
          </Link>
        );
      })}
    </div>
  );
}
