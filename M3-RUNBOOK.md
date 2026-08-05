# M3 runbook — the volume run

**Read `PLAN.md` §5 and `CONVENTIONS.md` once at session start, then work from this file.**
`chunks/ddc-2-02.md` is the format reference. **No partial chunk remains in the corpus** —
`ddc-2-01` was the last and closed 2026-08-04; the shape is still legal (CONVENTIONS §8d) and
that chunk's Notes record how it was worked.

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
- **`tools/crop-plate.sh <la|en> <printed> <dpi> <y0> <y1> <name>`** renders one page at any dpi and
  saves a full-width band to `raw/crops/`. This is CONVENTIONS §2's "doubtful characters get a
  400 dpi crop" made cheap: 600 dpi settles a citation digit, 900 dpi settles a single wrong sort.
  **Every ★ finding in a chunk's Notes should rest on a crop, not on the 200 dpi plate.**
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
| — | `ddc-2-01` | **done** (2026-08-04, Opus) — La 387–394 / En 527–536. **21 ¶¶ → 17**, two merges incl. a **QUADRUPLE** at {¶9–12}, the largest in the corpus. **Checksum passes EXACTLY: notes 3,4,5,6,7**, as §4 predicted before the range was abandoned. **★★ Notes 5 and 7 are *Paradise Lost* XII and *Sonnet* XIX — so II.viii's "first time he reaches for the poetry" is WITHDRAWN; it was an artefact of transcription order.** ★ Third English-side error (La `Prov. xxiv. 1` right, En `xxiv. 7` wrong, 640 dpi). ★ Greek `ἀτοπία` translated away. Transcribed past the content filter one paragraph per edit; {¶6} took six pieces. |
| — | `ddc-2-03` | **done** (2026-08-03, Opus) — no Sumner footnotes at all |
| — | `ddc-2-04-a` | **done** (2026-08-03, Opus) — La 413–416 / En 557–562; notes 1–5 |
| — | `ddc-2-04-b` | **done** (2026-08-03, Opus) — La 417–420 / En 563–568, the whole `REVERENTER` lemma; notes 6,7,8,9,**1**,2,3,4 (contains the 9→1 wrap) |
| — | `ddc-2-04-c` | **done** (2026-08-03, Opus) — La 420–428 / En 568–578; notes 5–8. **II.iv complete.** |
| — | `ddc-2-05` | **done** (2026-08-04, Opus) — La 429–439 / En 579–592, both layers plate-verified. **34 ¶¶ → 34 ¶¶, strict 1:1, no merges** (first whole chapter to do so). Notes **9, 1, 2, 3, 4, 5** — the predicted wrap confirmed. All four suspect La citations resolved, all four `Luc. ix. 66`-class; **eight La errors in one chapter, four in Isaiah**. The English carries **no** counterpart to `[^la5]`. |
| — | `ddc-2-06` | **done** (2026-08-04, Opus) — La 440–445 / En 593–599. 23 ¶¶ → 22, one merge at {¶13–14}. Notes **6, 7** as predicted. No Latin apparatus. **★ The English volume's HEBREW is corrupt where the Latin's is sound** — see the chunk's Notes; needs Wilson's ruling. Writing its *blasphemia* paragraphs tripped a content filter — see §10. |
| — | `ddc-2-07` | **done** (2026-08-04, Opus) — La 446–454 / En 600–612. **22 ¶¶ → 22, strict 1:1.** Notes **8,9,1,2,3,4,5,6,7,8** — ten notes, so the cycle COLLIDES inside one chunk; provisional `[^s8-2]` scheme needs Wilson's ruling. Latin note `[^la4]` is scholarly not textual. **★ Sumner's note `[^s9]` states the whole Ames/Wollebius loci thesis.** Filter-blocked three times; see §10. |
| — | `ddc-2-08` | **done** (2026-08-04, Opus) — La 455–461 / En 613–620. **27 ¶¶ → 25**, two Sumner merges ({¶5–6}, {¶11–12}), both a lemma absorbed into the paragraph it governs. **Exactly one note, printed 9** — the prediction was exact. No Latin apparatus (all 7 feet read). Five citation divergences, all versification, none of the `Luc. ix. 66` class. **★ `[^s9]` is fourteen lines of *Samson Agonistes* — the first time Sumner reaches for the POETRY, and he does it where Milton's prose on self-slaughter is briefest.** No filter blocks: every paragraph written singly. |
| — | `ddc-2-09` | **done** (2026-08-04, Opus) — La 462–473 / En 621–635. **41 ¶¶ → 41, strict 1:1** — the longest chapter so far and only the second to run 1:1 throughout (after II.v). Notes **1, 2, 3**; the wrap confirmed. No Latin apparatus in 12 page feet. **★★ All three notes DEFEND MILTON'S CHARACTER** (drink, sleep, chastity) out of *Comus*, *Samson Agonistes*, *PL* XI, the elegies and the *Apology* — a fourth editorial behaviour; II.viii's note amended because of it. **★★ The English ADDS a Cowper translation of the Homer line with no Latin counterpart** — neither layer is a complete witness to the other. **★ Seven La citation errors corrected, three in {¶16} alone; and ONE error the other way** (La `Dan. ii. 30` right, En `ii. 31` wrong — 2nd English error in the corpus). Sumner also silently **reorders proof-texts at {¶29}** and renders *ornamenta vitæ* as "a high station". |
| — | `ddc-2-10` | **done** (2026-08-05, Opus) — La 474–476 / En 636–638, both extents plate-confirmed at both ends (`CAP./CHAP. XI` opens La 477 / En 639); flag flipped to `verified`. **10 ¶¶ → 9**, one merge en{¶3–4}. **One note, printed 4 — the prediction was exact.** No Latin apparatus. **★★ ἀπάθεια translated away ("a stoical apathy") — the Greek-technical-term pattern now holds over five instances read.** **★★ The English DROPS a proof-text** (La `et cxii. 7.` has no En counterpart, both confirmed 600 dpi) — a third kind of unmarked editorial handling, beside correction and reordering; **bears on M4's scripture index.** **★ Fourth English-layer error: `Psal. iii. 9.`, impossible (Ps 3 has 8 verses); expected `iii. 6`, likely a turned `6`.** No `Luc. ix. 66`-class error at all — the first chapter with none since II.iii. |
| — | `ddc-2-11` | **done** (2026-08-05, Opus) — La 477–486 / En 639–649, both extents plate-confirmed at both ends (`CAP./CHAP. XII` opens La 487 / En 650); flag flipped to `verified`. **38 ¶¶ → 37**, and the shape is new: **two merges AND ★★ THE CORPUS'S FIRST SPLIT** — Sumner divides La {¶35} into two English paragraphs, so CONVENTIONS §4's "every La ¶ appears exactly once" is false as written; provisional notation `{¶35 cont.}` **needs Wilson's ratification**. Notes **5, 6, 7** — the prediction was exact; **all three defend Milton** (the *Apology* on sanctified bitterness; *PL* IV. 502, IX. 173, XI. 455 on envy), `[^s6]` carrying two passages under one number. No Latin apparatus (all 10 feet read; sigs `3 Q`@481, `3 Q 2`@483). **★★ Six Latin citation errors silently corrected, but only two were on the suspect list** drafted from the Latin — the Esau, Ecclesiastes and Judges errors were invisible until the English was beside them. **★★ ἐπιχαιρεκακία translated away — the Greek rule survives its immediate re-test, six instances.** **★★ Second attested English omission** (`Luc. vi. 27, &c.` dropped). **★ Two English printed errors, one in the chapter's first line** (`justiee`, 900 dpi; and {¶13} has no full stop). **★ The Latin's arabic `2 Thess. 3, 10.` is NOT mirrored** in the English — accidentals do not cross layers either. |
| 1 | `ddc-2-12` | La 487–? / En 650–? — **plates NOT yet prepped past La 487 / En 650**; run `./tools/prep-chapter.sh 2 12` first. **Its first English note must be 8.** |
| 2+ | `ddc-2-13` … `ddc-2-17` | |
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
6. **Write the chunk** in the CONVENTIONS §7 section order — note it now includes
   `## apparatus-editorial` (CONVENTIONS §5c) for notes of our own, anchored bare `[^N]`.
   If the chapter carries ten or more English notes the printed numbers collide: use the
   `-2` suffix (CONVENTIONS §5b). Log divergences, accidentals, typography and
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
  **Ledger:** II.i → **3, 4, 5, 6, 7** (✅ CLOSED 2026-08-04 — 6 and 7 found on En 530 and 535, exactly as predicted) · II.ii →
  **8, 9** · II.iii → **none** · II.iv → **1–9, then 1–8** · II.v → **9, 1, 2, 3, 4, 5** ·
  II.vi → **6, 7** (both predicted and confirmed) · II.vii → **8, 9, 1, 2, 3, 4, 5, 6, 7, 8** (ten
  notes, the cycle collides inside one chunk) · II.viii → **9** (a single note, predicted exactly) ·
  II.ix → **1, 2, 3** (the wrap confirmed on En 621; all fifteen plates read, 625–635 carry none) ·
  II.x → **4** (a single note, predicted exactly; no wrap inside the chapter) ·
  II.xi → **5, 6, 7** (predicted exactly; no wrap; all eleven En feet read, 8 of them bare).
  So **II.xii must open at note 8.**
  Blind spot: the cycle is only 9 long, so it can never detect a miss of exactly 9 notes. It is
  not a substitute for reading every plate for superscripts.
