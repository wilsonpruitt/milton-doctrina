#!/usr/bin/env python3
"""Print one paragraph from every text layer of a chunk, side by side in sequence.

Usage: show-para.py <chunk-id> <para-number> [<para-number> ...]
A reading aid for QA: the citation ledger names a chunk and a paragraph, and
settling a question about it means seeing both layers' wording of it.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAYERS = ("la", "en-sumner")


def sections(text):
    out, name, buf = {}, None, []
    for line in text.splitlines():
        m = re.match(r"^## (\S+)", line)
        if m:
            if name:
                out[name] = "\n".join(buf)
            name, buf = m.group(1), []
        elif name:
            buf.append(line)
    if name:
        out[name] = "\n".join(buf)
    return out


def paragraph(body, n):
    for block in body.split("\n\n"):
        if re.search(r"\{¶%d\}" % n, block):
            return block.strip()
    return None


def main():
    chunk, nums = sys.argv[1], [int(a) for a in sys.argv[2:]]
    secs = sections((ROOT / "chunks" / f"{chunk}.md").read_text())
    for n in nums:
        for layer in LAYERS:
            if layer not in secs:
                continue
            para = paragraph(secs[layer], n)
            print(f"===== {chunk} {layer} ¶{n} =====")
            print(para if para else "(no such paragraph)")
            print()


if __name__ == "__main__":
    main()
