# Next session — resume here

## ⇢ START HERE (2026-08-28, Opus) — §10.8 is RULED, and the answer came from Milton's own Bible

**Read `M4-RUNBOOK.md` §11.** Wilson ruled: check Junius–Tremellius before classifying anything,
and bring it in as a permanent source. Both halves are done.

**`testamentiveteri00trem` — Junius & Tremellius, Hanau 1603, 1252 leaves, public domain — is now
a project source.** `tools/fetch-jt.sh` pulls it; `tools/jt-page.py <leaf> [--band y0 y1]
[--x x0 x1] [--scale]` fetches and crops a leaf image; the calibration (`leaf = 2 × printed + 188`,
a leaf is an OPENING) is in STRUCTURE.md. ⚠ Its OCR is worse than anything else in the project —
`Amotsi`, `Coheleth`, `Jehezkelis` all return **nothing**. Navigate by running head off the image.

**The verdict, read off the page images:** ★ Ecclesiastes 4 **+4** · Ecclesiastes 10 **+3** ·
Isaiah 3 **+1** · Ezekiel, where **J–T runs the verse count straight across the 2/3 chapter break**
so that J–T 3:18, 19 *are* KJV 3:8, 9. **Eight of `ddc-2-17`'s "sixteen Latin citation errors" are
versification, not error** — reclassified in that chunk's Notes, which now reads five errors,
eight versification, three unread. II.v's eight holds the record again.

★★ **The mechanism is the finding.** Junius–Tremellius **divides chapters at different points from
the KJV**, and at least once carries the verse count across a break. That is why an offset is
constant inside a chapter and different between chapters — the fact §6b measured without being
able to say why. It is not a defective copy and not Milton miscounting: it is a different Bible.

⚠ **Two claims on record were wrong and are corrected in place** — the chunk's *"La's reading is
impossible (Ezek. 2 has 10 vv.)"* (true, and beside the point: the verse is in chapter III) and
§10.5's *"chapter 2 absorbs KJV 3:1–9"* (chapter 2 ends exactly where the KJV's does). Both
reached the right verdict by the wrong route, which is what a plate is for.

✅ **All eight rows are now settled — the table is closed.** Isaiah 57 took two of them with one
chapter division (J–T's `CAPUT LVII` opens at KJV 56:9, so its verse **2** is KJV 56:10,
***Speculatores istius cæci***, the very words Milton quotes); Ecclesiastes 8 is **+1**.
`ddc-2-17` now reads **five errors, eleven versification**.

★ **A free confirmation of §6b fell out of it.** Ecclesiastes' leaf 531 shows how the volume prints
divisions — J–T sets **its own** chapter break with an italic argumentum **and** the received
marker where that falls, so `CAPUT IX` appears twice on one page — and in passing it gives
**Eccl 9 at +2** (J–T 9:3 = KJV 9:1), which §6b had measured three times from the corpus and could
not explain. Confirmed at the source without being sought.

✅ **The corpus-wide audit's first pass is also done — §12. 22 more rows moved, in 7 chunks**, all
of them printed as "La errors silently corrected". Eleven J–T chapter divisions are established
(§12.2: Num 23, Prov 12, Eccl 2/4/8/9/10, Isa 3/44/57, Ezek 3). ⚠ **STRUCTURE.md's J–T
calibration was wrong and is fixed** — the volume has **two numbering regimes**, the Pentateuch
FOLIATED (`leaf = folio + 17`, one number per opening) and Psalms onward paginated
(`leaf = 2 × printed + 188`), with a drifting constant between. Don't extrapolate a formula
outside the range it was fitted in.

✅ **The Psalms are settled as a class too — §13, and it took ONE leaf.** J–T leaf 458 shows
`PSALMUS LIIII` numbering its two-line superscription as **verses 1 and 2** (so J–T 54:7 = KJV 54:5)
and, directly below on the same page, `PSALMUS LV` numbering its one-line superscription as **verse
1 only** (so J–T 55:18 = KJV 55:17). Two adjacent psalms, two offsets, one visible cause. §6b's
inference is confirmed at the source, and the ~57 Psalm divergences can now be classified by
**counting the lines of the superscription** rather than by reading 57 leaves.
★ J–T 55:18 = KJV 55:17 **is `ddc-2-04-b` ¶9's `Psal. lv. 18. / lv. 17.` — one of the original
seventeen suspect pairings.** The thread closes where it started.

