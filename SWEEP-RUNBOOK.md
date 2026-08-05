# The Book II Latin footnote sweep — runbook

## ✅ THE SWEEP IS RUN AND CLOSED — 2026-08-04 (Opus)

**All four exit criteria in §4 are met. Book II's Latin apparatus is complete for chapters i–ix.**
The record of what was actually read, and the one judgement, are in **§6 at the foot of this file**.
Everything above §6 is preserved as the procedure that was followed — read §6 first.

---

**Read this file and nothing else to run the sweep.** Background is in `M3-RUNBOOK.md` §9, §9b;
the rules are `CONVENTIONS.md` §5, §5a. Everything mechanical is already done — the sweep session
should spend its tokens on plates and on one judgement, not on setup.

**Why this exists.** Nobody read the Latin page feet before II.v, so a Latin note anywhere in
II.i–II.iv would have been missed entirely. And the two Latin notes we *do* have are numbered
**5** (La 431) and **4** (La 454) — decreasing, in reading order, which no running sequence
explains. **This sweep is a gate: Book II cannot be called complete until it has run.**

---

## 0. What the mechanical pass already established (2026-08-04)

`tools/detect-footnotes.py` measures line pitch on every page and flags pages carrying type set
smaller than the body. The 1825 Latin volume separates a note from the text by **nothing but a gap
and a smaller fount** — there is no rule — so pitch is the whole signal. Body text sits at pitch
33 (at 150 dpi); note text sits at 26.

It was validated against both known positives before being trusted: **La 431 and La 454 are both
flagged, and their immediate neighbours are all clean.**

**Result over La 387–473 (all Book II Latin transcribed so far, 87 pages): exactly TWO candidates,
La 431 and La 454 — the two already known.** Full table: `tools/sweep-candidates.tsv`.

Two consequences, and the second is the interesting one:

1. **No Latin note was missed in II.i–II.iv.** The §9 worry looks unfounded — *pending the visual
   confirmation in §2 below*, which is the part a detector cannot do for you.
2. **The numbering anomaly is NOT explained by missed notes.** The leading hypothesis was that
   seven notes (6,7,8,9,1,2,3) lay unread in La 432–453. There are none. So the "5 then 4"
   sequence has some other cause, and **it cannot be settled from Book II alone** — which is why
   §3 exists.

---

## 1. What the detector is and is NOT

**It is a pre-filter that ranks pages. It is not the sweep and it does not license skipping a
page.** A false negative here would defeat the entire purpose of the exercise, which exists
*precisely because nobody was looking*. Two independent methods, then reconcile — the same
corroboration discipline used everywhere else in this project.

Its known blind spots, stated plainly:

- A note of **one line** set at body pitch would not register. (Neither known note is like this,
  but nothing rules it out.)
- A page whose note runs to the very foot with no gap above it could be missed by the gap rule.
  The `page_is_small` backstop covers the extreme case (La 454) but not every case.
- Marginalia, or a note set beside rather than beneath the text, are invisible to it.

---

## 2. The visual pass — this is the actual sweep

**Render the foot crops** (costs no model tokens; `raw/` is gitignored and regenerable):

```
./tools/sweep-feet.sh 387 428          # II.i–II.iv, the never-checked chapters
```

The crop is the bottom 60% of the page at 200 dpi — validated on La 431, where the superscript
number and the full note text are legible. **Do not tile these into contact sheets.** Stacking
four pages makes an image that downscales past the point where a superscript can be read, and the
superscript is the one thing this sweep exists to record.

**Read, in this order:**

1. **All 42 pages of La 387–428 (II.i–II.iv).** These were never examined by anyone. This is the
   irreducible core of the sweep and it is not delegable to the detector.
2. **The 18 riskiest negatives elsewhere**, which the detector itself identifies:
   - *No large gap found on the page* (so the gap rule never fired) — La **387, 390, 394, 396,
     402, 403, 409, 425, 427, 433, 441, 442, 443, 457, 467, 473**
   - *Exactly one small-pitch line after the gap* (just under the 2-line threshold) — La **389, 421**
3. **La 431 and La 454**, to confirm the two known notes' numbers off the plate rather than off
   the existing chunk files. ✅ *Both already re-confirmed 2026-08-04: 431 = **5**, 454 = **4**.*

Then **reconcile**: any page where your reading and the detector disagree, in either direction,
gets a full-page look at 400 dpi before it is written off.

