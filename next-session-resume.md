# Next session — resume here

**Read first:** **`M3-RUNBOOK.md`** — the per-chapter procedure, the queue, the checks, and the
open suspect-flags. It is written so a session can start work immediately without re-deriving
anything. Behind it: `PLAN.md` (plan of record) · `CONVENTIONS.md` (frozen rules) ·
`STRUCTURE.md` (offsets). Format reference: `chunks/ddc-2-02.md`. Site: `site/`.
⚠ **There is no longer a partial chunk in the corpus** — `ddc-2-01` was the last one and closed
2026-08-04. The partial-chunk shape is still legal (CONVENTIONS §8d); its worked example now lives
in `ddc-2-01`'s Notes as history rather than as a live model.

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

## M3 — II.i, the last partial chunk, is CLOSED

- **II.i `De Bonis Operibus` ✅ COMPLETE 2026-08-04 (Opus)** — `chunks/ddc-2-01.md`,
  `status: verified`, both layers. La 387–394 (21 ¶¶) / En 527–536 (17 ¶¶), ratio 1.25.
  Its English was the range Wilson pulled a session off under content filtering on 2026-08-03;
  reopened on his instruction and transcribed with the one-paragraph-per-edit technique.
  {¶6} blocked twice as a whole paragraph and went through in six pieces. **Nothing paraphrased
  or omitted.** The footnote prediction held exactly (notes 3–7), closing the checksum ledger.
- Partial chunks remain architecturally fine and `build-content.mjs` was proved against this one
  while it was partial — the M2 language-array generalisation earned its keep, since a `la`-only
  chunk needed no special casing. **No partial chunk is currently open.**

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

- **II.v `De Jurejurando et Sorte` ✅ (2026-08-04, Opus)** — `chunks/ddc-2-05.md`,
  `status: verified`, both layers, all 25 plates read (La 429–439, En 579–592), extent
  plate-confirmed at both ends (blank tails; CAP. VI opens La 440, `CHAP. VI. Of Zeal.` opens
  En 593). Ratio 1.27. **II.v is the chapter that made every prediction come true**, and the
  four findings worth carrying forward are:
  1. **34 La ¶¶ → 34 En ¶¶ — strict 1:1, no merges at all.** First *whole* chapter to align
     perfectly (II.ii 28→25, II.iii 34→32, II.iv 57→56). Sumner's merging habit is real but not
     universal; don't treat a 1:1 count as evidence of a missed paragraph.
  2. **The footnote checksum passed on its first hard test, wrap included.** Predicted "must open
     at 9"; it does (En p. 580), wraps to 1 on p. 581, and closes at 5 on p. 592. Ledger:
     **9 · 1 · 2 · 3 · 4 · 5**. **II.vi must open at note 6.**
  3. **All four suspect Latin citations resolved, all four `Luc. ix. 66`-class** — La wrong,
     Sumner silently right (`Exod. vi. 7`→`vi. 8` · `Psal. ix. 5, 11`→`xcv. 11` ·
     `2 Sam. xix. 24`→`xix. 23` · `Num. xxiii. 27`→`xxiii. 23`). With four more found on the
     read, that is **eight outright Latin errors in one chapter, four of them in Isaiah**, the
     highest rate yet and the first time the errors cluster in one book. No English-layer error
     here — the two-way traffic seen in II.iii and II.iv-c didn't recur.
  4. **The English carries NO counterpart to `[^la5]`.** Owed-item 3 answered, negatively:
     Sumner disclosed his word-order change in the Latin volume only. En p. 582 renders the same
     sentence with no note. **A reader of the English alone cannot learn that the Latin there is
     not the manuscript's** — which bounds what `tools/sumner-interventions.tsv` can ever be
     built from.
  Also: **Greek turns up in the ENGLISH volume** (En p. 584 prints `νὴ τὴν ἡμετέραν καύχησιν`
  where La p. 433 gives the bare particle) — read English plates for Greek too, not just Latin.
  And a new §6 anomaly kept as printed: En p. 588 note `[^s2]` cites `Of truc Religion`,
  confirmed at 900 dpi — a misprint in the title of Milton's own tract, inside the note citing it.

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

