import fs from "node:fs";
import path from "node:path";
import Link from "next/link";
import { CrossDivider } from "@/components/decorations";
import listing from "@/data/scripture/index.json";

// Per-book JSON is read from disk at build time rather than imported, so a book page
// carries only its own citations into the bundle. The whole set is ~4 MB.
const DATA_DIR = path.join(process.cwd(), "src", "data", "scripture");

type Witness = {
  layer: string;
  raw: string;
  printed: string;
  anchor: string;
  para: string;
  snippet: string;
};

type Locus = {
  chunk: string;
  url: string;
  bookNum: number;
  chapterNum: number;
  title: string;
  titleEn: string;
  verse: number | null;
  witness: string;
  diverges: boolean;
  divergenceClass: string;
  divergenceWhy: string;
  resolution: string;
  witnesses: Witness[];
};

// Why the two 1825 volumes print different numbers for one verse, in the reader's terms.
// The classes come from `divergence_class` in the ledger, which is computed against the
// Junius–Tremellius chapter divisions read off that Bible's own pages (M4-RUNBOOK §14).
//
// ⚠ `unchecked` says exactly what it means and no more. It is NOT a claim that Milton erred:
// it says we have not yet opened his Bible at that chapter. The edition would rather print
// an honest blank than a confident guess about a man's accuracy.
const DIVERGENCE_NOTE: Record<string, string> = {
  versification:
    "The two editions number this verse differently \u2014 Milton\u2019s Bible divides the chapter at another point, so both numbers are right:",
  "versification-predicted":
    "The two editions number this verse differently \u2014 the Hebrew counts this psalm\u2019s heading as a verse of its own:",
  unchecked:
    "The two editions number this verse differently. Which numbering Milton was following here has not yet been checked:",
  anomaly:
    "The two editions number this verse differently, and not in a way Milton\u2019s Bible accounts for:",
  "open-end":
    "Both editions give the same verse; one leaves the reference open with &c. and the other closes it:",
};

type BookIndex = {
  key: string;
  slug: string;
  nameEn: string;
  nameLa: string;
  count: number;
  diverging: number;
  chapters: { chapter: number; loci: Locus[] }[];
};

const LAYER_LABEL: Record<string, string> = {
  la: "Latin",
  "en-sumner": "English (Sumner, 1825)",
};

export function generateStaticParams() {
  return (listing.books as { slug: string }[]).map((b) => ({ book: b.slug }));
}

function load(slug: string): BookIndex | null {
  const file = path.join(DATA_DIR, `${slug}.json`);
  if (!fs.existsSync(file)) return null;
  return JSON.parse(fs.readFileSync(file, "utf-8")) as BookIndex;
}

export default async function ScriptureBookPage({
  params,
}: {
  params: Promise<{ book: string }>;
}) {
  const { book: slug } = await params;
  const book = load(slug);
  if (!book) return <p>Book not found.</p>;

  return (
    <div>
      <Link href="/scripture" className="back-link">
        &larr; Index of Scripture
      </Link>

      <h2 className="h2" style={{ fontSize: "22px", marginBottom: "0.25rem" }}>
        {book.nameEn}
      </h2>
      <p className="card-meta" style={{ marginBottom: "1rem" }}>
        {book.nameLa} · {book.count} citation{book.count === 1 ? "" : "s"}
        {book.diverging > 0 && <> · {book.diverging} with divergent numbering</>}
      </p>

      <CrossDivider />

      {book.chapters.map((ch) => (
        <div key={ch.chapter} style={{ marginTop: "1.75rem" }}>
          <div className="section-title" style={{ fontSize: "12px" }}>
            Chapter {ch.chapter}
          </div>
          <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
            {ch.loci.map((l, i) => (
              <li
                key={`${l.chunk}-${i}`}
                style={{
                  padding: "0.6rem 0",
                  borderBottom: "1px solid rgba(139,105,20,0.15)",
                }}
              >
                <div style={{ display: "flex", gap: "0.75rem", alignItems: "baseline" }}>
                  <span
                    className="para-marker"
                    style={{ minWidth: "3.5rem", flexShrink: 0 }}
                  >
                    {l.verse === null ? "ch." : `v. ${l.verse}`}
                  </span>
                  <div style={{ flex: 1, minWidth: 0 }}>
                    <Link href={l.url} className="card-title" style={{ fontSize: "14px" }}>
                      Liber {l.bookNum === 1 ? "I" : "II"}, cap. {l.chapterNum}. {l.title}
                    </Link>

                    {/* Where the layers print different numbers for this same verse, both
                        are shown. Neither is corrected — CONVENTIONS §3. */}
                    {l.diverges && (
                      <p
                        className="card-meta"
                        style={{ margin: "0.3rem 0 0", fontStyle: "italic" }}
                        title={l.divergenceWhy || undefined}
                      >
                        {DIVERGENCE_NOTE[l.divergenceClass] ??
                          "The two editions number this verse differently:"}
                      </p>
                    )}

                    {l.witnesses.map((w) => (
                      <p
                        key={w.layer}
                        className="card-meta"
                        style={{ margin: "0.2rem 0 0" }}
                      >
                        <Link href={`${l.url}#${w.anchor}`} className="back-link">
                          {LAYER_LABEL[w.layer] ?? w.layer} {w.para}
                        </Link>{" "}
                        <span className={l.diverges ? "small-caps" : undefined}>
                          {w.raw}
                        </span>
                        {w.snippet && (
                          <span style={{ opacity: 0.75 }}> — {w.snippet}</span>
                        )}
                      </p>
                    ))}
                  </div>
                </div>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
