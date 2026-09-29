# Citation QA — read this, do not merely generate it

259 records · 6 unclassified · 0 out-of-range · 0 versification · 23 divergence rows, 2 suspect

## Per-layer counts (M4-RUNBOOK §6.1 — a gap of more than a few percent is a bug)

- `la` — 129
- `en-sumner` — 130
- spread: 1 records, 0.8%

## Unclassified — never a record with an invented target

- `ddc-1-30` `ddc-1-30:la:{¶12}:0` — `cap. xi. 1.` → chapter continuation with no book in scope
- `ddc-1-30` `ddc-1-30:la:{¶21}:0` — `entium minime negligendam exaravit; ut supra cap. xxvii.` → chapter continuation governed by lib./Book/supra/infra — a reference to a treatise, not to scripture. Not indexed.
- `ddc-1-30` `ddc-1-30:en-sumner:{¶21}:0` — `chap. xxvii.` → chapter continuation with no book in scope
- `ddc-1-30` `ddc-1-30:la:{¶30}:6` — `cap. vi. 16.` → ERR: Eccl 6 has 12 verses — 16 out of range — and the book here was CARRIED, not named, so the carry is the likelier defect. Not indexed; read the passage.
- `ddc-1-30` `ddc-1-30:en-sumner:{¶7}:9` — `i. 56, 57.` → ERR: Neh 1 has 11 verses — 56, 57 out of range — and the book here was CARRIED, not named, so the carry is the likelier defect. Not indexed; read the passage.
- `ddc-1-30` `ddc-1-30:en-sumner:{¶30}:6` — `vi. 16.` → ERR: Eccl 6 has 12 verses — 16 out of range — and the book here was CARRIED, not named, so the carry is the likelier defect. Not indexed; read the passage.

## Targets that do not exist

_none_

## Suspect pairings — the aligner slid; READ THESE

The two layers were paired but land too far apart to be one citation. Reported, never merged: each side keeps its own target, so the index cannot file one layer's verse under the other's. Some of these are real findings about the 1825 text and some are alignment slips, and telling them apart needs the paragraph in view.

- `ddc-1-30` ¶9 — la `1 Cor. xiv.` → 1Cor 14 vs en `1 Cor. i. 4.` → 1Cor 1:4
- `ddc-1-30` ¶29 — la `Tit. i. 14.` → Titus 1:14 vs en `Tit. i. 4.` → Titus 1:4

## ★ Divergences the J–T map does NOT explain — READ THESE

A Junius-Tremellius chapter division has been read for these chapters (tools/jt-divisions.json), and the Latin still does not map onto the English through it. Each is a genuine Latin error, an aligner slide, or a division that needs re-reading -- and telling those apart needs the paragraph in view. M4-RUNBOOK 14.

_none_

## Divergence classes — every pair, by why the numbers differ

| class | pairs | what it asserts |
|---|---|---|
| `open-end` | 5 |  |
| `unchecked` | 5 | no division read and no known mechanism. NOT a claim of error |
| `versification-predicted` | 2 | no division read, but the mechanism is known and the shape fits (Psalms +1/+2, numbered superscription) |
| `versification` | 1 | a READ J-T division maps the Latin onto the English exactly |

## Versification, not error (M4-RUNBOOK §6b)

Out-of-range citations reclassified as Junius-Tremellius numbering. These are records in the ledger, not findings against the 1825 text.

_none_

## Offset corroboration — the evidence behind the line above

A numbering offset is a system, so it repeats; a misprint is a singleton. **A book with no repeating offset cannot have an out-of-range citation excused as versification** — which is how `Luc. ix. 66.`, the only Luke divergence in the corpus, stays a printed error.

| book | ch | offset (La − En) | seen | repeating |
|---|---|---|---|---|
| Ps | 19 | +1 | 2 | **yes** |
| 2Kgs | 24 | +2 | 1 | no |
| Amos | 2 | -3 | 1 | no |
| Titus | 1 | +10 | 1 | no |

## Divergences between the layers