**On a hit,** follow CONVENTIONS §5a: transcribe the note into the chapter's chunk under
`## apparatus-sumner-la` with a `[^laN]` anchor, and **classify it textual or scholarly** —
only textual notes (Sumner disclosing that he changed what the manuscript reads) earn a row in
`tools/sumner-interventions.tsv`. When in doubt, do not ledger it.

---

## 3. The numbering question — Book I is the decisive test

**Do not guess at this.** The two facts are: La 431 carries note **5**, La 454 carries note **4**,
and there is nothing between them. Hypotheses that are now DEAD:

- ~~Seven notes were missed in La 432–453.~~ Killed by the mechanical pass.
- ~~The numbers restart per chapter.~~ Would make La 431's note **1**, not 5.

Hypotheses still live, and the evidence that would separate them:

| hypothesis | what would confirm it |
|---|---|
| The numbers cycle 1–9 across the **whole Latin volume**, Book I included | Book I carries Latin notes, and the run into La 431 lands on 5 |
| The numbers are keyed to the **English** volume's note at the same place | The English note numbers at the corresponding passages are 5 and 4 |
| They are not a sequence at all — Sumner numbered ad hoc | No consistent pattern emerges from either of the above |

### ✅ Book I HAS been scanned, and it changes the picture — read this before theorising

`tools/detect-footnotes.py 7 386` was run over the whole of Book I (380 pages); results in
`tools/sweep-book1.tsv`. **Book I carries Latin footnotes.** Five candidates:
**La 50, 129, 143, 188, 228.** Two were read off the plate on 2026-08-04 and are unambiguous
(the other three have weaker pitch signatures and may be false positives — check them):

| page | note | kind | content |
|---|---|---|---|
| **129** | **2** | textual | *Locus perdifficilis…* — a desperate crux, plus **Sumner's own statement of editorial method** (see below) and a conjectural emendation |
| **143** | **6** | textual | *Sic in MS. sed a manu secunda, contra constructionis legem…* — **the MS reads thus but IN A SECOND HAND**; someone corrupted the true reading; *Repone* **nomen** |

**So the observed note numbers, in page order, are: 2 (La 129) · 6 (La 143) · 5 (La 431) ·
4 (La 454).** That is not a sequence in either direction, and the "cycle across the whole volume"
hypothesis is now **dead too**. What remains live:

| hypothesis | how to test it |
|---|---|
| The Latin note number is keyed to the **English** volume's note at the same passage, so a reader can cross-refer | Find the English page for each of these four passages and compare. La 431's is the awkward case — `ddc-2-05.md` records that the English carries *no* counterpart there |
| Numbering restarts per **signature/gathering** | La 129's foot carries signature `S`; La 465/467/473 carry `3 O`, `3 O 2`, `3 P`. Map the signatures and see |
| It is ad hoc — Sumner numbered notes as he set them, with no system | The residue if both above fail |

⚠ **Do not settle this from four data points.** Check La 50, 188 and 228 first; more notes may
exist that the detector missed. A documented open question is an acceptable exit (§4).

⚠ **Until this is settled, `[^laN]` numbers remain LABELS, not a checksum** (M3-RUNBOOK §3). The
English checksum is a separate, independent run and is unaffected — it is still passing, and II.i's
closure on 2026-08-04 filled its last open cell.

---

---

## 3a. ★★★ THE FIND — Sumner states his editorial method in his own words, at La 129

This is the most consequential thing the mechanical pass turned up, and it is not about numbering.
La 129's note reads, in part:

> *In impressis, ut soleo, manuscriptum religiose secutus sum, ne puncto quidem mutato, et litteris
> majusculis fideliter servatis.*
>
> — "In what is printed, **as is my custom**, I have followed the manuscript religiously, not even
> a point changed, and the capital letters faithfully preserved."

**Sumner is stating a general editorial policy — *ut soleo*, as is my custom — of diplomatic
fidelity.** Set that beside La 431, where he writes *ordinem leviter mutavi* — "I slightly changed
the order" — and the project has, in Sumner's own hand, **both the claim and a confessed exception
to it.**

Why this matters beyond the sweep:

- **PLAN §4a** requires the About page to say the text is Sumner's, not the manuscript's. It can now
  say so **using Sumner's own words on both sides**, which is far stronger than our assertion.
- **PLAN §6.4** (manuscript-state notes, M4) gains a real evidence base rather than one instance.
- The note also carries a **conjectural emendation** and marks a crux with a **dagger (†)** —
  the Latin volume has a critical apparatus, not merely occasional remarks.
