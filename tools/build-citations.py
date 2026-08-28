#!/usr/bin/env python3
"""build-citations.py — the scripture-citation ledger for De Doctrina Christiana.

Read M4-RUNBOOK.md before changing anything here. The two rules that shape this file:

  §2  BOTH LAYERS ARE KEYED. Bonaventure's build-citations.py opens by declaring Latin
      the keying side and the English display-only. That rule is FALSE here and is not
      ported. Milton's two volumes disagree about citations systematically — the edition
      exists to show that disagreement — so each layer is parsed and keyed on its own
      terms and a mismatch becomes a divergence record, never a silent choice of side.

  §5  NEVER GUESS. Anything the grammar cannot classify becomes a QA line, not a record
      with an invented target. A confidently-wrong parser is PLAN §10 risk 5.

    ./tools/build-citations.py ddc-2-02          # one chunk (start here)
    ./tools/build-citations.py --all             # every chunk in chunks/
    ./tools/build-citations.py ddc-2-02 --dump   # + every record, readable, for hand-check

Writes index/citations.tsv and index/citation-qa.md. Derived, re-runnable, zero writes
under chunks/.
"""
import re, io, os, sys, json, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS_JSON = os.path.join(ROOT, "tools", "scripture-books.json")
VERS_JSON = os.path.join(ROOT, "tools", "versification.json")
INDEX_DIR = os.path.join(ROOT, "index")
LEDGER = os.path.join(INDEX_DIR, "citations.tsv")
QA_REPORT = os.path.join(INDEX_DIR, "citation-qa.md")

LAYERS = ("la", "en-sumner")

# ── Milton's numerals ────────────────────────────────────────────────────────────
# Chapters and (in the Latin) some verse material are set in LOWERCASE roman in both
# volumes; the apparatus uses uppercase for Milton's poetry (Paradise Lost, XII. 558)
# and that is not scripture. Restricting the class to lowercase kills most of hazard 2
# before it starts.
ROMAN_RE = r"(?:[ivxlc]{1,7})"
ROMAN_VAL = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}


def roman_to_int(s):
    s = s.lower()
    if not s or any(c not in ROMAN_VAL for c in s):
        return None
    total, prev = 0, 0
    for c in reversed(s):
        v = ROMAN_VAL[c]
        total = total - v if v < prev else total + v
        prev = max(prev, v)
    # reject the strings that are Latin words rather than numerals only by context,
    # never by value — `vi`, `ii`, `ix`, `li`, `ci` are all legal numerals.
    return total or None


# ── chunk reading ────────────────────────────────────────────────────────────────
def parse_frontmatter(raw):
    m = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
    fm = {}
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    return fm


def sections(raw):
    for m in re.finditer(r"\n## ([a-zA-Z0-9-]+)\n", raw):
        key = m.group(1)
        nxt = raw.find("\n## ", m.end())
        yield key, raw[m.end(): nxt if nxt > 0 else len(raw)]


PARA_RE = re.compile(r"\{¶([0-9]+)(?:[–—-]([0-9]+))?\}")


def paragraphs(text):
    """Yield (label, first_para_int, last_para_int, body) for each {¶N} / {¶N–M} block."""
    hits = list(PARA_RE.finditer(text))
    for i, m in enumerate(hits):
        end = hits[i + 1].start() if i + 1 < len(hits) else len(text)
        lo = int(m.group(1))
        hi = int(m.group(2)) if m.group(2) else lo
        yield m.group(0), lo, hi, text[m.end():end]


def strip_markup(t):
    """Remove page markers and apparatus anchors, PRESERVING length so offsets stay true."""
    t = re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), t, flags=re.S)
    t = re.sub(r"\[\^[^\]]+\]", lambda m: " " * len(m.group(0)), t)
    return t