Work from `M3-RUNBOOK.md` — **its queue table in §1 is the authoritative per-chapter record**,
kept current chapter by chapter. Book II first, then Book I, saving I.iv–I.vi for last. Opus per
chunk.

**▶ NEXT IS `ddc-2-17`** *De Officiis Publicis erga Proximum* — **the last chapter of Book II.**
La 525–536 (12 pp.) / En 696–711 (16 pp.), ratio 1.33, **all four boundaries plate-confirmed**
(La 536 ends `TOTIUS OPERIS FINIS`, En 711 ends `THE END`). **Nothing is prepped**: run
`./tools/prep-chapter.sh 2 17` first, and do not read a plate you did not just render.
**Its first English footnote must be 2** (II.xvi carried a single note, 1). At 12 Latin pages it sits
right at CONVENTIONS §7's split threshold — split at Milton's own lemma seams if it needs it, not at
a page count. Its subject is the magistrate, the people, and the church, so **treat it as a §10
polemical chapter and write one paragraph per edit from the start.**

**Finishing it closes Book II.** After that the run moves to Book I, i–iii and vii–xxxiii, saving
I.iv–I.vi for last (M3-RUNBOOK §5).

## ✅ BOOK II HAS NO SUSPECT FLAGS LEFT — 2.17 resolved 2026-08-27

The last one fell out of transcribing II.xvi and reading past its end: La 524 carries II.xvi's
closing *inhospitalitas* paragraph and a blank tail, so `CAP. XVII` could only open at **525**.
**The audit's text layer was right and the crosswalk was wrong** — the audit's discrepancies are now
2 for 2, the crosswalk 0 for 2. Correcting the start also exposed that **both** of 2.17's page counts
were wrong (La 12 not 11, En 16 not 15). Full reasoning and the two consequences for Book I's five
remaining flags are in **`M3-RUNBOOK.md` §7** — read it before resolving 1.28, the largest open gap.

## The findings from II.xv–II.xvi that change how the next chapter is read

1. **★★ Sumner adds doctrine the Latin does not contain.** II.xvi {¶5}: *ne absurda æquatio
   inæqualium fiat* becomes "lest we fall into the absurdity of equalizing **those whom nature never
   intended for an equality**." The Latin supplies neither *nature* nor *intention*. With II.xv's
   discovery that the divorce material in that chapter is Sumner's apparatus and not Milton's text,
   the rule is now general: **before attributing a position to Milton, check which layer it is in.**
2. **★★ The dash-range rule is confirmed and precise.** The English contracts every run of **three or
   more** consecutive verses to a dash range and **never** contracts a run of two — 7 and 10
   instances in II.xvi alone, no exceptions across two chapters.
3. **★★ The same-verse-two-halves habit is real, not an accident.** II.xv had `Prov. iii. 33 / xiv. 11
   / xv. 6` cited twice each on one page; II.xvi repeats it with `2 Cor. ix. 6` (bountifully /
   sparingly) and `Deut. xxvii. 19` (fatherless-and-widow / stranger). **The M4 scripture index must
   not de-duplicate by reference** — that would destroy the antithesis Milton is building.
4. **★ The English layer produces word errors, not only digit errors.** En 692 prints `he doth
   **create** the judgement` for *execute* (900 dpi). Every prior English error was a citation digit
   or a wrong sort; a wrong *word* reads as grammatical theology and will not be caught by a
   numeral check.

## ⚠⚠ TWO CONVENTION QUESTIONS ARE NOW WAITING ON WILSON — both from II.xi

Neither blocks transcription; both should be settled before Book I, whose longer chapters will hit
them repeatedly.

1. **How to notate a SPLIT.** Sumner divided a Latin paragraph for the first time in the corpus
   (La {¶35} → two English paragraphs). CONVENTIONS §4 says "every La ¶ appears exactly once on the
   En side," which is written for merges and is now false as stated. `ddc-2-11.md` uses
   **`{¶35}` then `{¶35 cont.}`** — provisional, the natural counterpart to `{¶N–M}`, and needing
   ratification.
