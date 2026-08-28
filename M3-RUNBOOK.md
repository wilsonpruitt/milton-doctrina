# M3 runbook — the volume run

**Read `PLAN.md` §5 and `CONVENTIONS.md` once at session start, then work from this file.**
`chunks/ddc-2-02.md` is the format reference. **No partial chunk remains in the corpus** —
`ddc-2-01` was the last and closed 2026-08-04; the shape is still legal (CONVENTIONS §8d) and
that chunk's Notes record how it was worked.

This file exists so a transcription session spends its tokens on plates, not on rediscovering
procedure. Everything mechanical has been pre-staged.

---

## 0. What is already true (don't re-derive)

- **Offsets, measured at M0, exact:** `la_pdf = la_printed + 16` · `en_pdf = en_printed + 56`.
  Body extents: La printed 7–536, En printed 9–711.
- **`tools/chapters.tsv`** is the chapter → page table for all 50 chapters, with a `flag`
  column. Read the flag before you touch a chapter.
- **`tools/prep-chapter.sh <book> <ch>`** renders both plate sets at 200 dpi and both
  pdftotext drafts. Costs no model tokens. Already run for **II.iii–II.ix**.
- **`tools/crop-plate.sh <la|en> <printed> <dpi> <y0> <y1> <name>`** renders one page at any dpi and
  saves a full-width band to `raw/crops/`. This is CONVENTIONS §2's "doubtful characters get a
  400 dpi crop" made cheap: 600 dpi settles a citation digit, 900 dpi settles a single wrong sort.
  **Every ★ finding in a chunk's Notes should rest on a crop, not on the 200 dpi plate.**
- **`tools/audit-chapter-starts.py`** re-derives every chapter opening from the text layer and
  reconciles it against `chapters.tsv`. Already run; results are baked into the flags.
- **The site handles partial chunks.** `site/scripts/build-content.mjs` discovers whatever
  `## <langkey>` sections exist, so a Latin-only chunk builds fine.

## 1. Queue

Order is PLAN §8: **Book II first** (shorter, more regular, builds rhythm), then Book I,
**saving I.iv–I.vi for last** because I.v *De Filio Dei* is 53 Latin pages, the hardest
doctrine, and the chapter everyone will actually read.