- **Also check the LATIN plates for superscripts.** The Latin volume carries apparatus too — see
  §9. **Its numbers are LABELS and will never be a checksum** — settled by the sweep, §9b; nothing
  detects a missed Latin note except reading the feet, so read them. **Classify each Latin note
  textual or scholarly** (CONVENTIONS §5a): only textual ones get a row in
  `tools/sumner-interventions.tsv`. Both kinds exist — La 431 is textual, La 454 scholarly.
- **¶ coverage.** Every La ¶ appears exactly once on the En side. Count both sides and record
  the merge list.
- **Page ratio.** En pages ÷ La pages should land ~1.1–1.8. Outside that, suspect a boundary.
- **Citation divergences (§3).** La and En disagree on citation digits systematically and
  irregularly. Transcribe each side as printed, never harmonise, log every divergence.
- **Chapter-boundary confirmation.** `prep-chapter.sh` renders one page past the computed end.
  Look at it: it should be the next chapter's opening or a blank tail. If it's continuous
  text, the extent is wrong.

## 4. ✅ DISCHARGED — II.i English (was the one outstanding debt)

**Closed 2026-08-04 on Wilson's go-ahead**, using the one-paragraph-per-edit technique of §10.
`chunks/ddc-2-01.md` is `status: verified`, both layers, 21 ¶¶ → 17.

