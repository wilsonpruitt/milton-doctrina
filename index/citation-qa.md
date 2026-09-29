# Citation QA — read this, do not merely generate it

260 records · 0 unclassified · 0 out-of-range · 0 versification · 11 divergence rows, 2 suspect

## Per-layer counts (M4-RUNBOOK §6.1 — a gap of more than a few percent is a bug)

- `la` — 130
- `en-sumner` — 130
- spread: 0 records, 0.0%

## Unclassified — never a record with an invented target

_none_

## Targets that do not exist

_none_

## Suspect pairings — the aligner slid; READ THESE

The two layers were paired but land too far apart to be one citation. Reported, never merged: each side keeps its own target, so the index cannot file one layer's verse under the other's. Some of these are real findings about the 1825 text and some are alignment slips, and telling them apart needs the paragraph in view.

- `ddc-1-29` ¶9-11 — la `Judæ 10` → Jude 1:10 vs en `Jude 20` → Jude 1:20
- `ddc-1-29` ¶29 — la `v. 23, 45.` → Acts 10:23,45 vs en `v. 45` → Acts 10:45

## ★ Divergences the J–T map does NOT explain — READ THESE

A Junius-Tremellius chapter division has been read for these chapters (tools/jt-divisions.json), and the Latin still does not map onto the English through it. Each is a genuine Latin error, an aligner slide, or a division that needs re-reading -- and telling those apart needs the paragraph in view. M4-RUNBOOK 14.

_none_

## Divergence classes — every pair, by why the numbers differ

| class | pairs | what it asserts |
|---|---|---|
| `unchecked` | 5 | no division read and no known mechanism. NOT a claim of error |
| `open-end` | 1 |  |

## Versification, not error (M4-RUNBOOK §6b)

Out-of-range citations reclassified as Junius-Tremellius numbering. These are records in the ledger, not findings against the 1825 text.

_none_

## Offset corroboration — the evidence behind the line above

A numbering offset is a system, so it repeats; a misprint is a singleton. **A book with no repeating offset cannot have an out-of-range citation excused as versification** — which is how `Luc. ix. 66.`, the only Luke divergence in the corpus, stays a printed error.

| book | ch | offset (La − En) | seen | repeating |
|---|---|---|---|---|
| 1Pet | 5 | -1 | 1 | no |
| Acts | 10 | -22 | 1 | no |
| Jude | 1 | -10 | 1 | no |
| Mark | 16 | -1 | 1 | no |

## Divergences between the layers

| chunk | ¶ | Latin | → | English | → | kind |
|---|---|---|---|---|---|---|
| ddc-1-29 | ¶4 | `Marc. xvi. 16, 17, 18.` | Mark 16:16,17,18 | `Mark xvi. 17, 18.` | Mark 16:17,18 | divergence |
| ddc-1-29 | ¶4 | `Deut. xiii. 1, 2, 3.` | Deut 13:1,2,3 | `Deut. xiii. 1—3.` | Deut 13:1,2,3 | same target, syntax differs (BOOK CH V-LIST / BOOK CH V-RANGE) |
| ddc-1-29 | ¶6-7 | `Deut. xxix. 2, 3, 4.` | Deut 29:2,3,4 | `Deut. xxix. 2—4.` | Deut 29:2,3,4 | same target, syntax differs (BOOK CH V-LIST / BOOK CH V-RANGE) |
| ddc-1-29 | ¶6-7 | `Psal. lxxviii. 11, &c.` | Ps 78:11 &c. | `Psal. lxxviii. 11.` | Ps 78:11 | divergence |
| ddc-1-29 | ¶9-11 | `Judæ 10` | Jude 1:10 | `Jude 20` | Jude 1:20 | divergence |
| ddc-1-29 | ¶9-11 | `Matt. xxvi. 33.` | Matt 26:33 | `—` | — | present in Latin only |
| ddc-1-29 | ¶17 | `Matt. xx. 25, &c.` | Matt 20:25 &c. | `Matt. xx. 25—28.` | Matt 20:25,26,27,28 | divergence |
| ddc-1-29 | ¶23 | `Eph. iv. 11, 12, 13.` | Eph 4:11,12,13 | `Eph. iv. 11—13.` | Eph 4:11,12,13 | same target, syntax differs (BOOK CH V-LIST / BOOK CH V-RANGE) |
| ddc-1-29 | ¶26-28 | `1 Pet. v. 2, 3.` | 1Pet 5:2,3 | `1 Pet. v. 3.` | 1Pet 5:3 | divergence |
| ddc-1-29 | ¶29 | `—` | — | `v. 23` | Acts 10:23 | present in English only |
| ddc-1-29 | ¶29 | `v. 23, 45.` | Acts 10:23,45 | `v. 45` | Acts 10:45 | divergence |
