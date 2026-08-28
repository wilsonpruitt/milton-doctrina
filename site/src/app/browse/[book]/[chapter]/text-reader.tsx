"use client";

import { useEffect, useState } from "react";
import type { ApparatusEntry, LangText } from "@/lib/content";

type PageMode = "off" | "margin" | "inline";

const PAGE_MODE_KEY = "milton.pageMode";
const PAGE_MODE_ORDER: PageMode[] = ["off", "margin", "inline"];
const PAGE_MODE_LABEL: Record<PageMode, string> = {
  off: "Page markers: off",
  margin: "Page markers: margin",
  inline: "Page markers: inline",
};

// The reader is a language ARRAY, not a fixed pair. View modes are generated
// dynamically: one per language, plus one N-up "parallel" mode when there is
// more than one language. This is the generalization the whole M2 milestone
// exists to do — do not hardcode "2 languages" or a fixed key order here.
export function TextReader({
  chunkId,
  texts,
  apparatus,
}: {
  chunkId: string;
  texts: LangText[];
  apparatus: ApparatusEntry[];
}) {
  const multi = texts.length > 1;
  const [viewMode, setViewMode] = useState<string>(multi ? "parallel" : texts[0]?.key ?? "parallel");
  const [pageMode, setPageMode] = useState<PageMode>("margin");

  useEffect(() => {
    try {
      const saved = localStorage.getItem(PAGE_MODE_KEY) as PageMode | null;
      if (saved && PAGE_MODE_ORDER.includes(saved)) setPageMode(saved);
    } catch {}
  }, []);

  useEffect(() => {
    try {
      localStorage.setItem(PAGE_MODE_KEY, pageMode);
    } catch {}
  }, [pageMode]);

  const cyclePageMode = () => {
    const idx = PAGE_MODE_ORDER.indexOf(pageMode);
    setPageMode(PAGE_MODE_ORDER[(idx + 1) % PAGE_MODE_ORDER.length]);
  };

  const modes = [
    ...(multi ? [{ key: "parallel", label: "Parallel" }] : []),
    ...texts.map((t) => ({ key: t.key, label: `${t.label} Only` })),
  ];

  const hasApparatus = apparatus.length > 0;

  return (
    <>
      <div className="view-toggle">
        {modes.map((m) => (
          <button
            key={m.key}
            onClick={() => setViewMode(m.key)}
            className={`view-btn ${viewMode === m.key ? "active" : ""}`}
          >
            {m.label}
          </button>
        ))}
        <button
          onClick={cyclePageMode}
          className="view-btn"
          style={{ marginLeft: "auto" }}
          title="Toggle page-break marker display"
        >
          {PAGE_MODE_LABEL[pageMode]}
        </button>
      </div>

      {viewMode === "parallel" ? (
        <div
          className="parallel-grid"
          style={{ ["--lang-count" as string]: texts.length }}
        >
          {texts.map((t) => (
            <TextColumn key={t.key} chunkId={chunkId} lang={t} pageMode={pageMode} />
          ))}
        </div>
      ) : (
        <div style={{ maxWidth: "700px" }}>
          {texts
            .filter((t) => t.key === viewMode)
            .map((t) => (
              <TextColumn key={t.key} chunkId={chunkId} lang={t} pageMode={pageMode} />
            ))}
        </div>
      )}

      {hasApparatus && <ApparatusBlock apparatus={apparatus} langOrder={texts.map((t) => t.key)} />}
    </>
  );
}

function TextColumn({
  chunkId,
  lang,
  pageMode,
}: {
  chunkId: string;
  lang: LangText;
  pageMode: PageMode;
}) {
  return (
    <div>
      <div className="section-title" style={{ fontSize: "12px" }}>
        {lang.label}
      </div>
      <div className="text-column" data-lang={lang.key}>
        {renderBody(lang.body, lang.key, pageMode, chunkId)}
      </div>
      {lang.scholion && (
        <div className="scholion-block">
          <div className="scholion-label">Scholion</div>
          <div className="text-column" data-lang={lang.key}>
            {renderBody(lang.scholion, lang.key, pageMode, chunkId)}
          </div>
        </div>
      )}
    </div>
  );
}

