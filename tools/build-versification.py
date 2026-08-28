#!/usr/bin/env python3
"""build-versification.py — derive tools/versification.json, the target-exists table.

M4-RUNBOOK §6 check 3: "Zero records whose target is a chapter or verse that does not
exist in that book. Reading a digit correctly is not reading it rightly — verify that
the target exists." That check needs a versification table, and this builds one.

SOURCE: ~/kjv-wesley/data/kjv/<slug>.json. That dataset is NOT clean and the defect is
recorded in the kjv-dataset-missing-verses memory: it holds 31,100 verses where the KJV
has 31,102. Matthew and Mark are each SHORT 3 verses and every chapter's verse array is
renumbered sequentially past a drop, so a max-verse read off those two books can be low.
Four books (1 Samuel, 1 Kings, 3 John, Revelation) read one verse OVER canonical, an
ordinary versification variant, not corruption.

So the table carries a per-book `trust`:
    exact     — use as a hard bound; a verse past it is an error
    slack+1   — the book is known to run one over somewhere; allow +1 before erring
    unreliable — Matthew and Mark; a verse past the bound is a WARNING, never an error

⚠ SEPARATELY, and not a defect in this table: Milton cites Junius-Tremellius and Sumner
adjusts toward KJV INCONSISTENTLY (CONVENTIONS §3). Hebrew numbering counts the psalm
superscription as verse 1, so a LATIN psalm verse may legitimately exceed the KJV bound
by one or two. build-citations.py owns that distinction; this file only reports what the
KJV has.

    ./tools/build-versification.py            # writes tools/versification.json
    ./tools/build-versification.py --check    # report only, write nothing
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KJV = os.path.expanduser("~/kjv-wesley/data/kjv")
BOOKS_JSON = os.path.join(ROOT, "tools", "scripture-books.json")
OUT = os.path.join(ROOT, "tools", "versification.json")

# our book key -> the dataset's filename slug
SLUG = {
    "Gen": "genesis", "Exod": "exodus", "Lev": "leviticus", "Num": "numbers",
    "Deut": "deuteronomy", "Josh": "joshua", "Judg": "judges", "Ruth": "ruth",
    "1Sam": "1samuel", "2Sam": "2samuel", "1Kgs": "1kings", "2Kgs": "2kings",
    "1Chr": "1chronicles", "2Chr": "2chronicles", "Ezra": "ezra", "Neh": "nehemiah",
    "Esth": "esther", "Job": "job", "Ps": "psalms", "Prov": "proverbs",
    "Eccl": "ecclesiastes", "Song": "songofsolomon", "Isa": "isaiah", "Jer": "jeremiah",
    "Lam": "lamentations", "Ezek": "ezekiel", "Dan": "daniel", "Hos": "hosea",
    "Joel": "joel", "Amos": "amos", "Obad": "obadiah", "Jonah": "jonah",
    "Mic": "micah", "Nah": "nahum", "Hab": "habakkuk", "Zeph": "zephaniah",
    "Hag": "haggai", "Zech": "zechariah", "Mal": "malachi",
    "Matt": "matthew", "Mark": "mark", "Luke": "luke", "John": "john",
    "Acts": "acts", "Rom": "romans", "1Cor": "1corinthians", "2Cor": "2corinthians",
    "Gal": "galatians", "Eph": "ephesians", "Phil": "philippians", "Col": "colossians",
    "1Thess": "1thessalonians", "2Thess": "2thessalonians", "1Tim": "1timothy",
    "2Tim": "2timothy", "Titus": "titus", "Phlm": "philemon", "Heb": "hebrews",
    "Jas": "james", "1Pet": "1peter", "2Pet": "2peter", "1John": "1john",
    "2John": "2john", "3John": "3john", "Jude": "jude", "Rev": "revelation",
}

TRUST = {b: "exact" for b in SLUG}
for b in ("Matt", "Mark"):
    TRUST[b] = "unreliable"          # short 3 verses each, silently renumbered
for b in ("1Sam", "1Kgs", "3John", "Rev"):
    TRUST[b] = "slack+1"             # read one over canonical; a variant, not damage


def main():
    check_only = "--check" in sys.argv
    if not os.path.isdir(KJV):
        sys.exit(f"FATAL: KJV dataset not found at {KJV}")

    known = {b["key"] for b in json.load(open(BOOKS_JSON))["books"]}
    table, total, problems = {}, 0, []

    for key, slug in sorted(SLUG.items()):
        path = os.path.join(KJV, slug + ".json")
        if not os.path.exists(path):
            problems.append(f"{key}: no file {slug}.json")
            continue
        chs = json.load(open(path))["chapters"]
        verses = []
        for i, ch in enumerate(chs, 1):
            if ch.get("chapter") != i:
                problems.append(f"{key}: chapter array out of order at index {i}")
            verses.append(max((v["verse"] for v in ch["verses"]), default=0))
        total += sum(verses)
        table[key] = {"chapters": len(chs), "verses": verses, "trust": TRUST[key]}

    missing = known - set(table)
    if missing:
        problems.append("in scripture-books.json but not mapped here: " + ", ".join(sorted(missing)))

    print(f"{len(table)} books · {sum(t['chapters'] for t in table.values())} chapters · {total} verses")
    print("  (the KJV has 31,102; this dataset is known short — see the docstring)")
    for p in problems:
        print("  !! " + p)
    unmapped = sorted(set(SLUG) - known)
    if unmapped:
        print("  note: no alias yet in scripture-books.json for " + ", ".join(unmapped))

    if check_only:
        return
    doc = {
        "_about": ("Derived by tools/build-versification.py from ~/kjv-wesley/data/kjv. "
                   "DO NOT HAND-EDIT — regenerate. `trust` is per book: exact | slack+1 | "
                   "unreliable (Matthew and Mark, which the source dataset renumbers past "
                   "three dropped verses each). `verses[i]` is the highest verse number in "
                   "chapter i+1."),
        "_hebrew_numbering": ("Milton cites Junius-Tremellius; Hebrew psalm numbering counts "
                              "the superscription, so a LATIN psalm verse may legitimately run "
                              "one or two past the KJV bound. That is a divergence to display, "
                              "not an error to report. See CONVENTIONS §3."),
        "_source_verse_total": total,
        "books": table,
    }
    with open(OUT, "w") as fh:
        json.dump(doc, fh, indent=1, sort_keys=False)
        fh.write("\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
