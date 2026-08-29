import Link from "next/link";
import { Illumination, CrossDivider, FleuronDivider } from "@/components/decorations";

export const metadata = {
  title: "About this Edition — De Doctrina Christiana",
  description:
    "A parallel Latin–English edition of Milton's systematic theology, from Sumner's 1825 editio princeps. What the text is, where it came from, and what this edition does and does not correct.",
};

// M5 EDITORIAL COPY. Every factual claim about the manuscript, its discovery,
// its scribes, and the authorship controversy is checked against Campbell,
// Corns, Hale and Tweedie, *Milton and the Manuscript of De Doctrina
// Christiana* (OUP, 2007) — read, synthesised, cited by author; never quoted
// or closely paraphrased, per PLAN.md §6.3.
export default function AboutPage() {
  return (
    <div style={{ maxWidth: "750px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="D" color="#3D1308" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          De Hoc Opere
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
          About this Edition
        </p>
      </div>

      <CrossDivider />

      <div className="body-text">
        <p style={{ marginBottom: "1.25rem" }}>
          <em>De Doctrina Christiana</em> is John Milton&rsquo;s systematic theology: fifty
          chapters in two books, arguing almost entirely by proof-text, and heterodox in
          ways that would have been dangerous to publish. It was not published in his
          lifetime. It was not published for a hundred and fifty years after his death.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          This site presents it in parallel &mdash; Milton&rsquo;s Latin beside an English
          translation, chapter by chapter, with every scriptural citation indexed and
          resolved. Both columns are drawn from Charles Richard Sumner&rsquo;s edition of
          1825, the <em>editio princeps</em>, which printed the Latin and Sumner&rsquo;s own
          English in the same year. Both are in the public domain.
        </p>

        <FleuronDivider />

        <div className="section-title">A Book Found in a Cupboard</div>
        <p style={{ marginBottom: "1.25rem" }}>
          In November 1823, Robert Lemon the elder, Deputy Keeper of His Majesty&rsquo;s
          State Papers, opened a press &mdash; a large cupboard &mdash; in the Old State
          Paper Office in the Middle Treasury Gallery at Whitehall, and found a manuscript
          treatise bundled together with a collection of Milton&rsquo;s state papers. The
          parcel was addressed to a merchant named Skinner. It had been lying in government
          custody, so far as anyone can reconstruct, since Sir Joseph Williamson placed it
          there around 1677, having pressed Daniel Skinner into surrendering the papers he
          had been trying to get printed in the Low Countries.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          The manuscript is now SP 9/61 at the National Archives. Sumner &mdash; then
          chaplain to George IV, later Bishop of Winchester &mdash; edited and translated
          it, and both volumes appeared at Cambridge in 1825. Milton&rsquo;s early
          biographers had recorded that he wrote a systematic theology and that it was
          unpublished at his death; nobody had seen it.
        </p>

        <div className="section-title">The Manuscript Is Not a Fair Copy</div>
        <p style={{ marginBottom: "1.25rem" }}>
          It matters, for an edition like this one, that SP 9/61 is not a clean authorial
          document. It is a work in progress, in more than one hand. The bulk of it is a
          scribal fair copy by Jeremie Picard, who served as Milton&rsquo;s amanuensis
          between 1658 and 1660; the opening sections are recopied in the hand of Daniel
          Skinner, apparently because they had been revised past the point where a printer
          could use them. The text was kept in separate fascicules, roughly a chapter each,
          with wide left margins &mdash; a working arrangement that let a blind man have one
          chapter at a time read to him and add scriptural material to it. Campbell, Corns,
          Hale and Tweedie reconstruct all of this in detail, and conclude that the treatise
          reached its present state around 1660 and was never made ready for the press.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          So there is no single moment at which Milton signed off on this text, and an
          edition that implied otherwise would be lying about its own foundations.
        </p>

        <div className="section-title">The Authorship Was Challenged, and Answered</div>
        <p style={{ marginBottom: "1.25rem" }}>
          In August 1991, at the Fourth International Milton Symposium in Vancouver, William
          Hunter argued that the attribution of the treatise to Milton was unsafe. The
          manuscript does carry Milton&rsquo;s name, but in a hand that is not clearly
          Skinner&rsquo;s and possibly added later, and Hunter&rsquo;s point was that the
          attribution therefore needed evidence beyond the work&rsquo;s general agreement
          with the rest of Milton. The question dominated Milton studies for the better part
          of two decades.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          It was answered. Thomas Corns convened the research group whose findings are set
          out in Campbell, Corns, Hale and Tweedie&rsquo;s{" "}
          <em>Milton and the Manuscript of De Doctrina Christiana</em> (Oxford, 2007), which
          traces the manuscript&rsquo;s passage from Milton&rsquo;s desk to the cupboard
          almost without a gap, and tests the Latin stylometrically against comparable
          works. Their conclusion is worth stating precisely, because it is more interesting
          than a simple yes. Systematic theology in the seventeenth century was an
          appropriative genre: its authors absorbed their predecessors&rsquo; arguments and
          proof-texts wholesale and made them their own by dissenting at the points that
          mattered. Measured that way, <em>De Doctrina Christiana</em> is at least as much
          Milton&rsquo;s as Wolleb&rsquo;s and Ames&rsquo;s treatises are theirs &mdash; and
          nobody disputes those.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          That is said here once, plainly, and then left alone. It is not relitigated in the
          chapter notes.
        </p>

        <FleuronDivider />

        <div className="section-title">What This Edition Prints</div>
        <p style={{ marginBottom: "1.25rem" }}>
          This is an edition of Sumner 1825, not of the manuscript. The 1825 Latin was set
          directly from SP 9/61, which is a point in its favour; but the transcription has
          been questioned by scholars who have had the manuscript unbound and on a lightbox,
          and this edition has not seen the manuscript at all. Where you need the critical
          text, the place to go is the edition prepared by John Hale and Donald Cullington
          for the Oxford <em>Complete Works of John Milton</em>, which is a fresh
          transcription and a fresh translation. It is in copyright, and it should be bought.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          What this site offers instead is the thing that is free to offer: the 1825 text,
          both languages, aligned paragraph to paragraph, fully searchable, deep-linkable,
          and indexed by scripture. That is not a substitute for Oxford. It is the version
          that can be put in front of anyone, anywhere, at no cost, which is a different
          kind of usefulness.
        </p>

        <div className="section-title">How the Text Is Set</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Each layer is transcribed from the scan of its own 1825 volume &mdash; the Latin
          from the 524-page <em>editio princeps</em>, the English from Sumner&rsquo;s
          separate translation volume &mdash; and each is checked against the page image.
          The two volumes have the same editor, the same year, and the same chapter
          divisions, so alignment is a matter of measurement rather than judgement: the
          offset between scan page and printed page has been anchored independently for each
          volume and holds without drift across the whole run.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          Optical character recognition is used as a finding aid and never as the text of
          record. On these scans it mangles chapter titles, drops others entirely, and is
          least reliable exactly where the citations are densest. Anything doubtful is read
          off the page image, and the printed page governs.
        </p>

        <FleuronDivider />

        <div className="section-title">Milton&rsquo;s Bible, and a Correction We Had to Make</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Milton quotes scripture in Latin from the Junius&ndash;Tremellius Bible, the
          Protestant Latin version that the whole genre used. Sumner&rsquo;s English quotes
          the Authorized Version. The two do not always number the same verse the same way,
          and Sumner converted from one to the other inconsistently. Across the corpus the
          two columns print different numbers for the same citation several hundred times.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          For a long stretch of this project those disagreements were recorded as{" "}
          <em>Milton&rsquo;s errors, silently corrected by Sumner</em>. That was wrong, and
          it was wrong for an embarrassing reason: nobody had opened the Bible Milton was
          actually using. When a copy of Junius&ndash;Tremellius (Hanau, 1603) was finally
          read page by page, chapter division by chapter division, roughly thirty-five of
          those supposed errors turned out to be nothing of the kind. That Bible simply
          divides some chapters at a different verse, so both numbers point at the same
          words and both are right. One chapter alone fell from sixteen alleged errors to
          three.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          Twenty-three of those chapter divisions have now been read off the page images and
          recorded, and the <Link href="/scripture">index of scripture</Link> says, for every
          divergence, which of them it is: a known difference of numbering, an open-ended
          reference that one edition closes, or a case nobody has checked yet. The last of
          those is printed as what it is. A great many citations are marked{" "}
          <em>not yet checked</em>, and that mark means we have not opened his Bible at that
          chapter &mdash; not that Milton got it wrong. Calling a citation an author&rsquo;s
          mistake is a claim about a real person, and this edition would rather print an
          honest blank than a confident guess.
        </p>

        <div className="section-title">What We Do Not Correct</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Each layer is printed as it stands in its own volume. Where the Latin cites one
          verse and the English another, both are shown and neither is adjusted toward the
          other. Where Sumner made a silent editorial decision, it stays, and is noted rather
          than reversed. Obvious scanning damage is repaired; anything that might be a real
          feature of the printed page is flagged and left for someone to settle against the
          image. This is an edition of Sumner, not an improvement on him.
        </p>

        <FleuronDivider />

        <div className="section-title">A Working Draft</div>
        <p style={{ marginBottom: "1.25rem" }}>
          Book II is complete &mdash; all seventeen chapters, on worship and on duty toward
          God and neighbour. Book I, the thirty-three chapters on God, creation, and
          redemption, is under way. It ends with the chapters that carry the treatise&rsquo;s
          reputation, and those are scheduled last, when the conventions are fully settled
          and nothing about the process is still being invented.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          Everything here should be cited as a draft. Corrections are wanted, not merely
          welcomed &mdash; a misread word, a citation resolved to the wrong verse, a
          divergence we have classed wrongly. Write to{" "}
          <a href="mailto:wilson@wrootlabs.com">wilson@wrootlabs.com</a>. It will be fixed,
          and the correction recorded. Terms of reuse are on the{" "}
          <Link href="/rights">rights page</Link>; the short version is that all of it is
          free.
        </p>

        <FleuronDivider />

        <div
          className="card"
          style={{ cursor: "default", background: "rgba(61,19,8,0.04)", textAlign: "center" }}
        >
          <p
            style={{
              fontFamily: "var(--font-cinzel), serif",
              fontSize: "14px",
              color: "#3D1308",
              marginBottom: "0.5rem",
            }}
          >
            Nova et Vetera
          </p>
          <p style={{ fontSize: "13px", color: "#6B4A3A", fontStyle: "italic" }}>
            &ldquo;In this treatise then no novelties of doctrine are taught; but, for the
            sake of assisting the memory, what is dispersed throughout the different parts of
            the Holy Scriptures is conveniently reduced into one compact body as it were, and
            digested under certain heads.&rdquo;
          </p>
          <p style={{ fontSize: "12px", color: "#8B6914", marginTop: "0.5rem" }}>
            &mdash; <em>De Doctrina Christiana</em>, I.i
          </p>
        </div>
      </div>
    </div>
  );
}