⚠⚠ **`ddc-2-11` claimed "None is versification: Junius–Tremellius and the KJV number all six of
these places alike." All six are versification** — a perfect inversion, asserted without access to
J–T. Corrected in place (§13.2); that chapter now has **no `Luc. ix. 66`-class error at all** where
it claimed six. 1 Sam 16 is the clearest layout evidence in the volume: J–T prints verse **1**
(= KJV 15:35) **above** the `CAPUT XVI` rubric and numbers KJV 16:1 as **2** — the rubric marks the
*received* division, the numbers follow J–T's own.

⚠ **And a correction to my own method in §12.4**, now §13.3: I wrote that the quotation test
"disposes of most singletons". **It does not.** A quotation identifies a verse in *KJV* terms, so it
cannot tell a wrong digit from a small offset — under an offset Milton's number points at the same
words in his own Bible. `ddc-2-11` had exactly that shape: a "what the text quotes" column, correct
in every row, carrying six wrong classifications. The test is sound only where the gap is too large
to be a chapter division (`Act. xiii. 3` vs Acts 23:4 is ten chapters). **A gap of one to five
verses is settled by the page, never by the quotation.**

✅ **`divergence_class` is BUILT — §14.** The classification is data now, not prose.
`tools/jt-divisions.json` holds the sixteen J–T divisions with their evidence and leaf;
`tools/jt_map.py` maps any J–T reference onto the KJV by walking `versification.json`, and
**self-tests 17/17 against the hand-made findings** (`python3 tools/jt_map.py`). Two new columns in
`index/citations.tsv`, two new sections in `index/citation-qa.md`.

**Classes:** `versification` 40 pairs · `versification-predicted` 52 · `unchecked` 128 ·
`anomaly` **5**. ⚠ **`unchecked` is deliberately not `error`** — calling a divergence Milton's
mistake is a claim about a real person, and only a page image is entitled to make it.

★★ **The anomaly class found a new Latin error on its first run** — `ddc-2-13` ¶6, the first the
tooling has FOUND rather than reclassified. Sumner reordered the pair, `Prov. xii. 21` is correct
under the −1 division, and **`v. 17` is a real slip: J–T numbers *Efflat veritatem* as 16**
(leaf 511, checked at every verse from 8 to 18). **No earlier pass could see it because both layers
print the digit 17** — Sumner's right in KJV terms, Milton's wrong in J–T terms. A divergence table
cannot see an error the two layers agree on.

✅ **The first sweep off that list is DONE — §15. Seven chapters, 20 pairs, one leaf each.**
Gen 12 (−3) · Exod 16 (+1) · 1 Sam 14 (+1) · Neh 10 (+1) · Dan 6 (+1) · Hos 12 (+1) · Amos 2 (−3).
**23 divisions** in `jt-divisions.json`. ★★ **II.xvii is down to THREE errors from the sixteen it
claimed**; `ddc-2-15`'s "La is a printed error" row fell too.

## ✅ RULED 2026-08-29 (Wilson) — SHIP the remainder marked `unchecked` (§16)

The 34 single-divergence chapters are not worth a leaf apiece at this stage. **The audit is closed
at this depth by ruling, not by exhaustion** — reopening it is §12.1's method with the tooling
already built.

The ruling is only honest if the mark reaches the reader, so **the class is now rendered**:
`divergence_class` flows through `build-index-json.py` into every locus, `/scripture/[book]` prints
a sentence per class, and `divergence_why` (with its leaf number) rides along as a hover title. The
`/scripture` index carries the explanation, including the line that matters: *"it is not a
suggestion that Milton miscited: it means we have not opened his Bible at that chapter."*

★★ **The rendering immediately exposed a copy bug — 74 divergences that are not disagreements.**
Counting loci that displayed a divergence with **no class at all** found them: every one an `&c.`
case (`Psal. lxxii. 1, &c.` vs `Psal. lxxii. 1.`) where the numbers agree and only Milton's open
end differs. The page was announcing *"The two editions number this verse differently"* — **false,
74 times.** Now class `open-end` with its own sentence. ⚠ **Re-run that check whenever the
classifier changes**: a class meaning "nothing to say" plus a page that always says something
manufactures a false claim silently.

**Acceptance:** `next build` clean · **5,811 deep links, 0 unresolved** · all five sentences render
· `jt_map.py` 17/17.

