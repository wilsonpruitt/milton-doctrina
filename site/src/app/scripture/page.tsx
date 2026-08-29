import Link from "next/link";
import { CrossDivider } from "@/components/decorations";
import listing from "@/data/scripture/index.json";

// The scripture index is a top-level destination, not something tucked inside a
// chapter page (PLAN §6.1). For a treatise that argues almost entirely by
// proof-text, "where does Milton use this verse?" is the primary question.
export const metadata = {
  title: "Index of Scripture — De Doctrina Christiana",
};

type Book = {
  key: string;
  slug: string;
  nameEn: string;
  nameLa: string;
  order: number;
  testament: string;
  count: number;
  diverging: number;
};

export default function ScriptureIndexPage() {
  const books = listing.books as Book[];
  const ot = books.filter((b) => b.testament === "OT");
  const nt = books.filter((b) => b.testament !== "OT");

  return (
    <div>
      <h2 className="h2" style={{ fontSize: "22px", marginBottom: "0.25rem" }}>
        Index of Scripture
      </h2>
      <p className="card-meta" style={{ marginBottom: "1rem" }}>
        {listing.total.toLocaleString()} citations across {books.length} books
      </p>

      <CrossDivider />

      <div className="headnote-block">
        <p>
          Milton argues by proof-text, and the treatise is largely a chain of them. Each
          entry below is <strong>one citation</strong>, shown as it is printed in each
          layer.
        </p>
        <p>
          Milton cites the Latin of Junius&ndash;Tremellius; Sumner&rsquo;s English adjusts
          toward the Authorized Version, but not consistently. Where the two number the
          same verse differently &mdash; <strong>{listing.diverging}</strong> times below
          &mdash; both numbers are shown and neither is corrected. That disagreement is
          part of what this edition exists to display, not an error to be tidied away.
        </p>
        <p>
          Where we can say <em>why</em> the two disagree, the entry says so. Milton&rsquo;s
          Bible often divides a chapter at a different verse from the Authorized Version, so
          that both numbers are right; in the Psalms the Hebrew counts the heading as a verse
          of its own. Those divisions have been read off a copy of Junius&ndash;Tremellius
          (Hanau, 1603) &mdash; the Bible Milton was using &mdash; page by page.
        </p>
        <p>
          Many entries say instead that the numbering{" "}
          <em>has not yet been checked</em>. That is meant literally, and it is not a
          suggestion that Milton miscited: it means we have not opened his Bible at that
          chapter. Calling a citation an author&rsquo;s mistake is a claim about a real
          person, and this edition would rather print an honest blank than a confident guess.
        </p>
      </div>

      {[
        { label: "Old Testament", list: ot },
        { label: "New Testament", list: nt },
      ].map((group) =>
        group.list.length === 0 ? null : (
          <div key={group.label} style={{ marginTop: "2rem" }}>
            <div className="section-title" style={{ fontSize: "12px" }}>
              {group.label}
            </div>
            <ul className="question-list" style={{ listStyle: "none", padding: 0 }}>
              {group.list.map((b) => (
                <li key={b.key}>
                  <Link href={`/scripture/${b.slug}`} className="card-link">
                    <div
                      className="card"
                      style={{ display: "flex", alignItems: "baseline", gap: "1rem" }}
                    >
                      <h3 className="card-title" style={{ flex: 1, margin: 0 }}>
                        {b.nameEn}
                      </h3>
                      <span className="card-meta">
                        {b.diverging > 0 && (
                          <span title="citations where the two editions print different numbers">
                            {b.diverging} divergent ·{" "}
                          </span>
                        )}
                        {b.count}
                      </span>
                    </div>
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        )
      )}
    </div>
  );
}