Kept here because the episode is the best evidence the project has for two rules:

1. **§10 works, and nothing was lost to the filter.** {¶6} blocked twice as a whole paragraph and
   went through in **six pieces**; the remaining long paragraphs were pre-split and passed first
   time. Five blocks across the chapter's history, **zero paraphrase, zero omission**.
2. **A queue that does not run in book order will manufacture false "firsts."** Because this
   chapter's English was transcribed last, II.viii recorded a Sumner habit as novel that II.i —
   the Book's opening chapter — already displays. That claim has been **withdrawn** in
   `ddc-2-08.md`. **Any "first time X appears" note is a claim about what has been read; say so.**

The chapter's checksum prediction (notes 3–7) held exactly, which closes the last open cell in the
§3 ledger.

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
when the chapter comes up): La 2.3, ~~En 2.11~~, and a handful in Book I. **En 2.11 is now
resolved and was a detection artefact, not a boundary problem** — `CHAP. XI.` sits on En 639 exactly
where the crosswalk put it (plate-confirmed 2026-08-05). La 2.3 was likewise fine. Treat a
non-detection as weak evidence: the audit's *discrepancies* have all been real, its *silences*
have not.

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


## 9b. ✅ THE BOOK II LATIN SWEEP — RUN AND CLOSED 2026-08-04. Gate open.