2. **Raised ordinals.** `2ᵈᵒ.` recurred at La 482, a second chapter needing the rule §2 still lacks.
   Written inline as `2do.` following II.iv-b's precedent. (Note the English is no help here: it
   renders the raised ordinal as plain "Secondly," so the feature exists in the Latin layer alone.)

Also **still awaiting ratification from II.viii**: the mid-word page break, written
`an<!-- p.486 -->gustia` at La 485/486 — second instance in the corpus, same treatment as
En 613/614.

## `ddc-2-11` ✅ COMPLETE (2026-08-05, Opus)

`chunks/ddc-2-11.md`, `status: verified`, both layers, all 22 plates read (La 477–487, En 639–650),
`chapters.tsv` flipped `ok` → `verified`. La 477–486 / En 639–649, **38 La ¶¶ → 37 En ¶¶**,
page ratio 1.10. Six findings worth carrying:

- **★★ THE FIRST SPLIT IN THE CORPUS.** Every alignment mismatch until now ran one way — Sumner
  merges, so the English count was always ≤ the Latin. Here he **divides** La {¶35} (*AMICITIA…*,
  one unbroken paragraph across La 484–485) into two English paragraphs at *Friendship, and even
  common companionship with good men.* See the convention question above. Two merges as well
  (en{¶2–3}, en{¶4–5}), so 38 − 2 + 1 = 37.
- **★★ Six Latin citation errors silently corrected — and only two were predictable from the
  Latin.** `1 Sam. xvi. 2`→`xvi. 1` · `Gen. xxvii. 43`→`41` · `Prov. xii. 9`→`xii. 10` **twice** ·
  `Eccles. iv. 5`→`iv. 9` · `Judic. xi. 5`→`Judges xi. 3`. All twelve readings confirmed at 600 dpi;
  none is versification. **The Esau, Ecclesiastes and Judges errors were invisible until the English
  was laid beside the Latin** — II.ix's lesson, now settled: reading the Latin for suspects tells
  you where to look, the English layer is the instrument. Both halves of the doubled `Prov. xii. 9`
  were wrong and Sumner caught both.
- **★★ ἐπιχαιρεκακία is translated away** ("a rejoicing in the misfortunes of others") — a direct
  re-test of the rule formulated one chapter earlier, and it holds. **Six instances now** (ἀτοπία,
  φιλαυτία, αὐταρκεία, ἀπάθεια, ἐπιχαιρεκακία) against the kept-and-Cowper-translated Homer line of
  II.ix: **Sumner keeps Milton's Greek when it is a quotation and removes it when it is a technical
  term.**
- **★★ The English drops a proof-text again** — `Luc. vi. 27, &c. idem.` at La {¶6} has no English
  counterpart (600 dpi both sides). Second attested omission after II.x's `et cxii. 7.`, and the
  mechanism looks identical: a bare `idem` reference standing between two quoted texts. The M4
  consequence stands and hardens — **the scripture index cannot be built from either layer alone.**
- **★★ All three Sumner notes defend Milton** — the *Apology for Smectymnuus* on "a sanctified
  bitterness against the enemies of truth" answering the chapter's *aliquod tamen odium etiam pium
  est*, then *Paradise Lost* IV. 502, IX. 173 and XI. 455 on the envy of Satan and Cain
  (`[^s6]` carries two passages under one printed number). Fourth chapter in a row: **Sumner reaches
  for Milton's verse and prose where the treatise leaves Milton exposed.**
- **★ Two printed errors in the ENGLISH volume, one in the chapter's opening line** — En 639 sets
  **`justiee`** for *justice* (confirmed at **900 dpi**; a wrong sort, `e` for `c`), and En 641's
  {¶13} ends *"absolute or reciprocal"* with **no full stop**. Kept as printed. With II.iv-c,
  II.ix and II.x: the English is not the corrected side, it is the other side.
- **★ The Latin's arabic `2 Thess. 3, 10.`** (La 481, first in the corpus, 600 dpi) **is not
  mirrored** — the English sets `2 Thess. iii. 10.`, roman. CONVENTIONS §8b's "never normalise
  chapter B from chapter A" gains a companion: **never normalise layer to layer either.**

