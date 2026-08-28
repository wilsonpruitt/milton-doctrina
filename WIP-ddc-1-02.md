# WIP — `ddc-1-02` *De Deo* (Latin layer read 2026-08-27; English layer not yet read)

**Status: NOT a chunk yet.** The Latin layer (La 10–21, 12 pp.) has been read plate by plate and
the findings below are recorded so they are not lost. The English layer (En 13–29, 17 pp.) is
prepped but unread except En 26, which was consulted to try to resolve the Hebrew question below.
`chapters.tsv` still says `ok`; do not flip it until the chunk exists.

## ⛔ BLOCKED ON WILSON — the pointed Hebrew

I.ii sets **pointed Hebrew in quantity**, and it is the divine-name argument that grounds the
anti-Trinitarian case. Read at 1000–1600 dpi with narrowed crops:

| page | token | reading | confidence |
|---|---|---|---|
| La 14 | Jehova | `יְהֹוָה` | confident |
| La 14 | Jah | `יָה` (no mappiq visible in the he) | confident |
| La 14 | Ehie (×2) | `אֶהְיֶה` | confident |
| La 14 | Adonai | `אֲדֹנָי` | confident |
| La 18 / En 26 | Gen. i. 1 | `אֱלֹהִים בָּרָא` — noun **first**, reversing the verse's own *bara Elohim*; almost certainly deliberate, since Milton's point is a plural noun governing a singular verb | confident |
| La 18 / En 26 | Eloah | `אֱלֹהַּ` | confident |
| **La 18 / En 26** | **Psal. vii. 10 / lxxxvi. 10** | **`אֱלֹהִים־בַּדִּים` — UNRESOLVED** | **⛔ not confident** |

**The unresolved token.** Both volumes typeset it identically, so it is not a misprint in one
setting. I read `אֱלֹהִים־בַּדִּים`, but *baddim* makes no sense in an argument that *Elohim*
denotes the one God. Ps. 7:10 (Heb.) ends `אֱלֹהִים צַדִּיק` and Ps. 86:10 has
`אֱלֹהִים לְבַדֶּךָ`; neither matches the letters I can see, which are four after the maqqef
ending in final mem. So either a letter is misread, or both settings carry the same error, or it
is a form I do not know. **I will not guess at Hebrew in this chapter.**

Crops for a Hebrew reader: `raw/crops/la18-heb5b.jpg` (Latin, 1600 dpi) and
`raw/crops/en26-heb2.jpg` (English, 1600 dpi). `raw/` is gitignored — regenerate with
`./tools/crop-plate.sh la 18 1600 0.652 0.676 x 0.145 0.30` and
`./tools/crop-plate.sh en 26 1600 0.552 0.575 x 0.74 0.96`.

## ★★★ TWO LATIN FOOTNOTES — AND THE DETECTOR MISSED BOTH

- **La 12, note ¹**, anchored after *qualis ipse est*: `Sic in MS. An legendum se?`
- **La 20, note ²**, anchored after *Secundo, est SUMME BEATUS*: `Sic in MS. Sed vide an legendum
  benignus, quod et contextus, et loci citati postulare videntur.`

Both are **textual** in the CONVENTIONS §5a sense and both need a row in
`tools/sumner-interventions.tsv`. Both open with the same formula, **`Sic in MS.`**, which gives
this note-class a searchable signature.

⚠ **`tools/sweep-book1.tsv` flags BOTH pages `.` (no candidate).** Book II's sweep recorded that
"the detector and the eye agree on every page"; that is no longer true. **Two false negatives in
the first long Book I chapter read.** The detector cannot be used to decide where to look in
Book I — only to suggest. The standing rule (read every Latin foot, every chapter) is now
load-bearing rather than belt-and-braces.

⚠ Note also the two are numbered **1 and 2, in order**. CONVENTIONS §9b settled that `[^laN]`
numbers are **labels, not a checksum**, on strong Book II evidence. Two sequential notes in one
chapter is **not** grounds to reopen that, and §9b says so explicitly. Record the observation; do
not act on it.

## ★★★ THE ARIAN ARGUMENT IS MADE HERE, NOT ONLY IN I.v

PLAN §6.2 places Milton's anti-Trinitarianism in I.v *De Filio Dei*. I.ii already contains:

- **La 15** — *hypostasis ergo plane idem quod essentia est*: Milton collapses hypostasis into
  essence, which removes the "three persons, one essence" formula before I.v needs it.
- **La 17** — glossing Isa. 45:22, *id est, **nullus spiritus, nulla persona, nullum ens**,
  præterea est Deus*; and *unum numero Deum, unum spiritum*.
- **La 18** — *quod **Patrem** Domini nostri Jesu Christi unum illum Deum esse testantur*, with a
  swipe at the schoolmen who "called into doubt the unity of God which they professed to assert."
- **La 18** — Milton's own forward reference: **`verum de his plura cap. 5.`**

**This is the second time a PLAN §6.2 claim has proved to be mislocated** (after II.xv's divorce
material turning out to be Sumner's apparatus). The pattern to carry: **§6.2 says where a doctrine
is *concluded*, not where it is *argued*.**

## Other Latin-layer findings held for the chunk

- **La 12** — Greek `ἀνθρωποπαθείᾳ` / `ἀνθρωποπαθῶς`, with Milton glossing it himself
  (*id est, more hominum*). A use/mention test for the rule corrected in I.i.
- **La 13** — Milton refuses to explain away Scripture's anthropomorphisms.
- **La 14** — Greek `Θεότης`, `Θειότης`, `τὸ θεῖον`, `Κύριος`. ⚠ **The accents on Θεότης and
  Θειότης could not be resolved at 1400 dpi** — that is the scan's limit, not the crop's. Standard
  accentuation to be used, flagged UNVERIFIED per §5c.
- **La 16** — Milton cites **the Syriac version** (*ubi Syrus habet*), a first for the corpus;
  `El Shaddai` and `El Elion` in roman letters, not Hebrew.
- **La 17** — Milton rejects the Aristotelian *actus purus*.
- **La 19** — Greek `καρδιογνώστης πάντων`.
- **La 20** — `et v. 5` is **Psalm V**, not verse 5 of Ps. 103: another instance of the `et v. N`
  ambiguity settled as unresolvable in II.xvii.
- **Accidental, three instances**: `Exod. xxxiii. 20. 23.`, `1 Chron. xvii. 12. 14.`,
  `cap. viii. 10. 11.` — a **period** between enumerated verses where the volume's convention is a
  comma. Not seen in Book II.
- **Citation suspects to test against the English**: `Num. xxiii. 23` (words are 23:19) ·
  `Isa. xliv. 1` (words are 44:6) · `Isa. v. 3` (words are 44:8).
- Extent: La 10–21 confirmed, `CAP. III` opens La 22. Signatures La `c 2`@11, `D`@17, `D 2`@19.