# ── the grammar ──────────────────────────────────────────────────────────────────
# A tail is the verse material after the chapter: digits joined by commas, periods,
# or dashes, optionally closed by `&c.`. Ranges are an ENGLISH feature (79 of them,
# zero in the Latin); period-separated pairs are a LATIN feature (M4-RUNBOOK §3).
# ⚠ the separator may LEAD the item, not only follow it: `v. 98—100.` and `xiii. 20—22.`
# are ranges whose first separator sits between two digits. An earlier form of this
# pattern required the item first and so read `v. 98—100.` as the single verse 98,
# manufacturing a divergence against the Latin's `98, 99, 100` that is not in the text.
TAIL_RE = re.compile(r"(?:\s*(?:[,.—–]\s*)?(?:\d{1,3}|&c)\.?)*")

# `cap.` / `Cap.` is a CHAPTER CONTINUATION, carrying the book forward — NOT a book
# token and NOT (usually) Milton citing his own treatise. M4-RUNBOOK §4.3 had this
# wrong; see the note this session added there. The self-reference use is marked by a
# governing word, and those become QA lines rather than scripture records.
# ⚠ CASE-SENSITIVE on `Book` deliberately — lowercase `book`/`books` is ordinary prose
# ("of making many books there is no end") and must not suppress a real continuation.
SELF_REF_CUES = re.compile(
    r"(?:\b(?:libro|libri|superiore|superiori|supra|infra)\b"
    r"|\blib\.|\bBook\b|\bBk\.)", re.UNICODE)

# ⚠ THE TWO LAYERS NEED DIFFERENT CONTINUATION RULES, and this is measured, not tidy.
# In the LATIN a chapter continuation is always announced — `et xxx. 5, 6.`, `cap. vi. 4.`,
# `cum xvii. 12.` — and it has to be, because `illi`, `vi`, `ii`, `ix`, `li`, `ci` are
# ordinary Latin words of exactly the numeral shape (M4-RUNBOOK §4.2). A bare roman in the
# Latin is therefore NOT read as a citation.
# In the ENGLISH Sumner drops the connective and sets the chapter bare — `Deut. iv. 35.
# v. 39. vi. 4. ... xxxii. 39.` — and the word hazard does not exist there. So the English
# cue is optional. Requiring it cost 34 records (a 21% layer spread) on the first run of
# this parser, which is precisely the invariant M4-RUNBOOK §6.1 exists to catch.
CONT_CUES_LA = r"(?:et|cum|ac|cap\.|Cap\.)"
CONT_CUES_EN = r"(?:and|with|compared\s+with|ch\.|chap\.)"


