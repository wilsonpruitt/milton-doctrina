# *De Doctrina Christiana* — Wroot Press edition

**Plan of record. Written 2026-08-03 (Fable session). Execution sessions should read this first, then `next-session-resume.md` once it exists.**

Web product first; print is sketched in §9 and deliberately deferred.

---

## 1. What this is

A free, parallel Latin–English edition of John Milton's systematic theology, built as a
research instrument rather than a reading text. Site: **milton.wrootpress.com**.

The pitch in one line: *Milton's most heterodox book, compiled entirely from Scripture,
made navigable by the Scripture it is compiled from.*

Nothing like it exists free. The two modern editions — Yale *Complete Prose Works* vol. VI
(Kelley/Carey, 1973) and the Oxford *Complete Works* vol. VIII (Campbell, Corns, Hale,
Tweedie, 2012) — are both in copyright and both expensive. What is freely online today is
scan images and unreadable OCR. A clean, aligned, indexed text is a real gap.

## 2. Sources (both PD, both Sumner 1825, both verified 2026-08-03)

| Layer | Archive ID | Description | Extent |
|---|---|---|---|
| Latin | `joannismiltonian00miltuoft` | *Joannis Miltoni Angli De Doctrina Christiana libri duo posthumi*, ed. C. R. Sumner, Cambridge: Typis Academicis, 1825 | 572 pp. scan; text runs printed pp. 1–524 |
| English | `treatiseonchrist00milt` | *A Treatise on Christian Doctrine, Compiled from the Holy Scriptures Alone*, trans. C. R. Sumner, Cambridge, 1825 | 782 pp. scan |

**Why this pairing is unusually favourable.** Unlike Bonaventure or Andrewes, a public-domain
English already exists, made by the same editor from the same manuscript in the same year,
following the same chapter divisions. Alignment is mechanical at chapter level and tractable
at paragraph level. This is the single biggest reason the project can ship in weeks.

