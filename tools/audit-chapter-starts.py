#!/usr/bin/env python3.11
"""
audit-chapter-starts.py — find every chapter heading in both 1825 volumes and
reconcile them against tools/chapters.tsv.

WHY THIS EXISTS. PLAN.md risk #1 is alignment drift: "Sumner's English paragraphing
does not reliably match his Latin. If alignment is assumed rather than verified per
chapter, it will silently rot and be very expensive to fix late." The M0 crosswalk was
built by detection and has at least one CONFIRMED error (the English II.v/II.vi
boundary — see notes below). This script re-derives every chapter start independently
so the errors are found in one pass instead of one chapter at a time.

METHOD. Chapter headings are set as a line reading "CAP. <roman>." (Latin) or
"CHAP. <roman>." (English). We locate them in the pdftotext layer, which is a
FINDING AID ONLY — its job here is to tell you which plate to open, exactly as
CONVENTIONS.md §2 permits. Nothing this script outputs is authoritative until the
plate is read. Verified starts are what belong in chapters.tsv.

Book boundary is detected from the "LIBER SECUNDUS" / "BOOK II" page.

Usage:  python3.11 tools/audit-chapter-starts.py
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
TSV = ROOT / "tools" / "chapters.tsv"

# Measured at M0. pdf = printed + offset. text_lo/text_hi are the printed-page extents
# of the BODY: front matter (title, preface, and above all the table of contents, which
# lists every "CAP. I." heading and would otherwise flood the scan with false hits) and
# back matter are excluded by these bounds.
LAYERS = {
    "la": {"pdf": RAW / "la.pdf", "offset": 16, "kw": r"CAP\.",
           "book2": r"LIBER\s+SECUNDUS", "text_lo": 7, "text_hi": 536},
    "en": {"pdf": RAW / "en.pdf", "offset": 56, "kw": r"CHAP\.",
           "book2": r"BOOK\s+II\b", "text_lo": 9, "text_hi": 711},
}

ROMAN = {
    "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
    "X": 10, "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17,
    "XVIII": 18, "XIX": 19, "XX": 20, "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24,
    "XXV": 25, "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30, "XXXI": 31,
    "XXXII": 32, "XXXIII": 33,
}


def pages(pdf: Path) -> list[str]:
    """Whole PDF as a list of page texts (pdftotext separates pages with \\f)."""
    out = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        capture_output=True, text=True, check=True,
    ).stdout
    return out.split("\f")


def scan(layer: str) -> dict[tuple[int, int], int]:
    """Return {(book, chapter): printed_page} as detected in the text layer."""
    cfg = LAYERS[layer]
    pgs = pages(cfg["pdf"])
    head_re = re.compile(rf"^\s*{cfg['kw']}\s*([IVXL]+)\s*\.?\s*$", re.M)
    book2_re = re.compile(cfg["book2"])

    def in_body(pdf_page: int) -> bool:
        printed = pdf_page - cfg["offset"]
        return cfg["text_lo"] <= printed <= cfg["text_hi"]

    book2_pdf = None
    for i, txt in enumerate(pgs, start=1):
        if in_body(i) and book2_re.search(txt):
            book2_pdf = i
            break

    found: dict[tuple[int, int], int] = {}
    for i, txt in enumerate(pgs, start=1):
        if not in_body(i):
            continue
        m = head_re.search(txt)
        if not m:
            continue
        roman = m.group(1)
        if roman not in ROMAN:
            continue
        ch = ROMAN[roman]
        book = 2 if (book2_pdf and i >= book2_pdf) else 1
        printed = i - cfg["offset"]
        found.setdefault((book, ch), printed)
    return found


def load_tsv() -> dict[tuple[int, int], dict]:
    rows = {}
    for line in TSV.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        f = line.split("\t")
        if f[0] == "book":
            continue
        rows[(int(f[0]), int(f[1]))] = {
            "la": int(f[2]), "la_pp": int(f[3]),
            "en": int(f[4]), "en_pp": int(f[5]),
            "flag": f[6], "title": f[7],
        }
    return rows


def main() -> int:
    for cfg in LAYERS.values():
        if not cfg["pdf"].exists():
            print(f"FATAL: {cfg['pdf']} missing (raw/ is gitignored — re-fetch)")
            return 1

    la_found, en_found = scan("la"), scan("en")
    tsv = load_tsv()

    print(f"{'ch':>6}  {'La tsv':>7} {'La txt':>7}  {'En tsv':>7} {'En txt':>7}   verdict")
    print("-" * 78)

    mismatches = []
    for key in sorted(tsv):
        book, ch = key
        row = tsv[key]
        la_t, en_t = la_found.get(key), en_found.get(key)

        bad = []
        if la_t is not None and la_t != row["la"]:
            bad.append(f"La tsv={row['la']} txt={la_t}")
        if en_t is not None and en_t != row["en"]:
            bad.append(f"En tsv={row['en']} txt={en_t}")
        missing = [n for n, v in (("La", la_t), ("En", en_t)) if v is None]

        if bad:
            verdict = "MISMATCH  " + " · ".join(bad)
            mismatches.append((key, verdict))
        elif missing:
            verdict = f"not found in {'/'.join(missing)} text layer — check plate"
        else:
            verdict = "ok"

        print(
            f"{book}.{ch:<4}  {row['la']:>7} {str(la_t or '-'):>7}"
            f"  {row['en']:>7} {str(en_t or '-'):>7}   {verdict}"
        )

    print()
    if mismatches:
        print(f"{len(mismatches)} MISMATCH(es) — each needs a plate read, then fix chapters.tsv:")
        for (book, ch), v in mismatches:
            print(f"  {book}.{ch}  {v}")
    else:
        print("No mismatches between chapters.tsv and the text layer.")
    print()
    print("REMINDER: the text layer is a finding aid. Confirm every correction off the")
    print("plate before writing it into chapters.tsv.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
