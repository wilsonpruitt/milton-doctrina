import Link from "next/link";
import { loadAllContent } from "@/lib/content";
import listing from "@/data/scripture/index.json";
import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

// M5 EDITORIAL COPY. The counts are read from the built corpus, never typed in
// — a hardcoded "17 chapters" goes stale the first time a chunk lands.
export default function HomePage() {
  const books = loadAllContent();
  const totalChapters = books.reduce((n, b) => n + b.chapters.length, 0);
  const citations = (listing.total as number).toLocaleString();

  return (
    <div>
      <div style={{ textAlign: "center", margin: "2rem 0 3rem" }}>
        <Illumination size={80} letter="M" />
        <h2
          style={{
            fontFamily: "var(--font-cinzel-decorative), serif",
            fontSize: "28px",
            color: "#3D1308",
            margin: "1.5rem 0 0.5rem",
            fontWeight: 400,
          }}
        >
          De Doctrina Christiana
        </h2>
        <p
          style={{
            fontFamily: "var(--font-cinzel), serif",
            fontSize: "14px",
            letterSpacing: "0.15em",
            color: "#8B6914",
            textTransform: "uppercase",
          }}
        >
          John Milton &middot; Sumner&rsquo;s Edition of 1825
        </p>
        <CrossDivider />
        <p className="body-text" style={{ maxWidth: "700px", margin: "0 auto", textAlign: "center" }}>
          Milton&rsquo;s systematic theology, unpublished in his lifetime and found in a
          Whitehall cupboard in 1823, set here in parallel &mdash; his Latin beside
          Sumner&rsquo;s English, paragraph for paragraph, with every scriptural citation
          indexed. Both texts are in the public domain and this edition is free.
        </p>
      </div>

      <FleuronDivider />

      <div className="section-title">Browse</div>
      {books.map((book) => (
        <Link key={book.id} href={`/browse/${book.id}`} className="card-link">
          <div className="card">
            <div style={{ display: "flex", alignItems: "flex-start", gap: "1rem" }}>
              <Illumination size={44} letter={String(book.id)} />
              <div>
                <h3 className="card-title">{book.title}</h3>
                <p className="card-meta">
                  {book.chapters.length} chapter{book.chapters.length !== 1 ? "s" : ""} published
                </p>
              </div>
            </div>
          </div>
        </Link>
      ))}

      <FleuronDivider />

      <Link href="/scripture" className="card-link">
        <div className="card">
          <div className="section-title" style={{ marginTop: 0 }}>Index of Scripture</div>
          <p className="body-text" style={{ marginBottom: 0 }}>
            The treatise argues almost entirely by proof-text, so &ldquo;where does Milton use
            this verse?&rdquo; is the question the book is built to answer. {citations}{" "}
            citations, each shown as printed in both layers &mdash; and where the two disagree
            about the number, both stand and the index says why.
          </p>
        </div>
      </Link>

      <div className="card" style={{ cursor: "default", background: "rgba(61,19,8,0.04)" }}>
        <div className="section-title" style={{ marginTop: 0 }}>A Working Draft</div>
        <p className="body-text" style={{ marginBottom: 0 }}>
          {totalChapters} of the fifty chapters are published. Book II is complete; Book I is in
          progress, and its heaviest chapters are scheduled last. What this edition prints,
          what it declines to correct, and why some citations are marked{" "}
          <em>not yet checked</em> are all set out in the{" "}
          <Link href="/about">About</Link> page.
        </p>
      </div>
    </div>
  );
}