- ⚠ **And the crux is on the eternity of matter** — *Ut extra Deum semper fuerit materia* — i.e. the
  hardest textual problem in the volume sits precisely on Milton's most heterodox metaphysical
  claim, creation *ex Deo* rather than *ex nihilo*. Whatever is said about that doctrine must
  acknowledge that its key sentence is, by the editor's own account, corrupt and reconstructed.

La 143 is the companion piece: *sic in MS. sed **a manu secunda*** — the manuscript reads thus **but
in a second hand** — which is direct editorial testimony to the layered, multi-scribe character of
SP 9/61 that the About page already means to describe.

**Both are TEXTUAL notes** under CONVENTIONS §5a and both earn rows in
`tools/sumner-interventions.tsv` **when Book I is transcribed**. They are recorded here now so the
finding is not lost; **do not back-fill them into chunks that do not yet exist.**

### ⚠ Scope consequence — Book I's Latin apparatus is real, and it is not this sweep's job

This sweep is scoped to Book II and stays scoped to Book II. But the Book I scan has established
that **Book I carries textual Latin apparatus of exactly the kind PLAN §6.4 was written for**, and
that it is thin enough to be tractable (about five pages in 380). When Book I transcription begins,
the standing obligation of M3-RUNBOOK §2 step 3 will pick these up chapter by chapter —
`tools/sweep-book1.tsv` already says where to look.

---

## 4. Exit criteria — all four, or the gate stays shut

1. Every page of La 387–428 has been looked at, page-foot, by eye.
2. The 18 riskiest negatives listed in §2 have been looked at.
3. Every hit is transcribed, classified, and (if textual) ledgered.
4. The numbering anomaly is either **resolved** or **explicitly recorded as unresolved with the
   Book I evidence attached** — a documented open question is an acceptable exit; a silent one
   is not.

Then, and only then, update `M3-RUNBOOK.md` §9b and §3, and Book II may be called complete for
chapters i–ix.

---

## 5. Scope note — why the range is 387–473 and not 387–454

§9b originally scoped the sweep to La 387–454, because II.viii and II.ix had not been transcribed
when it was written. They have been since, and their Latin feet were read as they were transcribed
(both chapters: no notes). The mechanical pass therefore covered **387–473**, the whole of Book II
Latin transcribed to date, and found nothing new in 455–473 either.

Chapters II.x–II.xvii (La 474–524) are not yet transcribed and are **out of scope** — their page
feet get read as those chapters are done, per M3-RUNBOOK §2 step 3. This sweep is about the debt,
not about future work.

---

## 6. ✅ RESULTS — the visual pass, run 2026-08-04 (Opus)

### 6.1 What was read, page by page

| set | pages | result |
|---|---|---|
| §2 step 1 — the never-examined core | **La 387–428, all 42** | **no note on any page** |
| §2 step 2 — the 18 riskiest negatives | La 387, 389, 390, 394, 396, 402, 403, 409, 421, 425, 427 (inside the core) + **433, 441, 442, 443, 457, 467, 473** | **no note on any page** |
| §2 step 3 — the two known positives | La **431**, La **454** | re-confirmed off the plate: **431 = ⁵**, **454 = ⁴** |
| §3 — the unverified Book I candidates | La **50**, **188**, **228** | **all three are false positives — no note** |

Two pages came up blank in the foot crop and were re-rendered full-page before being written off:
**La 394** (II.i's last page, chapter ends a third of the way down) and **La 403** (II.ii's last
page, five lines then blank). Both genuinely clean. **La 412** and **La 428** are the same shape —
II.iii's and II.iv's blank tails — and independently re-confirm those two chapter extents.

**Reconciliation: the detector and the eye agree on every one of the 62 pages looked at.** No
disagreement in either direction, so no page needed the 400 dpi fallback. The detector's two
sub-threshold flags (La 389, 421) are both false positives with an innocent cause — a short final
line of a paragraph, not small type.

### 6.2 The finding: §9's worry was unfounded

**No Latin note was missed in II.i–II.iv.** Those four chapters carry no Latin apparatus at all.
The standing obligation of M3-RUNBOOK §2 step 3 — read every chapter's Latin feet for superscripts —
stays in force for everything from here; it is the *back-check* on II.i–II.iv that is now discharged.

### 6.3 New evidence gathered on the way