def build_scanner(layer, books, vers):
    single, multi, lookup = [], [], {}
    for b in books:
        for a in b["aliases"].get(layer, []):
            lookup[a] = b["key"]
            (single if vers["books"].get(b["key"], {}).get("chapters") == 1
             else multi).append(a)
    # longest first so `1 John.` wins over `1 John`, `Judic.` over `Jud.`
    esc = lambda xs: "|".join(re.escape(a).replace(r"\ ", r"\s+")
                              for a in sorted(xs, key=len, reverse=True))
    alt, salt = esc(multi), esc(single) or r"(?!)"

    # ⚠ A tail must not swallow the LEADING NUMERAL OF THE NEXT BOOK. `2 Reg. xxiii.
    # 2 Chron. xxxiv. 4, &c.` reads its chapter-only citation, then the `2` of `2 Chron.`
    # looks exactly like another verse — the tail ate it, `Chron.` alone matched no alias,
    # and the bare `xxxiv.` carried 2 Kings forward to a chapter that does not exist.
    # The lookahead below refuses a number that is standing in front of a book token.
    allbooks = "|".join(x for x in (alt, salt) if x != r"(?!)")
    # ...and the numeral may be PART of the next book's token, which the lookahead above
    # cannot see because `2 Chron.` is one alias and bare `Chron.` is none. So refuse a
    # leading 1-4 that is standing in front of a numbered book's second word as well.
    numtails = esc({a.split(None, 1)[1] for a in list(multi) + list(single)
                    if re.match(r"^[1-4]\s", a)}) or r"(?!)"
    item = (rf"(?:(?![1-4]\s+(?:{numtails}))\d{{1,3}}(?!\s*(?:{allbooks}))|&c)")
    tail = rf"(?:\s*(?:[,.—–]\s*)?{item}\.?)*"

    if layer == "la":
        cont = rf"\b(?P<cue>{CONT_CUES_LA})\s+(?P<cch>{ROMAN_RE})\.(?P<ctail>{tail})"
    else:
        # ⚠ two exclusions, both of which the first run got wrong:
        #  · `(?<![&\w])` — without it the `c.` of `&c.` is read as the roman 100 and the
        #    parser emits `Eccl 100`, a chapter that does not exist.
        #  · `(?!v\.)` — in the English `v.` is ALWAYS *verse* (Sumner sets `Deut. iv. 35.
        #    v. 39. vi. 4.`), never the roman 5, so it must fall through to the verse branch.
        #    The Latin `et v. N` genuinely IS ambiguous; the English is not, and that
        #    asymmetry is what lets the English settle the Latin below.
        cont = (rf"(?:\b(?P<cue>{CONT_CUES_EN})\s+)?"
                rf"(?<![&\w])(?!v\.)(?P<cch>{ROMAN_RE})\.(?P<ctail>{tail})")
    pat = re.compile(
        # 1. SINGLE-CHAPTER BOOKS FIRST, because their citations carry no chapter and
        #    branch 2 would read the verse as one. Both forms occur and they differ by
        #    layer: En `Jude 20.` sets a bare arabic verse, La `Judæ v. 20.` prefixes `v.`,
        #    which as a roman is 5 — M4-RUNBOOK §4.4's misreading exactly, and it survived
        #    in this parser until the full-corpus run turned up `Jude chapter 5`.
        rf"(?P<sbook>{salt})\s+(?:v\.\s*)?(?P<sverse>\d{{1,3}})\b"
        # ⚠ `\s+`, NOT `\s*`, between the book token and its numeral. With `\s*` the alias
        # `Judæ` eats the head of `Judæi` and the trailing `i` is read as the roman 1, so
        # the ordinary Latin word for "the Jews" becomes a citation to Jude 1 (M4-RUNBOOK
        # §4.3). No citation in either volume sets the book tight against its chapter.
        rf"|(?P<book>{alt})"                                  # 2. book, then chapter
        rf"\s+(?P<bch>{ROMAN_RE})\.?(?P<btail>{tail})"
        rf"|{cont}"                                           # 3. chapter continuation
        rf"|\bv\.\s*(?P<vtail>\d{{1,3}}{tail})"             # 4. verse continuation
    )
    return pat, lookup


def parse_tail(tail):
    """Return (kind, verses, raw) for the verse material after a chapter."""
    raw = (tail or "").strip().rstrip(".,")
    if not raw:
        return "—", [], ""
    open_end = "&c" in raw
    nums = [int(n) for n in re.findall(r"\d{1,3}", raw)]
    if not nums:
        return "&c", [], raw
    if re.search(r"\d\s*[—–]\s*\d", raw):
        kind = "V-RANGE"
        # A range and a list name the same verses: `xiii. 20—22.` IS `xiii. 20, 21, 22.`
        # Expand so the TARGETS compare equal — ranges are an English-only feature
        # (79 in the English, zero in the Latin, M4-RUNBOOK §3.1), and an unexpanded
        # range reports every one of them as a divergence it is not. The syntax
        # difference stays visible in the `class` column, which is where it belongs.
        exp = []
        for a, b in re.findall(r"(\d{1,3})\s*[—–]\s*(\d{1,3})", raw):
            exp += list(range(int(a), int(b) + 1))
        for n in nums:
            if n not in exp:
                exp.append(n)
        nums = sorted(set(exp))
    elif re.search(r"\d\s*\.\s*\d", raw):
        kind = "V-PAIR"          # Latin-only: `xxxiii. 20. 23.`
    elif len(nums) > 1:
        kind = "V-LIST"
    else:
        kind = "V"
    if open_end:
        kind += "+&c"
    return kind, nums, raw


