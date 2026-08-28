#!/usr/bin/env python3
"""census-citations.py — measure the citation forms actually present in the corpus.

PREP FOR M4, not the index itself. PLAN §10 risk 5 says the citation parser "will
produce garbage confidently if it is not validated"; this tool exists so the session
that writes the parser starts from measurement rather than from guesses about what
Milton's reference style looks like.

It deliberately does NOT resolve anything. It reports shapes and counts, per layer,
so the grammar can be written against evidence. Anything it cannot shape is printed
verbatim under UNCLASSIFIED — that list is the parser's real specification.

    ./tools/census-citations.py            # summary
    ./tools/census-citations.py --shapes   # + every distinct shape with an example
    ./tools/census-citations.py --unclass  # + everything unclassified, verbatim
"""
import re, io, os, sys, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LAYERS = ("la", "en-sumner")

ROMAN = r"(?:[ivxlc]+)"
# a book token: optional leading numeral, then a capitalised word, optionally abbreviated
BOOK = r"(?:[1-4]\s+)?[A-Z][a-zæœ]{1,12}\.?"
# one reference: optional book, a roman chapter, optional verse material
# ⚠ WORD-BOUNDARY ANCHORED. Without \b the roman class matches inside words and the
# Latin layer reports ~4000 phantom citations that are single letters of ordinary prose.
REF = re.compile(
    rf"(?P<book>{BOOK}\s+)?"
    rf"\b(?P<ch>{ROMAN})\.?"
    rf"(?P<rest>(?:\s*[,–—-]?\s*(?:\d+|&c\.)){{0,6}})"
    r"(?=[\s.,;:)]|$)"
)
VERSE_ONLY = re.compile(r"\bv\.\s*\d+")


def sections(body):
    for m in re.finditer(r'\n## ([a-z0-9-]+)\n', body):
        key = m.group(1)
        nxt = body.find("\n## ", m.end())
        yield key, body[m.end(): nxt if nxt > 0 else len(body)]


def strip_markup(t):
    t = re.sub(r'<!-- .*? -->', ' ', t)
    t = re.sub(r'\[\^[^\]]+\]', ' ', t)
    t = re.sub(r'\{¶[^}]*\}', ' ', t)
    return t


def shape_of(m):
    """A coarse shape string — what the parser must be able to tell apart."""
    parts = []
    parts.append("BOOK" if m.group("book") else "—")
    parts.append("CH")
    rest = (m.group("rest") or "").strip()
    if not rest:
        parts.append("—")
    elif "&c" in rest:
        parts.append("V+&c" if re.search(r"\d", rest) else "&c")
    elif re.search(r"[–—-]", rest):
        parts.append("V-RANGE")
    elif rest.count(",") >= 1:
        parts.append("V-LIST")
    else:
        parts.append("V")
    return " ".join(parts)


def main():
    show_shapes = "--shapes" in sys.argv
    show_unclass = "--unclass" in sys.argv
    per_layer = {k: collections.Counter() for k in LAYERS}
    books = {k: collections.Counter() for k in LAYERS}
    shapes = {k: collections.Counter() for k in LAYERS}
    example = {}
    verse_only = {k: 0 for k in LAYERS}
    chunks = 0

    for path in sorted(glob.glob(os.path.join(ROOT, "chunks/ddc-*.md"))):
        raw = io.open(path, encoding="utf-8").read().split("\n## Notes")[0]
        chunks += 1
        for layer, text in sections(raw):
            if layer not in LAYERS:
                continue
            t = strip_markup(text)
            verse_only[layer] += len(VERSE_ONLY.findall(t))
            for m in REF.finditer(t):
                bk = (m.group("book") or "").strip()
                if bk:
                    books[layer][bk] += 1
                sh = shape_of(m)
                shapes[layer][sh] += 1
                per_layer[layer]["total"] += 1
                example.setdefault((layer, sh), m.group(0).strip())

    print(f"corpus: {chunks} chunks\n")
    for layer in LAYERS:
        print(f"── {layer} " + "─" * (58 - len(layer)))
        print(f"   reference-shaped tokens : {per_layer[layer]['total']}")
        print(f"   bare `v. N` continuations: {verse_only[layer]}")
        print(f"   distinct book tokens     : {len(books[layer])}")
        top = books[layer].most_common(14)
        print("   commonest books          : " +
              ", ".join(f"{b}({n})" for b, n in top))
        if show_shapes:
            print("   shapes:")
            for sh, n in shapes[layer].most_common():
                print(f"      {n:5}  {sh:22} e.g. {example[(layer, sh)]!r}")
        print()

    only_la = set(books["la"]) - set(books["en-sumner"])
    only_en = set(books["en-sumner"]) - set(books["la"])
    print("── book tokens appearing in ONE layer only " + "─" * 20)
    print("   la only :", ", ".join(sorted(only_la)) or "—")
    print("   en only :", ", ".join(sorted(only_en)) or "—")
    print("\n   ⚠ These are the abbreviation tables the parser needs, and they are NOT")
    print("     the same table. The layers must be parsed with different book maps.")


if __name__ == "__main__":
    main()
