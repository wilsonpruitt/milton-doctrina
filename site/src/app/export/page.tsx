import fs from "fs";
import path from "path";
import { Illumination, CrossDivider } from "@/components/decorations";

export const metadata = {
  title: "Bulk Export",
  description:
    "Every chapter of De Doctrina Christiana, Latin and English aligned, as a single downloadable JSONL file — no crawling required.",
};

// Placeholder — the shared `wroot-corpus-export` R2 bucket has not been
// provisioned yet (~/open-corpus/PLAN.md item 8, status log 2026-09-08).
// Update once it exists and re-deploy.
const EXPORT_R2_BASE_URL = "https://pending-r2-bucket.example/milton";

type Manifest = {
  generated: string;
  chapters: number;
  chapters_complete: number;
  chapters_in_progress: number;
  words: number;
  files: { name: string; description: string; size_bytes: number }[];
};

function loadManifest(): Manifest | null {
  try {
    const p = path.join(process.cwd(), "src", "data", "export-manifest.json");
    return JSON.parse(fs.readFileSync(p, "utf-8"));
  } catch {
    return null;
  }
}

function formatBytes(n: number) {
  if (n > 1024 * 1024) return `${(n / (1024 * 1024)).toFixed(1)} MB`;
  if (n > 1024) return `${(n / 1024).toFixed(0)} KB`;
  return `${n} B`;
}

export default function ExportPage() {
  const manifest = loadManifest();

  return (
    <div style={{ maxWidth: "750px", margin: "0 auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Illumination size={70} letter="E" color="#3D1308" />
        <h2 className="h2" style={{ fontSize: "24px", marginTop: "1rem" }}>
          Bulk Export
        </h2>
      </div>

      <CrossDivider />

      <div className="body-text">
        <p style={{ marginBottom: "1.25rem" }}>
          Every chapter of this edition, one JSON object each, Sumner&rsquo;s 1825 Latin and
          English aligned, source-edition citation and licence fields included. This is a
          mirror of the same content served on every page, packaged so a crawl of the whole
          site is not necessary.
        </p>

        {manifest ? (
          <>
            <p style={{ marginBottom: "1.25rem" }}>
              Generated {manifest.generated}. {manifest.chapters} chapters (
              {manifest.chapters_complete} complete, {manifest.chapters_in_progress} in
              progress), ~{manifest.words.toLocaleString()} words of English across the
              complete chapters.
            </p>
            <ul style={{ marginBottom: "1.25rem", paddingLeft: "1.5rem" }}>
              {manifest.files.map((f) => (
                <li key={f.name} style={{ marginBottom: "0.5rem" }}>
                  <a href={`${EXPORT_R2_BASE_URL}/${f.name}`}>{f.name}</a> (
                  {formatBytes(f.size_bytes)}) — {f.description}
                </li>
              ))}
            </ul>
            <p style={{ marginBottom: "1.25rem" }}>
              Every record carries a <code>status</code> field. An in-progress chapter&rsquo;s
              English may be a partial transcription — check <code>status</code> before
              treating it as finished.
            </p>
          </>
        ) : (
          <p style={{ marginBottom: "1.25rem", fontStyle: "italic" }}>
            The export bundle has not been published yet. Check back shortly, or write to{" "}
            <a href="mailto:wilson@wrootlabs.com">wilson@wrootlabs.com</a>.
          </p>
        )}

        <p style={{ marginBottom: "1.25rem" }}>
          Licensed the same as the rest of the site: both 1825 source texts are public
          domain, the structured corpus (addressing, citation index, Junius&ndash;Tremellius
          division data, notes) is CC BY-NC 4.0 with an explicit machine-learning-use
          permission — see <a href="/rights">Rights and Reuse</a>.
        </p>
      </div>
    </div>
  );
}
