import Link from "next/link";
import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

export const metadata = {
  title: "Rights and Reuse — De Doctrina Christiana",
  description:
    "Sumner's 1825 Latin and English are both public domain and free without condition. What is licensed CC BY-NC 4.0 is our encoding, alignment, citation index, and notes.",
};

// The human-readable face of the LICENSE file at the repo root. The two must
// agree; change both or neither.
//
// ⚠ This project differs from the other Wroot Press editions in one way that
// governs this whole page: there is NO fresh translation here. Both layers are
// Sumner 1825 and both are public domain. The only thing claimed is the
// encoding, the apparatus, and the Junius–Tremellius division data. Do not
// carry Bonaventure's "the English translation is licensed" language across —
// here it would be copyfraud.
export default function RightsPage() {
  return (
    <div style={{ maxWidth: "750px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="I" color="#3D1308" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          De Iure Utendi
        </h2>
        <p
          style={{
            fontFamily: "var(--font-cinzel), serif",
            fontSize: "13px",
            letterSpacing: "0.12em",
            color: "#8B6914",
            textTransform: "uppercase",
          }}
        >
          Rights and Reuse
        </p>
      </div>

      <CrossDivider />

      <div className="body-text">
        <p style={{ marginBottom: "1.25rem", fontStyle: "italic" }}>
          The short version: on this site, unusually, both languages are free without
          condition. What is licensed is only the scaffolding we built around them.
        </p>

        <div className="section-title">Both Texts Are Public Domain</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Milton died in 1674. Charles Sumner&rsquo;s edition of the Latin and his English
          translation of it were both published in 1825 and are long out of copyright.
          Transcribing a public-domain text faithfully creates no new copyright in it, and
          nothing here pretends otherwise.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          Most editions of this kind can claim the English, because the English is new. This
          one cannot, because it isn&rsquo;t. Take the Latin. Take Sumner&rsquo;s English.
          Print them, sell them, put them in an app, feed them to a machine. You need
          nothing from us for either one.
        </p>

        <FleuronDivider />

        <div className="section-title">What Is Licensed Is the Edition Around Them</div>
        <p style={{ marginBottom: "1.25rem" }}>
          A scan of two nineteenth-century volumes is not a usable edition, and the distance
          between the two is where all the work in this project went. What is claimed here,
          as a compilation and as original scholarship, is:
        </p>
        <ul style={{ marginBottom: "1.25rem", paddingLeft: "1.5rem" }}>
          <li style={{ marginBottom: "0.75rem" }}>
            <strong>The structure.</strong> The book&#8211;chapter addressing scheme and its
            slugs, the chunking, the paragraph segmentation, and the alignment of each
            English paragraph to its Latin &mdash; which is what makes the two columns
            readable side by side rather than two separate books.
          </li>
          <li style={{ marginBottom: "0.75rem" }}>
            <strong>The citation index.</strong> Every scriptural reference in both layers,
            parsed out of Milton&rsquo;s and Sumner&rsquo;s abbreviations, normalized,
            resolved to a book and verse, and given a stable deep link &mdash; several
            thousand of them, together with the paired records that show where the two
            layers disagree.
          </li>
          <li style={{ marginBottom: "0.75rem" }}>
            <strong>The Junius&ndash;Tremellius division data.</strong> Where a copy of the
            1603 Hanau Bible was opened, which leaf was read, where that Bible divides the
            chapter, and what that division explains &mdash; recorded as evidence, one entry
            at a time. This is not in any edition of Milton, because nobody had needed it in
            this form before.
          </li>
          <li style={{ marginBottom: "0.75rem" }}>
            <strong>The editorial text.</strong> The notes, the headnotes, the explanations
            on the scripture pages, and the prose on this site, including the{" "}
            <Link href="/about">About</Link> page.
          </li>
        </ul>
        <p style={{ marginBottom: "1.25rem" }}>
          All of that is offered to the public under the{" "}
          <a
            href="https://creativecommons.org/licenses/by-nc/4.0/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Creative Commons Attribution&#8209;NonCommercial 4.0 International License
          </a>
          . Lifting the text is free. Lifting our addressing, our alignment, and our index is
          not.
        </p>

        <FleuronDivider />

        <div className="section-title">So, Concretely</div>
        <p style={{ marginBottom: "1.25rem" }}>
          <strong>Yes, freely, and there is no need to ask.</strong> Quote a chapter in a
          sermon or a lecture. Assign a book to a seminar. Cite the citation index in a
          dissertation. Build a study guide you give away. Translate our notes. Correct us
          and publish the correction. Mirror the whole site. Just credit the work, link the
          license, and say if you changed something.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          <strong>Ask first.</strong> Selling <em>our edition</em> &mdash; a print or ebook
          made from these files, a paywalled database, a commercial product with our index or
          alignment inside it. Note again that this does not restrain you from selling
          Milton or Sumner: set the 1825 text yourself and it is yours to do as you like
          with.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          <strong>Asking works.</strong> Permission is given readily, and given free for
          scholarly and ecclesial projects. What the license is for is the case this project
          exists against: the reprint shops that would scrape a corpus like this one and sell
          it back to the people it was made for. Write to{" "}
          <a href="mailto:wilson@wrootlabs.com">wilson@wrootlabs.com</a> and say what you have
          in mind.
        </p>

        <FleuronDivider />

        <div className="section-title">Attribution</div>
        <p style={{ marginBottom: "1.25rem" }}>Anything along these lines will do:</p>
        <blockquote
          style={{
            margin: "1.5rem 0 1.5rem 1.5rem",
            paddingLeft: "1rem",
            borderLeft: "2px solid #8B6914",
            fontStyle: "italic",
          }}
        >
          Parallel edition, citation index, and notes to Milton&rsquo;s{" "}
          <em>De Doctrina Christiana</em> by Wilson Pruitt (Wroot Press), licensed
          CC&nbsp;BY&#8209;NC&nbsp;4.0. Source text: C. R. Sumner&rsquo;s edition and
          translation, Cambridge, 1825, public domain.
        </blockquote>
        <p style={{ marginBottom: "1.25rem" }}>
          This edition is a working draft and should be cited as one. See{" "}
          <Link href="/about">About</Link> for what is finished and what is not.
        </p>

        <p style={{ fontSize: "13px", opacity: 0.75, marginTop: "2.5rem" }}>
          This is a Wroot Press work; Wroot Press is an imprint of Wroot Labs LLC. The
          copyright holder retains all rights and is not bound by this license &mdash; Wroot
          Press publishes print editions drawn from this material, which is part of how the
          work gets paid for. The full legal statement lives in the <code>LICENSE</code> file
          in the project repository.
        </p>
      </div>
    </div>
  );
}