class Rec(dict):
    pass


def scan_layer(chunk_id, layer, text, books, pat, lookup, vers):
    recs, qa = [], []
    book = chapter = None          # carried state
    carried_from = ""
    for label, lo, hi, body in paragraphs(text):
        body = strip_markup(body)
        # state does not survive a paragraph boundary: Milton restarts with a named
        # book in every paragraph that cites, and carrying across is how a parser
        # invents targets.
        book = chapter = None
        carried_from = ""
        for i, m in enumerate(pat.finditer(body)):
            rid = f"{chunk_id}:{layer}:{label}:{i}"
            raw = m.group(0).strip()
            ctx = body[max(0, m.start() - 60): m.start()]

            if m.group("book"):
                key = lookup[re.sub(r"\s+", " ", m.group("book"))]
                ch = roman_to_int(m.group("bch"))
                if ch is None:
                    qa.append((rid, raw, "chapter numeral did not parse"))
                    continue
                book, chapter, carried_from = key, ch, ""
                kind, verses, tailraw = parse_tail(m.group("btail"))
                cls, res = f"BOOK CH {kind}", "book-named"

            elif m.group("sbook"):
                key = lookup[re.sub(r"\s+", " ", m.group("sbook"))]
                if vers["books"].get(key, {}).get("chapters") != 1:
                    qa.append((rid, raw, f"bare verse after {key}, which has more than one chapter"))
                    continue
                book, chapter, carried_from = key, 1, ""
                kind, verses = "V", [int(m.group("sverse"))]
                cls, res = "BOOK V (single-chapter book)", "book-named"

            elif m.group("cch"):
                cue = m.group("cue") or ""
                # A chapter continuation governed by `lib.` / `Book` / `supra` / `infra` is
                # not scripture at all — it is Milton pointing at his own treatise
                # (`Vide supra lib. 1. cap. xxvii.`), Sumner doing the same in English
                # (`See Book I. chap. xxvii.`), or Sumner citing another author by book and
                # chapter (`Ames, Medull. Theol. lib. ii. c. 13.`). Each of those, indexed
                # as scripture, becomes a citation to a chapter that does not exist —
                # 1 John 27, Luke 27, Deuteronomy 100. Refuse them all, not just `cap.`.
                if SELF_REF_CUES.search(ctx):
                    qa.append((rid, (ctx[-45:] + raw).strip(),
                               "chapter continuation governed by lib./Book/supra/infra — a "
                               "reference to a treatise, not to scripture. Not indexed."))
                    continue
                if book is None:
                    qa.append((rid, raw, "chapter continuation with no book in scope"))
                    continue
                ch = roman_to_int(m.group("cch"))
                if ch is None:
                    qa.append((rid, raw, "continuation numeral did not parse"))
                    continue
                kind, verses, tailraw = parse_tail(m.group("ctail"))

                # ⚠ M4-RUNBOOK §4.7 — `et v. N` is ambiguous BY FORM: `v` is both the
                # roman 5 and the abbreviation for *versus*. The first run of this parser
                # read every one of them as chapter 5 and produced Ps 5:98, Ps 5:157 and
                # six more targets that do not exist — the confidently-wrong failure PLAN
                # §10 risk 5 names. Form cannot settle it, so it is settled by whether the
                # target EXISTS, and the record says which way it went and why.
                if m.group("cch").lower() == "v":
                    chapter_reading_ok = chapter_exists(book, 5, verses, vers)
                    verse_reading_ok = chapter is not None and chapter_exists(book, chapter, verses, vers)
                    if verse_reading_ok and not chapter_reading_ok:
                        carried_from = recs[-1]["id"] if recs else ""
                        cls, res = f"— — {kind}", "et-v-read-as-verse"
                    elif chapter_reading_ok and not verse_reading_ok:
                        chapter, carried_from = 5, recs[-1]["id"] if recs else ""
                        cls, res = f"— CH {kind}", "et-v-read-as-chapter"
                    else:
                        # Both readings survive the range check, so form and canon are both
                        # exhausted. The PARALLEL LAYER is the remaining instrument
                        # (M4-RUNBOOK §5, and how I.ii's instance was settled): the English
                        # sets `v. N` for a verse and never for chapter 5, so an aligned
                        # English verse-continuation settles the Latin. Held pending until
                        # reconcile_et_v() below; still pending at the end means QA, not a
                        # record.
                        carried_from = recs[-1]["id"] if recs else ""
                        cls, res = f"— — {kind}", "et-v-pending"
                else:
                    chapter, carried_from = ch, recs[-1]["id"] if recs else ""
                    cls, res = f"— CH {kind}", "book-carried"

            else:  # `v. N`
                if book is None or chapter is None:
                    qa.append((rid, raw, "verse continuation with no chapter in scope"))
                    continue
                carried_from = recs[-1]["id"] if recs else ""
                kind, verses, tailraw = parse_tail(m.group("vtail"))
                cls, res = f"— — {kind}", "book-and-chapter-carried"

            recs.append(Rec(
                id=rid, chunk_id=chunk_id, layer=layer, section=layer, para=label,
                para_lo=lo, para_hi=hi, seq=i, cls=cls, raw_text=raw,
                book=book, chapter=chapter, verses=verses,
                resolution=res, carried_from=carried_from,
                target=fmt_target(book, chapter, verses, "&c" in cls),
                confidence="high" if res == "book-named" else "carried",
            ))
    return recs, qa