Also: no Latin apparatus (all ten feet read; sigs `3 Q`@481, `3 Q 2`@483 continue the sweep's
gathering map unbroken); Latin printed anomaly `Quæ **tamem** nonnunquam` at La 485; Sumner shifts
Milton's burial examples from the buriers (*Abrahami… Jacobi*) to the buried (*Sarah… Rachel*), and
softens *misericordia illicita* to "a misplaced compassion" — the same politening habit as II.vii,
II.ix and II.x, running in the same direction every time. Both volumes agree on small-caps emphasis
throughout, the second chapter running.

**Housekeeping:** the headnote word cap is being measured two ways (207 whole / 199 prose-only here;
*every* chunk in the corpus exceeds 200 on the whole-text count, 186–308). A one-line clarification
in CONVENTIONS §8 would stop it being re-litigated per chapter.

⚠⚠ **RUN `./tools/prep-chapter.sh 2 11 2 17` FIRST, and do not read a plate you did not just
render.** The script was fixed 2026-08-04 (commit `2b5e420`) to name plates by **printed** page;
it previously named them by **PDF** page, so `raw/plates/la-474.jpg` held printed **458** — a
16-page offset one step away from being transcribed as the wrong chapter, and it was caught only
because the plate had its own number at the head. Stale PDF-named plates from earlier preps are
still on disk and must not be trusted. `raw/` is gitignored and regenerable; re-prep, don't guess.

## `ddc-2-10` ✅ COMPLETE (2026-08-05, Opus)

`chunks/ddc-2-10.md`, `status: verified`, both layers, all 8 plates read. La 474–476 / En 636–638,
both extents plate-confirmed at **both** ends (`CAP. XI` opens La 477, `CHAP. XI` opens En 639), so
`chapters.tsv` is flipped to `verified`. **10 La ¶¶ → 9 En ¶¶**, one merge at en{¶3–4}. Four
findings worth carrying:

- **★★ ἀπάθεια is translated away** — La {¶10} *Et Stoica ἀπάθεια* → En "Lastly, a stoical apathy."
  That is **five instances read** of the same behaviour (ἀτοπία, φιλαυτία, αὐταρκεία, ἀπάθεια), against
  the kept-and-Cowper-translated Homer line in II.ix. The rule as it now stands: **Sumner keeps
  Milton's Greek when it is a quotation and removes it when it is a technical term.** Note the cost
  here is doubled — 1825 "apathy" does not carry the Stoic sense, so the English reads as a remark
  about listlessness rather than the rejection of a named doctrine.
- **★★ The English DROPS a proof-text.** La {¶5} has *et cxii. 7.* between Ps. xxvii. 1 and Prov. x.
  24; the English has nothing there. Both readings confirmed at **600 dpi** because it is an
  omission claim. **Three kinds of unmarked editorial handling of the citation apparatus are now
  attested: correction (II.iii ff.), reordering (II.ix {¶29}), and now omission.**
  ⚠ **This bears directly on M4:** the scripture index cannot be built from either layer alone,
  since a citation present in one volume may be simply absent from the other with nothing marking
  the gap. Build from the Latin, reconcile against the English, carry divergences as data.
- **★ Fourth plate-confirmed error in the ENGLISH layer: `Psal. iii. 9.`** (En 636, confirmed
  600 dpi). Psalm 3 has eight verses. La reads `iii. 7`, correct on the Hebrew numbering; Sumner's
  own conversion practice — verified three more times in this same chapter (xlvi, lvi, lxix, all
  correct) — makes the expected reading `iii. 6`. **Likeliest mechanism: a turned `6`.**
- **★ No `Luc. ix. 66`-class error anywhere in the chapter** — the first chapter since II.iii with
  none. After II.v's eight and II.ix's seven, that is worth recording: **the Latin error rate is
  not uniform across the volume**, so its absence is a finding, not a sign of a missed read.

