# Next session — resume here

**Read first:** `PLAN.md` (plan of record) · `CONVENTIONS.md` (frozen M1 rules) ·
`STRUCTURE.md` (offsets + crosswalk). Format reference: `chunks/ddc-2-02.md`.

## State (2026-08-03)

- **M0 ✅** — offsets measured and stable (La `pdf = printed + 16`, En `+56`), extent measured
  (La text 7–536, En text 9–711), 50-chapter crosswalk in `tools/crosswalk-output.txt`.
- **M1 ✅ (this session, Fable)** — pilot chapter II.ii transcribed BOTH layers, every page
  plate-verified (La pp. 395–403, En pp. 537–546), conventions frozen in `CONVENTIONS.md`,
  headnote form frozen (4 slots, ≤200 words), exemplar chunk `ddc-2-02.md` complete with
  citation-divergence table and accidentals log.
- Plates for the pilot are in `raw/plates/` (regenerable; raw/ is gitignored).

## The pilot's load-bearing findings (don't relearn)

1. **The two 1825 editions diverge on citation digits** — Junius–Tremellius vs KJV versification,
   applied INCONSISTENTLY by Sumner, plus at least one silent correction of a printed error
   (La `Luc. ix. 66` → En `ix. 62`). Rule frozen: as printed per layer, never harmonized, logged
   per chunk. The scripture index (M4) owns the mapping problem.
2. **pdftotext is a good draft and an unpublishable text** — it loses ALL italics (which carry
   the quote/connective distinction, the heart of the layout), and garbles digits and words
   (`delector`→"detector"). Plate pass per page is mandatory, as expected.
3. **Sumner merges paragraphs** (3 merges in 28 ¶¶) and converts Milton's `Et…` coordination
   into `First/Secondly…` enumeration. The `{¶N}` grid handles it; expect both throughout.
4. **The 1825's own emphasis typography is inconsistent** (some definitions small-caps, some
   not) — follow per instance, both layers mirror each other's inconsistency.

## NEXT: M2 — site skeleton + language-array generalisation

Fork `~/bonaventure-sentences/site/` → `site/`. Generalise the hardcoded language PAIR to an
ARRAY (la / en-sumner / later en-wp) — the pair is baked into ~5–6 files (`build-content.mjs`,
`src/lib/content.ts`, `text-reader.tsx`, `globals.css`, `search-client.tsx` — re-locate, the
line numbers in memory are stale). **This generalisation then ports to Andrewes** (which needs
Gk·La·En) — do it once, here, cleanly. Write a new `build-content.mjs` parser for this chunk
format (frontmatter + `## <lang>` sections + `{¶N}` grid + `[^sN]` apparatus). Render ddc-2-02.
Ship nothing public. Model: Sonnet (engineering against a working reference implementation).

Then **M3** — the volume run, Book II first (II.i, II.iii onward; II.ii done), Opus per chunk.

## Owed by Wilson

- **GitHub remote** for this repo (protected action) — no backup off this machine yet.
- Domain wiring for milton.wrootpress.com when M5 nears (Cloudflare, DNS-only per house rule).