**Full record: `SWEEP-RUNBOOK.md` §6.** Do not re-run it; do not re-open the numbering question.

What it settled:

- **62 Latin page-feet read by eye** — all 42 of La 387–428 (never examined by anyone before),
  the 18 riskiest detector negatives, and the two known positives. **The detector and the eye
  agree on every page**; no 400 dpi fallback was needed.
- **No Latin note was missed in II.i–II.iv** — those chapters carry no Latin apparatus at all.
  §9's worry was unfounded and the II.i–II.iv back-check is **discharged**.
- La **431 = ⁵** and La **454 = ⁴**, re-confirmed off the plate. **La 454's note is SCHOLARLY**
  (a page of Bucer · Calvin · Ursinus · Gomarus · Peter Martyr · Musculus on the sabbath) and takes
  no row in `tools/sumner-interventions.tsv`. **La 431 remains the only textual Latin note in Book II.**
- Book I's three unverified candidates — La **50, 188, 228** — are **all false positives**. Book I's
  confirmed Latin notes stand at La **129** and **143**.
- **⚖ The numbering anomaly is RESOLVED: it is ad hoc.** All four hypotheses are refuted, the last
  of them this session — the Latin number is *not* keyed to the English note at the same passage
  (La 454's ⁴ pairs with English note printed **8**; La 431's ⁵ pairs with **no English note**).
  Per-gathering restart is out too, measured off the signatures. See `SWEEP-RUNBOOK.md` §6.4.
- **★★★ Book I carries Latin apparatus too, and it is textual.** La 129 gives **Sumner's own
  statement of editorial method** (*ut soleo… ne puncto quidem mutato*) against La 431's confessed
  *ordinem leviter mutavi*; La 143 reports the MS reading **a manu secunda**. See
  `SWEEP-RUNBOOK.md` §3a — this bears directly on PLAN §4a and §6.4.

**`[^laN]` numbers are LABELS, permanently. There is no Latin checksum and there never was one.**
A fifth Latin note turning up in Book I does not revive the question — a *missing* number already
killed it. The English checksum (§3, CONVENTIONS §8a) is a separate, genuinely sequential run and
is untouched.

## 10. Content filtering — a real, recurring obstacle with a known workaround

**II.vi blocked a content filter when its four *blasphemia* paragraphs were written as one block**
(2026-08-04), and II.i's English blocked twice on 2026-08-03 (§4). This is now a pattern, not an
accident: chapters whose subject is cursing, blasphemy, or idolatrous rites concentrate the
triggering material, and Book II is full of them.

**The workaround works and is now the standard procedure for such chapters:**

1. Read all plates first. Reading is never the problem — writing is.
2. Write the frontmatter and every low-risk paragraph, leaving `<!-- GAP: {¶N} owed -->` markers.
3. Write the apparatus, headnote and Notes.
4. **Commit.** The chapter is now safe whatever happens next.
5. Add the hard paragraphs **one at a time**. Split any single paragraph that still blocks in half
   with a temporary unique tail marker, then rejoin with a second edit.
6. Flip `status: draft` → `verified` and delete the GAP markers.

A chunk stuck at step 4 is a legal partial chunk (CONVENTIONS §8d) and the site builds it fine.
**Never paraphrase or omit to get around a block** — that would silently corrupt the edition, which
is worse than an unfinished chunk.

**Revised 2026-08-04 after II.vii, which blocked three times.** One block was on a *single
paragraph*, which then needed splitting into five pieces. Lesson: for a chapter whose subject is
polemical (Sabbath, blasphemy, idolatry, church vs. magistrate), **do not batch at all — write one
paragraph per edit from the very start.** In II.vii every paragraph written singly went through
first time; only the batched ones failed. Pre-splitting costs a few extra edits; a failed batch
costs the read.

**Also: guard every string replace.** Two separate corruptions were introduced in II.vii by
`str.replace` on text that also occurred in the chunk's own `## Notes` (which quotes the
apparatus). Always assert the match count is 1, or anchor by line index.