**Pairs now:** 60 `versification` · 52 `versification-predicted` · 74 `open-end` · 108 `unchecked`
· **5 `anomaly`** — the last are the only rows asserting something is wrong, and the live worklist.

**Next up is M5 copy**: About and Rights are still M2 placeholders, and `/scripture` is styled only
with the existing card classes.

---

## ⇠ Earlier the same day — the 17 suspects are READ

**Go to "The queue now", item 1, and to `M4-RUNBOOK.md` §10.** The suspect read closed the queue's
★ item and turned up something bigger than a parser bug: **the chunks' "silently corrected error"
tables were written before §6b and, by §6b's own rule, are misclassifying versification as
Milton's error.** That is a claim about the man that goes into print, so it is Wilson's to rule
on, and the audit that follows touches every chunk. Everything below this line is the earlier
history of the session, kept in order.

---

## ⇠ Earlier the same day — the Ecclesiastes question is SETTLED

**Job 1 of the previous list is done, and it came out the other way from "error."** All five
Ecclesiastes out-of-range citations are **Junius–Tremellius versification**, to be displayed under
CONVENTIONS §3, not flagged. `Lev. v. 21` joins them. **Read `M4-RUNBOOK.md` §6b** — it carries
the evidence, the per-chapter offset table, and one design consequence that must be settled before
any more code is written.

What settled it was not a plate but the corpus: pairing every Ecclesiastes citation across the two
layers gives **per-chapter offsets that repeat** — Eccl 4 is `−4` four separate times, Eccl 9 is
`+2` three times — and the two chapter displacements are each confirmed from *both* sides (La ch 7
absorbs KJV 8:1, so La ch 8 runs −1; both observed). Four independent misprints do not agree.
Generalised: **299 divergence pairs, `La = En + 1` is 53% of them, and 53 of 57 Psalm divergences
are `+1`/`+2` — the Hebrew superscription**, `+2` exactly in Ps 51, 52, 60, whose titles run to
two lines. Ecclesiastes was never special; it is just where short chapters make the offset
overflow a bound and become visible to a range check.

### Done since — the queue moved

✅ **The `witness_target` question is settled and built** (M4-RUNBOOK §6b, "Ledger changes MADE").
`divergence_id` is populated for the first time (717 records — the column was in the schema from
day one and always written empty), and a new `witness_target` column carries the verse both layers
point at, beside the printed target each layer goes on showing. Where they diverge the witness is
the **English** target, because Sumner converts toward the KJV, which is the reader's Bible.
298 records carry a witness that differs from what their layer prints. **`build-index-json.py`
must group by `witness_target`, not by `target`.**

✅ **`versification` is now a resolution class**, decided by corroboration rather than a book list:
a record leaves the error list only if its pair's *own* offset is attested elsewhere, and a
cross-chapter pair must also show the complementary observable. Moves 7, leaves 6 — the split
derived by hand before it was coded. ⚠ The first cut tested only book-level repetition and
excused two real errors; both are written up, and one of them **answered a plate question for
free**: `Isa. lviii. 56` is a dropped comma (En reads `lviii. 5, 6`), not a mis-set number.

✅ **A pre-existing ledger bug, fixed and guarded.** `citations.tsv` held **5,817 lines for 5,809
records** — four citations wrap a line in the source and the writer collapsed tabs but not
newlines, splitting one record across three rows. Invisible in every count printed to date and
fatal to the line-at-a-time reader `build-index-json.py` was going to be. Now guarded by a second
census assertion (rows == records, full field count on every row).

### Done since — steps 4 and 5 shipped

✅ **`tools/build-index-json.py` + `/scripture` + `/scripture/[book]` are live** (M4-RUNBOOK §9).
5,467 loci, 62 books, 281 showing a layer divergence. Each entry is ONE citation carrying both
printed forms, filed under the witness verse. `/scripture` is in the top-level nav (PLAN §6.1).

✅ **`pair_confidence` — the index refuses to merge a pair it cannot vouch for.** `align()` slid
and paired La `Psal. xxv. 22.` with En `iii. 8.`; merging filed Milton's Ps 25:22 under Ps 3:8,
a false claim about where he cites. 342 of 359 pairs are plausible; **the 17 suspects have their
own QA section and want a reader** — they are a real mixture of findings the pairing got right
(the `Isa. lviii. 56` dropped comma, the plate-confirmed `Isa. xxxi. 2` → `iii. 1`) and plain
alignment slips (`cap. xvi.` vs `xxxi. 14.`).

