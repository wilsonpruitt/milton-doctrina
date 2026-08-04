import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import { Illumination, CrossDivider } from "@/components/decorations";

export default function BrowsePage() {
  const books = loadAllContent();

  return (
    <div>
      <div style={{ textAlign: "center", margin: "1.5rem 0 2rem" }}>
        <Illumination size={70} letter="M" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          Browse
        </h2>
      </div>

      <CrossDivider />

      {books.map((book) => (
        <Link key={book.id} href={`/browse/${book.id}`} className="card-link">
          <div className="card">
            <div style={{ display: "flex", alignItems: "flex-start", gap: "1rem" }}>
              <Illumination size={44} letter={String(book.id)} />
              <div>
                <h3 className="card-title">{book.title}</h3>
                <p className="card-meta">
                  {book.chunks.length} chapter{book.chunks.length !== 1 ? "s" : ""} available
                </p>
              </div>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}
