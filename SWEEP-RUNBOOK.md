# The Book II Latin footnote sweep — runbook

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

**`tools/detect-footnotes.py 7 386` has already been run over the whole of Book I**; results in
`tools/sweep-book1.tsv`. Start there: if Book I is empty of notes, the first hypothesis dies too
and the question narrows to the English-keying one. If Book I carries notes, read the last few
before La 431 and see whether the sequence walks into 5.

⚠ **Until this is settled, `[^laN]` numbers remain LABELS, not a checksum** (M3-RUNBOOK §3). The
English checksum is a separate, independent run and is unaffected — it is still passing, and II.i's
closure on 2026-08-04 filled its last open cell.

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