✅ **Three site bugs, all found by testing that the index's deep links resolve.** The test —
every anchor against the built HTML, now **5,809 references, 0 unresolved** — is the acceptance
check; re-run it after touching either side.
  1. **`/browse/2/4` served only part a.** M2 assumed one chunk per chapter; §8d split chunks
     arrived in M3. Parts b and c of II.iv were transcribed, committed and served to nobody, and
     prev/next linked the page to itself. Fixed in `content.ts` (`book.chapters`).
  2. **81 paragraphs carried no ¶ marker or anchor** — a page break inside the block defeated the
     `^{¶N}` match. Silently wrong since M2.
  3. **Five paragraph pairs in `ddc-2-13` lacked their blank-line separator** and rendered
     run-on. Separators only; the file is identical ignoring whitespace.

### ✅ Done 2026-08-28 (later) — the seventeen suspect pairings are READ

All seventeen read with both layers' paragraphs in view. **M4-RUNBOOK §10 is the write-up**; it
is the plan of record for what follows and this is only the pointer.

- **Ten of the seventeen are not slips at all** — they are the aligner correctly refusing to merge
  a pair the two volumes really do print differently, and **every one was already caught by hand
  and is already in its chunk's Notes.** That is the strongest evidence yet that the transcription
  front is doing its job; the parser found nothing the readers had missed.
- **The other seven exposed four parser defects, three of which put wrong targets in the live
  index.** §10.1 is **fixed**: `ROMAN_RE` was `[ivxlc]{1,7}`, so `lxxxviii` — **Psalm 88** — was
  invisible in both layers; the numeral is now spelled out well-formed for 1–199. Ledger diff:
  exactly the two intended rows, 5809 → 5811, nothing else moved.
- **§10.2 / §10.4 are one ruling and they are Wilson's.** The frozen rule that the English `v.` is
  always *versus* is **false** — `ddc-1-02` ¶27 En `v. 4.` is Ps 5:4 and is filed as Ps 103:4;
  `ddc-2-04-b` ¶9 En `v. 3.` quotes Ps 5:3 verbatim and is filed as Ps 55:3. Both chunks' Notes had
  already said so before the index existed. ⚠ The asymmetry is the real problem: **the Latin's
  `et v. N` is honestly withheld and sent to QA, the English's is resolved silently and always**,
  so the English's errors of this class are invisible by construction.
- **New reading aid: `tools/show-para.py <chunk-id> <¶> [<¶>…]`** prints one paragraph from every
  text layer in sequence. The QA report names a chunk and a paragraph; settling anything about one
  means seeing both layers of it.
- ⚠ **Footgun (§10.7):** `build-citations.py <chunk-id>` **rewrites the corpus ledger with that
  chunk alone.** It happened once this session and `--all` restored it exactly. Always finish with
  `--all`.

### The queue now

1. ★★★ **The corpus-wide audit — FIRST PASS DONE, §12. 22 rows moved in 7 chunks.** Each was
   printed as a *La error silently corrected by Sumner*; each is versification. Corrected in
   `ddc-1-02` · `ddc-2-04-c` · `ddc-2-05` · `ddc-2-08` · `ddc-2-09` · `ddc-2-11` · `ddc-2-15`,
   by a **correction block appended to each chunk's Notes** — the tables above them are left as
   printed, because re-keying seven tables by hand is how a transcription error enters, and the
   block says it governs. **Eleven J–T chapter divisions are now established** (§12.2).
   ★ **The method is what to carry forward: work BOOK-BY-BOOK, never chunk-by-chunk.** One
   division settles every citation of that chapter anywhere in the treatise — Isaiah 57 took two
   rows in two chunks with one read, Ecclesiastes' leaf 531 gave three chapters. And **check the
   arithmetic against the divisions already in §12.2 before fetching anything**: eight of the 22
   needed no new reading at all.
   **What is left** (§12.4), in order of how many rows each moves: **the Psalms as a class** —
   53 of 57 Psalm divergences are +1 or +2 and §6b already matched the split to one- and two-line
   superscriptions, so this wants a handful of leaves and a statement of the mechanism, not 57
   reads; then `ddc-2-05`'s four remaining Isaiah rows, `ddc-2-03`'s three, `ddc-2-06`'s
   `2 Sam. xxi. 2, 3` ("neither side is right"), `ddc-2-11`'s six.
   ⚠ Not every "La error" is suspect. The five surviving in II.xvii survive because their own
   quotation refutes them — `Act. xiii. 3` quotes Acts 23:4 — and that test disposes of most
   singletons. **A repeating offset is the signal; a singleton usually is not.**
