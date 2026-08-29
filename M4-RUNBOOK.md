# M4 — the scripture index

**Read this before writing any code.** The measurement is done; do not re-derive it. Behind this
file: `PLAN.md` §6.1 (why the index is the product), `CONVENTIONS.md` §3 (citations as printed,
never harmonized), `M3-RUNBOOK.md` (the transcription procedure this feeds on).

Wilson's ruling, 2026-08-28: **start now, on the 19 chapters in hand**, rather than waiting for the
corpus to be complete. PLAN §10 risk 5 is the reason — the parser "will produce garbage confidently
if it is not validated," and 19 chapters is enough to find that out cheaply.

---

## 1. What is already done — prep, 2026-08-28

| | |
|---|---|
| `tools/census-citations.py` | measures the citation forms actually present. Re-run it as chapters land; `--shapes` and `--unclass` for detail. |
| `tools/scripture-books.json` | abbreviation tables for both layers, seeded from the census. **62 books** — `3 John` added 2026-08-28. |
| this file | the design decisions and the hazards, below. |

## 1a. Steps 1-3 are DONE — 2026-08-28

- **`tools/versification.py`** does not exist; **`tools/build-versification.py`** does, and it
  derives `tools/versification.json` (66 books, 1189 chapters) from `~/kjv-wesley/data/kjv`.
  That dataset is known short — Matthew and Mark are each missing three verses and are
  *silently renumbered* past the drop — so the table carries a per-book `trust`
  (`exact` / `slack+1` / `unreliable`) and the range check reports Matthew and Mark as
  warnings only. Regenerate, never hand-edit.
- **`tools/build-citations.py`** — the parser. `./tools/build-citations.py ddc-2-02` for one
  chunk, `--all` for the corpus, `--dump` to read every record. Writes `index/citations.tsv`
  and `index/citation-qa.md`.
- **Step 2's gate is met on `ddc-2-02`**: 327 records, **0 unclassified**, layer spread 0.6%,
  and **all nine divergences hand-logged in the chunk's Notes are found** — check §6.4, the
  strongest validation available, passes on the format-reference chapter.
- **Step 3 is run across all 21 chunks**: 5,809 records, layer spread **0.1%** (2906 la /
  2903 en), 30 unclassified, 13 out-of-range, 427 divergence rows. Not yet hand-checked
  chapter by chapter — that is the next session's work, and `index/citation-qa.md` is the
  worklist.

⚠ Steps 4-6 (`build-index-json.py`, `/scripture`, the route) are **untouched**.

## 2. ★★★ The one decision that differs from Bonaventure — BOTH layers are keyed

Bonaventure's `build-citations.py` opens with a frozen rule:

> *Latin is the keying side. English bodies/apparatus are display-only and are NOT parsed —
> English punctuation drifts, Latin citation syntax is systematic.*

**That rule must NOT be ported.** It is false here, and porting it would destroy the edition's
central finding. Milton's two layers disagree about citations *systematically and substantively* —
CONVENTIONS §3 exists for exactly this, and 80 divergences are already logged by hand in the chunk
Notes across just 9 chunks (~4 per chapter; ~210 projected over 50). Keying off the Latin would
silently publish one side of a disagreement the edition exists to display.

**So: parse both layers, key each independently, and make the divergence a first-class field.**
A ledger record carries its `layer`. Two records that occupy the same `{¶N}` and resolve to
different targets are a *divergence pair*, and the scripture page should show both — that is the
parallel-text thesis applied to the index.

⚠ This also means the index is a **QA instrument twice over**: it will find defects in the text
(the Bonaventure lesson) *and* it will find divergences the per-chapter reading missed. Expect both.

## 3. Milton's citation grammar — measured, not guessed

From `census-citations.py` over the 21 chunks (19 chapters):

| | Latin | English |
|---|---|---|
| reference-shaped tokens | **3011** | **3090** |
| bare `v. N` continuations | 338 | 322 |
| distinct book tokens | 75 | 79 |

The near-parity of the two totals is a useful invariant: **a parser whose two layers differ by more
than a few percent has a bug.**

Shapes, commonest first (both layers agree on the ordering):

| shape | example | note |
|---|---|---|
| `BOOK CH V` | `Matt. xi. 27` | ~50% of all references |
| `— CH V` | `v. 9` | ~22%. **Stateful**: the book (and often the chapter) is carried from the preceding citation. |
| `BOOK CH V-LIST` | `1 Pet. i. 10, 11` | |
| `BOOK CH V+&c` | `Exod. xix. 18, &c.` | `&c.` is an open end, not a verse |
| `— CH V-LIST` | `vi. 1, 2, 3` | |
| `BOOK CH —` | `Apoc. i.`, `Isai. vi.` | chapter only. **Must not be given a verse.** |
| `BOOK CH V-RANGE` | `Job xi. 7—9` | **English only — see below** |

### Four measured divergences in the citation SYNTAX itself

1. **Verse ranges are an English feature: 79 in the English layer, ZERO in the Latin.**
2. **Period-separated verse pairs are a Latin feature**: `xxxiii. 20. 23.`, `xvii. 12. 14.` — 3 in
   the Latin, zero in the English. The English sets commas, or a range, or flattens the pair into a
   list (I.ii: La `1 Chron. xvii. 12. 14. cum 17.` → En `1 Chron. xvii. 12, 14, 17.`, which **loses
   a comparison**). So a Latin period-pair may correspond to an English range, a list, or one verse.
3. **The abbreviation tables are different**, and Sumner is inconsistent *within* a layer:
   `Levit.`/`Lev.`, `Numb.`/`Num.`, `Neh.`/`Nehem.`, `Micah`/`Mic.`, `Esther`/`Esth.`,
   `Lam.`/`Lament.`, `Hos.`/`Hosea`, `1 John`/`1 John.`
4. ✅ **`1 Reg.`/`2 Reg.` = 1-2 KINGS — CONFIRMED AT PLATE, 2026-08-28.** Read off freshly
   rendered I.ii plates, both layers: La 15 `1 Reg. viii. 27. cœli cœlorum non capiunt te`
   against En 22 `1 Kings viii. 27. the heaven and heaven of heavens cannot contain thee`.
   1 Samuel 8 has only 22 verses, so the Samuel reading is impossible on the digits alone,
   and the content is Solomon's dedication. La 17 carries the pair in one paragraph —
   `1 Reg. viii. 60.` and `2 Reg. xix. 15.` — against En 25's `1 Kings viii. 60.` and
   `2 Kings xix. 15.` The Latin volume uses `1 Sam.`/`2 Sam.` separately throughout, so this
   is not the Vulgate's 1-4 Regum.

## 4. Hazards, each already drawn blood in prep

1. **Word-boundary anchoring.** Without `\b`, the roman-numeral class matches inside words and the
   Latin layer reports **~3,900 phantom citations** that are single letters of ordinary prose
   (`i` 2478×, `c` 441×, `x` 270×). The census carries the fix and a comment saying why.
2. **Latin words that ARE roman numerals.** Even anchored, `illi`, `vi`, `ii`, `ix`, `li`, `ci` are
   shape-identical to numerals. A bare roman is a citation only in citation context — after a book
   token, after `et`, or after another citation. **This hazard does not exist in the English.**