def fmt_target(book, chapter, verses, open_end=False):
    t = f"{book} {chapter}" if not verses else \
        f"{book} {chapter}:" + ",".join(str(v) for v in verses)
    # `&c.` is an open end, not a verse — but one layer dropping it while the other
    # keeps it is a real divergence (attested at Exod. xix. 23 in this chapter), so it
    # has to be part of what the two targets compare on.
    return t + " &c." if open_end else t


def chapter_exists(book, chapter, verses, vers):
    """Would BOOK chapter:verses land inside the canon? Used to settle `et v. N`."""
    b = vers["books"].get(book)
    if not b or chapter is None or chapter > b["chapters"]:
        return False
    bound = b["verses"][chapter - 1]
    slack = 1 if b["trust"] == "slack+1" else 0
    if b["trust"] == "unreliable":
        slack = 3
    return all(v <= bound + slack for v in verses)


# ── target-exists check (M4-RUNBOOK §6.3) ────────────────────────────────────────
def check_exists(rec, vers):
    b = vers["books"].get(rec["book"])
    if not b:
        return "no versification data"
    if rec["chapter"] > b["chapters"]:
        return f"{rec['book']} has {b['chapters']} chapters — chapter {rec['chapter']} does not exist"
    bound = b["verses"][rec["chapter"] - 1]
    slack = 1 if b["trust"] == "slack+1" else 0
    # Milton's Latin follows Junius-Tremellius; Hebrew psalm numbering counts the
    # superscription, so a Latin psalm verse may legitimately run past the KJV bound.
    if rec["layer"] == "la" and rec["book"] == "Ps":
        slack = max(slack, 2)
    over = [v for v in rec["verses"] if v > bound + slack]
    if over:
        sev = "WARN" if b["trust"] == "unreliable" else "ERR"
        return (f"{sev}: {rec['book']} {rec['chapter']} has {bound} verses — "
                f"{', '.join(str(v) for v in over)} out of range")
    return None


# ── divergence pairing (M4-RUNBOOK §2) ───────────────────────────────────────────
def _sim(l, e):
    """How alike are two citation records? Drives the alignment below."""
    if l["target"] == e["target"]:
        return 4
    if l["book"] == e["book"] and l["chapter"] == e["chapter"]:
        return 2          # same passage, different verses — a divergence, still a pair
    if l["book"] == e["book"]:
        return 0          # same book, different chapter — usually a pair, sometimes not
    return -3


