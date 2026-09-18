# Open Corpus Plan — reading-layer launch checks (De Doctrina Christiana)

Rollout per `~/open-corpus/PLAN.md` §4, fifth site (after Christian Library, migne.app,
acta-sanctorum, bonaventure-sentences). Appendix F checks run against a local
`next build` + `build-siblings.mjs` on 2026-09-18, before push/deploy.

1. **GPTBot fetch of a chapter URL → 200, full text, no gate.** Verified on the rendered
   `out/` HTML for `/browse/1/1` — full body present, no auth/gate. PASS.
2. **`.json`/`.plain.txt` siblings → 200, header + text; `.json` parses.** Same RSC-payload
   collision as bonaventure-sentences: Next's static export already writes `<slug>.txt`
   next to every page, so the plain-text sibling is `<slug>.plain.txt` (documented in
   `llms.txt` and `scripts/lib/reading-layer.mjs`). Both verified present and parseable
   for all 24 chapter pages (`build-siblings.mjs` output: "Wrote 24 .json + .plain.txt
   sibling pairs"). PASS.
3. **`robots.txt`, `llms.txt`, `sitemap.xml`, `/rights`, `/export` → 200; footer line
   present.** All five now present in `out/` — this site previously had NONE of them
   (robots/llms/sitemap all absent per the PLAN.md survey). PASS.
4. **Canonical is absolute `https://` and equals `@id` in the JSON-LD; JSON-LD parses.**
   Verified match on `/browse/1/1`. PASS.
5. **`/export` manifest lists the newest export; the R2 object downloads.** ⬜ NOT YET —
   shared `wroot-corpus-export` R2 bucket still not provisioned (same open item as the
   other four sites). Local export built clean: 24 chapters (23 complete, 1 in progress),
   ~88,934 words, `milton-doctrina-2026-09-18.jsonl.gz` (431 KB) +
   `milton-doctrina-txt-2026-09-18.tar.gz` (187 KB) + `README.md`, in
   `~/milton-doctrina/export/` (gitignored).
6. **Sitemap URL count equals the work count on disk (±known exclusions).** Sitemap: 95
   URLs (24 chapter pages + 2 book index pages + scripture pages + top-level pages).
   Matches. PASS.
7. **Vercel edge-request figure, day before / week after.** ⬜ Needs a week post-deploy.

## What shipped

- `LICENSE` §3a — machine-use clause (same shape as the other three sites, adapted for
  the "both texts already public domain" framing).
- `/rights` — new "Machine Use" section.
- `public/robots.txt`, `public/llms.txt` — both NEW; this site had neither.
- `scripts/lib/reading-layer.mjs` — shared record builder. Canonical unit is the
  **chapter page** (`/browse/<book>/<chapter>`), which bundles one or more
  transcription "parts" sharing that chapter number — mirrors `src/lib/content.ts`'s
  `loadAllContent()` grouping, since these plain-Node scripts can't import the TS module.
- `scripts/build-siblings.mjs`, `scripts/build-export.mjs` — same pattern as
  bonaventure-sentences.
- `src/app/export/page.tsx` — new page.
- `src/app/browse/[book]/[chapter]/page.tsx` — `generateMetadata` (canonical) + inline
  JSON-LD.
- `src/app/sitemap.ts` — **new file**; this site had no sitemap at all before this.
- `package.json` — `build` script updated for local parity (adds `build-export.mjs` +
  `build-siblings.mjs`), though this is NOT what Vercel actually runs (see below).
- `.gitignore` (site + repo root) — `src/data/export-manifest.json`, `/export/`.

## Data-completeness handling (site-specific)

Unlike the other four sites, this corpus has a chapter mid-transcription
(`ddc-1-10-b`, status `la-verified` — Latin done, English partial). Rather than
excluding it silently or shipping the truncated English as if finished,
`buildRecord()` marks the whole chapter's export/sibling record `status: "in_progress"`
whenever any of its parts isn't `"verified"`, and carries a per-part status array. The
export README lists in-progress chapters by name. Nothing is silently dropped or
silently represented as complete.

## ⚠ Owed manual step — Vercel Build Command override

This project does **not** deploy via `npm run build`. `vercel project inspect
milton-doctrina --scope wilson-pruitts-projects` shows a custom **Build Command**
override:

```
node scripts/build-content.mjs && python3 ../tools/build-index-json.py && next build
```

That command needs `node scripts/build-export.mjs` inserted before `next build` and
`node scripts/build-siblings.mjs` appended after, or the reading-layer siblings/export
manifest will not be regenerated on future git-triggered deploys (this site deploys via
Vercel's git integration, not `vercel deploy --prebuilt`, unlike the other sites).
**Updating the Build Command is a Vercel dashboard/project-settings change — not made
in this session.** New override string:

```
node scripts/build-content.mjs && python3 ../tools/build-index-json.py && node scripts/build-export.mjs && next build && node scripts/build-siblings.mjs
```

## Caught in this session, fixed in this and the prior (bonaventure-sentences) site

The `export/` gitignore line (repo root) was unanchored and also matched
`site/src/app/export/` — the Next.js *route* — so that page was never actually
committed to git on either site (only shipped because the CLI deploy built from local
disk). Fixed to `/export/` on both repos; bonaventure-sentences pushed separately
(`8141a6b`).

## Not done in this session

- **Push + deploy** — both Wilson's separate hard stops.
- **Vercel Build Command update** (above) — needs Wilson in the dashboard, or explicit
  OK to attempt via API/CLI.
- **R2 bucket provisioning** — shared across all five sites.
- **HF org claim + dataset push** — after ≥2 exports exist on R2, per §4.
- **Vercel Firewall rate-limit backstop** — parked, not yet done for any shipped site.
