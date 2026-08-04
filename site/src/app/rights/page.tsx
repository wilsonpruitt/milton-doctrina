import { Illumination, CrossDivider } from "@/components/decorations";

export const metadata = {
  title: "Rights and Reuse",
  description: "Placeholder rights page — M2 site skeleton.",
};

// M2 SITE SKELETON. Do NOT draft real rights language from this file — read
// memory/wroot-press-licensing.md first, per PLAN.md §4. Placeholder only.
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
        <p style={{ marginBottom: "1.25rem" }}>
          Milton De Doctrina Christiana &mdash; site skeleton, M2. Expected shape: Sumner&rsquo;s
          1825 source text is public domain; the encoding, apparatus, headnotes, and any fresh
          translation are licensed CC BY-NC 4.0, matching the house convention used across Wroot
          Press editions.
        </p>
        <p style={{ marginBottom: "1.25rem" }}>
          The real rights statement is written at launch (M5), against the licensing memory, not
          drafted ahead of it.
        </p>
      </div>
    </div>
  );
}