def align(las, ens, gap=-1):
    """Needleman-Wunsch over the two layers' citation sequences.

    ⚠ NOT a positional zip. Neither layer is a complete witness to the other — the
    English adds citations the Latin has not got and drops ones it has (M4-RUNBOOK §2,
    and II.x's omission finding) — so a single insertion shifts a zip and every
    subsequent pair is reported as a divergence. That is exactly what happened on the
    first run of this parser: one extra English record in ddc-2-02 ¶14-15 manufactured
    six false divergences and hid the real insertion at the end of the run. Alignment
    gives the three attested classes directly: substitution, deletion, insertion.
    """
    n, m = len(las), len(ens)
    F = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        F[i][0] = F[i - 1][0] + gap
    for j in range(1, m + 1):
        F[0][j] = F[0][j - 1] + gap
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            F[i][j] = max(F[i - 1][j - 1] + _sim(las[i - 1], ens[j - 1]),
                          F[i - 1][j] + gap, F[i][j - 1] + gap)
    i, j, out = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and F[i][j] == F[i - 1][j - 1] + _sim(las[i - 1], ens[j - 1]):
            out.append((las[i - 1], ens[j - 1])); i -= 1; j -= 1
        elif i > 0 and F[i][j] == F[i - 1][j] + gap:
            out.append((las[i - 1], None)); i -= 1
        else:
            out.append((None, ens[j - 1])); j -= 1
    return list(reversed(out))


def reconcile_et_v(la_recs, en_recs):
    """Settle the Latin's `et v. N` from the English layer, or send it to QA.

    M4-RUNBOOK §4.7: `et v. N` cannot be resolved by form — `v` is both the roman 5 and
    the abbreviation for *versus*. Where the canon settles it (one reading targets a
    verse that does not exist) scan_layer already has. What is left is settled the way
    I.ii's instance was settled and the way §5 says mappings get settled generally: BY
    THE OTHER LAYER. Sumner sets `v. N` for a verse and never for chapter 5, so an
    aligned English verse-continuation carrying the same numbers fixes the Latin.

    Anything still pending after this is a QA line. It does not enter the index."""
    qa = []
    en_by_span = collections.defaultdict(list)
    for r in en_recs:
        en_by_span[(r["para_lo"], r["para_hi"])].append(r)
    for span, ens in sorted(en_by_span.items()):
        las = [r for r in la_recs if span[0] <= r["para_lo"] <= span[1]]
        for l, e in align(las, ens):
            if not l or l["resolution"] != "et-v-pending":
                continue
            if e and e["cls"].startswith("— —") and e["verses"] == l["verses"]:
                l["resolution"] = "et-v-settled-by-english-layer"
                l["confidence"] = "cross-layer"
    for r in la_recs:
        if r["resolution"] == "et-v-pending":
            qa.append((r["id"], r["raw_text"],
                       "`et v. N` — neither the canon nor the English layer settles whether "
                       "`v` is the roman 5 or *versus*. Not indexed."))
    return qa


