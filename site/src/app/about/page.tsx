import { Illumination, CrossDivider } from "@/components/decorations";

// M2 SITE SKELETON. Full editorial copy (the manuscript-authorship
// disclosure, the rights framing, the source table) is M5's job per
// PLAN.md §4 and §9 — this is a placeholder so the page exists and links.
export default function AboutPage() {
  return (
    <div style={{ maxWidth: "750px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="M" color="#3D1308" />
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
          About this Project
        </p>
      </div>

      <CrossDivider />

      <div className="body-text">
        <p style={{ marginBottom: "1.25rem" }}>
          Milton De Doctrina Christiana &mdash; site skeleton, M2. A free parallel
          Latin&ndash;English edition of John Milton&rsquo;s systematic theology, drawn from
          C. R. Sumner&rsquo;s 1825 <em>editio princeps</em> of both volumes.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          This page is a placeholder. The full About page &mdash; the manuscript-authorship
          question, Sumner&rsquo;s editorial hand, and how the text is checked &mdash; is written
          at launch (M5), not before the corpus exists.
        </p>
      </div>
    </div>
  );
}
