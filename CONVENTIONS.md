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
- **A word broken across a page keeps its integrity; the soft hyphen is dropped** (ratified
  2026-08-27, Wilson). Write `accept<!-- p.614 -->able`, `catho<!-- p.448 -->licæ`,
  `an<!-- p.486 -->gustia` — marker at the break, no hyphen. The end-of-line hyphen is a
  line-breaking artefact, not part of the word, and it belongs with the thin space above as
  typography rather than text. Keeping it would break the word for search and for the M4 index, and
  would assert a hyphen the word does not have. Fifteen instances across eleven chunks already
  follow this; it is now the rule, not a precedent.
- **Raised ordinals are set inline: `1m.` `2do.` `3tio.` `4to.` `5to.` `6to.` `7mo.`** (ratified
  2026-08-27, Wilson). The Latin prints them raised (`1ᵐ 2ᵈᵒ 3ᵗⁱᵒ`) as the ordinary abbreviation of
  *primo, secundo, tertio*; the raising is that abbreviation convention, and the numeral already
  carries the enumeration. Normalised for the same reason as the chapter-opening display capitals —
  **it is typography, not text**. ⚠ Note the cost, and state it where it matters: **the English
  layer destroys the feature entirely**, rendering the series as "first, Secondly, Thirdly", so
  after this normalisation the *raised* form survives only on the plate. Where a chapter's argument
  turns on the series (II.xvii's seven rules of war), say so in that chunk's `## Notes`. Nineteen
  instances across five chunks already follow this.

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
- Each `en-sumner` paragraph opens with the La paragraph(s) it renders: `{¶4}`, or `{¶2–3}` for
  Sumner's **merges**, or the `cont.` series below for his **splits**. Coverage must be complete and
  monotonic — **every La ¶ is fully accounted for on the En side, once as a whole or once across its
  `cont.` pieces.** (The old wording, "appears exactly once", was written before a split had been
  seen and is false as stated; corrected 2026-08-27.) Verify per chunk; record merges and splits in
  `## Notes`.
- **Splits, of any width** (ratified 2026-08-27 for two pieces, extended 2026-08-28 for three or
  more; Wilson). Where Sumner divides one Latin paragraph across several English ones, the first
  English piece takes the plain label and each later piece continues it:

  | pieces | labels |
  |---|---|
  | two | `{¶35}` · `{¶35 cont.}` |
  | three | `{¶10}` · `{¶10 cont.}` · `{¶10 cont. 2}` |
  | four | `{¶10}` · `{¶10 cont.}` · `{¶10 cont. 2}` · `{¶10 cont. 3}` |

  The numbered continuations follow the house pattern of §5b, which appends `-2`, `-3`, … to a
  repeated anchor label; the same logic, so the two rules read as one. First needed at II.xi (two
  pieces), then I.ii, which has **two three-piece splits** ({¶10}, {¶22}) as well as a two-piece one
  ({¶16}).
- **Expect merges in Book II and splits in Book I.** Book II is merge-dominated — Sumner welds
  Milton's short proof-text paragraphs together. Book I's opening chapters are split-dominated —
  Milton's prose there is long and argumentative and Sumner breaks it up (I.ii: 32 La ¶¶ → 37 En,
  three splits, no merges). The direction of the mismatch reverses between the books; do not carry
  an expectation from one into the other.
- Pilot measurement: 28 La ¶¶ → 25 En ¶¶, three merges. Sumner also converts Milton's `Et …`
  coordination of vices into `First/Secondly/Thirdly/Fourthly` enumeration — structural habit,
  expect it throughout; it does not break ¶ alignment.

## 5. Sumner's footnotes — BOTH VOLUMES carry them