3. **Capitalised Latin words that look like books** — `Judæis`, `Judæorum`, `Judæi`, and `Sic`
   (the opening of Sumner's textual notes). A book token is a citation only when a chapter or
   verse follows. ⚠ `Judæ` + `i` reads as *Jude 1* unless whitespace is REQUIRED between the
   book token and its numeral; the parser does, and no citation in either volume sets them tight.

3a. ⚠ **`cap.` WAS MISFILED HERE AND IS NOT A SELF-REFERENCE.** This entry used to say `Cap.`
   was "Milton's own chapter self-reference." It is wrong, and dropping `cap.` as a non-book
   would have silently lost an entire continuation class. `cap.`/`Cap.` means *chapter* and
   **carries the current book forward**: `Exod. xvii. 16. … Cap. iii. 14.` is Exodus 3:14
   (*Ehie, qui sum*), `Deut. iv. 35. … cap. vi. 4.` is Deuteronomy 6:4 (the Shema),
   `Gen. xii. 13. … cap. xiv. 22, 23.` is Genesis 14. The genuine self-reference exists but is
   rare and always **governed** — `Vide supra lib. 1. cap. xxvii.`, `ut superiore libro cap. x.`
   — four instances in 21 chunks. The English does the same thing (`See Book I. chap. xxvii.`),
   and Sumner cites other authors the same way (`Ames, Medull. Theol. lib. ii. c. 13.`). All
   three, indexed as scripture, produce 1 John 27, Luke 27, Deuteronomy 100. The parser refuses
   any continuation governed by `lib.` / `Book` / `supra` / `infra`.
4. ★ **Single-chapter books drop the chapter entirely**, and **the two layers do it differently**:
   La `Judæ v. 20.` prefixes `v.`, En `Jude 20.` sets a bare arabic verse. The Latin form is the
   dangerous one — as a roman, `v` is 5, so a parser expecting `BOOK CH V` emits *Jude chapter 5*.
   This parser did exactly that until the full-corpus run caught it; single-chapter books are now
   matched **before** the general book-and-chapter branch. `3 John` is in the corpus three times
   (`3 Joan. 5, 6, &c.`) and was missing from the book table, which is why the run reported
   `John 5`. Obadiah, Haggai, Philemon and 2 John have no chapter-and-verse citation yet;
   Philemon appears only as a whole epistle (`et Philemonis epistola`), which is not indexed.
5. ★ **`Jud.` is JUDGES, not Jude** — the first seeding of the book table got this wrong, and what
   caught it was the parallel: La `Jud. xiii. 18.` against En `Judges xiii. 18.`, versus La
   `Judæ v. 20.` against En `Jude 20.` **The other layer is the best check on a mapping.** This is
   §2's argument arriving from a second direction.
6. **Numeral-dropped tokens** — bare `Cor.`, `Kings`, `Thess.`, `Sam.`, `Tim.`, `Chron.`, `Pet.`
   occur in both layers. Almost certainly continuations carrying the numeral forward, but
   **unresolved**. Per the Bonaventure rule that ports verbatim: *never guess — a citation the
   parser cannot classify becomes a QA line, not a record with an invented target.*
7. **`et v. N` is ambiguous and unresolvable by form alone** — it may be verse N of the current
   chapter or chapter N of the current book. **Resolved in practice by a two-stage test, and the
   record says which stage settled it:** first the canon (does either reading target a verse that
   exists?), then, where both survive, **the parallel layer** — the English sets `v. N` for a
   verse and never for chapter 5, so an aligned English verse-continuation fixes the Latin. On
   ddc-2-02 that settles all thirteen instances (4 by canon, 9 by the English) with none left
   over; across the corpus ten remain genuinely unresolved and are in the QA report, not the
   ledger. ⚠ The first run of the parser read every `et v. N` as chapter 5 and emitted Ps 5:98,
   Ps 5:157 and six more targets that do not exist. That is PLAN §10 risk 5 in miniature.

8. **A verse tail eats the next book's numeral.** `2 Reg. xxiii. 2 Chron. xxxiv. 4, &c.` — the
   chapter-only citation's tail swallows the `2` of `2 Chron.`, bare `Chron.` matches no alias,
   and the following `xxxiv.` carries 2 Kings forward to a chapter that does not exist. Four
   false out-of-range records came from this one mechanism. The tail must refuse a number
   standing in front of a book token, including a `1`-`4` standing in front of a numbered book's
   second word.

9. ★★ **A book may be named in PROSE rather than in an abbreviation, and then cited bare.**
   Milton: `quam vana … luculenter ostendit Isaias cap. lix. 4`. Sumner: "the author of the
   Epistle to the **Hebrews** …" then a bare `vi. 1—3.` Nothing in the citation syntax marks
   either, so a state machine carries the wrong book forward. There is no reliable detector.
   The guard is a rule about output, not about input: **a citation whose book was CARRIED and
   whose target does not exist is refused**, because the carry is the likelier defect. A
   citation whose book is NAMED and whose target does not exist stays in the ledger, flagged —
   that one is a finding about the 1825 text.

## 5. What ports from Bonaventure, and what does not

Source: `~/bonaventure-sentences/tools/build-citations.py` (50 KB), `build-index-json.py`,
`site/src/app/scripture/{page.tsx,[book]/page.tsx}`, `site/src/data/scripture/*.json`.

**Ports — the pipeline shape, which is sound:**
- One ledger record per citation *occurrence* → `index/citations.tsv`. Every view is a view over it.
- `build-index-json.py` computes nothing about citations; it regroups and renders.
- Derived, never hand-tagged. Zero writes under `chunks/`. Re-runnable at will.
- A census assertion at exit: the ledger's chunk roster must equal the `chunks/` glob.
- Never guess → QA report, not an invented record.
- Only resolved classes enter the index; out-of-range is a QA line.
- `/scripture` in the top-level nav from day 1 (PLAN §6.1), not tucked inside a chapter page.

**Does NOT port:**
- The Latin-only keying rule (§2 above) — the single most important difference.
- Quaracchi's author sigla, `ibid.`/anaphora resolution, cross-reference-to-Sentences-loci
  machinery, `Cfr.`/`Vide` clause splitting. Milton has none of it.
- Vulgate Psalm numbering. Milton cites Junius–Tremellius and Sumner adjusts toward KJV,
  **inconsistently** (CONVENTIONS §3). Do not impose either numbering silently; the mapping is the
  index's problem to *display*, not to resolve away.

**Ledger columns** (Bonaventure's, adapted — note `layer` and the divergence fields):

```
chunk_id  layer  section  para  anchor_label  class  raw_text
normalized_target  confidence  resolution  carried_from  divergence_id
```

## 6. Acceptance checks — the index is not done until these pass

1. Latin and English reference counts within a few percent of each other, per chapter.
2. Every chunk in `chunks/` appears in the ledger (census assertion).
3. Zero records whose target is a chapter or verse that does not exist in that book. Reading a
   digit correctly is not reading it rightly — **verify that the target exists.**
4. The 80 hand-logged divergences in the chunk Notes are all found by the parser. **This is the
   strongest available validation** and it is free: they were recorded by eye, chapter by chapter,
   before any parser existed. A divergence the parser misses is a parser bug; a divergence it finds
   that the Notes lack is a reading the transcription missed — file it either way.
5. The QA report is read, not merely generated.

## 6a. ★★ What the first full run found — 2026-08-28

**Check §6.4 passes on ddc-2-02: all nine hand-logged divergences found, plus four the Notes
lack** — three `&c.` dropped by the English (`Job. v. 12, &c.`, `Eccles. iii. 1, &c.`, and the
already-logged `Exod. xix. 23, &c.`), a Latin verse-list truncated (`Job xii. 24, 25.` → `xii. 24.`),
and ★ **a citation the English ADDS**: at 1 Cor. i. 19, 20 Milton runs two proof-texts together
under one reference and Sumner supplies `v. 23.` for the second. With correction, reordering and
omission already attested, **that is a fourth kind of unmarked editorial handling of the citation
apparatus — supply.** All five want plate confirmation before they are written up as findings.

**Thirteen citations in the corpus name a book and point at a verse that does not exist.** Five
were already plate-confirmed by hand (`Luc. ix. 66.`, `2 Reg. vi. 35.`, `Deut. v. 38.`,
`Psal. iii. 9.`, `1 Kings xxvii. 29.`) — the parser found every one of them without being told.
The other eight are new and unread.

★★ **Five of the thirteen are Ecclesiastes, in the Latin layer** — `ii. 27`, `vii. 30`, `ix. 20`,
`ix. 22`, `xii. 15`, each running one to four verses past the KJV bound, in a book of twelve
chapters. Five over-runs concentrated in one small book is not printer's error. **The hypothesis
to test is that Junius-Tremellius versifies Ecclesiastes differently**, in which case these are
not errors at all but the numbering divergence CONVENTIONS §3 exists to display — and note that
Sumner corrects some of them (`ix. 20` → `ix. 18`) and leaves others (`xii. 15` in both layers).
Settle this before any of the five is called an error.

## 7. Sequence

1. ✅ **DONE 2026-08-28** — `1 Reg.` = Kings confirmed at plate (§3.4).
2. ✅ **DONE 2026-08-28** — `tools/build-citations.py` written and clean on `ddc-2-02`.
3. ✅ **RUN 2026-08-28.** Check 4 passes on ddc-2-02. The Ecclesiastes question is **settled —
   §6b**: versification, not error; six of the thirteen out-of-range citations reclassified and
   two still want a plate. Still owed: the report has not been read chapter by chapter (§6.5).
4. `tools/build-index-json.py` → `site/src/data/scripture/*.json`.
5. `/scripture` and `/scripture/[book]`, ported from Bonaventure, plus the divergence display.
6. Backfill each new chapter as it lands; add the index step to M3-RUNBOOK §2.

## 8. Model

Steps 1–2 are judgment-dense and belong on a strong model: the grammar is being *designed* against
a text that breaks the obvious rules, and a confidently-wrong parser is the failure mode PLAN §10
names. Step 3 onward is volume work over a frozen grammar and does not need one. The headnotes'
`*Loci: pending M4.*` line is §6.2's job, not this file's — Wolleb and Ames are on disk
(`tools/fetch-loci.sh`) and unread.

---

## 6b. ★★★ The Ecclesiastes question is SETTLED — 2026-08-28. They are NOT errors.

**Answer: all five Ecclesiastes out-of-range citations are Junius–Tremellius versification.**
They are divergences to *display* under CONVENTIONS §3, not errors to flag. §6a's hypothesis was
right, and the evidence is stronger than a plate reading could have been — it is the corpus
itself, cross-checked layer against layer.

### What settles it: per-chapter offsets that repeat

The out-of-range five were never the whole evidence. Every Ecclesiastes citation in the corpus was
paired across the two layers, and **the divergences are internally consistent chapter by chapter**,
each confirmed by the quoted text (which identifies the KJV verse independently of any digit):

| Eccl ch | La − KJV | instances | sample |
|---|---|---|---|
| 2 | **+1** | 2 | La `ii. 27` = En `ii. 26` *peccatori dat occupationem* |
| 4 | **−4** | 4 | La `iv. 1, 2` = En `iv. 5, 6` *stolidus complicat manus suas* |
| 7 | 0, runs past the KJV bound | 1 | La `vii. 30` = En `viii. 1` *sapientia hominis illustrat faciem* |
| 8 | **−1** | 2 | La `viii. 1` = En `viii. 2` *keep the king's commandment* |
| 9 | **+2**, runs past the KJV bound | 3 | La `ix. 20` = En `ix. 18` · La `ix. 22` = En `x. 2` |
| 10 | **−3** | 2 | La `x. 2, 3` = En `x. 5, 6` |
| 12 | **+2** (from v. 4 on) | 1 | La `xii. 15` = En `xii. 15` *summa rei est* (KJV 12:13) |
| 1, 3, 5, 6, 11 | 0 | ~14 | layers agree exactly |

**Four citations in Eccl 4 all off by exactly −4, and three in Eccl 9 all off by exactly +2, cannot
be four and three independent misprints.** That is one numbering system, described twice.

★ And the two chapter displacements are each confirmed **from both sides**, which is what makes
this airtight rather than merely likely:
- La ch 7 absorbs KJV 8:1 (we see `vii. 30` = KJV 8:1) — *and* La ch 8 therefore runs −1 (we see
  `viii. 1` = KJV 8:2). Predicted and observed.
- La ch 9 absorbs KJV 10:1–3 (we see `ix. 22` = KJV 10:2) — *and* La ch 10 therefore runs −3 (we
  see `x. 1` = KJV 10:4). Predicted and observed.

The remaining offsets fall out of the same model without contradiction: La ch 2 begins at KJV 1:18
(so La ch 1 = KJV 1:1–17, and `i. 16`/`i. 17` agree with the KJV exactly, as required); La ch 4
begins at KJV 4:5 (so La ch 3 absorbs KJV 4:1–4).

### Why the range check saw Ecclesiastes and nothing else

**Selection effect, not a property of Ecclesiastes.** Its chapters are short (12 chapters,
median ~18 verses), so an offset of +1 or +2 overflows the chapter bound often. The same offsets
in Psalms or Isaiah stay in range and are invisible to a range check. Do not conclude that
Ecclesiastes is where the Latin is unreliable — it is only where the divergence is *visible*.

### ★★ The same mechanism runs through the whole corpus — 149 same-chapter verse divergences

Offset distribution over every divergence pair the parser found, `La − En`:

`+1` **79** · `−1` 20 · `+2` 14 · `−3` 8 · `+4` 7 · `−5` 4 · `−4` 3 · `−2` 2 · `−6` 2 · `+6` 2 ·
`+9` 2 · one each of `−14, −9, +5, +11, +15, +51`

**`+1` alone is 53% of all divergences.** In the Psalms it is decisive: **53 of 57 Psalm
divergences are +1 or +2**, and the split is exactly the one Hebrew versification predicts —
`+1` where the psalm carries a one-line superscription (Ps 5, 12, 19, 30, 31, 40, 41, 58, 68,
69, 75, 92, 102, 140 …), **`+2` in Ps 51, 52 and 60**, whose superscriptions run to two lines
("when Nathan the prophet came unto him", "when Doeg the Edomite came and told Saul"). The
Hebrew counts the title as verse 1, or as verses 1–2. Nothing else produces that pattern.

Other chapters with a repeating, content-checkable offset: Prov 12 (−1, six times), Num 23 (+4,
three times), 1 Sam 14 (+1, four times), Dan 6 (+1, four times), Neh 10 (+1, three times),
Isa 44 (−5, four times), Isa 57 (+4, twice), Amos 2 (−3, twice), Gen 12 (−3, twice).

### Two more of the thirteen fall to the same lens, with no plate needed

- ✅ **`Lev. v. 21, &c.` (ddc-2-14 la ¶5) is NOT an error.** La *rependat—, deinde reatum suum
  afferto* = En `Levit. vi. 5, &c.` *he shall even restore it in the principal … and he shall
  bring his trespass offering* = KJV Lev 6:4–5. The Hebrew numbers KJV 6:1–7 as **5:20–26**;
  this is that division exactly. Reclassify as versification.
- ⚠ **`Psal. iii. 9.` (ddc-2-10 en ¶3–4) stays an English error, but the note's reason is wrong.**
  `chunks/ddc-2-10.md` says "Psalm 3 has only eight verses, in the Hebrew and in the KJV alike."
  **The Hebrew Psalm 3 has nine** — that is the whole point of the superscription rule the note
  itself invokes two sentences later. The finding survives and gets sharper: La reads `iii. 7`
  (Hebrew for KJV 3:6, the quoted text); En prints `iii. 9`, which is a *valid* Hebrew number but
  points at KJV 3:8, not at the verse Sumner quotes. So this is not a digit that could not exist —
  it is a conversion made in the wrong direction. Corrected in that chunk's Notes this session.

### What this means for the index — a design consequence M4 §5 did not anticipate

M4-RUNBOOK §5 says the versification mapping is "the index's problem to *display*, not to resolve
away." That is right about display and **insufficient for grouping.** La `Eccles. iv. 1` and En
`Eccles. iv. 5` are *one citation of one verse*. If `build-index-json.py` groups by the printed
target, the scripture page scatters that single act of citation into two unrelated entries four
verses apart — and does so 299 times across the corpus, concentrated in the Psalms, which is the
most-cited book in the treatise.

**So the index needs a third key: a `witness_target`, the verse both layers are pointing at,**
alongside the two printed targets it must go on showing. Where the layers agree it is the printed
target; where they diverge it is the English one (Sumner is converting *toward* the KJV, which is
the reader's Bible), and the record keeps both. This is a step-4 decision — settle it before
writing `build-index-json.py`, not after.

### ✅ Ledger changes MADE — 2026-08-28

All three landed in `tools/build-citations.py`; re-run `--all` and the numbers below should
reproduce exactly.

**1. `divergence_id` is populated at last.** The column was in the schema from the start and was
written as `""` on every row. It now keys the two records that are one citation: 717 records
carry one.

**2. `witness_target` is a new column** — the verse both layers point at, beside the printed
target each layer must go on showing. Where the layers agree it is the printed target; where they
diverge it is the **English** one, because Sumner is converting toward the KJV, which is the
reader's Bible and the numbering a reader can actually look up. 298 records now carry a witness
that differs from what their layer prints. This is what `build-index-json.py` must group by.

**3. `versification` is a resolution class, decided by CORROBORATION rather than a book list.**
An offset is a system, so it repeats; a misprint is a singleton. A record leaves the error list
only if it is paired with a resolving counterpart in the same book **and the offset that pair
exhibits is itself attested elsewhere**. For a cross-chapter pair the test is stricter still and
asks for the complementary observable: if La ch *n* runs past the KJV bound into ch *n+1*, then
La ch *n+1* must independently show a negative offset. Eccl 7/8 and 9/10 both pass it.

⚠ **The first cut of this rule tested only whether the BOOK repeats an offset, and it excused two
real printed errors.** Worth keeping, because both are instructive:

- `Isa. lviii. 56.` against En `Isai. lviii. 5, 6.` — **the Latin lost the comma** and ran the
  verse list together. Isaiah does repeat offsets (44 at −5, 57 at +4), so a book-level test
  passed a "+51 offset" seen exactly once. This also *answers* one of the two remaining plate
  questions without a plate: `lviii. 56` is not a mis-set number, it is a dropped comma.
- En `Psal. iii. 9.` against La `Psal. iii. 7.` — a −2 seen exactly once, in the book where +1 is
  nearly universal. Already confirmed at 600 dpi as an English error (§6b above).

The tightened rule moves **7** records and leaves **6** errors, which is exactly the split derived
by hand before any of it was coded. `Luc. ix. 66.` stays an error on its own merits: it is the
only Luke divergence in the corpus, so nothing corroborates it.

**Do not build a general J–T mapping table from the measured offsets** — they come from citations,
not from a Bible, one to four per chapter. The QA report's new **offset-corroboration table** is
the evidence, not a converter.

### ⚠ A pre-existing ledger bug, found by comparing rows to records

`index/citations.tsv` had **5,817 lines for 5,809 records.** Four citations wrap a line in the
source (`Num.` / newline / `xxxv. 31.`) and the writer collapsed tabs but not newlines, so each
wrote **one record across three rows**. Invisible in every headline count printed to date, and
fatal to `build-index-json.py`, which was about to read this file a line at a time.

Fixed (all whitespace collapsed) and now guarded by a **second census assertion**: rows must equal
records and every row must have the full field count. The first census assertion checks the chunk
roster; this one checks the file's own shape. `--all` now reports 5809 rows for 5809 records.

### Where the thirteen out-of-range now stand

| | |
|---|---|
| **Versification, not error — reclassify (6)** | `Eccles. ii. 27` · `vii. 30` · `ix. 20` · `ix. 22` · `xii. 15` · `Lev. v. 21` |
| **Error, plate-confirmed in an earlier session (5)** | `Luc. ix. 66` · `2 Reg. vi. 35` · `Deut. v. 38` · `Psal. iii. 9` (En) · `1 Kings xxvii. 29` (En) |
| **Still unread — need a plate (1)** | `et xi. 32` (ddc-2-13 la ¶47, carried book) |

**Job 2 of the resume file shrank from eight unread to one.** `Isa. lviii. 56` was settled while
coding the rule below — the English reads `lviii. 5, 6`, so the Latin dropped a comma rather than
mis-setting a number. The one survivor, `et xi. 32`, has a *carried* book, which §4.9 makes the
likelier defect.

---

## 9. Steps 4 and 5 are DONE — 2026-08-28

`tools/build-index-json.py` → `site/src/data/scripture/*.json` (63 files, ~4 MB), and
`/scripture` + `/scripture/[book]` are live in the nav. **5,467 loci across 62 books, 281
showing a layer divergence.** The builder computes nothing about citations; it regroups the
ledger and renders (§5).

**A locus is a citation, not a record.** Where the ledger paired the two layers, one entry
carries both printed forms and is filed under the `witness_target`. Both numbers are shown,
neither corrected.

### ★★ Suspect pairings — a claim the index must not make on its own

`align()` pairs by position inside a paragraph, and in a paragraph of twenty proof-texts one
insertion slides everything after it. Harmless in a divergence *report*, which a reader judges.
Not harmless in the index, where a merged pair **asserts that two printed numbers are one
verse**. La `Psal. xxv. 22.` had been paired with En `iii. 8.` — different verses — and merging
filed Milton's Ps 25:22 under Ps 3:8. That is not a divergence to display; it is a false
statement about where Milton cites.

So a pair now carries `pair_confidence`. **Plausible** = same book, and either the same chapter
within six verses or an adjacent chapter (the real boundary displacements of §6b are always
adjacent). **Suspect** = anything else: still reported as a divergence row, never merged, never
allowed to set a witness. 342 of 359 pairs are plausible; the 17 suspects have their own QA
section and want a reader, because they are a genuine mixture —

- **real findings** the pairing got right: `Isa. lviii. 56` vs `lviii. 5, 6` (the dropped comma),
  `Isa. xxxi. 2` vs `iii. 1` (already plate-confirmed at 400 dpi in II.iii), `1 Thess. v. 9` vs
  `i. 9`, and `Psal. cxiv. 2` vs `xciv. 2`, which looks like a printed transposition;
- **alignment slips**: `Psal. lv. 18` vs a bare `v. 3`, `cap. xvi.` vs `xxxi. 14.`

Telling them apart needs the paragraph in view. Do not resolve them from the table alone.

### Deep links, and the two bugs found by testing them

Each witness links to `/browse/<book>/<chapter>#<chunk>-<layer>-p<N>`. The anchor is scoped by
**chunk**, because a chapter transcribed in parts restarts `{¶N}` at 1 in each part (§8d);
`para_anchor()` here must stay in step with `anchorId` in `text-reader.tsx`.

**The acceptance test is that every anchor resolves**, checked against the built HTML: **5,809
references, 0 unresolved.** Run it after any change to either side. It found two defects that
nothing else would have:

1. **81 paragraphs carried no `¶` marker and no anchor.** The reader matched `^{¶N}` at the very
   start of a block, so any paragraph whose page break falls inside the block
   (`<!-- p.14 -->` newline `{¶11} Natura autem …`) lost its marker — silently, since M2. Fixed
   in `text-reader.tsx`; the page comment is handed back to `renderInline`.
2. **Five paragraph pairs in `ddc-2-13` were missing the blank line between them**, so each pair
   rendered as one run-on paragraph and the second lost its marker. Separators inserted, no words
   touched (verified: the file is identical ignoring whitespace). Corpus-wide there are now zero
   blocks carrying more than one paragraph marker — worth re-checking as chapters land.

### Known limitation, stated rather than special-cased

Where the **English** is the erroneous side, the witness inherits the error: En `Psal. iii. 9.` is
a printed mistake (§6b) and the pair is filed under Ps 3:9 rather than the Latin's correct Ps 3:7.
Both forms are displayed, so nothing is hidden, and the rule stays simple. Revisit only if the
error list grows.

### Owed next

Step 6 — backfill each new chapter as it lands, and add the index step to M3-RUNBOOK §2.
The `/scripture` pages are unstyled beyond the existing card/meta classes and the About and
Rights copy is still M2 placeholder (M5).

## 10. ★★★ The seventeen suspect pairings, READ — 2026-08-28

All seventeen were read with both layers' paragraphs in view. The headline is not the verdicts —
**ten of the seventeen are not slips at all**, and every one of those ten was already caught by
hand and is already in its chunk's Notes, which is the strongest evidence yet that the
transcription front is doing its job. The headline is what the other seven exposed: **the parser
has four defects, three of which put confidently-wrong targets into the live index**, and it took
a suspect list to find them because each one is silent.

### 10.1 ✅ FIXED — `ROMAN_RE` could not see Psalm 88

`ROMAN_RE` was `[ivxlc]{1,7}`. `lxxxviii` is eight characters, so **every citation of Psalm 88 was
invisible to the parser in both layers** — `ddc-2-04-b` ¶9 La `et lxxxviii. 14.` and En
`lxxxviii. 13.`, neither indexed, neither reported. Nothing failed; the records simply were not
there. `cxxxviii` (Ps 138) would have gone the same way and does not yet occur.

Merely lengthening the class is not the fix: `civili` is six letters drawn from the roman set, and
the class is loose enough already that only the 7-character cap was holding such words out. The
numeral is now **spelled out well-formed** for the range 1–199, which covers every chapter and
psalm in the canon, with a lookahead forbidding the empty match that the naive spelling allows.
Corpus effect, verified by diffing the ledger: **exactly the two intended rows, +5809 → 5811, and
no other line changed.**

### 10.2 ★★ OPEN, and Wilson's to rule — the English `v.` is NOT always *versus*

CONVENTIONS and the parser both hold that in the English layer `v.` is always the verse
abbreviation and never the roman 5 — the asymmetry that is supposed to let the English settle the
Latin's ambiguous `et v. N`. **It is false, and the chunk Notes had already said so before the
index existed.** `ddc-1-02` Notes: La ¶27's `et v. 5` is Psalm **V**, and En ¶28's answering
`v. 4.` is Ps 5:4 under KJV versification. The parser reads that same En `v. 4.` as verse 4 of the
carried Psalm 103 and files **Ps 103:4** — a target Milton did not cite.

`ddc-2-17`'s Notes put it more sharply still, from the Latin side: `et v. 23` in the Isaiah run of
¶7 is **Isaiah chapter V**, verse 23 — *absolventibus improbum propter munus* is Isa 5:23 and
nothing else — and **the English prints `v. 23` unchanged** in the middle of a run where it
corrected three neighbours. Both volumes carry the ambiguity identically. The parser is the only
party to the question that thinks it is settled.

A second instance, found this session and independent of the first: `ddc-2-04-b` ¶9 En `v. 3.`
quotes *my voice shalt thou hear in the morning, O Jehovah; in the morning will I direct my prayer
unto thee* — **Psalm 5:3**, verbatim. It is filed as Ps 55:3, whose text is *because of the voice
of the enemy*. The Latin's answering `et v. 4.` is Ps 5:4 (Hebrew), one verse up, exactly as the
superscription requires.

So the index carries at least **three wrong targets** from this rule and its knock-on:
`ddc-1-02` ¶27 En `v. 4.` → Ps 103:4 (is Ps 5:4) · `ddc-2-04-b` ¶9 En `v. 3.` → Ps 55:3 (is
Ps 5:3) · and see §10.3 for the third.

⚠ Note the asymmetry in how the two layers are treated, which is the part that matters more than
any single verse: **the Latin's `et v. N` is honestly flagged and withheld from the index when it
cannot be settled — thirty such lines sit in the QA report — while the English's `v. N` is
resolved silently and always.** The English's errors of this class are therefore invisible by
construction. Whatever rule replaces the frozen one, the English `v. N` must be able to reach QA
the way the Latin's already can.

### 10.3 ★ OPEN — the Latin DOES sometimes set a bare chapter continuation

The Latin rule refuses a bare roman, and it has to: `ii`, `vi`, `li`, `ci` are ordinary Latin
words (§4.2). But `ddc-1-02` ¶27 prints `…et xxv. 6. *benignitates a sæculo.* **ciii. 11.**
*prævalet benignitas ejus…* v. 17. *benignitas Jehovæ a sæculo usque in sæculum.*` — `ciii. 11.`
with no `et`, Sumner-fashion, in the Latin volume. The parser drops it, so the following `v. 17`
carries Psalm **25** forward instead of Psalm 103 and is filed as **Ps 25:17**. The quotation is
Ps 103:17 and the English says so. That is the third wrong target.

Two instances is not a rule, and this one cannot be relaxed by fiat — the word hazard is real and
measured. What is available is a **narrow** licence: read a bare Latin roman as a continuation only
where the numeral is not also a Latin word (`ciii` is not) *and* the aligned English sets the same
chapter. That is a convention change, so it waits for a ruling.

### 10.4 ★ OPEN — `reconcile_et_v()` settles by digits, and versification defeats it

`reconcile_et_v()` accepts the English's verse reading for a pending Latin `et v. N` only when
`e["verses"] == l["verses"]`. Where the two layers sit on opposite sides of a versification offset
the digits never agree, so the record is dropped. Five confirmed casualties, each of which is a
real citation whose identity is settled by its own quotation:

| chunk ¶ | La, dropped | En, indexed | the citation really is |
|---|---|---|---|
| `ddc-1-02` ¶27 | `et v. 5.` | `v. 4.` | Ps 5:5 Heb = Ps 5:4 KJV |
| `ddc-2-04-b` ¶9 | `et v. 4.` | `v. 3.` | Ps 5:4 Heb = Ps 5:3 KJV |
| `ddc-2-17` ¶7 | `et v. 13, 14.` | `v. 16, 17.` | Eccl 10, the §6b offset |
| `ddc-2-17` ¶7 | `et v. 13.` | `v. 14` | Isa 3, ditto |
| `ddc-2-17` ¶28 | `et v. 18, 19.` | `iii. 8, 9.` | see §10.5 |

The docstring's own reasoning does not need the digits — it needs the *form*. But the form-only
relaxation is exactly what §10.2 has just shown to be unsafe, so **10.2 and 10.4 are one ruling,
not two.**

### 10.5 ★★ `ddc-2-17` ¶28 Ezekiel is versification, and the chunk's own note supplies the proof

La `Ezech. ii. 6. … **et v. 18, 19.** *ecce, dispono faciem tuam obfirmatam adversus faciem
eorum*—.` against En `Ezek. ii. 6. … **iii. 8, 9.** *behold, I have made thy face strong against
their faces*—.` One quotation, two chapter-and-verse addresses.

The chunk's Notes already carry this row — as row twelve of "SIXTEEN Latin citation errors
silently corrected", with the gloss *La's reading is impossible (Ezek. 2 has 10 vv.)*. **That
observation is the refutation of its own classification.** KJV Ezekiel 2 has exactly ten verses,
and 10 + 8 = 18: Milton's chapter 2 absorbs KJV 3:1–9 entire, so his 2:18, 19 *are* KJV 3:8, 9.
This is the chapter-boundary displacement §6b measured in Ecclesiastes, reached here by arithmetic
rather than by corpus statistics, and with no plate. **Versification, not error** — see §10.8,
because it is not the only row in that table §6b has overtaken.

### 10.6 The rest — real findings the aligner tripped over, not aligner faults

Ten of the seventeen are the aligner correctly refusing to merge a pair the two volumes really do
print differently. **All ten are already in their chunks' Notes** and want no further work; they
are listed here only so a later reader does not re-open them.

`ddc-1-02` ¶13 La `1 Thess. v. 9` — quote *Deo vivo et vero* is 1 Thess 1:9 · `ddc-2-03` ¶13 La
`cap. xxxi. 2` — *amoturus est scipionem et bacillum* is Isa 3:1, plate-confirmed · `ddc-2-04-c`
¶3, ¶11, ¶16 — `Isa. lix. 12`, the `lviii. 56` dropped comma, and the En-side `1 Kings xxvii. 29`
collapse · `ddc-2-05` ¶3 La `Psal. ix. 5, 11` — *quibus juravi in ira mea* is Ps 95:11, `xcv`
broken into `ix. 5` · `ddc-2-12` ¶12 La `et cxiv. 2` for `xciv. 2` · `ddc-2-17` ¶13 La
`Act. xiii. 3` — the Latin quotes *pontifici Dei maximo convitiaris?*, Acts 23:4 · `ddc-2-17` ¶29
La `Isa. lvii. 2, &c.` — *speculatores istius* is Isa 56:10.

Three more are aligner slides with an ordinary editorial cause and no defect behind them:

- **`ddc-2-04-c` ¶1 — Sumner reorders AND omits.** La sets `Psal. iii. 9. … et xxviii. 9. idem.
  et xxv. 22. *redime Deus Israelem*…`; En sets `Psal. xxviii. 9.` first with its text, then
  *See also iii. 8.*, and **drops `xxv. 22` altogether.** The one-slot offset runs to the end of
  the paragraph — La 21 records, En 20. Reordering was already a known category; **this omission
  is new to the log** and is recorded in the chunk's Notes.
- **`ddc-2-07` ¶4 — a prose back-reference indexed on one side only.** La `recordare scilicet ex
  illo præcepto **cap. xvi.** supra citato`; En writes it out, *according to the previous
  commandment in the sixteenth chapter*. One layer has a numeral, the other has words.
  ⚠ `SELF_REF_CUES` searches the context *before* the numeral, so a trailing `supra citato` is
  never seen. Harmless here — the reference is to Exodus 16, real scripture — but the window is
  one-sided and should be widened when 10.2/10.4 are ruled on.
- **`ddc-2-17` ¶3, ¶7, ¶28, ¶29 — Sumner resolves Milton's open ranges.** La `et xxxi.` + `v. 1` +
  `v. 10` → En `xxxi. 1—10.`; La `et xxxiii. toto cap. a v. 2.` → En `xxxiii. 2—31.`; La
  `Mal. ii. 1, &c.` + `v. 10` → En `ii. 1—10.`; La `Amos. vii. 10.` → En `vii. 10—17.` Three La
  records collapse into one En record every time, and the aligner slides by two. This is the same
  editorial act already logged at `ddc-2-04-c`'s Deut. xxvii `a v. 13. ad finem capitis` →
  `xxvii. 13—26`; ¶3 additionally has En **supplying** `Deut. xvii. 20`, which the Latin lacks.

### 10.7 ⚠ A footgun in the tool itself

`./tools/build-citations.py <chunk-id>` **rewrites `index/citations.tsv` with that chunk alone** —
the corpus ledger is silently truncated to one file. It happened once this session and was caught
only because the next query returned nothing. The ledger is derived and `--all` restores it
exactly, so nothing was lost, but a single-chunk run should either write elsewhere or refuse.
Until then: **always finish with `--all`.**

### 10.8 ★★★ OPEN — the chunks' "silently corrected error" tables predate §6b and are now stale

This is the largest thing the suspect read turned up, and it is not a parser question. It is a
question about **what the published apparatus will say Milton did.**

`ddc-2-17`'s Notes open a table with **"SIXTEEN Latin citation errors silently corrected — twice
the previous record."** Every row is called an error of Milton's that Sumner put right. Then the
note two paragraphs down observes, correctly and in its own words, that *Ecclesiastes 10 is cited
twice and is three verses low both times; Isaiah 3 is cited four times and is one verse high every
time. A single compositor's slip does not repeat with a fixed offset across a chapter.*

**§6b, written afterwards, established that a repeating per-chapter offset is exactly the signature
of Junius–Tremellius versification** — and §6b's own corpus table already names `Isa 57 (+4,
twice)` among the repeating offsets. So the chunk's evidence and the runbook's rule now point the
same way, at a classification the chunk still labels the other way. Rows in that one table that
look like versification rather than error:

| row | offset | why it reads as versification |
|---|---|---|
| Eccles. iv. 9 / iv. 13 | +4 | Eccl 4, the offset §6b measured four times |
| Eccles. x. 2, 3 / x. 5, 6 | +3 | Eccl 10, repeating |
| Eccles. [x.] v. 13, 14 / v. 16, 17 | +3 | Eccl 10, the same offset again |
| Eccles. viii. 1 / viii. 2 | +1 | §6b: La ch. 7 absorbs KJV 8:1, so La ch. 8 runs one high |
| Isa. iii. 5 · v. 13 · v. 15 · iii. 8 | +1 ×4 | Isaiah 3, four times, never varying |
| Isa. lvii. 13, 14, 17 / lvii. 9, 10, 13 | +4 ×3 | Isa 57, and §6b already lists it |
| Isa. lvii. 2 / lvi. 10 | chapter | KJV Isa 56 ends at 12; a break after 56:8 gives 57:2 = 56:10 |
| Ezech. [ii.] v. 18, 19 / iii. 8, 9 | chapter | §10.5 — 10 + 8 = 18, exactly |

That would leave the genuinely erroneous rows a much shorter list — `Act. xiii. 3` / `Acts
xxiii. 4` (which the Latin's own quotation refutes), `1 Sam. xii. 2, 3`, `Amos. ii. 11`,
`1 Sam. xiv. 29`, `Prov. xxv. 4` — and it would turn "sixteen errors, twice the record" into
something closer to five.

⚠ **Do not edit the chunk on this reasoning alone.** Three things have to happen first, in order:

1. **A ruling from Wilson**, because the two classifications make opposite claims in print about
   the same man. "Milton miscited sixteen times and his editor quietly fixed it" and "Milton cited
   a different Bible and his editor converted it" are not two phrasings of one fact.
2. **The same audit run across every chunk**, not just II.xvii. Every error table in the corpus was
   written before §6b existed, and §6b's `+1` count (79, 53% of all divergences) says this is not
   a II.xvii problem.
3. **The `divergence_class` column, not prose, as the place the answer lives** — so the site can
   render "versification" and "error" differently and the chunk Notes stop being the sole record.

**✅ RULED and CLOSED 2026-08-28 — see §11.** Wilson's ruling was to check Junius–Tremellius first
and to bring it in as a permanent source. All eight rows came back **versification**. This section
is preserved as the reasoning that led to the check; §11 is the answer.

## 11. ★★★ §10.8 RULED, and the answer came from the Bible itself — 2026-08-28

Wilson's ruling: **check Junius–Tremellius before classifying anything, and bring it into the
project as a permanent source.** Both halves are done. The verdict is not close.

### 11.1 The witness

**`testamentiveteri00trem` — *Testamenti Veteris Biblia Sacra*, Junius & Tremellius, Hanau 1603,
typis Wechelianis. 1252 leaves, Latin, public domain, OCR and page images both.** It is the Bible
Milton cited. `tools/fetch-jt.sh` pulls the text into `raw/jt/`; `tools/jt-page.py <leaf>
[--band y0 y1] [--x x0 x1] [--scale]` fetches and crops a leaf image, because the numbers cannot
be read any other way.

⚠ **The OCR is unusable for this question and nearly unusable for any question.** Verse numbers
are set small beside the text and the marginal scholia bleed into the column; a search for
`Amotsi`, `Coheleth` and `Jehezkelis` returned nothing at all. Every reading below is off the
**page image**. Treat the text dump as the fetch script says: a finding aid, and a poor one.

**Calibration** (also recorded in STRUCTURE.md): each scan leaf is one two-page **opening**, so
`printed ≈ (leaf − 188) / 2`, i.e. `leaf ≈ 2 × printed + 188`, for the Old Testament sequence.
Verified against five heads carrying printed folios: Ps 97 (leaf 480 / p. 145), Cant 8 (540 /
175), Jer 2 (600 / 206), Ezek 8 (660 / 236), Dan 11 (720 / 266). ⚠ The volume carries the New
Testament after the Old, in parallel columns, with **its own printed sequence** — leaf 800 is
Matthew 12 at printed 21. This calibration is the OT's only.

### 11.2 ★★★ The mechanism, and it is not "a defective copy"

`ddc-2-17`'s note reasoned that a repeating offset means *"the error is in the source, not in the
setting"* — right that it is systematic, wrong about what the system is. **Junius–Tremellius
divides chapters at different points from the KJV, and at least once carries the verse count
straight across a chapter break.** The offsets Milton's citations show are consequences of those
divisions. That is why an offset is constant within a chapter and different between chapters —
the fact §6b measured from the corpus without being able to say why.

**Ecclesiastes 4** (leaf 528, printed 169). J–T's chapter III runs on past the KJV's break:
verses **23, 24, 25, 26** are KJV 4:1, 2, 3, 4. J–T's own `CAPUT IIII`, with its argumentum,
then opens lower on the same page at **verse 1** = KJV **4:5** — *Stolidus complicat manus suas,
& consumit carnem suam*, the fool folding his hands. Verse 2 = KJV 4:6, *Melior est plena vola
quietis*.
→ **offset +4, so J–T 4:9 = KJV 4:13.** Milton's `Eccles. iv. 9`, Sumner's `iv. 13`. Exact.

**Ecclesiastes 10** (leaf 533, printed 172). Six consecutive confirmations on one page: J–T 8 =
KJV 10:11 (*Si momorderit serpens*), 9 = 10:12, 10 = 10:13, 12 = 10:15, and decisively
**13** = KJV **10:16** *Hei tibi regio, cujus rex puer est* and **14** = KJV **10:17** *O te
beatam regionem*.
→ **offset +3, so J–T 10:2, 3 = KJV 10:5, 6 and J–T 10:13, 14 = KJV 10:16, 17.** Both of
II.xvii's Ecclesiastes-10 rows, and with them the cross-chunk claim that II.xv carries "the
identical error."

**Isaiah 3** (leaf 546, printed 177–178), confirmed on both halves of the chapter:

| J–T | text | KJV |
|---|---|---|
| 5 | *Daturus autem sum pueros principes eorum, & facinorosi dominabuntur in eos* | 3:4 |
| 8 | *Jurabit die illo dicendo, non essem obligaturus … ne ponatis me ductorem populi* | 3:7 |
| 11 | *Dicite justo, bene esse; nam fructu actionum suarum fruituros esse* | 3:10 |
| 13 | *Populum meum opprimentium quisque parvulus, & fœminæ dominium exercent* | 3:12 |
| 15 | *Jehova ad judicium advenit contra Seniores populi sui* | 3:14 |
| 19 | *Tempore illo amovebit Dominus ornamentum istud perischelidum* | 3:18 |

→ **offset +1 throughout.** J–T's own scholion divides the chapter at *v. 17* between men and
women, which in the KJV is 3:16, the daughters of Zion — the offset confirmed a third way, from
the editors' prose.

**Ezekiel 3** (leaves 655–656, printed 233–234), and this one is different in kind. J–T's chapter
II ends at **10**, exactly as the KJV does. Then `CAPUT III` opens — **and its first verse is
numbered 11, not 1**: *Edixit igitur mihi, fili hominis, quod præsens est tibi comede: comede
volumen hoc* = KJV 3:1. The count runs on unbroken to **25** = KJV 3:15 (*veni ad multitudinem
deportatam Thel-abib … desedi illic septem dies*).
→ **J–T Ezek 3:18, 19 = KJV 3:8, 9.** Milton wrote `Ezech. ii. 6.` and then `et v. 18, 19.`, and
in J–T that is not ambiguous at all — the numbers do not restart, so verse 18 is verse 18 whether
you name the chapter ii or iii. **Which is precisely why Sumner had to relabel it `iii. 8, 9`.**

⚠ Neither of the two explanations previously on record is right. The chunk's *"La's reading is
impossible (Ezek. 2 has 10 vv.)"* is true and irrelevant — the verse is in chapter III. §10.5's
*"chapter 2 absorbs KJV 3:1–9"* is simply wrong; chapter 2 ends where the KJV's does. Both
reached the right verdict by the wrong route, which is the thing a plate is for.

### 11.3 ✅ ALL EIGHT settled — the table is closed

**Every disputed row is confirmed versification at the source.** Counted as `ddc-2-17` counts them,
that is **eleven of its sixteen**, against **five** genuine errors. The claim "sixteen errors,
twice the previous record" does not survive; II.v's eight holds the record, and II.xvii's real
distinction is that it is the chapter where the treatise's versification shows most clearly.

The last three, read after the first pass:

**Isaiah 57** (leaf 590, printed 201) — **one chapter division settles two rows.** J–T's chapter
LVI ends at verse **8** (= KJV 56:8, *congregantis depulsos Jisraelis*). `CAPUT LVII` then opens at
KJV **56:9**: J–T 1 = *Omnes bestiæ agrestes, venite ad comedendum* (KJV 56:9), J–T **2** =
***Speculatores istius cæci*** (KJV **56:10**) — the very words Milton quotes.
→ `Isa. lvii. 2 / lvi. 10` is versification. And since KJV 56 ends at 12, J–T 57:5 = KJV 57:1 and
the rest of the chapter runs **+4**, giving `lvii. 13, 14, 17 / lvii. 9, 10, 13` at a stroke.
J–T's own scholion confirms the second half independently: *"deinde populi totius negligentis
justos, vers. 5. & 6."* — the neglect of the righteous is KJV 57:1.

**Ecclesiastes 8** (leaf 531) — J–T **8:14** = KJV **8:15**, *Quapropter laudaveram ego lætitiam,
nullum esse bonum homini sub sole, nisi ut comedat ac bibat & lætetur*. **+1**, so Milton's
`Eccles. viii. 1, &c.` is KJV 8:2, the king's commandment and the oath of God, which is what
Sumner prints.

### 11.3a ★★ How the volume prints its divisions — and a free confirmation of §6b

Ecclesiastes' leaf 531 shows the compositional habit that makes all of this legible: **J–T sets
its own chapter division with an italic argumentum, AND sets the received chapter marker where
that falls.** `CAPUT IX` therefore appears **twice** on the page. The verse numbers follow J–T's
division and never the received one — which is exactly why an offset is stable inside a chapter.

The same page gives **Ecclesiastes 9 at +2** for nothing: J–T's verse **3** is KJV **9:1** (*Nam
totum hoc condidi in animo meo … justos & sapientes, factaque eorum in manu Dei ipsius*), the
chapter having absorbed KJV 8:16–17 as its verses 1–2. J–T's scholion argues the case in its own
voice — *"duos hosce versus omnino ad sequentia pertinere res ipsa loquitur: nam hoc demum loco
Schelomo transitionem facit."* **§6b measured Eccl 9 as +2 three times from the corpus. It is now
confirmed at the source, and it was not even the thing being looked for.**

Running tally of J–T divisions established, all from page images — the first rows of the table
§11.4 asks for:

| book | J–T chapter begins at | effect |
|---|---|---|
| Eccl 4 | KJV 4:5 | +4 |
| Eccl 8 | KJV 8:2 | +1 |
| Eccl 9 | KJV 8:16 | +2 |
| Eccl 10 | KJV 10:4 | +3 |
| Isa 3 | KJV 2:22 (inferred from a constant +1) | +1 |
| Isa 57 | KJV 56:9 | +4 after KJV 56 ends |
| Ezek 3 | KJV 3:1, but the verse count does NOT restart | +10 |

### 11.4 What this changes beyond II.xvii

1. **Every error table in the corpus predates §6b and now predates this.** The audit runs
   corpus-wide; II.xvii was the case that surfaced it, not the extent of it.
2. **`divergence_class` must become a column**, not prose in a Notes paragraph, so the site can
   render *versification* and *error* differently and the classification stops being re-derivable
   only by reading English.
3. **A J–T chapter/verse-count table is now buildable** and is the right long-term instrument —
   `tools/versification.json` answers "could this verse exist?"; a J–T table would answer "what
   did Milton's Bible call it?", which is the question the corpus keeps asking. Every offset
   established above is a row in it.
4. ⚠ **The `et v. N` problem is smaller than it looked.** Ezekiel shows J–T running verse numbers
   across a chapter break; where it does, Milton's bare `et v. N` is not ambiguous in his Bible
   even though it is ambiguous in ours. That does not dissolve §10.2 — the English `v.` question
   is untouched — but it means some of the thirty QA lines are answerable from J–T rather than
   from the quotation alone.

## 12. ★★★ The corpus-wide audit, first pass — 22 rows move, in 7 chunks

§11 settled II.xvii. This is the same question asked of every other chunk, and the answer is the
same only more so: **the "silently corrected La error" tables across the corpus are substantially
misclassified, and the corrections are not distributed at random — they cluster in a handful of
chapters, because a chapter division is a property of the chapter, not of the citation.**

### 12.1 The method, and why it is cheap

**Work book-by-book, never chunk-by-chunk.** One chapter division settles every citation of that
chapter anywhere in the treatise. Isaiah 57 took two rows in two different chunks with one read;
Ecclesiastes' leaf 531 gave three chapters at once. Sort the corpus's divergences by book and
chapter, take the chapters with a **repeating** offset first (§6b's list is the ready-made
worklist), and read the chapter boundary off the page image.

**Eight of the 22 rows below needed no new reading at all** — they fell out of divisions §11 had
already established, by arithmetic. Always run that check before fetching anything.

### 12.2 The J–T chapter divisions established so far

Every row read off a page image. `→` is what the division does to a citation: J–T number **plus**
the offset gives the KJV number.

| book ch. | J–T's chapter begins at | offset | leaf |
|---|---|---|---|
| Num 23 | KJV **22:38** | **+4** | 154 (folio 137) |
| Prov 12 | KJV **12:2** | **−1** | 512 (printed 161) |
| Eccl 2 | KJV **1:18** | **+1** | 526 (printed 163) |
| Eccl 4 | KJV **4:5** | **+4** | 528 (printed 169) |
| Eccl 8 | KJV **8:2** | **+1** | 531 |
| Eccl 9 | KJV **8:16** | **+2** | 531 |
| Eccl 10 | KJV **10:4** | **+3** | 533 (printed 172) |
| Isa 3 | KJV **2:22** (inferred from a constant +1) | **+1** | 546 (printed 177–178) |
| Isa 44 | KJV **44:6** | **+5** | 581 |
| Isa 57 | KJV **56:9** | **+4** past KJV 56:12 | 590 (printed 201) |
| Ezek 3 | KJV 3:1, **but the verse count does not restart** | **+10** | 656 (printed 234) |

Readings that fixed the four new ones:

- **Numbers 23.** J–T's ch. XXII ends at *an verò non possum honore afficere te?* (KJV 22:37);
  `CAPUT XXIII` then opens at KJV **22:38**, *Dixit verò Bilham Balako, ecce veni ad te … illud
  ipsum verbum quod indiderit Jehova ori meo, eloquar*, and the next verse is Kirjath-huzoth
  (KJV 22:39). KJV 22 ends at 41, so J–T 23:5 = KJV 23:1.
- **Proverbs 12.** J–T 12:18 = KJV 12:19 (*Labium verax stabilitur in æternum*), and the chapter
  closes at **27** = KJV 12:28 where the KJV closes at 28. Ten consecutive verses check.
- **Ecclesiastes 2.** J–T's ch. I closes at **17** = KJV 1:17, so `CAPUT II` takes KJV 1:18.
- **Isaiah 44.** J–T's ch. XLIII runs on to **20** = KJV 44:5 (*Hic dicet, Jehovæ sum … de nomine
  Jisraëlis cognominabit*); `CAPUT XLIV` opens at KJV 44:6, which is the running head's own
  *eum nullum est Deus*.

### 12.3 The 22 rows, and where they are

Each was printed as a **La error silently corrected by Sumner**. Each is versification. Marked in
the chunks' Notes; the chunk tables themselves are left standing with a correction block, because
rewriting seven tables by hand is how a transcription error gets introduced.

| chunk | row | chapter | check |
|---|---|---|---|
| `ddc-1-02` | Isa. xliv. 1 / xliv. 6 | Isa 44 | 1+5 |
| `ddc-1-02` | Num. xxiii. 23 / xxiii. 19 | Num 23 | 23−4 |
| `ddc-2-04-c` | Num. xxiii. 12 / xxiii. 8 | Num 23 | 12−4 |
| `ddc-2-05` | Isa. lvii. 9, &c. / lvii. 5 | Isa 57 | 9−4 |
| `ddc-2-05` | et xliv. 5, &c. / xliv. 10 | Isa 44 | 5+5 |
| `ddc-2-05` | Isa. xliv. 12, 13 / xliv. 18 | Isa 44 | 13+5; En narrows to the second verse |
| `ddc-2-05` | et xliv. 20 / xliv. 25 | Isa 44 | 20+5 |
| `ddc-2-05` | Num. xxiii. 27 / xxiii. 23 | Num 23 | 27−4 |
| `ddc-2-08` ¶23 | Eccles. ii. 3 / ii. 2 | Eccl 2 | 3−1 |
| `ddc-2-08` ¶26 | Prov. xii. 15 / xii. 16 | Prov 12 | 15+1 |
| `ddc-2-08` ¶27 | et xii. 13 / xii. 14 | Prov 12 | 13+1 |
| `ddc-2-09` ¶16 | Eccles. ii. 27 / ii. 26 | Eccl 2 | 27−1 |
| `ddc-2-09` ¶16 | et iv. 4 / iv. 8 | Eccl 4 | 4+4 |
| `ddc-2-09` ¶16 | Isa. lvii. 21 / lvii. 17 | Isa 57 | 21−4 |
| `ddc-2-09` ¶21 | Eccles. iv. 1, 2 / iv. 5, 6 | Eccl 4 | 1+4, 2+4 |
| `ddc-2-09` ¶27 | Prov. xii. 8 / xii. 9 | Prov 12 | 8+1 |
| `ddc-2-09` ¶33 | Isa. iii. 10 / iii. 9 | Isa 3 | 10−1 |
| `ddc-2-11` ¶26 | Prov. xii. 9 / xii. 10 | Prov 12 | 9+1 |
| `ddc-2-11` ¶27 | Prov. xii. 9 / xii. 10 | Prov 12 | 9+1 |
| `ddc-2-11` ¶35 | Eccles. iv. 5, &c. / iv. 9, &c. | Eccl 4 | 5+4 |
| `ddc-2-15` | Isa. iii. 6 / Isai. iii. 5 | Isa 3 | 6−1 |
| `ddc-2-15` | Eccles. x. 2, 3 / x. 5, 6 | Eccl 10 | 2+3, 3+3 |

★ **`ddc-2-15` and `ddc-2-17` share the `Eccles. x. 2, 3` row**, and II.xvii built an argument on
the coincidence — that "the error travels with the passage" and that Sumner corrected it twice
independently. Both chunks are now corrected: it is one man citing one Bible twice.

### 12.4 What is left of the audit

**Not** every "La error" in the corpus is now suspect. The five that survive in II.xvii survive
because their own quotation refutes them (`Act. xiii. 3` quotes Acts 23:4), and the same test
disposes of most singletons. What wants the J–T treatment is **any chapter cited more than once
with a constant offset** — §6b's `+1` bucket alone holds 79 divergences, most of them Psalms,
where the Hebrew superscription already explains the pattern and a single leaf per psalm would
confirm it.

Still unread, in rough order of how many rows each would move:
- **The Psalms**, as a class. 53 of 57 Psalm divergences are +1 or +2, and §6b has already matched
  the split to one-line and two-line superscriptions. This does not need 57 leaves; it needs a
  handful, plus a note that the superscription rule is the mechanism.
- **Isa 44 is done, but `ddc-2-05` claims four more Isaiah errors** in chapters not yet read.
- `ddc-2-03`'s three (`2 Reg. vi. 35`, `Deut. v. 38`), `ddc-2-06`'s `2 Sam. xxi. 2, 3`
  ("neither side is right"), `ddc-2-11`'s six.

## 13. ★★★ The Psalms are settled as a class, and II.xi's table inverts completely

### 13.1 ★★★ One opening proves the whole Psalms mechanism — leaf 458

§6b inferred from the corpus that Psalm divergences are Hebrew superscription-counting: `+1` where
the psalm's title runs one line, `+2` where it runs two. **Leaf 458 shows it happening**, and shows
both cases side by side, which is why no further Psalm reading is needed.

**`PSALMUS LIIII`** numbers its superscription as **two verses**:
- **1** *Magistro symphoniæ à fidium, ode didascalica Davidis:*
- **2** *Quum venientes Ziphæi dixissent Schauli, an non David latitat apud nos?*
- **3** *Deus propter nomen tuum serva me* = KJV **54:1**
- **7** *Redde istud malum observatoribus meis, per veritatem tuam succide eos* = KJV **54:5**

→ **+2**, and `ddc-2-12`'s `et liv. 7. / liv. 5.` is versification.

Directly below it on the same page, **`PSALMUS LV`** numbers its shorter superscription as **verse
1 only** — *Magistro symphoniæ à fidium, ode didascalica Davidis.* → **+1**, confirmed on the
facing page nine times over, including **J–T 55:18 = KJV 55:17**, *Vespere & mane atq; meridie
meditabor & perstrepam, donec audiverit vocem meam*.

★ **That last one is `ddc-2-04-b` ¶9's `Psal. lv. 18. / lv. 17.` — one of the original seventeen
suspect pairings in §10.** The thread that began with an aligner slide ends at the page of the
Bible that explains it.

**Two adjacent psalms, two different offsets, one visible cause.** The rule is now source-confirmed
and can be applied to the corpus's ~57 Psalm divergences without reading 57 leaves: **count the
lines of the superscription.** Where a psalm has none (Ps 1, 2, 33, 91, …) there is no offset, which
is why 4 of the 57 do not fit.

### 13.2 ★★★ `ddc-2-11`'s six "Latin citation errors" are SIX versification cases

That chunk states: *"Six corrections, of five distinct kinds of slip. **None is versification:
Junius–Tremellius and the KJV number all six of these places alike**, so each is simply a wrong
digit in the Latin volume that Sumner mended without a word."*

**The claim is a perfect inversion.** It was made without access to J–T — reasonably, since the
volume was not in the project until today — and every one of the six is J–T's numbering:

| ¶ | La | En | J–T | offset |
|---|---|---|---|---|
| 9 | 1 Sam. **xvi. 2** | xvi. 1 | J–T 16:2 = KJV 16:1 | **+1** |
| 24 | Gen. **xxvii. 43** | xxvii. 41 | J–T Gen 27 runs +2 throughout | **+2** |
| 26 | Prov. **xii. 9** | xii. 10 | §12.2 | **−1** |
| 27 | Prov. **xii. 9** | xii. 10 | §12.2 | **−1** |
| 35 | Eccles. **iv. 5** | iv. 9 | §12.2 | **+4** |
| 37 | Judic. **xi. 5** | Judges xi. 3 | J–T Judg 11 runs +2 | **+2** |

- **1 Sam 16 is the clearest layout evidence in the volume.** J–T prints verse **1** — *Posteà non
  perrexit Schemuel invisere Schaulem … quia Jehovam pœnitebat regem constituisse Schaulem super
  Jisraelem* (KJV 15:35) — **above** the `CAPUT XVI` rubric, and numbers KJV 16:1 as **2**. The
  rubric marks the *received* division; the numbers follow J–T's own. Its scholion says so:
  *hunc versum ad sequentia pertinere res ipsa docet.*
- **Genesis 27**: J–T 7 = KJV 27:5, 8 = 27:6, 9 = 27:7, 13 = 27:11, 21 = 27:19. So 27:43 = KJV
  27:41, Esau's envy.
- **Judges 11**: J–T 35 = KJV 11:33, 36 = 11:34, 37 = 11:35, 41 = 11:39. So 11:5 = KJV 11:3.

⚠ The chunk drew a methodological lesson from this table — *"reading the Latin for suspect
citations is a way of knowing where to look, never a census. The English layer is the
instrument."* **That lesson is still right, and now needs one clause added: the English layer
tells you WHERE the two volumes differ; only the Bible tells you WHY.** Its other conclusion —
that "both halves of the doubled `Prov. xii. 9` were wrong" — dissolves: both halves were right.

### 13.3 ⚠ A correction to §12.4's own method

§12.4 said the quotation test "disposes of most singletons" — that where a citation's quoted words
identify a verse, a divergence is settled as error. **That is unsound as stated, and I should not
have written it.** A quotation identifies the verse in *KJV* terms; it cannot distinguish a wrong
digit from a small numbering offset, because under an offset Milton's number is *also* pointing at
those same words in his own Bible. `ddc-2-11`'s table had exactly that shape — a "what the text
quotes" column, correct in every row, and six wrong classifications resting on it.

The test is sound only where **the gap is too large to be a chapter division**: `Act. xiii. 3`
against Acts 23:4 is ten chapters, and no versification does that. **A gap of one to five verses
is never settled by the quotation. It is settled by the page.**

### 13.4 Divisions added this pass

| book ch. | J–T's chapter begins at | offset |
|---|---|---|
| Gen 27 | KJV 26:33 (inferred from a constant +2) | **+2** |
| Judg 11 | KJV 10:17 (inferred from a constant +2) | **+2** |
| 1 Sam 16 | KJV **15:35**, printed above the rubric | **+1** |
| Ps 54 | superscription numbered as **2 verses** | **+2** |
| Ps 55 | superscription numbered as **1 verse** | **+1** |
| *Psalms generally* | **the superscription is numbered** | **+1 / +2 by title length** |

## 14. ✅ `divergence_class` — the classification is data now, not prose

§10.8's third requirement, and the one that keeps the other two from decaying. Until now, whether a
citation divergence was Milton's error or his Bible's numbering lived in a paragraph of a chunk's
Notes: unrenderable, uncountable, and re-derivable only by reading English.

### 14.1 What was built

- **`tools/jt-divisions.json`** — the sixteen Junius–Tremellius chapter divisions read off the page
  images, each with its evidence quoted and its leaf. `status` is `read` (a boundary put in view)
  or `inferred` (a constant, content-checked offset across the chapter). **Nothing here is a
  guess; a guess does not go in the file.**
- **`tools/jt_map.py`** — `to_kjv(book, ch, verse)` and `classify(...)`. One entry says *J–T's
  chapter X begins at KJV Y and its first verse carries number N*; everything else follows by
  walking the KJV verse counts already in `versification.json`, crossing chapter boundaries.
  **That one shape covers all four mechanisms observed** — a chapter starting early or late, a
  count that does not restart (Ezek 3), a numbered superscription (Ps 54/55), and a verse printed
  above the received rubric (1 Sam 16). Run it directly for a self-test: **17/17 of the hand-made
  findings reproduce mechanically**, including both hard cases.
- **`divergence_class` + `divergence_why`** in `index/citations.tsv`, and two new sections in
  `index/citation-qa.md`.

### 14.2 The classes, and what each is allowed to assert

| class | pairs | asserts |
|---|---|---|
| `versification` | 40 | a **read** division maps the Latin onto the English exactly |
| `versification-predicted` | 52 | no division read, but the mechanism is known and the shape fits — Psalms `+1`/`+2`, §13.1 |
| `unchecked` | 128 | no division read, no known mechanism. **NOT a claim of error** |
| `anomaly` | 5 | a division **is** read and does not explain it — these earn a reader |

⚠ **`unchecked` is deliberately not `error`.** Calling a divergence Milton's mistake is a claim
about a real person that goes into print, and the only thing entitled to make it is a page image.
The column will say `unchecked` forever rather than guess.

### 14.3 Two bugs the first run exposed, both in the classifier

- **Identical numbers are not a numeric divergence.** `Psal. lv. 5, 6, 7.` against `lv. 5—7.` is a
  syntax row (list vs dash-range); running the map over it manufactured an anomaly where nothing
  disagrees. Now skipped. This is what dropped `unchecked` from 262 pairs to 128.
- **The English narrows constantly.** `Isa. xliv. 12, 13.` against `xliv. 18.` is one citation with
  Sumner keeping only its last verse. A narrowed English is still versification, so a `want` that
  is a strict subset of the mapped Latin now passes.

### 14.4 ★★ The anomaly class immediately found a new Latin error

`ddc-2-13` ¶6, and it is the **first citation error the tooling has found rather than
reclassified.** The paragraph carries two things at once:

1. **Sumner reordered.** The pairs go by quotation, not position: La `Prov. xii. 21.`
   (*abominationi sunt Jehovæ labia fallacia*) answers En `v. 22.`, and La `v. 17.` (*efflat
   veritatem*) answers En `Prov. xii. 17.`
2. **`Prov. xii. 21` is correct** under the −1 division. **`v. 17` is a real slip**: J–T numbers
   *Efflat veritatem* as **16** (leaf 511, in a run checking at every verse from 8 to 18). Milton's
   own Bible calls it 16 and he wrote 17.

★ **Why no earlier pass caught it: both layers print the digit `17`.** Sumner's is right in KJV
terms, Milton's is wrong in J–T terms, and they coincide. **A divergence table cannot see an error
the two layers happen to agree on** — only the third witness can.

Leaf 511 also confirmed `ddc-2-11` ¶26/¶27 verbatim: J–T Prov 12:**9** is *Curat justus vitam
jumenti sui*, the very words that chunk's "what the text quotes" column gives for KJV 12:10.

### 14.5 What this leaves

The 128 `unchecked` pairs are the remaining audit, and they are now enumerable rather than
anecdotal — group them by book and chapter, take the ones with repeating offsets, read the
division, and the class flips wholesale. The `anomaly` list is the standing worklist; it should be
re-read after every division added, because adding a division can move a pair either way.

## 15. The seven repeating-offset chapters, read — 20 more pairs, and II.xvii falls to three

§14 made the audit enumerable. This is the first sweep run against that list: group the
`unchecked` pairs by book and chapter, take the chapters cited **more than once with a consistent
offset** (§6b's signal, now computable), and read the division. Seven chapters, twenty pairs, one
leaf each.

| book ch. | J–T's chapter begins at | offset | pairs | evidence |
|---|---|---|---|---|
| Gen 12 | KJV **12:4** | −3 | 2 | the received `CAPUT XII` carries the count on (33 = KJV 12:1); J–T's own restarts at 12:4 |
| Exod 16 | KJV **15:27** | +1 | 2 | J–T's own `CAPUT XVI` opens at *Deinceps venerunt Elima* |
| 1 Sam 14 | KJV **13:23** | +1 | 4 | J–T 3 = KJV 14:2 *sub malo punica quæ est in Migrone*, checked to 10 |
| Neh 10 | KJV **9:38** | +1 | 3 | J–T's own `CAPUT X` opens at *pepigimus constitutionem federis*; the received rubric follows |
| Dan 6 | KJV **5:31** | +1 | 5 | the chapter ends at **29** = KJV 6:28, where the KJV ends at 28 |
| Hos 12 | KJV **11:12** | +1 | 2 | J–T 5 = KJV 12:4 *flevit & supplex oravit eum*, the running head's *Jaħakob flevit* |
| Amos 2 | KJV **2:4** | −3 | 2 | ch. I runs to 15; the received `CAPUT II` carries on as 16–18; J–T's own restarts at 1 |

`versification` 40 → **60 pairs**; `unchecked` 128 → **108**; **no new anomalies** — the seven
divisions explain all twenty cleanly, which is itself a check on them.

### 15.1 ★★ Two more of II.xvii's "genuine errors" fall, and the chapter is down to three

`Amos. ii. 11 / Amos ii. 14` and `1 Sam. xiv. 29 / xiv. 28` were both in the surviving errors table
after §11 and §13. Both are versification. **II.xvii now claims three errors where it claimed
sixteen** — and one of the three, `Prov. xxv. 4`, has an unread division and a single instance, so
it is not yet settled either.

`ddc-2-15`'s `1 Sam. xiv. 45 / xiv. 44` goes with them. Its note reads *"**La is a printed error**
— omnino moriturus es, Jonathan is Saul's speech at 14:44"*. The quotation is identified correctly
and the conclusion does not follow: **that is §13.3's failure mode exactly**, a quotation read in
KJV terms and taken to settle a one-verse gap. Corrected in place.

### 15.2 ★ The volume's own cross-references corroborate the table

Amos 1's scholion 34, on Edom's perpetual anger, cites **`Gen. 27. 43.`** — in J–T's own numbering.
The table built from page images maps J–T Gen 27:43 to KJV 27:41, *Esau hated Jacob … I will slay
my brother*, which is precisely the text the note is arguing from. **J–T's internal apparatus is
itself a check on the divisions**, and a free one: every `sup.`/`infr.` reference in the scholia is
a testable assertion about this table. Worth a pass of its own if the table ever needs auditing.

### 15.3 ★★ The double rubric is now confirmed as the volume's standard habit

Seen once it looked like an oddity of Ecclesiastes. It is the house style, now attested in
**Gen 12, Exod 16, Neh 10, Amos 2, Eccl 4, Eccl 9 and 1 Sam 16**: J–T prints **its own** chapter
division with an italic argumentum **and** the received rubric where that falls, and **the verse
numbers follow J–T's division, never the received one.** In Genesis the editors say why, in their
own voice — *"Quamobrem tres hosce v. cum antecedentibus visum est conjungere"*, "wherefore it
seemed right to join these three verses with what precedes."

That habit is what makes this volume readable at all for our purpose: **the boundary is visible on
the page rather than inferred from an offset.** It is also why `status: read` is worth
distinguishing from `status: inferred` in `jt-divisions.json` — a read boundary is a fact about the
book, an inferred one is a fact about a run of verses.

### 15.4 What remains

**108 `unchecked` pairs**, now with **34 chapters carrying a single divergence each** — no
repeating offset to go on, so each needs its own leaf, and each is cheap but individually
unrewarding. The remaining `versification-predicted` 52 are Psalms, where §13.1's superscription
rule is the mechanism and only the per-psalm title length is unread.

The five `anomaly` rows are unchanged and remain the standing worklist: two are the `et v. N`
records the parser drops (§10.4), one is the English `v. 3` misparse (§10.2), and two are
`ddc-2-13` ¶6 (§14.4).

## 16. ✅ RULED — ship the remainder marked `unchecked`, and make that mean something

Wilson, 2026-08-29: **ship marked `unchecked` for now.** The 34 chapters carrying a single
divergence each are not worth a leaf apiece at this stage.

That ruling is only honest if the mark reaches the reader, so the class is now rendered and
explained rather than sitting in a TSV. `divergence_class` and `divergence_why` flow through
`build-index-json.py` into every locus, and `/scripture/[book]` prints a sentence per class.

### 16.1 What a reader now sees, per class

| class | the sentence on the page |
|---|---|
| `versification` | *The two editions number this verse differently — Milton's Bible divides the chapter at another point, so both numbers are right:* |
| `versification-predicted` | *…the Hebrew counts this psalm's heading as a verse of its own:* |
| `unchecked` | *The two editions number this verse differently. **Which numbering Milton was following here has not yet been checked**:* |
| `anomaly` | *…and not in a way Milton's Bible accounts for:* |
| `open-end` | *Both editions give the same verse; one leaves the reference open with `&c.` and the other closes it:* |

`divergence_why` — the technical reason, with the leaf number — rides along as the `title`
attribute, so a curious reader gets *"J–T Isa 57 begins at Isa 56:9 (read, leaf 590)"* on hover
without it cluttering the page.

The `/scripture` index carries the explanation in full, including the sentence that matters most:
**"That is meant literally, and it is not a suggestion that Milton miscited: it means we have not
opened his Bible at that chapter. Calling a citation an author's mistake is a claim about a real
person, and this edition would rather print an honest blank than a confident guess."**

### 16.2 ★★ A copy bug the rendering exposed — 74 divergences that are not disagreements

Counting which displayed loci carried **no class at all** turned up 74. Every one is an **`&c.`
divergence**: `Psal. lxxii. 1, &c.` against `Psal. lxxii. 1.`, where the verse numbers are
identical and only Milton's open end differs. The classifier had correctly returned "no numbering
disagreement here"; the *page* was nonetheless announcing **"The two editions number this verse
differently."** That sentence was false 74 times.

They now have their own class, `open-end`, and their own sentence. ★ **The lesson is worth
keeping: a class that means "nothing to say" and a page that always says something will silently
manufacture a false claim.** Every branch of a display needs a class, including the empty one —
which is why the check that found this (count the loci that render a divergence with an empty
class) should be re-run whenever the classifier changes.

### 16.3 Acceptance

`next build` clean. **5,811 deep links, 0 unresolved** (up from 5,809 — the two Psalm 88 records
§10.1 recovered). All five sentences render. `tools/jt_map.py` self-test 17/17.

### 16.4 The standing state, for whoever picks this up

- **23 J–T divisions** read, in `tools/jt-divisions.json`, each with evidence and leaf.
- **Divergence pairs:** 60 `versification` · 52 `versification-predicted` · 74 `open-end` ·
  108 `unchecked` · 5 `anomaly`.
- **The audit is CLOSED at this depth by ruling, not by exhaustion.** Reopening it means the 34
  single-divergence chapters, one leaf each; the method is §12.1 and the tooling is built.
- **The `anomaly` five remain the live worklist** and are the only rows asserting something is
  wrong: two `et v. N` parser drops (§10.4), one English `v. 3` misparse (§10.2), two at
  `ddc-2-13` ¶6 (§14.4).