Also: no Latin apparatus (all three feet read; La 475's signature `3 P 2` independently confirms
the gathering map built during the sweep). **Page ratio 1.00**, below the runbook's 1.1–1.8 band —
a true negative, since all four boundaries are plate-confirmed; don't widen the band on it.
Sumner's *first / Secondly / Lastly* enumeration of Milton's *Huic opponitur… Et… Et…* is at its
clearest here, "Lastly" having no Latin counterpart at all.

**Book II is now done through II.ix.** II.ix came in at **41 ¶¶ → 41, strict 1:1** — the longest
chapter transcribed and only the second to run 1:1 throughout. Three findings from it are worth
carrying forward, because each changes how the next chapter should be read:

- **★★ All three of its Sumner notes defend Milton's CHARACTER** — that he drank little, rose at
  four, and did not frequent the bordelloes — answered from the *Apology for Smectymnuus*, *Comus*,
  *Samson Agonistes*, *Paradise Lost* XI and the elegies. A fourth editorial behaviour, and
  `ddc-2-08.md`'s poetry note has been amended because of it. The generalisation that now holds:
  **Sumner reaches for the poetry where the prose treatise leaves Milton personally exposed.**
- **★★ The English ADDS a Cowper verse translation of Milton's Homer line, in the running text,
  with no Latin counterpart.** With II.v's converse case (English carrying no counterpart to
  `[^la5]`), this settles it: **neither layer is a complete witness to the other**, and the
  parallel-layer design in CONVENTIONS §1 is doing real work, not being tidy.
- **★ Citations: seven Latin errors corrected by Sumner, three in one paragraph — but one error
  runs the OTHER way** (La `Dan. ii. 30` is right, En `ii. 31` is wrong; second plate-confirmed
  English error in the corpus). **Two of the seven were not on the suspect list drafted from the
  Latin.** Inspecting the Latin alone is a starting point, never a census; the English layer is
  the instrument. Also logged: Sumner silently **reorders proof-texts** at {¶29}, and renders
  *ornamenta vitæ* as "a high station", which the Latin does not say.

## ✅ THE SWEEP IS RUN AND CLOSED — 2026-08-04 (Opus). BOOK II i–ix IS COMPLETE.

Full record: **`SWEEP-RUNBOOK.md` §6**. All four exit criteria met; the gate is open. Headlines:

- **62 Latin page-feet read by eye** — all 42 of La 387–428, which nobody had ever examined, plus
  the 18 riskiest detector negatives and the two known positives. **Detector and eye agree on every
  page.** No new note anywhere.
- **§9's worry was unfounded: II.i–II.iv carry no Latin apparatus at all.** That back-check is
  discharged. The standing obligation to read every *future* chapter's Latin feet stays in force —
  nothing but reading detects a missed Latin note.
- **La 431 = ⁵ (textual, the only one in Book II) · La 454 = ⁴ (SCHOLARLY** — a page of Bucer,
  Calvin, Ursinus, Gomarus, Peter Martyr, Musculus on the sabbath; **no ledger row).**
- **Book I's unverified candidates La 50, 188, 228 are all false positives.** Book I's confirmed
  Latin notes stand at La 129 and La 143 — the two that matter, and both textual.
- **⚖ The numbering anomaly is RESOLVED: ad hoc, no system.** All four hypotheses refuted; the last
  fell this session — the Latin number is **not** keyed to the English note at the same passage
  (La 454's ⁴ pairs with English note printed **8**; La 431's ⁵ pairs with **no English note**).
  Per-gathering restart is out too, measured off the signatures (8pp gatherings opening at 385, 393,
  401 …). **`[^laN]` numbers are LABELS, permanently — there is no Latin checksum and never was.**
  A fifth Latin note in Book I does not re-open it; a *missing* number already killed the cycle.
- Incidental, but useful before Book I: **La 441 sets pointed Hebrew** (גְּדוּפָה, קְלָלָה with roots)
  in the running Latin text alongside Greek — the Latin volume uses three non-Latin scripts.
- **★★★ Book I carries textual Latin apparatus, and La 129 is Sumner stating his own editorial
  method** — *"as is my custom I have followed the manuscript religiously, not even a point
  changed"* — which sits directly against La 431's confessed *ordinem leviter mutavi*. We now have
  both the claim and the confessed exception **in the editor's own words**. That is a much stronger
  footing for the About page than our own assertion, and it bears on PLAN §4a and §6.4.
  ⚠ Its crux is on **the eternity of matter** — the hardest textual problem in the volume sits on
  Milton's most heterodox metaphysical claim. See `SWEEP-RUNBOOK.md` §3a.

