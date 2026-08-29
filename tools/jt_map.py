#!/usr/bin/env python3
"""jt_map.py — map a Junius–Tremellius reference onto the KJV, and classify a divergence.

M4-RUNBOOK §11–13. The two 1825 volumes disagree on citation digits because Milton cites
Junius–Tremellius and Sumner converts toward the KJV (CONVENTIONS §3). Until now that was a
claim a reader had to re-derive from prose in a chunk's Notes. This makes it computable:
`tools/jt-divisions.json` says where each known J–T chapter begins, and everything else
follows by walking the KJV verse counts in `tools/versification.json`.

    from jt_map import JTMap
    m = JTMap()
    m.to_kjv("Isa", 57, 2)          -> ("Isa", 56, 10)
    m.classify("Isa", 57, [2], "Isa", 56, [10])   -> ("versification", "...")

⚠ What this does NOT do: invent a division. A chapter with no entry classifies as
`unchecked`, never as error. Calling a divergence an error is a claim about Milton, and the
only thing entitled to make it is a page image.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
REF_RE = re.compile(r"^\s*(\S+)\s+(\d+):(\d+)\s*$")


class JTMap:
    def __init__(self):
        self.vers = json.loads((ROOT / "versification.json").read_text())["books"]
        data = json.loads((ROOT / "jt-divisions.json").read_text())
        self.div = {}
        for d in data["divisions"]:
            self.div[(d["book"], d["chapter"])] = d

    def _verses(self, book, chapter):
        b = self.vers.get(book)
        if not b or not (1 <= chapter <= len(b["verses"])):
            return None
        return b["verses"][chapter - 1]

    def to_kjv(self, book, chapter, verse):
        """Where does J–T <book> <chapter>:<verse> land in the KJV? None if unknown."""
        d = self.div.get((book, chapter))
        if d is None:
            return None
        m = REF_RE.match(d["begins_at"])
        if not m:
            return None
        bk, ch, v = m.group(1), int(m.group(2)), int(m.group(3))
        if bk != book:
            return None
        step = verse - d["first_verse"]
        if step < 0:
            return None
        # walk forward, crossing chapter boundaries on the KJV's verse counts
        while step:
            n = self._verses(bk, ch)
            if n is None:
                return None
            room = n - v
            if step <= room:
                v += step
                step = 0
            else:
                step -= room + 1
                ch += 1
                v = 1
        return (bk, ch, v)

    def classify(self, la_book, la_ch, la_verses, en_book, en_ch, en_verses):
        """Why do the two layers print different numbers for one citation?

        Returns (class, note). The classes, and what each is allowed to assert:
          versification            a READ J–T division maps the Latin onto the English exactly
          versification-predicted  no division read, but the mechanism is known and the shape
                                   fits — Psalms +1/+2, the numbered superscription (§13.1)
          unchecked                no division read and no known mechanism. NOT an error.
          anomaly                  a division IS read and the Latin does not map onto the
                                   English through it. These are the rows worth a reader.
        """
        if not la_verses or not en_verses or la_book != en_book:
            return ("unchecked", "different books, or a chapter-only citation")
        # ⚠ Identical numbers on both sides are NOT a numeric divergence — the pair is a
        # syntax row (a list against a dash-range, M4-RUNBOOK §3.1). Running the J–T map
        # over one manufactures an anomaly out of `Psal. lv. 5, 6, 7.` / `lv. 5—7.`, where
        # nothing whatever disagrees. (It does mean Sumner left that one unconverted, which
        # is a real observation about his inconsistency — but it belongs to the syntax row,
        # not here.)
        if la_ch == en_ch and la_verses == en_verses:
            return ("", "")
        d = self.div.get((la_book, la_ch))
        if d is not None:
            mapped = [self.to_kjv(la_book, la_ch, v) for v in la_verses]
            want = [(en_book, en_ch, v) for v in en_verses]
            why = (f"J–T {la_book} {la_ch} begins at {d['begins_at']}"
                   + (f", first verse numbered {d['first_verse']}" if d["first_verse"] != 1 else "")
                   + f" ({d['status']}, leaf {d['leaf']})")
            if None in mapped:
                return ("anomaly", f"{why} — but the Latin verse falls outside the mapping")
            if mapped == want:
                return ("versification", why)
            # ⚠ The English narrows constantly: `Isa. xliv. 12, 13.` against `xliv. 18.` is
            # the SAME citation with Sumner keeping only its last verse (attested across the
            # corpus as its own class). A narrowed English is still versification — the
            # numbers it does print must simply be among the ones the Latin maps onto.
            if set(want) < set(mapped):
                return ("versification", why + "; the English narrows the range")
            return ("anomaly",
                    f"{why} and does NOT give the English reading — worth a reader")
        # no division read. Is the mechanism nonetheless known?
        if la_book == "Ps" and la_ch == en_ch and len(la_verses) == len(en_verses):
            deltas = {a - b for a, b in zip(la_verses, en_verses)}
            if deltas <= {1} or deltas <= {2}:
                n = deltas.pop()
                return ("versification-predicted",
                        f"Psalm superscription numbered as {n} verse{'s' if n > 1 else ''} "
                        f"(§13.1 rule; this psalm's own leaf not read)")
        return ("unchecked", "no J–T division read for this chapter")


if __name__ == "__main__":
    m = JTMap()
    checks = [
        ("Isa", 57, 2, ("Isa", 56, 10)), ("Isa", 57, 13, ("Isa", 57, 9)),
        ("Isa", 3, 5, ("Isa", 3, 4)),    ("Isa", 44, 1, ("Isa", 44, 6)),
        ("Eccl", 4, 9, ("Eccl", 4, 13)), ("Eccl", 10, 13, ("Eccl", 10, 16)),
        ("Eccl", 2, 3, ("Eccl", 2, 2)),  ("Eccl", 8, 1, ("Eccl", 8, 2)),
        ("Eccl", 9, 3, ("Eccl", 9, 1)),  ("Prov", 12, 9, ("Prov", 12, 10)),
        ("Num", 23, 12, ("Num", 23, 8)), ("Gen", 27, 43, ("Gen", 27, 41)),
        ("Judg", 11, 5, ("Judg", 11, 3)),("1Sam", 16, 2, ("1Sam", 16, 1)),
        ("Ps", 54, 7, ("Ps", 54, 5)),    ("Ps", 55, 18, ("Ps", 55, 17)),
        ("Ezek", 3, 18, ("Ezek", 3, 8)),
    ]
    bad = 0
    for book, ch, v, want in checks:
        got = m.to_kjv(book, ch, v)
        ok = got == want
        bad += not ok
        print(f"{'ok ' if ok else 'FAIL'} J–T {book} {ch}:{v} -> {got}" + ("" if ok else f"  want {want}"))
    print(f"\n{len(checks) - bad}/{len(checks)} map correctly")
