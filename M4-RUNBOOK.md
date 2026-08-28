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
| `tools/scripture-books.json` | **starter** abbreviation tables for both layers, seeded from the census, 61 books. |
| this file | the design decisions and the hazards, below. |

Nothing else exists. There is no ledger, no parser, no route.

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
4. ⚠ **The Latin uses `1 Reg.`/`2 Reg.` for 1–2 KINGS** while separately using `1 Sam.`/`2 Sam.`
   That is not the Vulgate convention. Counts corroborate (La `1 Reg.` 37 / En `1 Kings` 34; La
   `2 Reg.` 30 / En `2 Kings` 30) but **confirm it at a plate** before the index ships.

## 4. Hazards, each already drawn blood in prep

1. **Word-boundary anchoring.** Without `\b`, the roman-numeral class matches inside words and the
   Latin layer reports **~3,900 phantom citations** that are single letters of ordinary prose
   (`i` 2478×, `c` 441×, `x` 270×). The census carries the fix and a comment saying why.
2. **Latin words that ARE roman numerals.** Even anchored, `illi`, `vi`, `ii`, `ix`, `li`, `ci` are
   shape-identical to numerals. A bare roman is a citation only in citation context — after a book
   token, after `et`, or after another citation. **This hazard does not exist in the English.**
3. **Capitalised Latin words that look like books** — `Judæis`, `Judæorum`, `Judæi`, and `Sic`
   (the opening of Sumner's textual notes) and `Cap.` (Milton's own chapter self-reference). A book
   token is a citation only when a chapter or verse follows.
4. ★ **Single-chapter books drop the chapter entirely**: La `Judæ v. 20.` / En `Jude 20.` A parser
   expecting `BOOK CH V` reads the verse as a chapter and emits a citation to a chapter that does
   not exist. Attested for Jude; assume the same for Obadiah, Philemon, 2 and 3 John.
5. ★ **`Jud.` is JUDGES, not Jude** — the first seeding of the book table got this wrong, and what
   caught it was the parallel: La `Jud. xiii. 18.` against En `Judges xiii. 18.`, versus La
   `Judæ v. 20.` against En `Jude 20.` **The other layer is the best check on a mapping.** This is
   §2's argument arriving from a second direction.
6. **Numeral-dropped tokens** — bare `Cor.`, `Kings`, `Thess.`, `Sam.`, `Tim.`, `Chron.`, `Pet.`
   occur in both layers. Almost certainly continuations carrying the numeral forward, but
   **unresolved**. Per the Bonaventure rule that ports verbatim: *never guess — a citation the
   parser cannot classify becomes a QA line, not a record with an invented target.*
7. **`et v. N` is ambiguous and unresolvable by form alone** — it may be verse N of the current
   chapter or chapter N of the current book. Attested at I.ii and II.xvii; I.ii's instance was
   settled only because the English applied KJV versification to it, which makes sense only for a
   chapter reference. Treat as its own resolution class; do not force it.

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

## 7. Sequence

1. Confirm the `1 Reg.` = Kings mapping at a plate (§3.4). Cheap, and everything downstream leans on it.
2. Write `tools/build-citations.py` for ONE chapter — `ddc-2-02`, the format reference — both layers.
   Hand-check every record it emits against the chapter. Do not scale until that is clean.
3. Extend to the 19 chapters. Run check 4 against the logged divergences.
4. `tools/build-index-json.py` → `site/src/data/scripture/*.json`.
5. `/scripture` and `/scripture/[book]`, ported from Bonaventure, plus the divergence display.
6. Backfill each new chapter as it lands; add the index step to M3-RUNBOOK §2.

## 8. Model

Steps 1–2 are judgment-dense and belong on a strong model: the grammar is being *designed* against
a text that breaks the obvious rules, and a confidently-wrong parser is the failure mode PLAN §10
names. Step 3 onward is volume work over a frozen grammar and does not need one. The headnotes'
`*Loci: pending M4.*` line is §6.2's job, not this file's — Wolleb and Ames are on disk
(`tools/fetch-loci.sh`) and unread.