⚠ **Book I's apparatus is NOT this sweep's job** — it gets picked up chapter by chapter when Book I
is transcribed, per M3-RUNBOOK §2 step 3. `tools/sweep-book1.tsv` already says where to look.

**Both of the big debts are now discharged; one item remains:**
1. ✅ ~~II.i's English~~ — **DONE 2026-08-04.** Both layers verified; see below.
2. ✅ ~~The Book II Latin sweep~~ — **DONE 2026-08-04.** Gate open, Book II i–ix complete.
3. **The six open suspect flags (runbook §7)** — the only outstanding debt, biggest is
   **1.28 (La 309 vs 315)**. These are Book I boundaries and are cheap to settle when Book I opens.

Two small convention questions are still owed and are **cheap to ratify before Book I**, where both
recur: the **raised ordinals** (La 417 prints 1ᵐ · 2ᵈᵒ · 3ᵗⁱᵒ …, set inline as `1m.` `2do.` for want
of a superscript markup — CONVENTIONS §2 defines none) and the **mid-word page break**
(En 613/614 breaks *accept-* | *-able*, written `accept<!-- p.614 -->able`, soft hyphen dropped).
Both are precedent-by-accident until Wilson rules.

**✅ II.i is CLOSED — the last outstanding debt in Book II.** Transcribed past the content filter
with the one-paragraph-per-edit technique; {¶6} blocked twice as a whole paragraph and went through
in six pieces. **Nothing was paraphrased or omitted to get past a block.** 21 ¶¶ → 17, including a
**quadruple merge** at {¶9–12}, the largest in the corpus. Its footnote prediction (notes 3–7) held
exactly, closing the last open cell in the checksum ledger.

⚠⚠ **The finding to carry into every future chapter: a queue that does not run in book order
manufactures false "firsts."** II.viii recorded Sumner's use of Milton's poetry as a novelty; II.i,
the Book's **opening** chapter, already quotes *Paradise Lost* and *Sonnet* XIX. The claim has been
**withdrawn** in `ddc-2-08.md` (amended twice). **Any note of the form "the first time X appears"
is a claim about what has been READ, not about the book — write it that way or don't write it.**

★ Also from II.i: a **third** plate-confirmed error in the English layer (La `Prov. xxiv. 1` is
right, En prints `xxiv. 7`), and the Greek pattern is now clean over four instances — **Sumner
translates Milton's Greek technical terms away** (ἀτοπία, φιλαυτία, αὐταρκεία) **but keeps his
Greek poetic quotation** (Homer, with Cowper added). A reader of the English alone cannot tell
Milton left Latin; that belongs on the About page.

**One small convention question is now owed** (recorded in `chunks/ddc-2-08.md` Notes): a printed
page break falling **mid-word** — En 613/614 breaks *accept-* | *-able*. Written as
`accept<!-- p.614 -->able`, dropping the soft hyphen as a typographic artifact. First instance in
the corpus; CONVENTIONS §2 has no rule for it. Cheap to ratify, but it should be ratified rather
than left as precedent-by-accident.

## Owed by Wilson

- ~~GitHub remote~~ **done 2026-08-04** — `wilsonpruitt/milton-doctrina`, **PRIVATE**, `main`
  tracking `origin/main`. `raw/` (PDFs, plate renders, OCR dumps) is gitignored and stays local;
  verified 0 `raw/` paths on the remote. **Flip to public only at M5**, and not before
  `site/src/app/rights/page.tsx` carries a real rights statement — CC BY-NC 4.0 on the English and
  the encoding, PD on the 1825 source (see the Wroot Press licensing memory). Note the repo landed
  under `wilsonpruitt`, not the `littleeachdayapp-droid` bridge account.
- Domain wiring for milton.wrootpress.com when M5 nears (Cloudflare, DNS-only per house rule).