**Amended 2026-08-04 (Wilson's ruling).** The original rule assumed apparatus was English-only.
**The Latin volume has footnotes too** — first found at La p. 431 (II.v). Both are kept, in
separate sections, with separate anchor namespaces:

| volume | section | anchor | note numbers |
|---|---|---|---|
| English | `## apparatus-sumner-en` | `[^sN]` | Sumner's printed English number; cycles 1–9 (§8a) |
| Latin | `## apparatus-sumner-la` | `[^laN]` | Sumner's printed Latin number; **independent run** |

The two numbering runs are independent and WILL collide (both contain a note "5"). Never merge
them, never renumber either to avoid a clash — that is what the distinct anchor prefixes are for.
The `s` prefix still reserves bare `[^N]` for editorial apparatus of our own — see §5c.

## 5a. Latin notes are TEXTUAL or SCHOLARLY — only textual ones are ledgered

Added 2026-08-04. The Latin-volume note at p. 431 is not a cross-reference. It is Sumner
disclosing that **the manuscript reads differently from what he printed**, and that he changed it
(*ordinem leviter mutavi*).

**Amended 2026-08-04 (Wilson's ruling), from II.vii.** Latin-volume notes come in **two kinds**,
and the transcriber must classify each one:

| kind | what it is | goes where |
|---|---|---|
| **textual** | Sumner discloses that the manuscript differs from what he printed, or that he changed something (La p. 431, *ordinem leviter mutavi*) | `## apparatus-sumner-la` **and** a row in `tools/sumner-interventions.tsv` |
| **scholarly** | Sumner argues for or around Milton — assembling authorities, glossing an allusion, defending a position (La p. 454, the Reformed divines on the Sabbath) | `## apparatus-sumner-la` **only** |

**When in doubt, do not ledger it.** `tools/sumner-interventions.tsv` exists to answer one
question — *where did Sumner admit changing Milton's text?* — and it feeds PLAN §6.4
(manuscript-state notes) at M4. A page of Reformed proof-texts filed as an "intervention" would
corrupt exactly the evidence base that file exists to provide. Scholarly notes stay discoverable
because they are transcribed in full in the chunk.

**State the limit whenever this data is used.** The ledger records only what Sumner *admitted*.
He normalised silently and at scale (PLAN §4a); the undisclosed changes are the larger set. The
ledger is evidence of specific interventions, never a collation and never a clean bill of health.

This does not disturb the transcription rule. `la` remains verbatim-1825 — we print what Sumner
printed, and his note is part of what he printed. It also does not disturb PLAN §4a, which already
says in terms that the text is Sumner's and not the manuscript's, and requires the About page to
say so.

## 5b. Anchor collisions WITHIN one chunk — `-2` suffix

**Added 2026-08-04 (Wilson's ruling), from II.vii.** §5 assumed fewer than ten notes per chunk.
That fails: Sumner's English numbers cycle 1–9 (§8a), so **any chunk carrying ten or more notes
repeats a printed number.** II.vii carries ten — ledger `8 · 9 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8` —
and would otherwise need two anchors called `[^s8]`.

**Rule.** The first occurrence keeps the plain anchor (`[^s8]`). Each later occurrence of the same
printed number appends `-2`, `-3`, … in reading order (`[^s8-2]`). The definition must open by
stating the printed number and which occurrence it is:

> `[^s8-2]: (printed En pp. 611–612 as note **8** — the chapter's SECOND note so numbered; anchored after …)`

Chosen because it keeps the printed number visible in the anchor, sorts predictably, and cannot be
mistaken for a note printed "8-2". It applies to `[^laN]` equally if the Latin ever collides.
Book I's longer chapters will hit this repeatedly; do not invent a second scheme.

## 5c. OUR OWN apparatus — bare `[^N]`, section `## apparatus-editorial`

**Added 2026-08-04 (Wilson's ruling), from II.vi.** §5 had reserved bare `[^N]` for editorial
apparatus of our own without ever defining where it lives. It lives in **`## apparatus-editorial`**,
anchored `[^1]`, `[^2]`, … numbered per chunk in reading order.

This layer is **ours, not 1825**, and that distinction is the whole point of keeping it separate
from `apparatus-sumner-*`. Use it only where the printed text would otherwise mislead a reader who
cannot check it — the founding case is II.vi's corrupt Hebrew, where the English volume prints two
non-words and no reader without Hebrew could tell.

Two hard constraints:
- **It never alters the text.** Verbatim-1825 (§2) and never-harmonize (§3) still govern. The note
  says what is wrong; the text keeps saying what Sumner printed.
- **Every claim in it is verified or explicitly marked unverified**, per
  `feedback_christian-library-apparatus-headnotes-unverified`. A note resting on our own reading of
  a plate, in a script we do not command, carries **⚠ UNVERIFIED** until a specialist confirms it,
  and must not be published without that mark.

Anchor where the printed superscript sits; N is Sumner's own printed number. Definitions carry the
printed page. Verse quoted in the notes is roman with the work-title italic, as printed. English
notes are mostly cross-references to *Paradise Lost* and Milton's prose; the Latin notes seen so
far are **textual** — see §5a.

**Read the Latin plates for superscripts too.** Until II.v nobody was looking, so any Latin note
in II.i–II.iv would have been missed. Those four chapters need a superscript-only re-check of
their Latin plates before Book II is called complete.

## 5d. An anchor falling INSIDE an italic quotation — deliberately NOT ruled yet

**Seen once, at I.ii (2026-08-28). Wilson's decision: wait for a second instance.** This is a
recorded deferral, not an oversight — do not treat it as an open question needing a ruling, and do
not invent a rule for it in the meantime.

En 24 prints *I am the Almighty*⁵ *God,* — Sumner's superscript sits between two words of one
continuous italic Scripture quotation. Markdown cannot nest an anchor inside emphasis, so the
current form breaks the run in two:

> `Gen. xvii. 1. *I am the Almighty*[^s5-2] *God,* literally, *sufficient.*`

The anchor keeps its printed position and no word is altered; what is lost is the fact that the
italic is continuous across it. That loss is recorded in `ddc-1-02`'s Notes.

**Why wait.** One instance does not show the shape of the problem. A second may differ in a way
that changes the answer — an anchor inside a small-caps run rather than an italic one, or one
falling inside a single word, or one where the split would separate a citation from its quotation.
Ruling once on complete evidence beats ruling twice. **Follow I.ii's form until then**, and record
each new instance in its chunk's Notes so the second case arrives with the first attached.

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
`## la` · `## en-sumner` · `## apparatus-sumner-en` · `## apparatus-sumner-la` ·
`## apparatus-editorial` (§5c) · `## headnote` · `## Notes`. Omit any apparatus section with no
content. `build-content.mjs` treats every `apparatus-*` header as reserved, so the editorial
section parses without a parser change.

## 8. Headnote — frozen shape

**Aim 200 words; hard cap 300** (revised 2026-08-27, Wilson — the original flat ≤200 was breached by
14 of the first 19 chunks, ranging to 343, because the doctrinally dense chapters cannot be served in
200). Aim at 200 and stay there when the chapter allows; go past it only when the chapter's substance
requires it, and never past 300. **Count the prose of the four slots**, including the `*Loci*` line —
the two ways of counting this was formerly measured differ by three words and the distinction is
noise; do not re-litigate it per chunk.

Four fixed slots, always in this order:
1. **Place** — where the chapter sits in Milton's system (1–2 sentences).
2. **Argument** — what the chapter actually does (2–3 sentences).
3. **Pressure point** — where heterodoxy or controversy lives, if anywhere (1–3 sentences;
   omit the slot only if genuinely nothing).
4. **Loci** — the Wolleb/Ames correspondence (1 sentence; placeholder `*Loci: pending M4.*`
   until the compendia are sourced and checked).

Secondary-source claims enter headnotes only in M4, cited author+page, verified per
`feedback_christian-library-apparatus-headnotes-unverified`. Until then headnotes state only
what the primary text shows.

## 8a. Sumner's footnote numbering is a CONTINUOUS 1–9 CYCLE — use it as a checksum

Added 2026-08-03 from II.i. **Revised 2026-08-03 from II.iv — the original rule was wrong in a
load-bearing way and the revision is plate-proved; read this section, not the old one.**

Sumner does **not** restart his English footnote numbers at each chapter or each page. They run
continuously — but they are **single-digit and cycle: after 9 the next note is 1 again.** The
original rule said "continuously through the whole book," which implied an ever-increasing
ledger. It does not increase past 9.

Plate proof (all 400 dpi-legible at 200 dpi, En vol.):
- p. 565 carries notes **⁷** and **⁸** (note 8's text runs over the page with catchword "I cannot").
- p. 566 carries **⁹** and then **¹** — the wrap happens *mid-page*, mid-chapter, mid-sentence-run.
- II.iv's own first note is **¹**, on p. 557, exactly as the cycle predicts after II.ii closed at 9
  and II.iii carried none.

Ledger so far: II.i → **3–7** · II.ii → **8, 9** · II.iii → **none** · II.iv → **1 … 9, then 1 …**.

Procedure, per chapter:

- Record the first and last note number the chapter carries, and every wrap inside it.
- The first note of chapter *N+1* must be exactly one past the last note of chapter *N*,
  **wrapping 9 → 1**. A chapter with no notes passes the number through untouched (II.iii).
- A break in that succession means **a note was missed** — go back and find it before the chunk
  is called verified. Do not rationalise it; Sumner does not skip numbers.
- **Know the check's blind spot:** because the cycle is only 9 long, it can never detect a miss
  of exactly 9 notes (or any multiple of 9). It is a strong check on ones and twos, not a proof
  of completeness. Do not let it substitute for reading every plate for superscripts.

Book I's numbering must be re-established independently when it is reached (do not assume it
continues from Book II, and do not assume it restarts).

## 8b. The 1825's inconsistency crosses chapters, not just paragraphs

Added 2026-08-03 from II.i. §2 already says the volume's emphasis typography is inconsistent
and must be followed per instance. II.i shows the same is true of *accidentals in quoted
Scripture across chapters*: Philipp. iv. 8 is set `siqua virtus et siqua laus est` at La p. 387
but `si qua virtus, si qua laus est` at La p. 395 — one volume, one editor, one verse, two
settings, nine pages apart.

Consequence: **never normalise a reading in chapter B because of how chapter A set it.** Per
instance means per instance, even when the two instances are the same verse. Log the pair in
both chunks' `## Notes` so the divergence is discoverable from either end.

## 8c. Roman inside an italic quotation is Milton's own voice — recurring, not exceptional

Now attested twice (Philipp. ii. 15, La p. 400, `*…et integri* sive *simplices…*`; Heb. xi. 6,
La p. 390, `*…mercedem* sive *præmium reddere.*`). A roman word inside an italic Scripture
quotation is Milton supplying an alternative rendering, and the italic/roman boundary carries
that meaning. Transcribe the boundary exactly; never absorb the roman word into the italic run.
`sive` is the usual trigger word — treat it as a flag to look closely.

## 8d. Partial chunks are legal

A chunk may carry a subset of the language layers (§1 already requires the site to treat them
as an array, and `site/scripts/build-content.mjs` discovers whatever `## <langkey>` sections
are present). When only one layer is done, set `status: <layer>-verified` and add
`<other>_status: pending`, and put a numbered "Owed on return" list at the top of `## Notes`
saying exactly what remains. `chunks/ddc-2-01.md` is the reference for this shape.

## 9. Session discipline (inherited, applies here)

One chapter (or split-part) per session unit; commit chunk + resume-note update separately.
Plate-verify before commit — a chunk without a plate pass is a DRAFT and says so in its
frontmatter (`status: draft`). OCR-derived text never ships silently.