def pair_divergences(la_recs, en_recs):
    """Align the two layers paragraph by paragraph and report every pair that differs.

    The {¶N} grid IS the alignment key at paragraph level — an English paragraph
    labelled {¶2-3} covers Latin ¶2 and ¶3 (CONVENTIONS §4). Within a paragraph the
    citations are aligned by align() above, never zipped.
    """
    out = []
    en_by_span = collections.defaultdict(list)
    for r in en_recs:
        en_by_span[(r["para_lo"], r["para_hi"])].append(r)
    for span, ens in sorted(en_by_span.items()):
        las = [r for r in la_recs if span[0] <= r["para_lo"] <= span[1]]
        label = f"¶{span[0]}" if span[0] == span[1] else f"¶{span[0]}-{span[1]}"
        for l, e in align(las, ens):
            if l and e and l["target"] == e["target"]:
                # Compare only the VERSE syntax. Whether the book is named or carried is
                # not a divergence — Sumner drops the repeated book name constantly and
                # reporting it would bury the real rows. V-LIST against V-RANGE is worth
                # a row: ranges are an English-only feature (M4-RUNBOOK §3.1).
                if l["cls"].split()[-1] != e["cls"].split()[-1]:
                    out.append({"para": label, "la": l["raw_text"], "la_target": l["target"],
                                "en": e["raw_text"], "en_target": e["target"],
                                "kind": f"same target, syntax differs ({l['cls']} / {e['cls']})"})
                continue
            out.append({
                "para": label,
                "la": l["raw_text"] if l else "—",
                "la_target": l["target"] if l else "—",
                "en": e["raw_text"] if e else "—",
                "en_target": e["target"] if e else "—",
                "kind": ("divergence" if l and e else
                         "present in Latin only" if l else "present in English only"),
            })
    # Latin paragraphs with no English counterpart at all would vanish above; catch them.
    covered = set()
    for span in en_by_span:
        covered |= set(range(span[0], span[1] + 1))
    for r in la_recs:
        if r["para_lo"] not in covered:
            out.append({"para": r["para"], "la": r["raw_text"], "la_target": r["target"],
                        "en": "—", "en_target": "—",
                        "kind": "Latin paragraph absent from the English layer"})
    return out