| chunk | ¶ | Latin | → | English | → | kind |
|---|---|---|---|---|---|---|
| ddc-1-30 | ¶6 | `—` | — | `2 Tim. iii. 15—17.` | 2Tim 3:15,16,17 | present in English only |
| ddc-1-30 | ¶6 | `2 Pet. iii. 15, 16, 17.` | 2Pet 3:15,16,17 | `—` | — | present in Latin only |
| ddc-1-30 | ¶6 | `—` | — | `Rom. i. 7. 15.` | Rom 1:7,15 | present in English only |
| ddc-1-30 | ¶6 | `cap. i. 7, 15.` | 2Pet 1:7,15 | `—` | — | present in Latin only |
| ddc-1-30 | ¶7 | `Deut. xxxi. 9, 10, 11, &c.` | Deut 31:9,10,11 &c. | `Deut. xxxi. 9—11.` | Deut 31:9,10,11 | divergence |
| ddc-1-30 | ¶7 | `cap. xi. 18, 19, 20.` | Deut 11:18,19,20 | `xi. 18—20.` | Deut 11:18,19,20 | same target, syntax differs (— CH V-LIST / — CH V-RANGE) |
| ddc-1-30 | ¶7 | `—` | — | `i. 56, 57.` | Neh 1:56,57 | present in English only |
| ddc-1-30 | ¶9 | `Psal. xix. 8.` | Ps 19:8 | `Psal. xix. 7.` | Ps 19:7 | divergence |
| ddc-1-30 | ¶9 | `1 Cor. xiv.` | 1Cor 14 | `1 Cor. i. 4.` | 1Cor 1:4 | divergence |
| ddc-1-30 | ¶12 | `—` | — | `Hosea xi. 1.` | Hos 11:1 | present in English only |
| ddc-1-30 | ¶13 | `2 Chron. xvii. 9, 10.` | 2Chr 17:9,10 | `2 Chron. xvii. 9.` | 2Chr 17:9 | divergence |
| ddc-1-30 | ¶13 | `1 Cor. xiv. 1, &c.` | 1Cor 14:1 &c. | `1 Cor. xiv. 1.` | 1Cor 14:1 | divergence |
| ddc-1-30 | ¶14 | `2 Reg. xxiv. 10.` | 2Kgs 24:10 | `2 Kings xxiv. 8.` | 2Kgs 24:8 | divergence |
| ddc-1-30 | ¶15 | `Eph. iv. 11, 12, 13.` | Eph 4:11,12,13 | `Eph. iv. 11—13.` | Eph 4:11,12,13 | same target, syntax differs (BOOK CH V-LIST / BOOK CH V-RANGE) |
| ddc-1-30 | ¶18 | `Psal. xix. 10.` | Ps 19:10 | `Psal. xix. 9.` | Ps 19:9 | divergence |
| ddc-1-30 | ¶19-20 | `—` | — | `i. 19.` | John 1:19 | present in English only |
| ddc-1-30 | ¶19-20 | `2 Pet. i. 19.` | 2Pet 1:19 | `—` | — | present in Latin only |
| ddc-1-30 | ¶19-20 | `et v. 25, 26.` | 1Cor 7:25,26 | `v. 25` | 1Cor 7:25 | divergence |
| ddc-1-30 | ¶29 | `1 Tim. vi. 3, &c.` | 1Tim 6:3 &c. | `1 Tim. vi. 3.` | 1Tim 6:3 | divergence |
| ddc-1-30 | ¶29 | `Tit. i. 14.` | Titus 1:14 | `Tit. i. 4.` | Titus 1:4 | divergence |
| ddc-1-30 | ¶30 | `2 Chron. xxix. 6, &c.` | 2Chr 29:6 &c. | `2 Chron. xxix. 6.` | 2Chr 29:6 | divergence |
| ddc-1-30 | ¶30 | `Amos. ii. 1.` | Amos 2:1 | `Amos ii. 4.` | Amos 2:4 | divergence |
| ddc-1-30 | ¶30 | `Jer. xliv. 17, &c.` | Jer 44:17 &c. | `Jer. xliv. 17.` | Jer 44:17 | divergence |
