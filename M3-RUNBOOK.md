# M3 runbook — the volume run

**Read `PLAN.md` §5 and `CONVENTIONS.md` once at session start, then work from this file.**
`chunks/ddc-2-02.md` is the format reference. `chunks/ddc-2-01.md` is the reference for a
*partial* chunk.

This file exists so a transcription session spends its tokens on plates, not on rediscovering
procedure. Everything mechanical has been pre-staged.

---

## 0. What is already true (don't re-derive)

- **Offsets, measured at M0, exact:** `la_pdf = la_printed + 16` · `en_pdf = en_printed + 56`.
  Body extents: La printed 7–536, En printed 9–711.
- **`tools/chapters.tsv`** is the chapter → page table for all 50 chapters, with a `flag`
  column. Read the flag before you touch a chapter.
- **`tools/prep-chapter.sh <book> <ch>`** renders both plate sets at 200 dpi and both
  pdftotext drafts. Costs no model tokens. Already run for **II.iii–II.ix**.
- **`tools/audit-chapter-starts.py`** re-derives every chapter opening from the text layer and
  reconciles it against `chapters.tsv`. Already run; results are baked into the flags.
- **The site handles partial chunks.** `site/scripts/build-content.mjs` discovers whatever
  `## <langkey>` sections exist, so a Latin-only chunk builds fine.

## 1. Queue

Order is PLAN §8: **Book II first** (shorter, more regular, builds rhythm), then Book I,
**saving I.iv–I.vi for last** because I.v *De Filio Dei* is 53 Latin pages, the hardest
doctrine, and the chapter everyone will actually read.

| # | chunk | state |
|---|---|---|
| — | `ddc-2-02` | **done** (M1 pilot, Fable) |
| — | `ddc-2-01` | **Latin done, English owed** — see §4 |
| — | `ddc-2-03` | **done** (2026-08-03, Opus) — no Sumner footnotes at all |
| — | `ddc-2-04-a` | **done** (2026-08-03, Opus) — La 413–416 / En 557–562; notes 1–5 |
| — | `ddc-2-04-b` | **done** (2026-08-03, Opus) — La 417–420 / En 563–568, the whole `REVERENTER` lemma; notes 6,7,8,9,**1**,2,3,4 (contains the 9→1 wrap) |
| — | `ddc-2-04-c` | **done** (2026-08-03, Opus) — La 420–428 / En 568–578; notes 5–8. **II.iv complete.** |
| 1 | `ddc-2-05` | **Latin done, English owed** (2026-08-03, Opus) — `status: la-verified`. La 429–439 complete, 34 ¶¶, all 11 plates. En 579–592 not begun; **must open at note 9**. Read the numbered "Owed on return" list in the chunk's `## Notes` rather than reconstructing. **⚠ This chapter proved the Latin volume also carries footnotes — see §9 below.** |
| 2 | `ddc-2-06` | prepped — extents corrected & plate-verified |
| 3 | `ddc-2-07` | prepped |
| 4 | `ddc-2-08` | prepped |
| 5 | `ddc-2-09` | prepped |
| 6+ | `ddc-2-10` … `ddc-2-17` | run `prep-chapter.sh 2 10 2 17` first |
| then | Book I, i–iii and vii–xxxiii | |
| last | `ddc-1-04`, `ddc-1-05`, `ddc-1-06` | see §5 |

## 2. Per-chapter procedure

1. **Check the flag** in `chapters.tsv`. If `suspect`, resolve the boundary off the plate
   *first* and correct the file — do not transcribe against a bad range.
2. **Prep** if not already: `./tools/prep-chapter.sh <book> <ch>`.
3. **Latin layer.** Read every plate in order. The pdftotext draft is a finding aid to speed
   reading; it is never the text. Number paragraphs `{¶1}…{¶N}` in reading order — the Latin
   paragraphing is the reference grid. **Check every Latin page foot for footnotes** (§9) — the
   Latin volume carries apparatus, and its notes are textual: they go in
   `## apparatus-sumner-la` AND in `tools/sumner-interventions.tsv`.
