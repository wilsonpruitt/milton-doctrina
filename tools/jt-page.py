#!/usr/bin/env python3
"""jt-page.py — fetch and crop a leaf of the Junius–Tremellius Bible (Hanau 1603).

★ This is the Bible Milton cited. CONVENTIONS §3 and M4-RUNBOOK §6b/§10.8 turn on what its
verse numbers say, and the OCR cannot answer that: the numbers are set small, and the
marginal scholia bleed into the text column. Read them off the IMAGE, at the band and the
scale you need, exactly as the Sumner plates are read (CONVENTIONS §2).

    ./tools/jt-page.py 812                       # whole leaf, cached
    ./tools/jt-page.py 812 --band 0 0.06         # the running head, to identify the book
    ./tools/jt-page.py 812 --band .30 .46 --x .5 1  # right column, middle — for verse digits

Leaves are the SCAN's numbering (`page/n<LEAF>.jpg`), not the volume's printed folios; the
volume prints Old and New Testament in one sequence with its own signatures. Record any
calibration you establish in STRUCTURE.md next to the two Sumner volumes'.

Everything lands under raw/jt/ and is gitignored and re-fetchable.
"""
import argparse
import pathlib
import sys
import urllib.request

ID = "testamentiveteri00trem"
ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "raw" / "jt" / "pages"
CROPS = ROOT / "raw" / "jt" / "crops"


def leaf(n):
    PAGES.mkdir(parents=True, exist_ok=True)
    f = PAGES / f"n{n}.jpg"
    if not f.exists() or f.stat().st_size == 0:
        url = f"https://archive.org/download/{ID}/page/n{n}.jpg"
        with urllib.request.urlopen(url, timeout=180) as r, open(f, "wb") as out:
            out.write(r.read())
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("leaf", type=int)
    ap.add_argument("--band", nargs=2, type=float, metavar=("Y0", "Y1"),
                    help="vertical slice as fractions of page height")
    ap.add_argument("--x", nargs=2, type=float, default=(0.0, 1.0), metavar=("X0", "X1"),
                    help="horizontal slice as fractions of page width")
    ap.add_argument("--scale", type=float, default=1.0, help="resample the crop by this factor")
    ap.add_argument("--out", help="name under raw/jt/crops/ (default: n<leaf>[-band])")
    a = ap.parse_args()

    src = leaf(a.leaf)
    if not a.band:
        print(src)
        return
    from PIL import Image
    im = Image.open(src)
    w, h = im.size
    box = (int(a.x[0] * w), int(a.band[0] * h), int(a.x[1] * w), int(a.band[1] * h))
    im = im.crop(box)
    if a.scale != 1.0:
        im = im.resize((int(im.width * a.scale), int(im.height * a.scale)), Image.LANCZOS)
    CROPS.mkdir(parents=True, exist_ok=True)
    name = a.out or f"n{a.leaf}-{a.band[0]}_{a.band[1]}"
    dst = CROPS / f"{name}.jpg"
    im.save(dst, quality=92)
    print(dst)


if __name__ == "__main__":
    sys.exit(main())