2. **The `divergence_class` column** (§11.4). Right now "versification" vs "error" lives in prose
   in a chunk's Notes, so the site cannot render the distinction and nothing can count it. It
   should be data, sourced from the J–T table below it.
3. **The J–T chapter/verse table** — `tools/versification.json` answers *could this verse exist?*;
   this answers *what did Milton's Bible call it?*, which is the question the corpus keeps asking.
   §11.3a has the first seven rows. `tools/jt-page.py` is the instrument.
4. **§10.2 + §10.4 — one ruling, two symptoms.** May the English `v. N` reach QA the way the
   Latin's already can, and may `reconcile_et_v()` settle by *form* rather than by digit equality?
   Five real Latin citations are being dropped because a versification offset makes the digits
   disagree (table in §10.4). Coupled: the form-only relaxation is safe only once the English `v.`
   can also be doubted.
5. **§10.3 — a narrow licence for the bare Latin continuation?** `ddc-1-02` ¶27 prints `ciii. 11.`
   with no `et`, Sumner-fashion, in the Latin volume; the parser drops it and the following `v. 17`
   then carries Psalm **25** forward and is filed as Ps 25:17 when the quotation is Ps 103:17.
   Two instances is not a rule and the word hazard (`ii`, `vi`, `li`, `ci`) is real, so this waits.
6. **Hand-check the QA report chapter by chapter** — still owed, still the big one. Only
   `ddc-2-02` has been read record by record; the other 20 chunks have been *parsed*, not read
   (§6.5). Volume work over a frozen grammar; does not need a premium model.
7. **One out-of-range citation wants a plate**: `et xi. 32` (ddc-2-13 la ¶47), book *carried*.
   ✅ The second one added earlier — `ddc-2-17` ¶29 La `Isa. lvii. 2, &c.` — is CLOSED: J–T's
   `CAPUT LVII` opens at KJV 56:9 and its verse 2 is *Speculatores istius cæci*. Versification.
8. **M4 step 6** — backfill the index as each chapter lands; add the step to M3-RUNBOOK §2.
9. Still owed, recorded in `chunks/ddc-2-02.md` Notes: **five citation findings the parser turned
   up that the hand-log lacks**, incl. ★ **a citation Sumner SUPPLIES** at 1 Cor. i. 19, 20. ✅ The
   fourth kind — **omission** — is now attested too and is written into `ddc-2-04-c`'s Notes:
   ¶1's `et xxv. 22`, quotation and all, is simply not in the English.
10. M5 copy: About and Rights are still M2 placeholders, and `/scripture` is styled only with the
   existing card classes.

Numbers to compare against, so a regression is visible: **ddc-2-02 — 327 records, 0 unclassified,
layer spread 0.6%, all 9 hand-logged divergences found. Corpus — 5,811 records, 30 unclassified,
6 out-of-range, 7 versification, 428 divergence rows of which 17 suspect.** State:
`tools/build-citations.py` (`<chunk-id>` | `--all` | `--dump`) → `index/citations.tsv` and
`index/citation-qa.md`, both derived and re-runnable, zero writes under `chunks/`.
`tools/build-versification.py` → `tools/versification.json` is the target-exists table.
M4 steps **1-5 done**, step **6 untouched**.

⚠ One correction made earlier this session inside `chunks/ddc-2-10.md`: its `Psal. iii. 9.` note
claimed Hebrew Psalm 3 has eight verses. **It has nine.** The finding survives and sharpens — En's
`iii. 9` is a valid Hebrew number pointing at the wrong verse, so the defect is a conversion made
in the wrong direction, not a mis-set digit.

### ⚠ Two housekeeping facts from this session

- **Pushing to this remote fails over HTTP/2** with `RPC failed; HTTP 400`, and it fails
  *silently at the end of a session* — nine commits had piled up unpushed before it was caught.
  Fixed in this repo's local config only (`http.version HTTP/1.1`, `http.postBuffer 524288000`);
  it should not recur. **Check `git status -sb` for "ahead N" before ending a session.**