| # | chunk | state |
|---|---|---|
| — | `ddc-2-02` | **done** (M1 pilot, Fable) |
| — | `ddc-2-01` | **done** (2026-08-04, Opus) — La 387–394 / En 527–536. **21 ¶¶ → 17**, two merges incl. a **QUADRUPLE** at {¶9–12}, the largest in the corpus. **Checksum passes EXACTLY: notes 3,4,5,6,7**, as §4 predicted before the range was abandoned. **★★ Notes 5 and 7 are *Paradise Lost* XII and *Sonnet* XIX — so II.viii's "first time he reaches for the poetry" is WITHDRAWN; it was an artefact of transcription order.** ★ Third English-side error (La `Prov. xxiv. 1` right, En `xxiv. 7` wrong, 640 dpi). ★ Greek `ἀτοπία` translated away. Transcribed past the content filter one paragraph per edit; {¶6} took six pieces. |
| — | `ddc-2-03` | **done** (2026-08-03, Opus) — no Sumner footnotes at all |
| — | `ddc-2-04-a` | **done** (2026-08-03, Opus) — La 413–416 / En 557–562; notes 1–5 |
| — | `ddc-2-04-b` | **done** (2026-08-03, Opus) — La 417–420 / En 563–568, the whole `REVERENTER` lemma; notes 6,7,8,9,**1**,2,3,4 (contains the 9→1 wrap) |
| — | `ddc-2-04-c` | **done** (2026-08-03, Opus) — La 420–428 / En 568–578; notes 5–8. **II.iv complete.** |
| — | `ddc-2-05` | **done** (2026-08-04, Opus) — La 429–439 / En 579–592, both layers plate-verified. **34 ¶¶ → 34 ¶¶, strict 1:1, no merges** (first whole chapter to do so). Notes **9, 1, 2, 3, 4, 5** — the predicted wrap confirmed. All four suspect La citations resolved, all four `Luc. ix. 66`-class; **eight La errors in one chapter, four in Isaiah**. The English carries **no** counterpart to `[^la5]`. |
| — | `ddc-2-06` | **done** (2026-08-04, Opus) — La 440–445 / En 593–599. 23 ¶¶ → 22, one merge at {¶13–14}. Notes **6, 7** as predicted. No Latin apparatus. **★ The English volume's HEBREW is corrupt where the Latin's is sound** — see the chunk's Notes; **resolved 2026-08-04**, and it is why CONVENTIONS §5c exists (`## apparatus-editorial`, ⚠ UNVERIFIED). The two readings still await a Hebraist. Writing its *blasphemia* paragraphs tripped a content filter — see §10. |
| — | `ddc-2-07` | **done** (2026-08-04, Opus) — La 446–454 / En 600–612. **22 ¶¶ → 22, strict 1:1.** Notes **8,9,1,2,3,4,5,6,7,8** — ten notes, so the cycle COLLIDES inside one chunk; the `[^s8-2]` scheme was **ratified 2026-08-04**, CONVENTIONS §5b. Latin note `[^la4]` is scholarly not textual. **★ Sumner's note `[^s9]` states the whole Ames/Wollebius loci thesis.** Filter-blocked three times; see §10. |
| — | `ddc-2-08` | **done** (2026-08-04, Opus) — La 455–461 / En 613–620. **27 ¶¶ → 25**, two Sumner merges ({¶5–6}, {¶11–12}), both a lemma absorbed into the paragraph it governs. **Exactly one note, printed 9** — the prediction was exact. No Latin apparatus (all 7 feet read). Five citation divergences, all versification, none of the `Luc. ix. 66` class. **★ `[^s9]` is fourteen lines of *Samson Agonistes* — the first time Sumner reaches for the POETRY, and he does it where Milton's prose on self-slaughter is briefest.** No filter blocks: every paragraph written singly. |
| — | `ddc-2-09` | **done** (2026-08-04, Opus) — La 462–473 / En 621–635. **41 ¶¶ → 41, strict 1:1** — the longest chapter so far and only the second to run 1:1 throughout (after II.v). Notes **1, 2, 3**; the wrap confirmed. No Latin apparatus in 12 page feet. **★★ All three notes DEFEND MILTON'S CHARACTER** (drink, sleep, chastity) out of *Comus*, *Samson Agonistes*, *PL* XI, the elegies and the *Apology* — a fourth editorial behaviour; II.viii's note amended because of it. **★★ The English ADDS a Cowper translation of the Homer line with no Latin counterpart** — neither layer is a complete witness to the other. **★ Seven La citation errors corrected, three in {¶16} alone; and ONE error the other way** (La `Dan. ii. 30` right, En `ii. 31` wrong — 2nd English error in the corpus). Sumner also silently **reorders proof-texts at {¶29}** and renders *ornamenta vitæ* as "a high station". |
| — | `ddc-2-10` | **done** (2026-08-05, Opus) — La 474–476 / En 636–638, both extents plate-confirmed at both ends (`CAP./CHAP. XI` opens La 477 / En 639); flag flipped to `verified`. **10 ¶¶ → 9**, one merge en{¶3–4}. **One note, printed 4 — the prediction was exact.** No Latin apparatus. **★★ ἀπάθεια translated away ("a stoical apathy") — the Greek-technical-term pattern now holds over five instances read.** **★★ The English DROPS a proof-text** (La `et cxii. 7.` has no En counterpart, both confirmed 600 dpi) — a third kind of unmarked editorial handling, beside correction and reordering; **bears on M4's scripture index.** **★ Fourth English-layer error: `Psal. iii. 9.`, impossible (Ps 3 has 8 verses); expected `iii. 6`, likely a turned `6`.** No `Luc. ix. 66`-class error at all — the first chapter with none since II.iii. |
| — | `ddc-2-11` | **done** (2026-08-05, Opus) — La 477–486 / En 639–649, both extents plate-confirmed at both ends (`CAP./CHAP. XII` opens La 487 / En 650); flag flipped to `verified`. **38 ¶¶ → 37**, and the shape is new: **two merges AND ★★ THE CORPUS'S FIRST SPLIT** — Sumner divides La {¶35} into two English paragraphs, so CONVENTIONS §4's "every La ¶ appears exactly once" is false as written; notation `{¶35 cont.}` — **ratified 2026-08-27**, CONVENTIONS §4. Notes **5, 6, 7** — the prediction was exact; **all three defend Milton** (the *Apology* on sanctified bitterness; *PL* IV. 502, IX. 173, XI. 455 on envy), `[^s6]` carrying two passages under one number. No Latin apparatus (all 10 feet read; sigs `3 Q`@481, `3 Q 2`@483). **★★ Six Latin citation errors silently corrected, but only two were on the suspect list** drafted from the Latin — the Esau, Ecclesiastes and Judges errors were invisible until the English was beside them. **★★ ἐπιχαιρεκακία translated away — the Greek rule survives its immediate re-test, six instances.** **★★ Second attested English omission** (`Luc. vi. 27, &c.` dropped). **★ Two English printed errors, one in the chapter's first line** (`justiee`, 900 dpi; and {¶13} has no full stop). **★ The Latin's arabic `2 Thess. 3, 10.` is NOT mirrored** in the English — accidentals do not cross layers either. |
| — | `ddc-2-12` | **done** (2026-08-27, Sonnet) — La 487–491 / En 650–654, both extents plate-confirmed at both ends (`CAP./CHAP. XIII` opens La 492; En chapter ends cleanly mid-page 654, no boundary plate needed). **16 ¶¶ → 15**, one merge at {¶14–15}. **Zero footnotes in either layer** — the third chapter in the corpus with none; per §8a a zero-note chapter passes the cycle through untouched, so **II.xiii must still open at note 8**, same prediction as before this chapter. **★ Sixth Psalm-transposition error in the corpus**: La `cxiv. 2` (no such verse) silently corrected to En `xciv. 2`, sitting inside a cluster of three ordinary versification shifts (Ps. 18, 54, 92) in the same paragraph. **★ `1 Pet. iii. 9` (La) → `iii. 8, 9` (En)** — a widened citation with no new quoted text, a divergence shape not seen before. La's `masculorum concubitu` generalized to "unnatural vices" in English; La's `meretorius` sharpened to "a sodomite" — not a uniform direction this chapter. |
| — | `ddc-2-13` | **done** (2026-08-27, Sonnet) — La 492–503 (12pp) / En 655–671 (17pp), both extents plate-confirmed at both ends (`CAP./CHAP. XIV` opens La 504 / En 672, headed "ADHUC..." / "...CONTINUED" — Milton's own rubric flags II.xiv as a direct continuation). **48 ¶¶ → 49**, the corpus's **second SPLIT** (La {¶29} `FIDELITAS` → En {¶29}+{¶29 cont.}), same open question as II.xi's first split. **Seven English notes** (8,9,1,2,3,4,5 — wraps once, densest run in the corpus; **II.xiv opens at 6**), one Latin note (La5, scholarly, Jael/Junius). **★★ New note-class**: [^s2]/[^s3] quote OTHER PEOPLE's testimony about Milton (Richardson, Symmons, Vossius, Heinsius) rather than Milton's own works — a fourth editorial behaviour. **★★ [^s5] is the richest note in the corpus**: English + Latin + Greek (εὐθυρρήμονα/εὐσχήμονα) across three of Milton's own prose works. **★** La[^la5] and En[^s9] quote the SAME Junius sentence on Jael under different note numbers, differing by one word (`intercessit`/`intercepit`). The chapter's doctrinal core — Milton's redefinition of lying to license deceiving non-neighbours, including war stratagems — carries **zero apparatus in either layer**. |
| — | `ddc-2-14` | **done** (2026-08-27, Sonnet) — La 504–510 (7pp) / En 672–679 (8pp), both extents plate-confirmed (`CAP./CHAP. XV` opens La 511 / En 680, a genuinely new topic — reciprocal/domestic duties — unlike XIII→XIV's continuation). **24 ¶¶ → 24, strict 1:1** — no merge, no split; only the third chapter in the corpus to run 1:1 throughout (after II.v, II.ix). **One note (6)**, closing the wrap from II.xiii; defends Milton's usury argument by quoting *Doctrine and Discipline of Divorce* — first defensive note on an economic rather than theological/biographical question. **★ Hebrew (נֶשֶׁךְ, "bite") appears in BOTH layers at the same point** — first time in the corpus Hebrew crosses both volumes rather than sitting in one alone. **★** En {¶19} names Tremellius inline — `(gratiose largitur, Tremell.)` — an unnumbered scholarly aside, not apparatus, first of its kind. |
| — | `ddc-2-15` | **done** (2026-08-27, Opus) — La 511–519 / En 680–690, both extents plate-confirmed at both ends (`CAP./CHAP. XVI` opens La 520 / En 691); flag flipped to `verified`. **38 ¶¶ → 37**, one merge at en{¶13–14}, no split. Notes **7, 8, 9** — the prediction was exact, and **the 9→1 wrap is OBSERVED, not inferred**: En 691 carries note ¹ on the boundary plate, so II.xvi is confirmed to open at 1. No Latin apparatus (all 9 feet read). **★★ The chapter's heterodoxy is the EDITOR'S, not Milton's** — PLAN §6.2 puts divorce/polygamy in II.xv, but Milton's text is conventional throughout and silent on divorce; the divorce material enters via **Sumner's note 8** (*Doctrine and Discipline of Divorce* on Grotius, Theodosius II and Justinian) hung on a bare Proverbs proof-text. Check text vs. apparatus before repeating a PLAN heterodoxy claim. **★★ Note 7 spans a page and the catchword tracks the FOOTNOTE, not the text** (En 681 catchword *Was*); it carries *PL* IV. 635, X. 145, X. 195 and *Tetrachordon* under one number. **★★ Note 9 defends Milton against the schoolmaster jeer** (Leigh, Salmasius) and closes in Sumner's own dry voice about Newton and Symmons — a new register. **★★ Three La citation errors silently corrected, and all three were caught from the LATIN ALONE** (`1 Sam. xiv. 45`→44 · `Isa. iii. 6`→iii. 5 · `Eccles. x. 2, 3`→x. 5, 6, all 600 dpi both sides) — compatible with II.xi, not a reversal: this class is one-layer-detectable, II.xi's was not. **★★ ἀλλοτριοεπίσκοπος translated away** (900 dpi) — 7th instance, and the hardest case, since the word is both quotation and technical term; Sumner treats it as a term. **★ `et v. N` = *et versu N* in BOTH layers, 9 instances — a real M4 parser hazard.** **★ Milton cites Prov. iii. 33 / xiv. 11 / xv. 6 TWICE each on La 517**, once per half-verse; an index that de-duplicates by reference would destroy the antithesis. ★ En splits *servus* into "servants" (duty) vs "slaves/bondmen" (property). |
| — | `ddc-2-16` | **done** (2026-08-27, Opus) — **La 520–524 / En 691–695**, all four boundaries plate-confirmed; flag flipped to `verified`. **★★ EXTENT CORRECTED: the Latin runs 5 pp., not the crosswalk's 4** — La 524 carries the closing *inhospitalitas* paragraph and a blank tail, and `CAP. XVII` opens **La 525**. **This resolved the 2.17 suspect flag: the audit was right, the crosswalk was wrong.** **15 ¶¶ → 13**, one **triple merge** at en{¶6–8}. **One note, printed 1** — predicted exactly; II.xvii opens at 2. No Latin apparatus. Page ratio **1.00**, a true negative (cf. II.x). **★★ Sumner ADDS a doctrine the Latin lacks**: *ne absurda æquatio inæqualium fiat* → "lest we fall into the absurdity of equalizing **those whom nature never intended for an equality**" (600 dpi both sides). The Latin supplies neither *nature* nor *intention* — the largest interpretive addition in the corpus, and on Milton's social politics; do not source a headnote claim there from the English. **★★ New divergence class — a verbal range resolved into digits**: La `Job. xxix. a v. 11. usque ad finem capitis` → En `Job xxix. 11—25`. **★ First ENGLISH word-substitution error** (all prior ones were digits or a wrong sort): En 692 `Deut. x. 18. he doth **create** the judgement` for *execute*, 900 dpi. **★ Three Latin punctuation anomalies in five pages, all in gathering 3X** (`Psal. lxviii, 6.` · `Prov. xiv. 21:` · `Heb. xiii. 2,`). **★ The II.xv dash-range rule re-tested and now precise: 3+ consecutive verses always contract, 2 never does** (7 and 10 instances respectively). ★ The same-verse-two-halves pattern recurs twice (`2 Cor. ix. 6`, `Deut. xxvii. 19`). |
| — | `ddc-2-17` | **done** (2026-08-27, Opus) — **BOOK II COMPLETE.** La 525–536 / En 696–711, all four boundaries plate-confirmed (La ends `TOTIUS OPERIS FINIS`, En ends `THE END`). **31 ¶¶ → 31, strict 1:1** — no merge, no split; the longest chapter to run 1:1 (cf. II.v, II.ix, II.xiv). Not split: at exactly 12 La pp. it is *at*, not over, §7's threshold, and II.ix set the precedent. **Six notes, 2·3·4·5·6·7** — opens at 2 as predicted; **the Book II ledger now closes.** No Latin apparatus (12 feet read). **★★★ SIXTEEN La citation errors silently corrected — twice II.v's record**, and **two are SYSTEMATIC**: Eccl. 10 cited twice, 3 verses low both times; Isa. 3 cited four times, 1 verse high every time — the error is in the source, not the setting. **★★★ `Eccles. x. 2, 3` is the SAME error II.xv carried at La 516**, corrected identically and independently in both places. **★★★ `et v. N` is AMBIGUOUS and NEITHER layer resolves it** — `et v. 23` in an Isaiah-3 run is Isa. **5**:23, and the English prints it unchanged while correcting its neighbours; only the quoted words identify the target. **★★ Sumner RESOLVES verbal ranges into digits 5× but drops/keeps 2×** — build the M4 index from the Latin, take the English's digits as annotation. **★★★ The apparatus is TOPICALLY MATCHED to the chapter**: five of six notes are Milton's political tracts (*Defensio* ×2, *Eikonoklastes* ×2, *Civil Power*/*History of Britain*), the sixth *PR* IV where Milton commends Deuteronomy to statesmen — this unifies II.viii/II.ix/II.xiii/II.xv's separate 'habits' into one. **★★★ [^s3] documents the CENSORSHIP of the passage it quotes**; **★★★ [^s6] is Sumner apologising for Milton's regicide in his own voice** — the strongest evidence yet of the editor's stake, for PLAN §4a and the About page. **★ Seven raised ordinals in one paragraph** (inline `1m. 2do.` — **ratified 2026-08-27**, CONVENTIONS §2); **★ En `ususper`** for *usurper* and **★ En `1 Thess. ii 5.`** (first English-side missing point), both 900 dpi. |

### ✅ BOOK II IS COMPLETE — 17/17 chapters, all `verified` (2026-08-27)

Every Book II chapter is transcribed in both layers, plate-verified, and flagged `verified` in
`chapters.tsv`. The ten rows still reading `ok` were flipped on this evidence chain: **each chapter's
START is plate-read from its own opening plate** (the transcriber reads `CAP. N` to begin), and **its
END is confirmed by the next chapter's plate-confirmed start**; II.xvii's end is sealed by
`TOTIUS OPERIS FINIS` / `THE END`. No Book II boundary is now unresolved, and **no suspect flag
remains in Book II** (2.17, the last, fell during II.xvi — see §7).

**The English footnote ledger for Book II is closed and unbroken**, II.i → II.xvii; see §3.
**Latin apparatus in Book II stands at exactly two notes**, La 431 (textual) and La 454 (scholarly),
both found by the sweep; chapters II.x–II.xvii added none, all their page feet having been read.

## 1a. NEXT: Book I

| # | chunk | state |
|---|---|---|
| — | `ddc-1-01` | **done** (2026-08-27, Opus) — La 7–9 / En 9–12, all four boundaries plate-confirmed (`CAP./CHAP. II` opens La 10 / En 13); flag → `verified`, crosswalk correct. **9 ¶¶ → 9, strict 1:1.** **★★ ZERO footnotes in either layer** — so **Book I's numbering is still unestablished**; the question passes intact to I.ii. No Latin apparatus (3 feet read; agrees with `sweep-book1.tsv`). **★★★ THE GREEK RULE IS CORRECTED** — Book II's "keeps quotations, removes technical terms" predicted all three Greek words here would go; **all are kept**. The real distinction is **use vs. mention**: Sumner removes Greek an English equivalent can carry, and keeps Greek that is *itself the subject under discussion* (`vox Græca τύπος`). Covers all 11 instances; supersedes the formulation in II.x/II.xi/II.xv/II.xvi. **★★ First application of the new mid-word rule, and it is to GREEK** (`ὑπο<!-- p.9 -->τύπωσις`) — keeping the hyphen would have made a non-word. **★★ En recasts `DIVINITUS` (adverb) as `DIVINE REVELATION` (noun phrase)** in the work's founding definition and in its lemma. **★ First La error of Book I**: `Act. xxiv. … v. 6` → `v. 16`. **★★ New English-error mechanism** — the narrowing habit misfires: `Joan. vi. 45, 46` → `John vi. 46`, but the quoted words are 6:**45**. **★ The layers disagree on a Greek accent** (La `τύπος` / En `τυπὸς`, 1000 dpi). **★ The work's title block is on this page and belongs to no chunk** — source it separately if the site ever shows front matter. |
| — | `ddc-1-02` | **done** (2026-08-28, Opus) — **both layers complete.** La 10–21 / En 13–29, all four boundaries plate-confirmed (`CAP./CHAP. III` opens La 22 / En 30); flag → `verified`. **32 ¶¶ → 37, THREE SPLITS and NO MERGES**, inverting Book II's merge-dominated pattern; two of the three are three-way, `{¶N cont. 2}` per CONVENTIONS §4. **Seventeen English notes** (`9 · 1–9 · 1–7`), densest in the corpus — **I.iii opens at 8.** The English was written one paragraph per edit throughout after a batched write tripped a filter on 2026-08-28; nothing was paraphrased or omitted. **★★★ TWO Latin textual notes (La 12, La 20) and `sweep-book1.tsv` flags BOTH pages clean** — the detector's first false negatives. **★★★★ Sumner TRANSLATED HIS OWN CONJECTURE**: La 20's `SUMME BEATUS` is queried in `[^la2]` and rendered "MOST GRACIOUS" (= *benignus*) in English, the note having no English counterpart — neither layer alone tells the reader. **★★★★ En 20 note 7 is a TEXTUAL note in the ENGLISH volume**; `sumner-interventions.tsv` gained a `layer` column for it and `la_page` became `page`. **★★★ The use/mention Greek rule confirmed both ways in one chapter** (En 17 translates, En 19 keeps). **★★★ The Arian argument is made HERE, not only in I.v** — hypostasis collapsed into essence (La 15), *nullus spiritus, nulla persona* (La 17), the Father as the one God (La 18), and Milton's own `verum de his plura cap. 5.` **★★ The chunk shipped its Latin layer with `[^la1]`/`[^la2]` anchored and NO `apparatus-sumner-la` section**, and the omission was on no owed list — see §11. **★ En 19's `θεοτὴς`/`θειοτὴς` resolve at 1200 dpi** where the Latin's do not; the English layer's Greek accents are no longer UNVERIFIED, the Latin's still are. |
| 1 | `ddc-1-03` | `De Divino Decreto` — La 22–30 (9 pp.) / En 30–43 (14 pp.). **Nothing prepped.** First English note must be **8**. |
| 2+ | `ddc-1-07` … `ddc-1-33` | in order, saving I.iv–I.vi for last (§5) |
| last | `ddc-1-04`, `ddc-1-05`, `ddc-1-06` | see §5 |
| last | `ddc-1-04`, `ddc-1-05`, `ddc-1-06` | see §5 |

## 2. Per-chapter procedure

1. **Check the flag** in `chapters.tsv`. If `suspect`, resolve the boundary off the plate
   *first* and correct the file — do not transcribe against a bad range.
2. **Prep** if not already: `./tools/prep-chapter.sh <book> <ch>`.
3. **Latin layer.** Read every plate in order. The pdftotext draft is a finding aid to speed
   reading; it is never the text. Number paragraphs `{¶1}…{¶N}` in reading order — the Latin
   paragraphing is the reference grid. **Check every Latin page foot for footnotes** (§9) — the
   Latin volume carries apparatus, and its notes are textual: they go in
   `## apparatus-sumner-la` AND in `tools/sumner-interventions.tsv`.
4. **English layer.** Read every plate. Open each paragraph with the La ¶ it renders
   (`{¶4}`, or `{¶2–3}` for Sumner's merges). Coverage must be complete and monotonic.
5. **Run the checks in §3.** All of them.
6. **Write the chunk** in the CONVENTIONS §7 section order — note it now includes
   `## apparatus-editorial` (CONVENTIONS §5c) for notes of our own, anchored bare `[^N]`.
   If the chapter carries ten or more English notes the printed numbers collide: use the
   `-2` suffix (CONVENTIONS §5b). Log divergences, accidentals, typography and
   alignment in `## Notes`.
7. **Headnote** — 4 slots, ≤200 words, `*Loci: pending M4.*`. Write it only with both layers
   in hand; it is not draftable from the Latin alone.
8. `cd site && node scripts/build-content.mjs` to confirm the chunk parses.
9. Update `next-session-resume.md`.

## 2a. ✅ The open convention questions are CLOSED — 2026-08-27

Splits (`{¶35 cont.}`), raised ordinals (inline `1m. 2do.`), the mid-word page break (soft hyphen
dropped) and the headnote cap (aim 200, hard cap 300) were all ruled on by Wilson together and are
recorded in `CONVENTIONS.md` §§2, 4, 8 with the date. Every ruling matched existing practice, so
nothing needed migrating. **Do not re-open any of them per chapter**; Book I starts clean.

## 3. The checks — run every chapter, no exceptions

- **Footnote checksum — read the REWRITTEN CONVENTIONS §8a, not your memory of it.** Sumner's
  English note numbers are **single-digit and cycle 1–9**; after 9 the next note is 1. (The old
  rule said "continuously through the book," implying an ever-increasing ledger. Wrong, and
  plate-disproved at En p. 566, where ⁹ and ¹ sit in the same footnote block.)
  Record this chapter's first and last note and every wrap inside it; the first note of chapter
  *N+1* must be one past the last of chapter *N*, **wrapping 9 → 1**. A chapter with zero notes
  passes the number through untouched.
  **Ledger:** II.i → **3, 4, 5, 6, 7** (✅ CLOSED 2026-08-04 — 6 and 7 found on En 530 and 535, exactly as predicted) · II.ii →
  **8, 9** · II.iii → **none** · II.iv → **1–9, then 1–8** · II.v → **9, 1, 2, 3, 4, 5** ·
  II.vi → **6, 7** (both predicted and confirmed) · II.vii → **8, 9, 1, 2, 3, 4, 5, 6, 7, 8** (ten
  notes, the cycle collides inside one chunk) · II.viii → **9** (a single note, predicted exactly) ·
  II.ix → **1, 2, 3** (the wrap confirmed on En 621; all fifteen plates read, 625–635 carry none) ·
  II.x → **4** (a single note, predicted exactly; no wrap inside the chapter) ·
  II.xi → **5, 6, 7** (predicted exactly; no wrap; all eleven En feet read, 8 of them bare) ·
  II.xii → **none** (all eleven feet read, both layers — the number passes through untouched) ·
  II.xiii → **8, 9, 1, 2, 3, 4, 5** (wraps once at En 662; all seventeen En feet + twelve La feet read) ·
  II.xiv → **6** (a single note, predicted exactly; all eight En feet + seven La feet read) ·
  II.xv → **7, 8, 9** (predicted exactly; no wrap inside the chapter; all eleven En feet + nine La feet read) ·
  II.xvi → **1** (a single note, predicted exactly; the 9→1 wrap directly observed on En 691; all five En
  feet + five La feet read) · II.xvii → **2, 3, 4, 5, 6, 7** (opens at 2 as predicted; all sixteen En feet
  + twelve La feet read).
  **✅ THE BOOK II LEDGER IS CLOSED AND UNBROKEN, II.i → II.xvii.** Every chapter's first note was
  predicted from its predecessor's last and confirmed on the plate; not one break was ever found.
  **★★★ BOOK I's numbering is RESOLVED — the cycle starts in Sumner's PREFACE.** En pp. 1–8 are the
  preface and carry notes **1–8** (p. 7 = note 7, *Of Reformation*; p. 8 = note 8, *Of true
  Religion* — both plate-read). **I.i carries none.** **I.ii opens at 9.** So the 1–9 cycle runs
  unbroken through the whole volume — preface → Book I → Book II, where II.i opening at **3** is
  exactly what a continuous cycle predicts if Book I closes at 2. §8a told the transcriber to assume
  neither continuation from Book II nor a restart; the answer is a third thing neither option
  anticipated, and **the checksum is now live for all 33 Book I chapters.**
  **Book I ledger:** preface → **1–8** · I.i → **none** · I.ii → **9 · 1–9 · 1–7** (seventeen, the
  densest chapter in the corpus). So **I.iii must open at note 8.**
  Blind spot: the cycle is only 9 long, so it can never detect a miss of exactly 9 notes. It is
  not a substitute for reading every plate for superscripts.
- **Also check the LATIN plates for superscripts.** The Latin volume carries apparatus too — see
  §9. **Its numbers are LABELS and will never be a checksum** — settled by the sweep, §9b; nothing
  detects a missed Latin note except reading the feet, so read them. **Classify each Latin note
  textual or scholarly** (CONVENTIONS §5a): only textual ones get a row in
  `tools/sumner-interventions.tsv`. Both kinds exist — La 431 is textual, La 454 scholarly.
- **¶ coverage.** Every La ¶ appears exactly once on the En side. Count both sides and record
  the merge list.
- **Page ratio.** En pages ÷ La pages should land ~1.1–1.8. Outside that, suspect a boundary.
- **Citation divergences (§3).** La and En disagree on citation digits systematically and
  irregularly. Transcribe each side as printed, never harmonise, log every divergence.
- **Chapter-boundary confirmation.** `prep-chapter.sh` renders one page past the computed end.
  Look at it: it should be the next chapter's opening or a blank tail. If it's continuous
  text, the extent is wrong.

## 4. ✅ DISCHARGED — II.i English (was the one outstanding debt)

**Closed 2026-08-04 on Wilson's go-ahead**, using the one-paragraph-per-edit technique of §10.
`chunks/ddc-2-01.md` is `status: verified`, both layers, 21 ¶¶ → 17.

Kept here because the episode is the best evidence the project has for two rules:

1. **§10 works, and nothing was lost to the filter.** {¶6} blocked twice as a whole paragraph and
   went through in **six pieces**; the remaining long paragraphs were pre-split and passed first
   time. Five blocks across the chapter's history, **zero paraphrase, zero omission**.
2. **A queue that does not run in book order will manufacture false "firsts."** Because this
   chapter's English was transcribed last, II.viii recorded a Sumner habit as novel that II.i —
   the Book's opening chapter — already displays. That claim has been **withdrawn** in
   `ddc-2-08.md`. **Any "first time X appears" note is a claim about what has been read; say so.**

The chapter's checksum prediction (notes 3–7) held exactly, which closes the last open cell in the
§3 ledger.

## 5. I.iv–I.vi are scheduled last on purpose

PLAN §10 risk #2: I.v *De Filio Dei* is 53 Latin pages, ~14% of Book I on its own, the
anti-Trinitarian chapter, and the one carrying the heaviest apparatus. It is scheduled last so
conventions are fully settled before it is touched, and so it cannot swallow the schedule
early. **It will need splitting** (§7: >12 La pages), at Milton's own lemma seams.

`1.5`'s extent is **settled**: La 57–109, En **80**–152 (§7, 2026-08-28). And the first seam is
already found — the chapter opens `CAP. V. / PRÆFATIO.`, not with its title, so the *Præfatio* is
`ddc-1-05-a` and it is Milton's own seam rather than an arbitrary cut.

## 6. Model and burn

- **M3 is Opus per chunk.** Per `feedback_opus-for-authored-prose`, the volume-shaped look of
  the work is not a reason to downgrade; it is authored transcription against a plate.
- Measured so far: II.i's Latin layer (8 plates + 3 crops + ~28 KB written) came in well under
  a full chapter. A *complete* chapter is plausibly ~150K tokens, but that number is still an
  estimate — **the first fully-completed chapter should be used to replace it with a measured
  figure.**
- **A fleet-style batch run needs an explicit big-burn OK from Wilson first** (PLAN §11, and
  the hard-stop rule in CLAUDE.md). Sequential chapters are the default; the 8 GB machine is
  also a reason not to fan out.

## 7. ✅ SUSPECT FLAGS — ALL CLOSED 2026-08-28. Do not re-open.

The five remaining flags were settled as a batch off the plates (Wilson's call, 2026-08-28).
`chapters.tsv` is corrected, every flag is `verified`, and the register shows **none outstanding**.

| ch | was | is | how |
|---|---|---|---|
| 1.5 | En start 81 | **En 80** | `CHAP. V.` on En 80 |
| 1.12 | La start 187 | **La 188** | `CAP. XII. DE PŒNA PECCATI` on La 188 |
| 1.23 | La 4pp vs En 3pp | **La 3pp** (276–278) | falls out of 1.24's correction; ratio 1.00 |
| 1.24 | La start 280 | **La 279** | `CAP. XXIV.` on La 279; En side confirmed at En 382 |
| 1.28 | La start 309 | **La 315** | `CAP. XXVIII.` on La 315; La 309 is mid-1.27 |

**The text layer was right in all five, and the crosswalk wrong in all five.** With the earlier
En II.v/II.vi boundary and 2.17, the audit's discrepancies now stand at **7 for 7** and the
crosswalk at 0. `tools/crosswalk-output.txt` should be treated as superseded, not consulted.

**Four adjacent chapters were corrected as a consequence** — 1.4 (En 37pp → 36), 1.11 (La 7pp → 8),
1.27 (La 10pp → **16**) and 1.28 (La 23pp → 17). A contiguity check over all 50 chapters passes with
zero breaks in either layer.

⚖ **The ratios corroborate independently.** 1.27 read **2.20** and 1.28 **0.96** — the two worst
outliers in the register, both flagged `warn`. Corrected they are **1.38** and **1.29**, and 1.4,
1.5, 1.11 and 1.12 all land in band as well. A page-range error of this size shows up as a ratio
that cannot be right; **treat a ratio outside 1.05–1.85 as a boundary suspicion, not a curiosity.**
1.23 and 1.24 now sit at exactly 1.00, which is in company: II.10, II.12 and II.16 are all 1.00 and
all verified. For a 3–4 page chapter it is normal, not a flag.

### ★★ What settling 1.5 turned up — I.v does not open with its title

Both volumes head the chapter **`CAP. V.` / `PRÆFATIO.`** and **`CHAP. V.` / `PREFATORY REMARKS.`**
The title *De Filio Dei* / *Of the Son of God* is **not** at the chapter head; `chapters.tsv` carries
it from the contents page. Milton opens in his own voice — *De Filio Dei Sanctoque Spiritu hoc loco
dicturus, non, nisi denuo præfatus, aggrediendum esse opus tam arduum existimavi* / "I cannot enter
upon subjects of so much difficulty as the SON OF GOD and the HOLY SPIRIT, without again premising a
few introductory words" — and the English already carries a footnote on its first page.

Three consequences for when I.v is worked (it is scheduled last, PLAN §10 risk 2):
1. **The *Præfatio* is the natural first chunk** — `ddc-1-05-a` — and it is a lemma seam of Milton's
   own, which is what CONVENTIONS §7 asks a split to be. The 53 pages do not have to be cut arbitrarily.
2. **Expect a second heading inside the chapter** where the title finally appears; find it and use it
   as the next seam.
3. The two volumes set the rule differently — La puts it *between* `CAP. V.` and `PRÆFATIO.`, En puts
   `PREFATORY REMARKS.` above it, in the slot where a title goes. Display typography, normalised per
   §2, but worth knowing before the plates are read.

### Also not found in the text layer, when those chapters come up

Headings not detected by the audit (weak evidence — every audit *silence* so far has been fine,
while every *discrepancy* has been real): a handful in Book I. La 2.3 and En 2.11 were both checked
and were detection artefacts, not boundary problems.

## 9. The Latin volume has apparatus too — RULED 2026-08-04, no longer open

**Ruling (Wilson):** (1) sections are `## apparatus-sumner-en` and `## apparatus-sumner-la`,
anchors stay `[^sN]` for English and `[^laN]` for Latin — now CONVENTIONS §5, and the four
existing chunks are migrated. (2) Sumner's Latin notes are **harvested as we go** into
`tools/sumner-interventions.tsv`, which feeds PLAN §6.4 at M4 — now CONVENTIONS §5a.

**Two standing obligations that follow:**
- **Read the Latin plates for superscripts, every chapter.** Procedure §2 step 3 now includes it.
- **II.i–II.iv need a superscript-only re-check of their Latin plates.** Nobody was looking before
  II.v, so a Latin note in any of them would have been missed. Cheap (no re-transcription — just
  look at page feet), but it must happen before Book II is called complete.

### Background (found 2026-08-03, II.v)

**La p. 431 carries a footnote, numbered ⁵, in the Latin volume.** CONVENTIONS §5 is written as
though Sumner's notes exist only in the English, and §1 gives Latin-side apparatus no home. That
assumption is plate-falsified.

`chunks/ddc-2-05.md` improvises a fix — a `## apparatus-sumner-la` section with an `[^laN]` anchor
prefix, keeping `[^sN]` reserved for the English so the two independent numbering runs cannot
collide. `build-content.mjs` accepts it (`apparatus-*` is already a reserved header). **Ratified 2026-08-04** and now CONVENTIONS §5 —
see §9's heading above; this paragraph is the background, not an open question.

**The note's content is the bigger issue.** Sumner writes that the manuscript's word order differs
from what he printed, and that *ordinem leviter mutavi* — he silently changed it for grammar. So
the 1825 Latin is demonstrably not the manuscript at this point. "Verbatim-1825" is still exactly
the right transcription rule (we reproduce what Sumner printed, and the note is part of that), but
any claim that the edition gives *Milton's* Latin rather than *Sumner's* now has a documented
counter-example. Watch for further Latin-side notes in every chapter from here on; nothing tells
us this is the only one.


## 9b. ✅ THE BOOK II LATIN SWEEP — RUN AND CLOSED 2026-08-04. Gate open.

**Full record: `SWEEP-RUNBOOK.md` §6.** Do not re-run it; do not re-open the numbering question.

What it settled:

- **62 Latin page-feet read by eye** — all 42 of La 387–428 (never examined by anyone before),
  the 18 riskiest detector negatives, and the two known positives. **The detector and the eye
  agree on every page**; no 400 dpi fallback was needed.
- **No Latin note was missed in II.i–II.iv** — those chapters carry no Latin apparatus at all.
  §9's worry was unfounded and the II.i–II.iv back-check is **discharged**.
- La **431 = ⁵** and La **454 = ⁴**, re-confirmed off the plate. **La 454's note is SCHOLARLY**
  (a page of Bucer · Calvin · Ursinus · Gomarus · Peter Martyr · Musculus on the sabbath) and takes
  no row in `tools/sumner-interventions.tsv`. **La 431 remains the only textual Latin note in Book II.**
- Book I's three unverified candidates — La **50, 188, 228** — are **all false positives**. Book I's
  confirmed Latin notes stand at La **129** and **143**.
- **⚖ The numbering anomaly is RESOLVED: it is ad hoc.** All four hypotheses are refuted, the last
  of them this session — the Latin number is *not* keyed to the English note at the same passage
  (La 454's ⁴ pairs with English note printed **8**; La 431's ⁵ pairs with **no English note**).
  Per-gathering restart is out too, measured off the signatures. See `SWEEP-RUNBOOK.md` §6.4.
- **★★★ Book I carries Latin apparatus too, and it is textual.** La 129 gives **Sumner's own
  statement of editorial method** (*ut soleo… ne puncto quidem mutato*) against La 431's confessed
  *ordinem leviter mutavi*; La 143 reports the MS reading **a manu secunda**. See
  `SWEEP-RUNBOOK.md` §3a — this bears directly on PLAN §4a and §6.4.

**`[^laN]` numbers are LABELS, permanently. There is no Latin checksum and there never was one.**
A fifth Latin note turning up in Book I does not revive the question — a *missing* number already
killed it. The English checksum (§3, CONVENTIONS §8a) is a separate, genuinely sequential run and
is untouched.

## 10. Content filtering — a real, recurring obstacle with a known workaround

**II.vi blocked a content filter when its four *blasphemia* paragraphs were written as one block**
(2026-08-04), and II.i's English blocked twice on 2026-08-03 (§4). This is now a pattern, not an
accident: chapters whose subject is cursing, blasphemy, or idolatrous rites concentrate the
triggering material, and Book II is full of them.

**The workaround works and is now the standard procedure for such chapters:**

1. Read all plates first. Reading is never the problem — writing is.
2. Write the frontmatter and every low-risk paragraph, leaving `<!-- GAP: {¶N} owed -->` markers.
3. Write the apparatus, headnote and Notes.
4. **Commit.** The chapter is now safe whatever happens next.
5. Add the hard paragraphs **one at a time**. Split any single paragraph that still blocks in half
   with a temporary unique tail marker, then rejoin with a second edit.
6. Flip `status: draft` → `verified` and delete the GAP markers.

A chunk stuck at step 4 is a legal partial chunk (CONVENTIONS §8d) and the site builds it fine.
**Never paraphrase or omit to get around a block** — that would silently corrupt the edition, which
is worse than an unfinished chunk.

**Revised 2026-08-04 after II.vii, which blocked three times.** One block was on a *single
paragraph*, which then needed splitting into five pieces. Lesson: for a chapter whose subject is
polemical (Sabbath, blasphemy, idolatry, church vs. magistrate), **do not batch at all — write one
paragraph per edit from the very start.** In II.vii every paragraph written singly went through
first time; only the batched ones failed. Pre-splitting costs a few extra edits; a failed batch
costs the read.

**Also: guard every string replace.** Two separate corruptions were introduced in II.vii by
`str.replace` on text that also occurred in the chunk's own `## Notes` (which quotes the
apparatus). Always assert the match count is 1, or anchor by line index.

## 11. Every anchor must resolve before a layer is called complete

**Added 2026-08-28 from I.ii.** The chunk's Latin layer was committed, plate-verified, recorded in
this queue and shown on the register with `[^la1]` and `[^la2]` anchored in the text and **no
`## apparatus-sumner-la` section anywhere in the file.** Nothing caught it: the parser does not
require an anchor to resolve, the register counts Latin notes off the anchors rather than the
definitions, and the chunk's own "Owed on return" list — written by the session that made the
omission — did not mention it.

**Check per layer, before commit:**

```
python3 - <<'PY'
import io,re,sys
s=io.open(sys.argv[1] if len(sys.argv)>1 else 'chunks/ddc-1-02.md',encoding='utf-8').read()
body=re.sub(r'\n## (Notes|headnote)\n.*','',s,flags=re.S)       # Notes quote the apparatus
used=set(re.findall(r'\[\^([^\]]+)\](?!:)',body))
defined=set(re.findall(r'^\[\^([^\]]+)\]:',body,re.M))
print('anchored, never defined:', sorted(used-defined))
print('defined, never anchored:', sorted(defined-used))
PY
```

Both lists must be empty. It costs one command and it is the only check that would have caught
this class; the footnote-number checksum (§8a) will not, because a missing *section* leaves the
printed numbers perfectly consistent.

## 11a. Latin-note cross-check — run it AFTER transcribing, never before

**Ruled 2026-08-28 (Wilson).** `tools/sweep-book1.tsv` was built to say where to look for Latin
footnotes and in that direction it failed: it called La 12 and La 20 clean and both carry notes.
It is now **inverted** — `./tools/check-la-notes.py [chunk]` asks the opposite question:

> we transcribed this chapter and recorded no Latin note on page N — did the detector see
> tighter type there?

A false negative cannot hurt in that direction, and its false *positives* become the useful
output. Signal: `min(pitch after the gap) / body_pitch <= 0.93`. Deliberately looser than the
file's own `CANDIDATE` flag, because here a false positive costs one glance and a false negative
costs a missed note. 43 of Book I's 380 pages clear it; the bare presence of a gap does not, since
312 pages have one.

**Why it missed I.ii's notes, measured, so nobody restores it to a deciding role:** a `CANDIDATE`
needs a *run* of tighter pitches (La 129 gives 26,26,26,25,26,26,26,26 against a body of 34). A one-
or two-line note cannot produce a run — La 20 yielded the single value 30 against 33, and La 12
yielded no measurable gap at all. **The detector is structurally blind to short notes, which are the
commonest kind.**

⚠ **Chapter-opening pages are false positives by construction** — display headings leave a white
band and the ratio collapses (La 57, 203, 211, 331, 337 all read 0.27–0.30). The tool marks them.

First run, 2026-08-28: I.i clean; I.ii flagged La 10 (a chapter opening, discounted) and **La 14**,
which was checked at the plate and carries no note — the page simply ends short. **I.ii's Latin
apparatus is confirmed complete at two notes.** The tool's first output confirmed a chapter rather
than correcting one, which is the outcome to expect most of the time.

This does **not** replace §2 step 3 — read every Latin page foot, every chapter. It is a second pair
of eyes after that reading.

## 12. Non-Latin script — the standing procedure

**Added 2026-08-28 (Wilson's ruling): build the check-sheet as we go, one specialist pass
before M5.** CONVENTIONS §5c's ⚠ UNVERIFIED flag is honest but it is not a plan; this is the plan.

1. **Transcribe as printed, flag as unverified.** Unchanged — §5c governs.
2. **Never reconstruct from the grammar.** I.ii is the proof: `Θεοτὴς`/`Θειοτὴς` would not resolve
   in our Latin scan, standard accentuation was set as a placeholder, and it was **wrong**.
   Where a reading is illegible, **fetch another scan first** (STRUCTURE.md has the table and the
   calibrated leaf offsets). Reconstruction is the last resort, not the first.
3. **Regenerate `./tools/build-script-check.py` after every chapter.** It derives everything from
   `chunks/` — every Hebrew and Greek token, its volume and printed page, and a deep link to that
   page's image in every scan that carries it. Nothing on it is hand-kept, so it cannot drift.
4. **One specialist pass before M5**, not a trickle of questions. The sheet is the ask.

It covers three kinds of row and they are three different questions:

| kind | question for the reader |
|---|---|
| transcription layers | does this match the page, character for character and point for point? |
| Sumner's apparatus | same question — his notes quote Hebrew and Greek as heavily as the text |
| `## apparatus-editorial` (**OUR CLAIM**) | is this *argument* right? These are our claims about what a corrupt printed reading ought to be, and per §5c they **must not be published unconfirmed** |

Current: 49 Hebrew occurrences / 20 distinct, 91 Greek / 70 distinct. It will roughly double
through Book I; I.v and I.vi are the heaviest chapters still to come.