COLUMNS = ["chunk_id", "layer", "section", "para", "seq", "class", "raw_text",
           "book", "chapter", "verses", "target", "confidence", "resolution",
           "carried_from", "divergence_id"]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    do_all = "--all" in sys.argv
    do_dump = "--dump" in sys.argv

    books = json.load(open(BOOKS_JSON))["books"]
    vers = json.load(open(VERS_JSON))
    scanners = {L: build_scanner(L, books, vers) for L in LAYERS}

    paths = sorted(glob.glob(os.path.join(ROOT, "chunks", "ddc-*.md")))
    if not do_all:
        if not args:
            sys.exit("usage: build-citations.py <chunk-id> | --all   [--dump]")
        want = set(args)
        paths = [p for p in paths
                 if os.path.basename(p)[:-3] in want]
        missing = want - {os.path.basename(p)[:-3] for p in paths}
        if missing:
            sys.exit("no such chunk: " + ", ".join(sorted(missing)))

    all_recs, all_qa, all_div = [], [], []
    for path in paths:
        chunk_id = os.path.basename(path)[:-3]
        raw = io.open(path, encoding="utf-8").read().split("\n## Notes")[0]
        per_layer = {}
        for layer, text in sections(raw):
            if layer not in LAYERS:
                continue
            pat, lookup = scanners[layer]
            recs, qa = scan_layer(chunk_id, layer, text, books, pat, lookup, vers)
            per_layer[layer] = recs
            all_recs += recs
            all_qa += [(chunk_id,) + q for q in qa]
        for r in all_recs:
            pass
        et_v_qa = reconcile_et_v(per_layer.get("la", []), per_layer.get("en-sumner", []))
        all_qa += [(chunk_id,) + q for q in et_v_qa]
        pending = {q[0] for q in et_v_qa}
        for L in per_layer.values():
            L[:] = [r for r in L if r["id"] not in pending]
        all_recs = [r for r in all_recs if r["id"] not in pending]
        divs = pair_divergences(per_layer.get("la", []), per_layer.get("en-sumner", []))
        for d in divs:
            d["chunk_id"] = chunk_id
        all_div += divs

    # ── target-exists (M4-RUNBOOK §6.3) ─────────────────────────────────────────
    # A citation whose BOOK IS NAMED and whose target does not exist is a finding about
    # the 1825 text — `Luc. ix. 66.`, `Psal. iii. 9.`, `1 Kings xxvii. 29.` are all printed
    # errors, three of them already plate-confirmed by hand. It stays in the ledger,
    # flagged, because the edition's job is to show it.
    #
    # A citation whose book was CARRIED and whose target does not exist is almost always
    # this parser's fault, not the book's: the state machine carried the wrong book across
    # a book named in PROSE rather than in an abbreviation — Sumner writes "the author of
    # the Epistle to the Hebrews" and then cites a bare `vi. 1—3.`, and Milton writes
    # "ostendit Isaias cap. lix. 4." Nothing in the citation syntax marks either. So it is
    # refused: a QA line, never a record with an invented target.
    range_problems, dropped = [], set()
    for r in all_recs:
        msg = check_exists(r, vers)
        if not msg:
            continue
        if r["resolution"] == "book-named":
            range_problems.append((r, msg))
        else:
            dropped.add(r["id"])
            all_qa.append((r["chunk_id"], r["id"], r["raw_text"],
                           f"{msg} — and the book here was CARRIED, not named, so the "
                           f"carry is the likelier defect. Not indexed; read the passage."))
    if dropped:
        all_recs = [r for r in all_recs if r["id"] not in dropped]
        all_div = [d for d in all_div
                   if not (d["kind"] == "divergence" and False)]

    os.makedirs(INDEX_DIR, exist_ok=True)
    div_key = {}
    for i, d in enumerate(all_div, 1):
        div_key[(d["chunk_id"], d["para"])] = f"d{i}"
    with io.open(LEDGER, "w", encoding="utf-8") as fh:
        fh.write("\t".join(COLUMNS) + "\n")
        for r in all_recs:
            fh.write("\t".join(str(x) for x in [
                r["chunk_id"], r["layer"], r["section"], r["para"], r["seq"], r["cls"],
                r["raw_text"].replace("\t", " "), r["book"], r["chapter"],
                ",".join(str(v) for v in r["verses"]), r["target"], r["confidence"],
                r["resolution"], r["carried_from"], "",
            ]) + "\n")

    with io.open(QA_REPORT, "w", encoding="utf-8") as fh:
        fh.write("# Citation QA — read this, do not merely generate it\n\n")
        fh.write(f"{len(all_recs)} records · {len(all_qa)} unclassified · "
                 f"{len(range_problems)} out-of-range · {len(all_div)} divergence rows\n\n")
        counts = collections.Counter(r["layer"] for r in all_recs)
        fh.write("## Per-layer counts (M4-RUNBOOK §6.1 — a gap of more than a few percent is a bug)\n\n")
        for k, v in counts.items():
            fh.write(f"- `{k}` — {v}\n")
        if len(counts) == 2:
            a, b = counts.values()
            fh.write(f"- spread: {abs(a - b)} records, {abs(a - b) / max(a, b):.1%}\n")
        fh.write("\n## Unclassified — never a record with an invented target\n\n")
        for row in all_qa:
            fh.write(f"- `{row[0]}` `{row[1]}` — `{row[2]}` → {row[3]}\n")
        if not all_qa:
            fh.write("_none_\n")
        fh.write("\n## Targets that do not exist\n\n")
        for r, msg in range_problems:
            fh.write(f"- `{r['chunk_id']}` {r['layer']} {r['para']} `{r['raw_text']}` — {msg}\n")
        if not range_problems:
            fh.write("_none_\n")
        fh.write("\n## Divergences between the layers\n\n")
        fh.write("| chunk | ¶ | Latin | → | English | → | kind |\n|---|---|---|---|---|---|---|\n")
        for d in all_div:
            fh.write(f"| {d['chunk_id']} | {d['para']} | `{d['la']}` | {d['la_target']} | "
                     f"`{d['en']}` | {d['en_target']} | {d['kind']} |\n")

    print(f"{len(all_recs)} records · {len(all_qa)} unclassified · "
          f"{len(range_problems)} out-of-range · {len(all_div)} divergence rows")
    print(f"  {os.path.relpath(LEDGER, ROOT)}  {os.path.relpath(QA_REPORT, ROOT)}")

    if do_dump:
        for r in all_recs:
            print(f"  {r['layer']:<10} {r['para']:<8} {r['cls']:<22} "
                  f"{r['raw_text'][:34]:<36} → {r['target']}")


if __name__ == "__main__":
    main()