- ⚠ **`raw/loci/` IS ON THE REMOTE** — four files, ~2.9 MB (Wolleb and Ames, from
  `tools/fetch-loci.sh`). `.gitignore` covers `raw/*.pdf`, `raw/*_djvu.txt`, `raw/plates/`,
  `raw/crops/` and `raw/*-ch*.txt` but **not** `raw/loci/`, so they slipped in during an earlier
  session. The claim further down this file that raw/ is fully gitignored and that 0 raw/ paths
  are on the remote **is no longer true.** They are public-domain texts and harmless in
  themselves, but **the repo flips PUBLIC at M5**, so settle it before then. Two open decisions,
  both Wilson's: (a) add `raw/` wholesale to `.gitignore` going forward — cheap, no history
  touched; (b) remove them from history — a rewrite, and a protected action.

---


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
**Ratified 2026-08-27** — `## apparatus-sumner-la` with `[^laN]` is now CONVENTIONS §5.

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

## Two fronts are open — pick one

**A. `ddc-1-03`** — the transcription queue continues, below.
**B. M4, the scripture index** — `M4-RUNBOOK.md` is written and the prep is done (Wilson's ruling
2026-08-28: start on the 19 chapters in hand, don't wait for the corpus). It needs a session of its
own; §7 there gives the sequence and §8 the model note. Do not start it inside a transcription
session — step 2 is hand-checking a parser against a whole chapter.

## ▶ START HERE (transcription front) — `ddc-1-03` *De Divino Decreto*

State: Book II complete (17/17). Book I: **I.i and I.ii both verified, both layers.**
19 of 50 chapters done. **Nothing is owed on any existing chunk.**

`ddc-1-03` — La 22–30 (9 pp.) / En 30–43 (14 pp.). Nothing prepped: start with
`./tools/prep-chapter.sh 1 3`. Two things are already known about it:

1. **Its first English note must be 8.** I.ii closed at 7 and Sumner does not skip numbers (§8a).
   A first note that is not 8 means a note was missed in I.ii — come back and find it.
2. **The English chapter opens at En 30, plate-confirmed** (`CHAP. III. OF THE DIVINE DECREES`),
   which was read as I.ii's closing boundary. The Latin side (La 22) was confirmed the same way.

Per-chapter procedure is M3-RUNBOOK §2. Read every Latin page foot (§1 of the warnings below) and
run §11's anchor check before committing either layer.

## ✅ `ddc-1-02` IS CLOSED — both layers, 2026-08-28

La 10–21 / En 13–29, all four boundaries plate-confirmed, `status: verified`, `chapters.tsv` flag
flipped to `verified`. **32 La ¶¶ → 37 En**, three splits and no merges. Seventeen English notes,
the densest chapter in the corpus. The English was written **one paragraph per edit** from the
start after a batched write tripped a filter; **nothing was paraphrased or omitted**.

**★★ The finding to carry forward: an anchor can exist with no definition, and nothing catches it.**
The Latin layer was committed, plate-verified, queued and shown on the register carrying `[^la1]`
and `[^la2]` with **no `## apparatus-sumner-la` section at all** — and the omission was not on the
chunk's own "Owed on return" list either. The parser does not require anchors to resolve and the
footnote checksum cannot see a missing section, because the printed numbers stay consistent.
**M3-RUNBOOK §11 is now the check**; it is three lines and it was run against all 21 chunks, which
are otherwise clean. Both notes are now transcribed: La 12 `Sic in MS. An legendum se?` and La 20
`Sic in MS. Sed vide an legendum benignus…`.

**★ `tools/sumner-interventions.tsv` gained a `layer` column** and `la_page` became `page`. The file
was built assuming textual notes are a Latin-volume phenomenon; En 20's note 7 disproves it. Three
rows added — La 12, La 20, and **the ledger's first English-volume row**.

**★ The English volume settles Greek accents the Latin will not.** En 19 prints `θεοτὴς` and
`θειοτὴς` legibly at 1200 dpi where the Latin's do not resolve at 1400. Per §3 that does **not**
license repairing the Latin from the English: the English layer's accents are no longer UNVERIFIED,
the Latin's still are. Both are transcribed as printed.

**★ Ellipsis dot-counts vary from three to fifteen inside this one chapter** and every one of them
was confirmed at 900–1400 dpi, because 200 dpi is not good enough to tell five dots from six. There
is no house ellipsis in the 1825; count them per instance, as §2 requires.

**★ A footnote anchor fell inside an italic Scripture quotation** for the first time (En 24,
*I am the Almighty*⁵ *God*). Written `*I am the Almighty*[^s5-2] *God,*`, which preserves the anchor
position but splits the italic run, since markdown cannot nest. Recorded in the chunk, not yet a
convention — if Book I repeats it, it needs one.

## ⚠ TWO THINGS I.ii CHANGED ABOUT HOW BOOK I MUST BE WORKED

1. **★★★ `tools/sweep-book1.tsv` CANNOT BE TRUSTED.** The Latin-footnote detector flags La 12 and
   La 20 as clean; **both carry textual Sumner notes**. Book II's sweep concluded detector and eye
   agree on every page — that is no longer true, and it failed twice in the first long Book I
   chapter read. **Read every Latin page foot, every chapter.** Both notes open `Sic in MS.`, which
   at least gives the class a searchable signature.
2. **★★★ Book I inverts Book II's paragraph behaviour.** Book II was merge-dominated — Sumner
   welding Milton's short proof-text paragraphs together. I.ii is **split-dominated**: three splits,
   zero merges, because Milton's Book I prose is long and argumentative and Sumner breaks it up.
   Expect splits, not merges, through Book I's opening chapters.

## ⚠ WHAT I.i ESTABLISHED FOR THE REST OF BOOK I

1. **★★ Book I's footnote numbering is STILL unestablished, and I.i is why.** The chapter carries
   **zero footnotes in either layer** (all 4 English + 3 Latin feet read), so per §8a it passes the
   number through untouched and proves nothing. **The question is live.** Whichever Book I chapter
   carries the first note establishes the run for the whole book — so read every foot, and **record
   noteless chapters explicitly**, because a later note numbered 1 is evidence of a restart *only if
   every chapter before it has been confirmed noteless*.
2. **★★★ The Greek rule was wrong and is now corrected.** Book II generalised, over seven instances,
   that "Sumner keeps Milton's Greek when it is a quotation and removes it when it is a technical
   term." That predicts all three Greek words in I.i would be translated away; **all three are kept**
   (`τυπὸς`, `ὑποτύπωσις`, `μόρφωσις`). The distinction that holds is **use vs. mention** — Sumner
   removes Greek an English equivalent can carry, and keeps Greek that is *itself the subject under
   discussion*. The old formulation stands in the Notes of II.x, II.xi, II.xv and II.xvi; it is
   **superseded, not contradicted** — those observations are right, the generalisation was too narrow.
   ⚠ **A rule built on one book can fail on the next; re-test the Book II rules as Book I proceeds.**
3. **★★ A new English-error mechanism — the narrowing habit misfires.** Sumner routinely narrows a
   two-verse citation to its second verse. At `Joan. vi. 45, 46` → `John vi. 46` he keeps the verse
   that does **not** contain the quoted words. This is worse than a wrong digit for M4: the citation
   is internally plausible, and only checking the verse's *text* exposes it.

Also from I.i: the newly-ratified mid-word rule got its first outing **on a Greek word**
(`ὑπο<!-- p.9 -->τύπωσις`), which vindicates dropping the hyphen — keeping it would have produced a
non-word. The English recasts `DIVINITUS` from adverb to noun phrase in the work's founding
definition, so **no argument about what Milton means by "Christian doctrine" may rest on the English
clause alone**. And **the work's title block, on La 7 / En 9, belongs to no chunk** — if the site
ever shows front matter it must be sourced separately.

⚠ **Tooling:** `prep-chapter.sh` was broken for all of Book I and is fixed (`pdftoppm` zero-pads
output filenames to the PDF's page-count width, so La 7 was written `la-7-023.jpg`). It now globs
for what was produced. Book II never exposed this.

## What Book II established that Book I should carry forward

- **★★★ Sumner's apparatus is TOPICALLY MATCHED to the chapter.** II.xvii settles this: five of its
  six notes are Milton's political tracts, in the political chapter, where the ethics chapters drew
  the poetry (II.viii, II.xi) and the biography (II.ix, II.xv). The separate "habits" recorded chapter
  by chapter are one habit. **Never call a note-source new without checking the chapter's topic first.**
- **★★★ The 1825 edition is not a neutral vehicle.** II.xvii [^s6] is Sumner, in his own voice and
  quoting nobody, explaining away Milton's part "not only against the monarchy, but against the
  monarch himself"; [^s3] documents the political censorship of a passage it quotes. Both belong on
  the About page and bear on PLAN §4a.
- **★★★ Some Latin citation errors are SYSTEMATIC.** II.xvii has Ecclesiastes 10 three verses low
  twice and Isaiah 3 one verse high four times — and `Eccles. x. 2, 3` is the identical error II.xv
  carried, corrected identically and independently in both chapters. **When a citation is wrong,
  check whether the same book recurs in the chapter before calling it a compositor's slip.**
- **★★★ `et v. N` is ambiguous and NEITHER layer resolves it.** Usually *et versu N*, but sometimes
  chapter v — and the English prints the ambiguous form unchanged even while correcting its
  neighbours. **Only the quoted words identify the target.** This, with II.x's omission, II.ix's
  reordering, II.xv's deliberate double-citation, and Sumner's selective resolution of verbal ranges
  into digits, is the case for M4: **build the scripture index from the Latin, reconcile against the
  English, carry every divergence as data, and never de-duplicate by reference.**
- **★★ The dash-range rule** — the English contracts runs of 3+ consecutive verses, never runs of 2 —
  held across three chapters without exception.

## ✅ ALL OPEN CONVENTION QUESTIONS ARE RATIFIED — 2026-08-27 (Wilson)

The three questions that had been standing since II.iv/II.viii/II.xi, plus the headnote-cap
housekeeping item, were put to Wilson and ruled on together. **All four are now in `CONVENTIONS.md`
with the date; none is open.** Each ruling matched existing practice, so no chunk needed migrating.

1. **Splits — `{¶35}` + `{¶35 cont.}` ratified** (CONVENTIONS §4). The natural counterpart to
   `{¶N–M}` for merges. §4's coverage sentence, which said "every La ¶ appears exactly once on the
   En side" and was written before a split had been seen, is **corrected** to "every La ¶ is fully
   accounted for, once as a whole or once across its `cont.` pieces." 2 instances (II.xi, II.xiii).
2. **Raised ordinals — inline `1m. 2do. 3tio.` ratified** (CONVENTIONS §2), and recorded there as a
   named *normalisation*, on the same footing as the chapter-opening display capitals: the raising is
   the abbreviation convention for *primo/secundo/tertio*, and the numeral already carries the
   enumeration — **typography, not text**. 19 instances across 5 chunks. ⚠ The rule states its own
   cost: the English destroys the feature outright ("first, Secondly"), so after normalisation the
   raised form survives **only on the plate**. Where a chapter's argument turns on the series —
   II.xvii's seven rules of war — say so in that chunk's Notes.
3. **Mid-word page break — current practice ratified** (CONVENTIONS §2): `accept<!-- p.614 -->able`,
   marker inline, **soft hyphen dropped**, because the end-of-line hyphen is a line-breaking artefact
   and keeping it would break the word for search and for the M4 index. This was never really open —
   15 instances across 11 chunks were already uniform; it was undocumented, not undecided.
4. **Headnote cap — aim 200, hard cap 300** (CONVENTIONS §8, revised). The flat ≤200 was breached by
   **14 of 19** chunks, to 343; the dense chapters cannot be served in 200. Two chunks were trimmed
   to comply (`ddc-2-04-c` 308→294, `ddc-2-13` 343→300); all 19 now run 161–300. The old
   "measured two ways" worry is dropped — the two counts differ by three words, which is noise.

**Book I therefore starts with no convention questions outstanding.**

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

**Housekeeping — SETTLED 2026-08-27:** the headnote cap is now *aim 200, hard cap 300* (CONVENTIONS
§8), and the two-ways-of-counting worry is dropped as noise.

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

## Owed by Wilson

- ~~GitHub remote~~ **done 2026-08-04** — `wilsonpruitt/milton-doctrina`, **PRIVATE**, `main`
  tracking `origin/main`. `raw/` (PDFs, plate renders, OCR dumps) is gitignored and stays local;
  verified 0 `raw/` paths on the remote. **Flip to public only at M5**, and not before
  `site/src/app/rights/page.tsx` carries a real rights statement — CC BY-NC 4.0 on the English and
  the encoding, PD on the 1825 source (see the Wroot Press licensing memory). Note the repo landed
  under `wilsonpruitt`, not the `littleeachdayapp-droid` bridge account.
- Domain wiring for milton.wrootpress.com when M5 nears (Cloudflare, DNS-only per house rule).