4. **English layer.** Read every plate. Open each paragraph with the La ¶ it renders
   (`{¶4}`, or `{¶2–3}` for Sumner's merges). Coverage must be complete and monotonic.
5. **Run the checks in §3.** All of them.
6. **Write the chunk** in the §7 section order. Log divergences, accidentals, typography and
   alignment in `## Notes`.
7. **Headnote** — 4 slots, ≤200 words, `*Loci: pending M4.*`. Write it only with both layers
   in hand; it is not draftable from the Latin alone.
8. `cd site && node scripts/build-content.mjs` to confirm the chunk parses.
9. Update `next-session-resume.md`.

## 3. The checks — run every chapter, no exceptions

- **Footnote checksum — read the REWRITTEN CONVENTIONS §8a, not your memory of it.** Sumner's
  English note numbers are **single-digit and cycle 1–9**; after 9 the next note is 1. (The old
  rule said "continuously through the book," implying an ever-increasing ledger. Wrong, and
  plate-disproved at En p. 566, where ⁹ and ¹ sit in the same footnote block.)
  Record this chapter's first and last note and every wrap inside it; the first note of chapter
  *N+1* must be one past the last of chapter *N*, **wrapping 9 → 1**. A chapter with zero notes
  passes the number through untouched.
  **Ledger:** II.i → **3–7** (3, 4, 5 identified; 6 and 7 must be in pp. 530–536) · II.ii →
  **8, 9** · II.iii → **none** · II.iv → **1–9, then 1–8**. So **II.v must open at note 9.**
  Blind spot: the cycle is only 9 long, so it can never detect a miss of exactly 9 notes. It is
  not a substitute for reading every plate for superscripts.
- **Also check the LATIN plates for superscripts.** The Latin volume carries apparatus too — see
  §9. Its numbering is independent of the English run.
- **¶ coverage.** Every La ¶ appears exactly once on the En side. Count both sides and record
  the merge list.
- **Page ratio.** En pages ÷ La pages should land ~1.1–1.8. Outside that, suspect a boundary.
- **Citation divergences (§3).** La and En disagree on citation digits systematically and
  irregularly. Transcribe each side as printed, never harmonise, log every divergence.
- **Chapter-boundary confirmation.** `prep-chapter.sh` renders one page past the computed end.
  Look at it: it should be the next chapter's opening or a blank tail. If it's continuous
  text, the extent is wrong.

## 4. The one outstanding debt: II.i English

`chunks/ddc-2-01.md` has a complete, plate-verified Latin layer and **no English**. Printed
pp. 527–536 were set aside on 2026-08-03 because Wilson hit content filtering on that range
twice. Nothing about the Latin is provisional.

The chunk's `## Notes` opens with a numbered **"Owed on return"** list — read it rather than
reconstructing. It already records three Sumner behaviours observed before the stop (the
`(to use a logical expression)` gloss, the two `et` → "or" readings in ¶1, and the dropped
connective `et` before `iv. 8.`), plus the footnote-range test.

**Before retrying, ask Wilson whether that range is workable now.** Don't silently re-attempt
a range he pulled the session off.

## 5. I.iv–I.vi are scheduled last on purpose

PLAN §10 risk #2: I.v *De Filio Dei* is 53 Latin pages, ~14% of Book I on its own, the
anti-Trinitarian chapter, and the one carrying the heaviest apparatus. It is scheduled last so
conventions are fully settled before it is touched, and so it cannot swallow the schedule
early. **It will need splitting** (§7: >12 La pages), at Milton's own lemma seams.

Note also that `1.5`'s English start is currently flagged `suspect` (the audit reads 80, the
crosswalk says 81) — resolve that off the plate before splitting anything.

## 6. Model and burn

- **M3 is Opus per chunk.** Per `feedback_opus-for-authored-prose`, the volume-shaped look of
  the work is not a reason to downgrade; it is authored transcription against a plate.
- Measured so far: II.i's Latin layer (8 plates + 3 crops + ~28 KB written) came in well under
  a full chapter. A *complete* chapter is plausibly ~150K tokens, but that number is still an
  estimate — **the first fully-completed chapter should be used to replace it with a measured
  figure.**
- **A fleet-style batch run needs an explicit big-burn OK from Wilson first** (PLAN §11, and
  the hard-stop rule in CLAUDE.md). Sequential chapters are the default; the 8 GB machine is
  also a reason not to fan out.

## 7. Suspect flags still open

Resolve off the plate before transcribing these; correct `chapters.tsv` and set the flag to
`verified` when you do.

| ch | issue |
|---|---|
| 1.5 | En start: crosswalk 81, text layer 80 |
| 1.12 | La start: crosswalk 187, text layer 188 |
| 1.23 | En (3pp) shorter than La (4pp) — ratio below 1.0 |
| 1.24 | La start: crosswalk 280, text layer 279 |
| 1.28 | La start: crosswalk 309, text layer **315** — a 6-page gap, the largest open discrepancy |
| 2.17 | La start: crosswalk 524, text layer 525 |

Also **not found in the text layer** (heading not detected; may be fine, confirm on the plate
when the chapter comes up): La 2.3, En 2.11, and a handful in Book I.

## 9. The Latin volume has apparatus too — RULED 2026-08-04, no longer open

**Ruling (Wilson):** (1) sections are `## apparatus-sumner-en` and `## apparatus-sumner-la`,
anchors stay `[^sN]` for English and `[^laN]` for Latin — now CONVENTIONS §5, and the four
existing chunks are migrated. (2) Sumner's Latin notes are **harvested as we go** into
`tools/sumner-interventions.tsv`, which feeds PLAN §6.4 at M4 — now CONVENTIONS §5a.

**Two standing obligations that follow:**
- **Read the Latin plates for superscripts, every chapter.** Procedure §2 step 3 now includes it.
- **II.i–II.iv need a superscript-only re-check of their Latin plates.** Nobody was looking before
  II.v, so a Latin note in any of them would have been missed. Cheap (no re-transcription — just
  look at page feet), but it must happen before Book II is called complete.

### Background (found 2026-08-03, II.v)

**La p. 431 carries a footnote, numbered ⁵, in the Latin volume.** CONVENTIONS §5 is written as
though Sumner's notes exist only in the English, and §1 gives Latin-side apparatus no home. That
assumption is plate-falsified.

`chunks/ddc-2-05.md` improvises a fix — a `## apparatus-sumner-la` section with an `[^laN]` anchor
prefix, keeping `[^sN]` reserved for the English so the two independent numbering runs cannot
collide. `build-content.mjs` accepts it (`apparatus-*` is already a reserved header). **This is
provisional and needs Wilson's explicit decision before it spreads to other chunks** — CONVENTIONS
itself requires rule changes to be recorded with a date and a decision.

**The note's content is the bigger issue.** Sumner writes that the manuscript's word order differs
from what he printed, and that *ordinem leviter mutavi* — he silently changed it for grammar. So
the 1825 Latin is demonstrably not the manuscript at this point. "Verbatim-1825" is still exactly
the right transcription rule (we reproduce what Sumner printed, and the note is part of that), but
any claim that the edition gives *Milton's* Latin rather than *Sumner's* now has a documented
counter-example. Watch for further Latin-side notes in every chapter from here on; nothing tells
us this is the only one.