function ApparatusBlock({
  apparatus,
  langOrder,
}: {
  apparatus: ApparatusEntry[];
  langOrder: string[];
}) {
  return (
    <div className="apparatus-block">
      <div className="section-title" style={{ fontSize: "12px" }}>
        Apparatus
      </div>
      <ol className="apparatus-list">
        {apparatus.map((e) => {
          // Render entries in the same order as the discovered languages,
          // falling back to whatever keys the entry actually has.
          const keys = langOrder.filter((k) => e.entries[k]);
          const extra = Object.keys(e.entries).filter((k) => !keys.includes(k));
          return (
            <li key={e.id} id={`fn-${e.id}`} className="apparatus-entry">
              <span className="apparatus-num">{e.id.replace(/^s/, "")}</span>
              {e.anchor && (
                <div className="apparatus-anchor">anchored after {renderInline(e.anchor, "off")}</div>
              )}
              {[...keys, ...extra].map((k) => (
                <div key={k} className="apparatus-text" data-lang={k}>
                  {renderInline(e.entries[k], "off")}
                </div>
              ))}
            </li>
          );
        })}
      </ol>
    </div>
  );
}

// --- Rendering helpers ------------------------------------------------------

function renderBody(
  body: string,
  langKey: string,
  pageMode: PageMode,
  chunkId: string
) {
  if (!body) return null;
  const paragraphs = body.split(/\n{2,}/);
  const nodes: React.ReactNode[] = [];
  paragraphs.forEach((para, i) => {
    const trimmed = para.trim();
    if (!trimmed) return;

    // A paragraph consisting solely of a page-break comment renders as a
    // standalone marker (a page break that falls between paragraphs).
    const pageOnly = trimmed.match(/^<!--\s*p\.(\d+)\s*-->$/);
    if (pageOnly) {
      if (pageMode !== "off") {
        nodes.push(<PageMarker key={`p-${i}`} page={pageOnly[1]} mode={pageMode} standalone />);
      }
      return;
    }

    // Leading {¶N} / {¶N–M} paragraph marker, kept as small muted text.
    const parMatch = trimmed.match(/^\{¶([^}]+)\}\s*([\s\S]*)$/);
    const marker = parMatch ? parMatch[1] : null;
    const rest = parMatch ? parMatch[2] : trimmed;

    // The scripture index deep-links to a paragraph in a given layer. Scope the id by
    // CHUNK: a chapter transcribed in parts restarts {¶N} at 1 in each part, so
    // `la-p1` alone would collide three times on one page (§8d). Matches the
    // `paraAnchor()` in tools/build-index-json.py — change both together.
    const anchorId = marker ? `${chunkId}-${langKey}-p${marker.replace(/[^0-9]+/g, "-")}` : undefined;
    nodes.push(
      <p
        key={i}
        id={anchorId}
        className={`chunk-text lang-${langKey}`}
        style={{ marginBottom: "1rem", scrollMarginTop: "5rem" }}
      >
        {marker && <span className="para-marker">¶{marker}</span>}
        {renderInline(rest, pageMode)}
      </p>
    );
  });
  return nodes;
}

function renderInline(text: string, pageMode: PageMode = "off"): React.ReactNode[] {
  const tokens: React.ReactNode[] = [];
  const regex = /<!--\s*p\.(\d+)\s*-->|\[\^([^\]]+)\]|\*\*([^*]+)\*\*|\*([^*]+)\*/g;
  let lastIndex = 0;
  let m: RegExpExecArray | null;
  let key = 0;
  while ((m = regex.exec(text)) !== null) {
    if (m.index > lastIndex) {
      tokens.push(text.slice(lastIndex, m.index));
    }
    if (m[1] !== undefined) {
      if (pageMode !== "off") {
        tokens.push(<PageMarker key={`pm-${key++}`} page={m[1]} mode={pageMode} />);
      }
    } else if (m[2] !== undefined) {
      const id = m[2];
      tokens.push(
        <sup key={`fn-${key++}`} className="fn-ref">
          <a href={`#fn-${id}`}>{id.replace(/^s/, "")}</a>
        </sup>
      );
    } else if (m[3] !== undefined) {
      // Bold-caps runs render as small caps via CSS, not literal bold —
      // CONVENTIONS.md §2 ("small caps → bold caps" transcription rule).
      tokens.push(
        <span key={`b-${key++}`} className="small-caps">
          {m[3]}
        </span>
      );
    } else if (m[4] !== undefined) {
      tokens.push(<em key={`i-${key++}`}>{m[4]}</em>);
    }
    lastIndex = regex.lastIndex;
  }
  if (lastIndex < text.length) tokens.push(text.slice(lastIndex));
  return tokens;
}

function PageMarker({
  page,
  mode,
  standalone,
}: {
  page: string;
  mode: PageMode;
  standalone?: boolean;
}) {
  const label = `p. ${page}`;
  if (standalone) {
    return <div className={`page-marker page-marker-${mode} page-marker-standalone`}>{label}</div>;
  }
  return <span className={`page-marker page-marker-${mode}`}>{label}</span>;
}
