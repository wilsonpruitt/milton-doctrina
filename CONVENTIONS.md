# CONVENTIONS — frozen at M1 (2026-08-03, Fable pilot on II.ii)

These rules were settled by transcribing II.ii *De Bonorum Operum Causis Proximis* against the
plates of both volumes. `chunks/ddc-2-02.md` is the format reference — when a rule here seems
ambiguous, that file shows what was meant. Change these rules only with an explicit decision
recorded here with a date; do not drift.

## 1. Layers

Every chunk carries language-keyed blocks. Frozen keys:

| key | contents |
|---|---|
| `la` | Sumner's 1825 Latin (the *editio princeps* text) |
| `en-sumner` | Sumner's 1825 English translation |
| `en-wp` | reserved — fresh Wroot Press English, added per-chapter later; absent until then |

The site build must treat the set as an ARRAY (any subset may be present per chunk).

## 2. Transcription — verbatim-1825, plate-verified

- **The plate rules; OCR (djvu or pdftotext layer) is a finding aid only.** Every page of every
  chunk gets read against its 200 dpi plate (`pdftoppm -jpeg -r 200`); doubtful characters get a
  400 dpi crop. The pdftotext layer for these volumes is good enough to draft from — it is never
  good enough to publish from. (The pilot's error harvest from pdftotext: `delector`→"detector",
  `æqua`→"aqua", `Græcis`→"Gratis", `xlii`→"xiii", dropped em-dashes, all italics lost.)
- **Ligatures as printed:** æ and œ are used throughout the Latin (`quæ`, `cœlo`, `pœnæ`) —
  transcribe them. Site search normalizes æ→ae, œ→oe at index time; the TEXT keeps the ligature.
- **Italics as printed**, marked `*…*`. Scripture quotations are italic, citations and Milton's
  connective prose roman. Watch for roman words INSIDE italic quotes — they are Milton's own
  insertions (e.g. `*…et integri* sive *simplices…*`, Philipp. ii. 15 at p. 400) and the
  boundary is meaningful. Italic is also used for word-mention (`reverentia Domini *sapientia*
  dicitur`); transcribe as printed, don't rationalize.
- **Small caps → bold caps** (`**CAUSÆ PROXIMÆ**`). Preserve the printed capitalization inside
  the bold exactly — information-preserving; the site can render `**CAPS**` runs as small caps
  via CSS later, but caps lost in transcription are unrecoverable. Lowercase words the printer
  left roman inside a small-caps run stay outside the bold (`**SAPIENTIA** est **VIRTUS QUA …**`).
  The 1825's own use of small caps for definitions is INCONSISTENT (Sapientia's definition is
  full small caps; Prudentia's is not) — follow each instance as printed.
- **Chapter-opening display capitals** (drop-cap + spaced small caps on the first word) are
  display typography, not emphasis — normalize to plain text.
- **Truncation dashes as printed:** Milton/Sumner mark truncated quotes with an em-dash closed
  up against the last word (`est—.` `meam—:` `eum—!`). Use U+2014, closed up. The English also
  uses **dotted ellipses** (`.....`, dot-count varies) — transcribe the dots as counted per
  instance.
- **Punctuation:** keep as printed, including `&c.`, single quotation marks (`'…'`), and printed
  anomalies (see §6). Normalize the 1825's thin space before `; : ? !` to closed-up modern
  spacing — spacing is typography, not text.
- **Page breaks:** `<!-- p.NNN -->` comment at each printed-page boundary, inline mid-paragraph
  where the break falls mid-paragraph. Running heads, page numbers, signature marks (`3 E 2`),
  and catchwords are dropped. Greek, when it occurs, is restored in Greek script from the plate —
  never from OCR.

## 3. Citations — as printed per layer, NEVER harmonized

**The two editions disagree on citation digits, systematically and irregularly.** Milton cites
by Junius–Tremellius versification; Sumner's English sometimes adjusts to KJV numbering, sometimes
keeps Milton's, and at least once silently corrects an outright error. All plate-confirmed in the
pilot chapter:

| La (printed) | En (printed) | class |
|---|---|---|
| Eccles. ix. 20 | Eccles. ix. 18 | versification adjusted to KJV |
| Eccles. xii. 14 | Eccles. xii. 12 | versification adjusted to KJV |
| Psal. xl. 9 | xl. 8 | versification adjusted to KJV |
| Psal. xix. 14 | Psal. xix. 13 | versification adjusted to KJV |
| Eccles. xii. 15 | Eccles. xii. 15 | **NOT adjusted** (KJV = 12:13) — Sumner is inconsistent |
| Luc. ix. 66 | Luke ix. 62 | **La is a printed error** (Luke 9 has 62 verses); Sumner corrected silently |
| 1 Cor. ii. 7, 8 | 1 Cor. ii. 8 | En narrows the range |
| Job xxxi. 5, 6 | xxxi. 6 | En narrows the range |
| 2 Cor. vi. 3, &c. | 2 Cor. vi. 4, &c. | starting-verse shifted |

Rules: (a) transcribe each layer's citations exactly as printed; (b) never repair either side
from the other; (c) log every divergence found in the chunk's `## Notes` table; (d) versification
mapping is the scripture index's problem (M4), not the text's. The En also sometimes fills La's
truncated quotes and sometimes drops an `&c.` — same rule, don't "fix" either side.

## 4. Paragraph alignment — the `{¶N}` grid

- The **Latin paragraphing is the reference grid**: number every La paragraph `{¶1}…{¶N}` in
  reading order.
- Each `en-sumner` paragraph opens with the La paragraph(s) it renders: `{¶4}` or `{¶2–3}` for
  Sumner's merges. Coverage must be complete and monotonic — every La ¶ appears exactly once on
  the En side. Verify per chunk; record merges in `## Notes`.
- Pilot measurement: 28 La ¶¶ → 25 En ¶¶, three merges. Sumner also converts Milton's `Et …`
  coordination of vices into `First/Secondly/Thirdly/Fourthly` enumeration — structural habit,
  expect it throughout; it does not break ¶ alignment.

## 5. Sumner's footnotes — `[^sN]`

Sumner's English footnotes (cross-references to *Paradise Lost* and Milton's prose) are part of
the 1825 and are kept, as `en-sumner` apparatus. Anchor `[^sN]` where the printed superscript
sits; N is Sumner's own printed note number. Definitions live under `## apparatus-sumner` with
the printed page noted. Verse quoted in the notes is roman with the work-title italic, as
printed. The `s` prefix reserves bare `[^N]` for any future editorial apparatus.

## 6. Printed anomalies — kept as printed, flagged, never mended

Standing house rule, restated because the pilot already hit four: `1 Cor. viii 7.` (no period
after viii, La p. 401); `1 Tim. i. 13` (no period after 13, La p. 397, confirmed at 400 dpi);
`preposterously, they interpret` (En p. 542's comma); `chearful` (En p. 544). Also Milton's own
compressions that look like errors but aren't (`sannis`, La p. 398 = Acts 17:32 compressed).
Each goes in the chunk's `## Notes`; the text itself is never normalized.

## 7. Chunk files

`chunks/ddc-<book>-<chapter, 2 digits>.md`, with `-a`, `-b`… suffixes when a chapter is split
(threshold: La > 12 printed pages; split at Milton's own lemma seams, never at page counts).
Frontmatter carries `id`, `book`, `chapter`, `title_la`, `title_en`, `pages_la`, `pages_en`
(printed pages; pdf offsets live in STRUCTURE.md). Sections in order:
`## la` · `## en-sumner` · `## apparatus-sumner` (omit if none) · `## headnote` · `## Notes`.

## 8. Headnote — frozen shape

≤ 200 words, four fixed slots, always in this order:
1. **Place** — where the chapter sits in Milton's system (1–2 sentences).
2. **Argument** — what the chapter actually does (2–3 sentences).
3. **Pressure point** — where heterodoxy or controversy lives, if anywhere (1–3 sentences;
   omit the slot only if genuinely nothing).
4. **Loci** — the Wolleb/Ames correspondence (1 sentence; placeholder `*Loci: pending M4.*`
   until the compendia are sourced and checked).

Secondary-source claims enter headnotes only in M4, cited author+page, verified per
`feedback_christian-library-apparatus-headnotes-unverified`. Until then headnotes state only
what the primary text shows.

## 9. Session discipline (inherited, applies here)

One chapter (or split-part) per session unit; commit chunk + resume-note update separately.
Plate-verify before commit — a chunk without a plate pass is a DRAFT and says so in its
frontmatter (`status: draft`). OCR-derived text never ships silently.