- **La 454's note is confirmed SCHOLARLY, not textual**, off the plate: six lines of body text
  (`…aliosque video fuisse.⁴`) and then roughly forty lines of Bucer · Calvin · Ursinus · Gomarus ·
  Peter Martyr · Musculus on the sabbath. It earns **no** row in `tools/sumner-interventions.tsv`,
  which is what `ddc-2-07.md` already records. La 431's remains the only **textual** Latin note in
  Book II.
- **The Latin volume's gathering structure, measured off the signatures**, since §3 asked for it:
  8 pages per gathering, signed on leaves 1 and 3. Observed: `3 D 2`@387 · `3 E`@393 · `3 F`@401 ·
  `3 F 2`@403 · `3 G`@409 · `3 G 2`@411 · `3 H`@417 · `3 H 2`@419 · `3 I`@425 · `3 I 2`@427 ·
  `3 K`@433 · `3 L`@441 · `3 L 2`@443 · `3 N`@457 · `3 O 2`@467 · `3 P`@473. So gatherings open at
  385, 393, 401, 409, 417, 425, 433, 441, 449, 457, 465, 473.
- **La 441 carries pointed Hebrew** (גְּדוּפָה and קְלָלָה with their roots) in the running Latin text,
  alongside Greek. Worth knowing before Book I: the Latin volume sets three non-Latin scripts.

### 6.4 ⚖ THE NUMBERING QUESTION — RESOLVED as *ad hoc*, which is the §3 residue

Exit criterion 4 is met by resolution, not by deferral. **All four candidate hypotheses are now
positively refuted**, each by evidence rather than by argument:

| hypothesis | verdict | what kills it |
|---|---|---|
| Seven notes lie unread in La 432–453 | **dead** | the mechanical pass, and the transcription reads of II.v–II.vii |
| Numbers restart per **chapter** | **dead** | La 431's note would be ¹, and it is ⁵ |
| Numbers cycle 1–9 across the **whole Latin volume** | **dead** | ⁵ at La 431 → ⁴ at La 454 needs seven notes in the 22 pages between them. There are none — two independent methods agree |
| The Latin number is keyed to the **English** note at the same passage | **dead — settled this session** | La 454's ⁴ pairs with English note `[^s8-2]`, printed **8** (`ddc-2-07.md`); and La 431's ⁵ pairs with **no English note at all** (`ddc-2-05.md`) |

Also tested and discarded: restart per **signature/gathering** (§3's second column). The map in
§6.3 puts La 431 on leaf 7 of gathering `3 I` and La 454 on leaf 6 of `3 M`; a per-gathering restart
makes both ¹. (Their being *position − 2* in both cases is a two-point coincidence — La 129 sits on
leaf 1 of gathering `S` and its note is ², not −1.)

**What remains is §3's own third column: Sumner numbered his Latin notes ad hoc, as he set them,
with no system.** The four observed numbers in page order — **2 (La 129) · 6 (La 143) · 5 (La 431) ·
4 (La 454)** — are a sequence in no direction, under no reset rule, and against no external key.
That is a small and unsurprising result for an editor who set seven-odd notes across a 530-page
volume: there was nothing for a system to be *for*.

**The practical consequence is unchanged but now rests on evidence rather than on caution:
`[^laN]` numbers are LABELS, permanently. There is no Latin checksum and there never was one.**
Do not re-open this on finding a fifth Latin note in Book I — a new number cannot revive a
hypothesis that a *missing* number already killed. The English checksum (CONVENTIONS §8a) is a
separate, genuinely sequential run and is untouched by any of this.

⚠ One honest limit, stated because §1 demands it: the refutation of the cycle rests on La 432–453
being note-free, which comes from the detector plus the reads made while II.v–II.vii were
transcribed — not from a dedicated by-eye foot pass of those 22 pages. Two independent methods
agree, which is this project's corroboration standard, but it is not the same grade of evidence
as the 62 pages in §6.1.

### 6.5 Exit criteria — all four met

1. ✅ Every page of La 387–428 looked at, page-foot, by eye — 42 of 42.
2. ✅ All 18 riskiest negatives looked at.
3. ✅ Every hit transcribed, classified, ledgered — no new hits; the two known notes re-confirmed
   and La 454 re-classified as scholarly (no ledger row).
4. ✅ The numbering anomaly **resolved**, with the Book I evidence attached (§6.4).

**Book II is complete for chapters i–ix.** The gate is open.