**The 1825 also contains engraved facsimile specimens of the manuscript** (visible at the tail
of the Latin volume's scan). These are PD and feed §6.4 directly — do not discard them as scan
noise, which is what they look like in OCR.

**OCR is a finding aid ONLY.** The `_djvu.txt` layer is the usual 19th-century mush: the
contents page alone gives *De Hesipiscentia* for *Resipiscentia*, *De Iiuitione* for *Insitione*,
and drops six chapter titles entirely. Standard house rule applies without exception — **the
plate rules, the OCR only helps you find the plate.**

## 3. Structure of the work (verified from the 1825 contents, 2026-08-03)

- **Liber I — De Cognitione Dei**, 33 chapters, printed pp. 1–386
- **Liber II — De Dei Cultu**, 17 chapters, printed pp. 387–524
- **50 chapters total.**

Chapter sizes are wildly uneven and this drives the whole content pipeline:

- **I.v *De Filio Dei* — pp. 57–110, fifty-three pages, one chapter.** This is the anti-Trinitarian
  chapter, the most contested thing in the book, and on its own it is ~14% of Book I.
- **I.iv *De Praedestinatione* (pp. 31–57) and I.vi *De Spiritu Sancto* (pp. 110–124)** flank it.
- Against which the average Book II chapter is 8–12 pages.

**Implication: chunk ≠ chapter.** See §5.

## 4. The scholarly problem, and how the site handles it

This edition cannot be honest and also pretend it is printing Milton's manuscript. Two things
must be stated on the About page in plain language, not buried:

**(a) The text is Sumner's, not the manuscript's.** SP 9/61 (The National Archives) is a layered
composite in at least two scribal hands, with heavy revision. Sumner normalised silently. Campbell,
Corns, Hale and Tweedie's *Milton and the Manuscript of De Doctrina Christiana* — which is in
`~/Downloads/` — is the study that established this in detail. Our site publishes the 1825
*editio princeps* and says so.

**(b) The authorship was seriously challenged and the challenge was answered.** William Hunter
disputed Milton's authorship through the 1990s; the Campbell/Corns/Hale/Tweedie work is the
sustained response, and the scholarly consensus is that the work is Milton's — but as a layered,
revised, dictated composite rather than a clean authorial holograph. Say this once, clearly, on
the About page. Do not litigate it in the headnotes.

Both statements are *strengths*, not disclaimers. An edition that knows what it is beats one that
doesn't. This is the same discipline as the Andrewes watch-items and the Bonaventure plate rule.

**Rights.** Read `memory/wroot-press-licensing.md` before writing any rights page. Expected
shape: source text PD; our encoding, apparatus, headnotes and any fresh translation CC BY-NC 4.0.
Do not draft the rights page from this paragraph — read the memory.

## 5. Content pipeline

### 5.1 Chunking

Chunk = **chapter**, subdivided where a chapter exceeds roughly 8 printed pages. Subdivide at
Milton's own argumentative seams — his definitions, his transitions, and above all his
proof-text block boundaries — never at an arbitrary page count.

Estimated **150–200 chunks** total. That is an order of magnitude smaller than Bonaventure
(2,012 chunks), which matters in §7.

Chunk id scheme: `ddc-1-05-a`, `ddc-2-17`. Book, zero-padded chapter, optional section letter.

### 5.2 Alignment

Chapter-level alignment between the two volumes is mechanical (same editor, same divisions).
Paragraph-level alignment must be **verified, not assumed** — Sumner's English is more expansive
than his Latin and his paragraphing does not always match. Build a chapter→page crosswalk table
for both volumes as the very first artifact, in `STRUCTURE.md`, with the pdf↔printed offset for
each volume measured and anchored. Both offsets will differ; neither is guessable.

### 5.3 The reader is a language ARRAY, not a pair

**This is the load-bearing architectural decision.** Ship day 1 with `la` + `en-sumner`. A fresh
Wroot Press English (`en-wp`) drops in later, per chapter, without re-architecting.

Fork the Bonaventure site (`~/bonaventure-sentences/site/`) — Next.js static export, content
compiled to JSON at build time. The language pair is currently hardcoded in about five or six
files: `build-content.mjs`, `src/lib/content.ts`, `text-reader.tsx`, `globals.css`, and
`search-client.tsx`. (Line numbers from the Andrewes notes are ~2 months stale; re-locate them,
don't trust them.)

> **★ Do the language-array generalisation ONCE, and share it.** Andrewes needs exactly this same
> generalisation for its Greek·Latin·English trilingual reader, and it is listed there as
> outstanding engineering. Milton is the *easier* place to do it — two languages, clean prose, no
> polytonic Greek, no four-script pages, no fragile page-mirror layout. **Generalise here, then
> port to Andrewes.** Doing it twice would be the single most wasteful thing this project could do.

## 6. The four apparatus layers (all four approved, 2026-08-03)

### 6.1 Scripture index — *the product*

DDC is subtitled *ex sacris duntaxat libris petita* — "sought from the sacred books alone." The
book is not a treatise with proof-texts appended; it is a chain of proof-texts with connective
tissue. So the Scripture index is not apparatus. **It is the thesis of the book turned into
navigation.**

The query this unlocks — *what does Milton actually do with Romans 9?* — is a genuine research
question with no free instrument to answer it. `/scripture/[book]` puts the whole argumentative
use of a verse on one page.

Port `tools/build-citations.py` → `tools/build-index-json.py` → `/scripture` + `/scripture/[book]`
from Bonaventure. The parser will need a new citation grammar (Milton's Latin reference style,
not Quaracchi's) but the pipeline shape, the build-fails-on-missing-index guard, and the page
components all carry over.

**Two hard-won Bonaventure lessons apply verbatim:**
- The index is a **QA instrument** and will find real defects in the text. Expect it to.
- **Reading a digit correctly is not reading it rightly** — verify that a citation's *target
  exists*, not merely that the numerals were transcribed accurately.

**Scripture in the top-level nav from day 1**, not tucked into a chapter page.

### 6.2 Loci parallels — Wolleb and Ames

DDC's skeleton demonstrably follows the Reformed scholastic *loci* tradition, and specifically
Wolleb's *Compendium Theologiae Christianae* and Ames's *Medulla Theologica* — this is
long-established (Maurice Kelley's *This Great Argument*; restated by Campbell/Corns). Milton's
originality is visible precisely as *deviation from a template he is otherwise following*.

Both compendia are PD and both have PD English (Ross's 1650 Wolleb; Ames's *Marrow of Sacred
Divinity*, 1642). Both are short — this layer is cheap relative to its payoff.

Deliverable: a per-chapter **"the loci behind this chapter"** panel giving the corresponding
Wolleb and Ames locus, with a one-line statement of whether Milton follows, extends, or breaks.
Where he breaks — Arianism in I.v, mortalism in I.xiii, creation *ex Deo* in I.vii, divorce and
polygamy in II.xv — the panel is where the reader sees it happen structurally rather than being
told about it.

This is the layer that directly answers "the loci theologicae which would have shaped him."

**Do not overreach.** The correspondence is real at the level of *structure and sequence*. Assert
a verbal dependence only where you have checked both texts. Source the compendia as a scoped M4
task; they are not yet on disk.

### 6.3 Reading-guide headnotes

Per-chapter headnotes: what is at stake, where Milton departs from orthodoxy, what the
scholarship contests. Synthesised from the five secondary works now in `~/Downloads/`:

- Campbell, Corns, Hale & Tweedie, *Milton and the Manuscript of De Doctrina Christiana* — the
  manuscript, the hands, the authorship question. Governs §4 and §6.4.
- John K. Hale, *Milton's Scriptural Theology: Confronting De Doctrina Christiana* — the method
  and the Latin. Closest to our actual editorial work; likely the most used.
- Dobranski & Rumrich, eds., *Milton and Heresy* — the doctrinal departures, chapter by chapter.
- William Poole, *Milton and the Idea of the Fall* — I.x–I.xii especially.
- Barbara Lewalski, *The Life of John Milton* — dating, biography, the *Paradise Lost* relation.

**Hard boundary on these five: they shape the guide, they never appear in it.** They are in
copyright. Read them, synthesise, cite by author and page. No block quotation, no close
paraphrase, no reproduction. A headnote is our prose making our argument, with citations pointing
the reader to the books.

**And per the Christian Library lesson: headnote claims are UNVERIFIED until checked.** Verifying
a cross-reference is not verifying the sentence around it. Every factual claim in a headnote —
dates, attributions, "Milton is the first to…", "the manuscript reads…" — gets checked before it
ships, not after.

### 6.4 Manuscript-state notes

A per-chapter note flagging where our printed text is known *not* to be the manuscript: Sumner's
normalisations, the revision layers, the passages where the MS is damaged or the hands change.
Sourced from Campbell/Corns/Hale/Tweedie, and from the 1825's own facsimile plates.

**Scope this deliberately.** It is the most research-heavy of the four and the easiest to let
sprawl into a critical apparatus we are not equipped to build. Day-1 target: notes on the
chapters where it materially affects reading — I.v above all — plus a general statement in About.
Not a variorum.

## 7. What does NOT need re-litigating

Bonaventure's deploy-scale analysis is measured and parked. **Milton does not go near those
limits.** At ~150–200 chunks against Bonaventure's 2,012, every number scales down by roughly
10×: expect a low-hundreds-of-megabytes build at most, a `content.json` of a few MB rather than
55 MB, and no realistic OOM risk on the 8 GB machine under the 1 GB Node heap cap.

Use `--prebuilt` and `--archive=tgz` on deploy because they are the house recipe, not because
this project needs them. **Do not re-open the static-export-vs-on-demand question here** — Milton
is not the project that forces it.

## 8. Milestones

**M0 — Structure and offsets.** Fetch both scans. Measure and anchor the pdf↔printed offset for
each volume independently. Build the 50-chapter crosswalk (Latin pp. ↔ English pp.) into
`STRUCTURE.md`. Confirm the six OCR-dropped chapter titles off the plates. *No text work.*

**M1 — Pilot, one chapter, both layers.** Recommended pilot: **II.ii *De Bonorum Operum Causis
Proximis*** (pp. 395–404) — nine pages, self-contained, doctrinally unexciting. Pilot the
*mechanics* on a boring chapter; do not pilot on I.v, where the doctrinal stakes will disguise
process failures. Output: frozen `CONVENTIONS.md` (transcription rules, alignment rules, citation
grammar, chunk-id scheme, headnote form) and one exemplar chunk that is the format reference.

**M2 — Site skeleton + the language-array generalisation.** Fork the Bonaventure site; generalise
the hardcoded language pair to an array; get the pilot chapter rendering. Ship nothing public.

**M3 — Volume run.** The 50 chapters, Latin + Sumner English, chunk by chunk. This is the grind
and it is the bulk of the work. Book II first (shorter, more regular, better for building rhythm),
then Book I, saving I.iv–I.vi for last when conventions are fully settled.

**M4 — Apparatus.** Scripture index first (it is the product and it QAs the corpus). Then loci
parallels — which requires sourcing Wolleb and Ames, a scoped sub-task. Then headnotes. Then
manuscript-state notes.

**M5 — Launch.** About page carrying §4 honestly, rights page per the licensing memory, deploy.

*A fresh `en-wp` English is deliberately outside M0–M5.* When it is taken up, it starts with I.v —
the chapter where Sumner, a royal chaplain who later became Bishop of Winchester, is most
suspected of having softened an Arian text. That is where a fresh translation earns its keep, and
where a genuine scholarly claim is available to us. It should get its own pilot session at that
point, not be folded into this plan.

## 9. Print (deferred — sketch only)

Facing-page Latin/English via `~/wroot-press/_pipeline`, as `wroot-press/milton-doctrina/`.
At 524 Latin pages a facing-page setting lands near 1,100 pages, so it is certainly a **two-volume
set split at the book division** (Liber I / Liber II), which is also the natural intellectual
seam. Do not size or price this until M3 is done and real page counts exist. Cardo covers
everything needed; there is no Greek or Hebrew problem here.

## 10. Risks, in order of how likely they are to bite

1. **Alignment drift.** Sumner's English paragraphing does not reliably match his Latin. If
   alignment is assumed rather than verified per chapter, it will silently rot and be very
   expensive to fix late. *Mitigation: the M0 crosswalk, and per-chapter parity checks in M3.*
2. **I.v swallows the schedule.** Fifty-three pages, the hardest doctrine, the heaviest apparatus,
   and the chapter everyone will actually read. *Mitigation: it is scheduled last on purpose.*
3. **Headnote scope creep.** Five substantial monographs invite an editorial commentary rather
   than a reading guide. *Mitigation: fixed length per headnote, decided in M1 and frozen.*
4. **The copyright boundary on the secondary sources.** Real, and the one place where sloppiness
   would be genuinely damaging. *Mitigation: §6.3's rule, applied without exception.*
5. **Citation-grammar parser.** Milton's reference style is not Quaracchi's; the ported parser
   will need real work and will produce garbage confidently if it is not validated against
   hand-checked chapters. *Mitigation: validate against the M1 pilot chapter before scaling.*

## 11. Model plan

Per `memory/reference_model-prudence-rubric.md`:

- **M0, M2 — cheap.** Mechanical: offsets, crosswalks, a known site fork. Haiku/Sonnet.
- **M1 — Fable.** It is a genre-boundary pilot that freezes conventions; that is exactly what the
  rubric reserves the top tier for.
- **M3 — Opus**, chunk by chunk. Authored prose against a Latin plate; per
  `feedback_opus-for-authored-prose`, do not let the volume-shaped look of it trigger a downgrade.
- **M4 — split.** Scripture index is engineering (Sonnet). Headnotes and loci parallels are
  judgment and synthesis (Opus).
- Any fleet-style batch run needs an explicit big-burn OK first.

---

## 12. M4 is scoped — see `M4-RUNBOOK.md` (added 2026-08-28)

§6.1's index is measured and specified; the prep is in `tools/census-citations.py` and
`tools/scripture-books.json`. **One decision recorded here because it changes §6.1's shape:**
Bonaventure keys its index off the Latin alone and treats the English as display. That rule does
not survive contact with this edition — the two volumes disagree about citations systematically
(§3; ~210 divergences projected), so **both layers are parsed and keyed, and the divergence is a
displayed field rather than a resolved one.** The index does not adjudicate between Milton's
Junius–Tremellius numbering and Sumner's inconsistent KJV adjustments; it shows both.

§6.2's Wolleb and Ames are now on disk — `tools/fetch-loci.sh`, four texts, OCR as finding-aid only.
They are unread; the `*Loci: pending M4.*` line in every headnote still stands.
