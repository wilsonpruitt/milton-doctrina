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
3. ✅ **RUN 2026-08-28**, not yet hand-checked chapter by chapter. Check 4 passes on ddc-2-02.
   **Next session starts here**: read `index/citation-qa.md`, settle the Ecclesiastes question
   at a plate, and confirm the eight unread out-of-range citations.
4. `tools/build-index-json.py` → `site/src/data/scripture/*.json`.
5. `/scripture` and `/scripture/[book]`, ported from Bonaventure, plus the divergence display.
6. Backfill each new chapter as it lands; add the index step to M3-RUNBOOK §2.

## 8. Model

Steps 1–2 are judgment-dense and belong on a strong model: the grammar is being *designed* against
a text that breaks the obvious rules, and a confidently-wrong parser is the failure mode PLAN §10
names. Step 3 onward is volume work over a frozen grammar and does not need one. The headnotes'
`*Loci: pending M4.*` line is §6.2's job, not this file's — Wolleb and Ames are on disk
(`tools/fetch-loci.sh`) and unread.
