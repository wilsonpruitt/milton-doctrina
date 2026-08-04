#!/usr/bin/env python3.11
"""
Mechanical pre-filter for the Book II Latin footnote sweep (M3-RUNBOOK §9b).

The 1825 Latin volume separates a footnote from the text by NOTHING but a gap and
a smaller type size -- there is no horizontal rule. So the detectable signal is a
DROP IN LINE PITCH in the lower part of the page.

Method. Measure the baseline-to-baseline pitch of every text line. Body text sits at
pitch ~33 at 150 dpi; note text at ~26. The signature of a footnote is therefore A
LARGE WHITE GAP FOLLOWED BY TWO OR MORE LINES AT NOTE PITCH. A page whose body text
simply continues to the foot shows body pitch after that gap instead.

(An earlier version compared median tail pitch against median body pitch. It FAILED on
both known positives: La 431's note is only two lines, so the median washed it out, and
La 454's note fills the page, so there was no body left to compare against. Absolute
pitch after the last gap is the discriminating measurement, not a ratio. Kept in the
record because the failure is instructive -- a metric can look principled and still be
blind to both instances of the thing it was built to find.)

Output: TSV to stdout -- printed_page, pdf_page, n_lines, body_pitch,
pitches_after_last_gap, flag.

Validated 2026-08-04 against both known positives and their immediate neighbours
before being trusted on unread pages.

⚠ THIS IS A PRE-FILTER, NOT THE SWEEP. It ranks pages so the reading session knows
where to look hardest. It does NOT license skipping any page: a false negative here
would defeat the entire purpose of the sweep, which exists precisely because nobody
was looking. Read the foot crops regardless of what this says (SWEEP-RUNBOOK.md §2),
then reconcile the two lists. Disagreement in either direction gets a full-page look.

Usage:  python3.11 tools/detect-footnotes.py <first_printed> <last_printed>
"""
import subprocess, sys, tempfile, os, statistics

LA_OFFSET = 16          # la_pdf = la_printed + 16   (M0, measured)
DPI = 150
INK = 160               # 0-255; below this counts as ink
MIN_LINE_ROWS = 2       # ignore specks

MERGE_GAP = 7           # rows; below this, two runs are one line (ascender band)
BODY_PITCH_MIN = 31     # body text sits at ~33 at 150 dpi
NOTE_PITCH = (22, 30)   # footnote type sits at ~26
GAP_MIN = 40            # the white band between body text and a note


def page_lines(path):
    """Return (line_top, line_bottom) pairs and the text-column bounds."""
    from PIL import Image
    im = Image.open(path).convert("L")
    w, h = im.size
    px = im.load()

    # horizontal extent of the text column: columns carrying a decent amount of ink
    colink = [0] * w
    for x in range(0, w, 2):                      # stride 2: plenty for a column profile
        c = 0
        for y in range(0, h, 2):
            if px[x, y] < INK:
                c += 1
        colink[x] = c
    peak = max(colink) or 1
    cols = [x for x in range(0, w, 2) if colink[x] > peak * 0.06]
    if not cols:
        return [], (0, w)
    x0, x1 = min(cols), max(cols)

    # row ink profile within the text column
    rows = []
    for y in range(h):
        c = 0
        for x in range(x0, x1, 2):
            if px[x, y] < INK:
                c += 1
        rows.append(c)
    rpeak = max(rows) or 1
    thresh = rpeak * 0.04

    raw, run = [], None
    for y, v in enumerate(rows):
        if v > thresh:
            if run is None:
                run = y
        else:
            if run is not None and y - run >= MIN_LINE_ROWS:
                raw.append((run, y))
            run = None
    if run is not None:
        raw.append((run, h))

    # Merge runs separated by only a sliver of white: an ascender band and the body
    # of the SAME line get detected separately and would otherwise fake tiny pitches.
    # Body pitch is ~33 at 150 dpi with ~13 rows of true interline white, so a gap
    # under MERGE_GAP can only be within-line.
    lines = []
    for top, bot in raw:
        if lines and top - lines[-1][1] < MERGE_GAP:
            lines[-1] = (lines[-1][0], bot)
        else:
            lines.append((top, bot))
    return lines, (x0, x1)


def main():
    first, last = int(sys.argv[1]), int(sys.argv[2])
    print("printed\tpdf\tn_lines\tbody_pitch\tpitches_after_last_gap\tflag")
    tmp = tempfile.mkdtemp()
    for printed in range(first, last + 1):
        pdf = printed + LA_OFFSET
        stem = os.path.join(tmp, "p")
        subprocess.run(["pdftoppm", "-f", str(pdf), "-l", str(pdf), "-r", str(DPI),
                        "-gray", "-jpeg", "raw/la.pdf", stem],
                       check=True, capture_output=True)
        img = f"{stem}-{pdf}.jpg"
        if not os.path.exists(img):                     # pdftoppm pads short numbers
            cands = [f for f in os.listdir(tmp) if f.endswith(".jpg")]
            img = os.path.join(tmp, cands[0])
        lines, _ = page_lines(img)
        os.remove(img)

        if len(lines) < 8:
            print(f"{printed}\t{pdf}\t{len(lines)}\t-\t-\tTOO_FEW_LINES")
            continue

        tops = [a for a, _ in lines]
        pitches = [tops[i + 1] - tops[i] for i in range(len(tops) - 1)]
        body = statistics.median([p for p in pitches if p >= BODY_PITCH_MIN] or [33])

        # Signature of a footnote: the last large white gap on the page, followed by
        # two or more lines set at note pitch. Body text after the gap => no note.
        gap_idx = max((i for i, p in enumerate(pitches) if p >= GAP_MIN), default=None)
        after = pitches[gap_idx + 1:] if gap_idx is not None else []
        n_small = sum(1 for p in after if NOTE_PITCH[0] <= p <= NOTE_PITCH[1])

        # Whole-page case: a note so long it dominates the page (La 454) shows a body
        # median already at note pitch, with no gap needed.
        page_is_small = body <= NOTE_PITCH[1]

        flag = "CANDIDATE" if (n_small >= 2 or page_is_small) else "."
        tail = ",".join(str(p) for p in after[:8]) or "-"
        print(f"{printed}\t{pdf}\t{len(lines)}\t{body:.0f}\t{tail}\t{flag}")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
