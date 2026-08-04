# Next session — resume here

**Read first:** **`M3-RUNBOOK.md`** — the per-chapter procedure, the queue, the checks, and the
open suspect-flags. It is written so a session can start work immediately without re-deriving
anything. Behind it: `PLAN.md` (plan of record) · `CONVENTIONS.md` (frozen rules) ·
`STRUCTURE.md` (offsets). Format reference: `chunks/ddc-2-02.md`; partial-chunk reference:
`chunks/ddc-2-01.md`. Site: `site/`.

## State (2026-08-03)

- **M0 ✅** — offsets measured and stable (La `pdf = printed + 16`, En `+56`), extent measured
  (La text 7–536, En text 9–711), 50-chapter crosswalk in `tools/crosswalk-output.txt`.
- **M1 ✅ (Fable)** — pilot chapter II.ii transcribed BOTH layers, every page
  plate-verified (La pp. 395–403, En pp. 537–546), conventions frozen in `CONVENTIONS.md`,
  headnote form frozen (4 slots, ≤200 words), exemplar chunk `ddc-2-02.md` complete with
  citation-divergence table and accidentals log.
- Plates for the pilot are in `raw/plates/` (regenerable; raw/ is gitignored).
- **M2 ✅ (this session, Sonnet)** — `site/` forked from `~/bonaventure-sentences/site/`
  (rsync, not `.git`), fresh `pnpm install`. Language-pair hardcode generalised to a
  string-keyed array throughout (`content.ts`, `build-content.mjs`, `text-reader.tsx`,
  `globals.css`) — no fixed "2 languages" or `la`-as-position-0 assumption anywhere, so this
  is ready to port to Andrewes (Gk·La·En) without redoing the generalisation. New parser
  (`site/scripts/build-content.mjs`) discovers `## <langkey>` h2 sections generically (reserved
  headers: `apparatus-*`, `headnote`, `notes`), handles `{¶N}`/`{¶N–M}` grid + `<!-- p.NNN -->`
  inline, and Milton's `[^sN]: (printed p. NNN, anchored after …)` apparatus format. Route
  scheme simplified to `/browse/[book]/[chapter]` (DDC has no distinctio/articulus/quaestio
  nesting, so Bonaventure's 4-level route was dropped, not force-fit). Pilot chunk `ddc-2-02`
  verified rendering (`pnpm run build` clean; dev server curl-checked for `SAPIENTIA`, `WISDOM`,
  headnote text, apparatus, small-caps CSS, ¶-markers, then killed; `.next`/`out` cleaned up).
  Nothing deployed, no git repo in `site/`.
  **Deferred to M3+:** search is a single flat index (no per-language mode toggle); `/scripture`
  and the citation index absent entirely (M4 scope); headnote renders as raw markdown, not
  parsed into Place/Argument/Pressure-point/Loci fields; `## Notes` (editorial QA) not rendered
  anywhere on-site (internal-only); dropped Bonaventure's `cited-by.tsx`, `distinction-content.tsx`,
  `browse/tome/[tomeId]`, and the footer Stripe support-tier section as inapplicable to DDC's
  flat structure. Home/About/Rights pages are M2 placeholders only — full editorial copy is M5.

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

## M3 IN PROGRESS

- **II.i `De Bonis Operibus` — LATIN DONE, ENGLISH OWED.** `chunks/ddc-2-01.md`,
  `status: la-verified`, `en_status: pending`. All 8 Latin plates (printed 387–394) verified,
  21 ¶¶. Greek `ἀτοπία` (p.388) confirmed at 800 dpi. **English pp. 527–536 deliberately not
  transcribed** — Wilson hit content filtering on that range twice and called it off; that is
  the only reason the chunk is partial, nothing about the Latin is provisional. The chunk's
  `## Notes` carries a numbered "Owed on return" list — read it before resuming, especially
  the footnote-numbering test (II.i must yield exactly notes 3–7, of which 3, 4, 5 are already
  identified). NB the numbering cycles 1–9 — see the rewritten CONVENTIONS §8a.
- Partial chunks are architecturally fine and `build-content.mjs` was confirmed against this
  one (2 chunks from 2 files, no error) — the M2 language-array generalisation earns its keep
  here, since a `la`-only chunk needs no special casing.

## Staged for the next session (2026-08-03)

Mechanical prep done so the expensive session doesn't spend Opus tokens on shell work:

- **`tools/chapters.tsv`** — all 50 chapters, printed page ranges both layers, with a `flag`
  column (`verified` / `ok` / `suspect`). The single source for page ranges from here on;
  `crosswalk-output.txt` is superseded by it.
- **`tools/prep-chapter.sh <book> <ch>`** (or a range) — renders both plate sets at 200 dpi
  plus both pdftotext drafts, and one page PAST the chapter end so the boundary can be
  confirmed. Costs no model tokens. **Already run for II.iii–II.ix** (~55 MB of plates).
- **`tools/audit-chapter-starts.py`** — re-derives every chapter opening from the text layer
  and reconciles against `chapters.tsv`. Guards PLAN §10 risk #1 (alignment drift).
- **`M3-RUNBOOK.md`** — queue, per-chapter procedure, the mandatory checks, open flags.

**Alignment drift is real and was caught here, not late.** The audit found 6 discrepancies
across 50 chapters. One is fixed and plate-confirmed: **the English II.v/II.vi boundary was
wrong by 5 pages** — the crosswalk had II.vi opening at printed 598, but 598 is mid-chapter and
593 is the actual `CHAP. VI. OF ZEAL.` page. That had II.v at 19pp (1.7×) and II.vi at 2pp
(0.33×); corrected they are 14pp and 7pp. Five discrepancies remain flagged `suspect` —
listed in the runbook §7, biggest is **1.28 (La 309 vs 315)**.

**New frozen conventions** from II.i, now in `CONVENTIONS.md` §8a–8d: Sumner's footnote numbers
are a checksum on whether footnotes were missed (**§8a was REWRITTEN 2026-08-03 — the numbers
cycle 1–9, they do not increase indefinitely; see below**) · the 1825's
inconsistency crosses chapters, so never normalise chapter B from chapter A · roman-inside-italic
is Milton's own voice and recurs · partial chunks are legal and have a defined shape.

## M3 — chapters complete

- **II.iii `De Virtutibus ad Dei Cultum pertinentibus` ✅ (2026-08-03, Opus)** — `chunks/ddc-2-03.md`,
  `status: verified`, both layers, all 19 plates read (La 404–412, En 547–556), extent
  plate-confirmed at both ends (blank tails, Cap. IV opens La 413). 34 La ¶¶ → 32 En ¶¶, one
  triple merge en{¶32–34}. Ratio 1.11.
  Three findings that change the standing picture:
  1. **The chapter carries NO Sumner footnotes at all.** The runbook's "II.iii must begin at
     note 10" was an expectation, not a fact — note 10 now falls to the next chapter that
     carries one (II.iv). Ledger: II.i → 3–7 · II.ii → 8, 9 · **II.iii → none**.
  2. **The `Luc. ix. 66` class is not a one-off** — three La citation errors silently corrected
     by Sumner in this chapter alone (2 Reg. vi. 35 → 2 Kings vii. 2 · Isa. xxxi. 2 → iii. 1 ·
     Deut. v. 38 → v. 32), all six readings confirmed at 400 dpi. Expect it per chapter now.
  3. **First plate-confirmed error in the ENGLISH layer** — En p. 554 `departed from Canaan`
     where La has `profectus est Charane` (out of Haran, Gen. 12:4). The correction traffic runs
     both directions; don't assume En is the corrected side.

- **II.iv-a `De Cultu Externo` ✅ (2026-08-03, Opus)** — `chunks/ddc-2-04-a.md`, `status: verified`,
  both layers, La 413–416 / En 557–562, notes 1–5, 15 La ¶¶ → 15 En ¶¶ (first strict 1:1 so far).
  Split made at Milton's lemma seam, which lands on a page boundary in *both* volumes
  independently (La 416/417 `REVERENTER`, En 562/563 `REVERENTLY`).
  **This chapter corrected CONVENTIONS §8a** — see below.

## ⚠ CONVENTIONS §8a was WRONG and has been rewritten (2026-08-03)

The old rule said Sumner's footnote numbers "run continuously through the whole book," implying an
ever-increasing ledger. **They are single-digit and cycle 1–9.** Plate proof, taken before any of
II.iv was transcribed: En p. 565 carries notes ⁷ and ⁸; En p. 566 carries ⁹ and then **¹**, the
wrap falling mid-page and mid-chapter; and II.iv's first note is ¹ on p. 557, exactly as the cycle
predicts after II.ii closed at 9 and II.iii carried none.

Ledger: II.i → 3–7 · II.ii → 8, 9 · II.iii → none · II.iv → 1 … 9, then 1 …

The checksum survives as "next = previous + 1, **wrapping 9 → 1**," but it now carries a stated
blind spot: it can never detect a miss of exactly 9 notes. Under the old rule the p. 566 wrap
would have read as an eight-note gap and sent a session hunting for notes that never existed.

- **II.iv-b ✅ (2026-08-03, Opus)** — `chunks/ddc-2-04-b.md`, `status: verified`, La 417–420 /
  En 563–568: the whole `REVERENTER` lemma (inward affection · voice · alone-or-in-company ·
  vain repetition · posture · dress · place and time). 9 La ¶¶ → 9 En ¶¶, no merges.
  Carries notes **6, 7, 8, 9, 1, 2, 3, 4** — i.e. this is the chunk containing the 9→1 wrap, and
  the p. 566 footnote block that proved it is transcribed in full.
  **Open convention gap raised here:** La p. 417 numbers Milton's seven marks of reverence with
  raised ordinal suffixes (1ᵐ · 2ᵈᵒ · 3ᵗⁱᵒ …). CONVENTIONS §2 defines no superscript markup, so
  they were set inline (`1m.` `2do.`) rather than inventing one. Information-preserving, but
  **settle it explicitly before Book I**, where numbered enumerations will be commoner.

- **II.iv-c ✅ (2026-08-03, Opus)** — `chunks/ddc-2-04-c.md`, `status: verified`, La 420–428 /
  En 568–578. **II.iv is now complete** (parts a+b+c = La 413–428 / En 557–578; both volumes end
  the chapter mid-page with a blank tail and CAP. V opens La 429, re-confirming the 2.5 extent).
  Chapter alignment across all three parts: 57 La ¶¶ → 56 En ¶¶, a single merge in sixteen printed
  pages — far tighter than II.ii (28→25) or II.iii (34→32).
  - **Note ledger:** II.iv carries **1–9, then 1–8** (seventeen notes, one full cycle plus eight).
    **II.v must open at note 9.**
  - **Second ENGLISH-layer error, and diagnosable:** En p. 574 prints `1 Kings xxvii. 29.`
    (confirmed 400 dpi); 1 Kings has 22 chapters. La reads `1 Reg. xxi. 27, 28, 29.` and is right
    (Ahab humbling himself). The compositor collapsed `xxi. 27, 28,` into `xxvii.`
  - **Four more La errors silently corrected by Sumner** (Isa. lix. 12→1,2 · Num. xxiii. 12→8 ·
    Isa. lviii. **56**→5, 6 · `et xxxvi. 37`→v. 36, 37). The `lviii. 56` case is a *dropped comma*,
    not a misread numeral — the exact mirror of the En `xxvii` slip, one such accident per volume.

- **II.v `De Jurejurando et Sorte` — LATIN DONE, ENGLISH OWED (2026-08-03, Opus).**
  `chunks/ddc-2-05.md`, `status: la-verified`, `en_status: pending`. All 11 Latin plates
  (printed 429–439) verified, 34 ¶¶; chapter ends mid-p. 439 with a blank tail and CAP. VI opens
  La 440, re-confirming the 2.6 extent. English pp. 579–592 not begun. The chunk's `## Notes`
  carries a numbered **"Owed on return"** list — read it rather than reconstructing; it already
  records four suspect Latin citations for the English to adjudicate.

## The LATIN volume has footnotes too — RULED 2026-08-04, settled

Wilson ruled: sections are `## apparatus-sumner-en` / `## apparatus-sumner-la`, anchors stay
`[^sN]` / `[^laN]` (CONVENTIONS §5, four existing chunks migrated, build green); and Sumner's
Latin notes are **harvested as we go** into `tools/sumner-interventions.tsv`, feeding PLAN §6.4
at M4 (CONVENTIONS §5a).

**Two obligations now standing:** every chapter's Latin plates get checked for superscripts
(runbook §2 step 3), and **II.i–II.iv need a superscript-only re-check of their Latin plates** —
nobody was looking before II.v. Cheap, but required before Book II is called complete.

Note the ledger's stated limit: it records only what Sumner *admitted*. He normalised silently and
at scale (PLAN §4a), so it is evidence of specific interventions, never a collation.

### Background

**La p. 431 carries a note, numbered ⁵, in the Latin volume.** CONVENTIONS §5 had assumed apparatus was
English-only (*"Sumner's English footnotes …"*) and §1 gives Latin-side notes no home. Falsified.

`ddc-2-05.md` improvises: a `## apparatus-sumner-la` section with an `[^laN]` prefix, leaving
`[^sN]` to the English so the two independent numbering runs can't collide. The build accepts it.
**Provisional — needs your explicit decision before it spreads**, since CONVENTIONS requires rule
changes to be recorded with a date.

**The content is the real issue.** Sumner writes that the manuscript's word order differs from what
he printed, and *ordinem leviter mutavi* — he changed it for grammar. So the 1825 Latin is
demonstrably not the manuscript here. "Verbatim-1825" stays exactly right as a transcription rule
(we print what Sumner printed, and the note is part of that), but any claim that the edition gives
*Milton's* Latin rather than *Sumner's* now has a documented counter-example. He discloses this
one change; nothing tells us it is the only one. **Every chapter from here needs its Latin plates
checked for superscripts too**, which the runbook §3 now says.

## NEXT: M3 — the volume run continues

Work from `M3-RUNBOOK.md`. Book II first, then Book I, saving I.iv–I.vi for last. Opus per chunk.
**Next is II.v's English layer** (pp. 579–592) — start from the "Owed on return" list, and note
that its first English footnote must be **9**. Then `ddc-2-06 De Zelo` (La 440–445 / En 593–599).

Two debts to settle when convenient: II.i's English (pp. 527–536 — Wilson has approved a retry
**in small chunks**, a few pages at a time, so a filter hit doesn't cost a whole large read),
and the six open suspect flags.

## Owed by Wilson

- **GitHub remote** for this repo (protected action) — no backup off this machine yet.
- Domain wiring for milton.wrootpress.com when M5 nears (Cloudflare, DNS-only per house rule).
