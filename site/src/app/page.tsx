import Link from "next/link";
import { loadAllContent, totalChunkCount } from "@/lib/content";
import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

// M2 SITE SKELETON. This is a placeholder — full editorial home-page copy
// (project pitch, source table, apparatus layers) is M5's job per PLAN.md.
// Goal here is only: don't say "Bonaventure" anywhere, and get the pilot
// chapter reachable.
export default function HomePage() {
  const books = loadAllContent();
  const totalChunks = totalChunkCount();

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
          John Milton &middot; Site Skeleton (M2)
        </p>
        <CrossDivider />
        <p className="body-text" style={{ maxWidth: "700px", margin: "0 auto", textAlign: "center" }}>
          A parallel Latin&ndash;English edition of Milton&rsquo;s systematic theology, from
          Sumner&rsquo;s 1825 <em>editio princeps</em>. This is a development skeleton — only the pilot
          chapter is transcribed. Full editorial copy, the scripture index, and the reading-guide
          apparatus land in later milestones.
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
                  {book.chunks.length} chapter{book.chunks.length !== 1 ? "s" : ""} transcribed
                </p>
              </div>
            </div>
          </div>
        </Link>
      ))}

      <FleuronDivider />

      <div className="card" style={{ cursor: "default", background: "rgba(61,19,8,0.04)" }}>
        <div className="section-title">Status</div>
        <p className="body-text">
          {totalChunks} chapter{totalChunks !== 1 ? "s" : ""} built. Not deployed; local development
          only. See <Link href="/about">About</Link> for the plan.
        </p>
      </div>
    </div>
  );
}
