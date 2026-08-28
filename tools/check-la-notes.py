#!/usr/bin/env python3
"""Cross-check transcribed Latin notes against sweep-book1.tsv — INVERTED.

WHY INVERTED (Wilson's ruling, 2026-08-28). The detector was built to say where to LOOK,
and in that direction it failed: it called La 12 and La 20 clean and both carry notes, in
the first long Book I chapter read. Used that way it is worse than useless, because it
invites a session to expect nothing.

Run the other way it is sound. The question here is not "where might a note be" but
"we transcribed this chapter and recorded no note on page N — did the detector see
something there?" A false negative cannot hurt in this direction, and the detector's
false POSITIVES become exactly what we want: pages worth a second look.

WHY IT MISSES, measured. A CANDIDATE needs a RUN of consistently smaller pitches after a
gap — La 129 gives 26,26,26,25,26,26,26,26 against a body pitch of 34, and La 143 gives
26,27 against 34. A ONE- OR TWO-LINE note cannot produce such a run: La 20's note yielded
the single value 30 against a body of 33, under threshold, and La 12's yielded no
measurable gap at all. **The detector is structurally blind to short notes, which is the
commonest kind.** Never restore it to a deciding role.

THE SIGNAL USED HERE is deliberately looser than CANDIDATE, because in this direction a
false positive costs one glance and a false negative costs a missed note: a page is worth a
second look when min(pitches after the gap) / body_pitch <= 0.93, i.e. the type after the
gap is at least 7% tighter than the body. Measured over all 380 Book I pages that yields 43
pages, and it catches every known note that leaves a measurable gap at all — La 20 (0.909),
La 129 (0.735), La 143 (0.765). La 12 has no gap and cannot be caught by any threshold.
The bare presence of a gap is NOT the signal: 312 of the 380 pages have one.

CHAPTER OPENINGS ARE FALSE POSITIVES BY CONSTRUCTION. A display heading leaves a large
white band, and the ratio collapses — La 57, 203, 211, 331, 337 all read 0.27–0.30 with no
note anywhere near them. Openings are marked below so they can be discounted at a glance.

This does not replace M3-RUNBOOK §2 step 3 — read every Latin page foot, every chapter.
It is a second pair of eyes AFTER that reading, not a substitute for it.

    ./tools/check-la-notes.py            # every transcribed Book I chunk
    ./tools/check-la-notes.py ddc-1-02   # one chunk
"""
import re, os, io, glob, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


TIGHTNESS = 0.93   # min(pitch after gap) / body_pitch at or below which a page is worth a look


def sweep():
    """printed page -> (worth_a_look, ratio, flag, detail)"""
    d = {}
    for line in io.open(os.path.join(ROOT, "tools/sweep-book1.tsv"), encoding="utf-8"):
        f = line.rstrip("\n").split("\t")
        if len(f) < 6 or f[0] == "printed":
            continue
        if f[4] == "-" or not f[3].isdigit():
            d[int(f[0])] = (False, None, f[5], f[4])
            continue
        body = int(f[3])
        ratio = min(int(x) for x in f[4].split(",")) / body if body else None
        d[int(f[0])] = (ratio is not None and ratio <= TIGHTNESS, ratio, f[5], f[4])
    return d


def chapter_openings():
    """La printed pages on which a chapter opens — display type, so a false positive here."""
    op = set()
    for line in io.open(os.path.join(ROOT, "tools/chapters.tsv"), encoding="utf-8"):
        f = line.rstrip("\n").split("\t")
        if len(f) == 8 and f[0].isdigit():
            op.add(int(f[2]))
    return op


def la_note_pages(path):
    """printed La pages on which this chunk anchors a [^laN], and the chunk's La range."""
    t = io.open(path, encoding="utf-8").read()
    fm = t.split("---")[1]
    meta = dict(re.findall(r'^(\w+):\s*"?([^"\n]*)"?$', fm, re.M))
    if meta.get("book") != "1":
        return None
    lo, hi = (int(x) for x in meta["pages_la"].split("-"))
    body = t.split("\n## Notes")[0]
    m = re.search(r'\n## la\n', body)
    if not m:
        return None
    nxt = body.find("\n## ", m.end())
    la = body[m.end(): nxt if nxt > 0 else len(body)]
    pages, page = set(), lo
    for piece in re.split(r'(<!-- p\.\d+ -->)', la):
        pm = re.match(r'<!-- p\.(\d+) -->', piece)
        if pm:
            page = int(pm.group(1)); continue
        if re.search(r'\[\^la\d+\]', piece):
            pages.add(page)
    return lo, hi, pages


def main():
    sw, openings = sweep(), chapter_openings()
    want = sys.argv[1:] or None
    paths = sorted(glob.glob(os.path.join(ROOT, "chunks/ddc-1-*.md")))
    if want:
        paths = [p for p in paths if os.path.basename(p)[:-3] in want]
    if not paths:
        sys.exit("no Book I chunks matched")

    total_look = 0
    for path in paths:
        got = la_note_pages(path)
        if not got:
            continue
        lo, hi, noted = got
        cid = os.path.basename(path)[:-3]
        look, blind = [], []
        for p in range(lo, hi + 1):
            saw, ratio, flag, detail = sw.get(p, (False, None, "NOT_IN_SWEEP", ""))
            if p not in noted and saw:
                look.append((p, ratio, flag, detail, p in openings))
            if p in noted and not saw:
                blind.append(p)
        print(f"\n{cid}  La {lo}–{hi}   recorded notes on: "
              f"{', '.join(str(p) for p in sorted(noted)) or 'none'}")
        if look:
            total_look += len(look)
            print("  ⚠ type after the gap is tighter than the body, and we recorded no note:")
            for p, ratio, flag, detail, is_open in look:
                tag = "  ← chapter opening, display type; discount" if is_open else ""
                print(f"      La {p}  ratio {ratio:.2f}  [{flag}]  after gap: {detail}{tag}")
        else:
            print("  ✓ nothing tighter than the body that we did not already record")
        if blind:
            print(f"  · we recorded notes the detector missed entirely: La "
                  f"{', '.join(str(p) for p in blind)} — expected for short notes, see the docstring")

    real = total_look
    print(f"\n{real} page(s) to look at again (threshold {TIGHTNESS}; "
          f"43 of Book I's 380 pages clear it in total).")
    print("This is a cross-check, NOT a substitute for reading every Latin foot (M3-RUNBOOK §2).")


if __name__ == "__main__":
    main()
