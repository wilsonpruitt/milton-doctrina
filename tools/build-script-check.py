#!/usr/bin/env python3
"""Build script-check.html — every non-Latin-script token in the corpus, for a specialist.

WHY THIS EXISTS. CONVENTIONS §5c says a reading of ours, in a script we do not command,
carries ⚠ UNVERIFIED until a specialist confirms it. That flag is honest but it is not a
plan. This page IS the plan: it gathers every Hebrew and Greek token we have transcribed,
says where each one is printed, and deep-links the plate so a reader can check it against
the source in one click rather than taking our word for anything.

The Greek accents on Θεοτὴς/Θειοτὴς are the cautionary tale and are noted on the page:
our standard-accentuation fallback was WRONG, and only a second scan caught it.

Regenerate after every chapter:  ./tools/build-script-check.py
Everything is derived from chunks/ — there is nothing to keep in sync by hand.

Published (private) at
    https://claude.ai/code/artifact/c88eb1e4-df24-4f86-aea0-150ccae56faf
Republish to THAT url after regenerating; never create a second artifact.
"""
import re, glob, os, io, html, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# archive.org: leaf = printed + OFFSET, endpoint /download/<id>/page/n<leaf>.jpg
#
# ⚠ THE LEAF OFFSET IS NOT THE PDF OFFSET. STRUCTURE.md gives pdf = printed + 16 (La) and
# + 56 (En); the leaf offsets are ONE LESS, because leaf numbering is 0-based. Every value
# below was calibrated by fetching a leaf and reading its printed folio — never assumed:
#   joannismiltonian00miltuoft  n30 = printed 15  -> 15
#   bwb_T5-ARK-705              n30 = printed 13  -> 17
#   treatiseonchrist00milt      n76 = printed 21  -> 55
SCANS = {
    "la":        [("joannismiltonian00miltuoft", 15, "working copy"),
                  ("bwb_T5-ARK-705",             17, "cleaner second copy")],
    "en-sumner": [("treatiseonchrist00milt",     55, "working copy")],
}
LAYER_NAME = {"la": "Latin volume", "en-sumner": "English volume", "editorial": "our note on"}

HEB = re.compile(r'[֐-׿יִ-ﭏ]+')
GRK = re.compile(r'[Ͱ-Ͽἀ-῿]+')
POINT = re.compile(r'[֑-ׇ]')          # vowel points / accents
BREATH = re.compile(r'[̀-ͅἀ-῿]')


def chunks():
    for path in sorted(glob.glob(os.path.join(ROOT, "chunks/ddc-*.md"))):
        t = io.open(path, encoding="utf-8").read()
        fm = t.split("---")[1]
        meta = dict(re.findall(r'^(\w+):\s*"?([^"\n]*)"?$', fm, re.M))
        body = t.split("\n## Notes")[0]
        yield os.path.basename(path)[:-3], meta, body


APPARATUS_LAYER = {"apparatus-sumner-en": "en-sumner", "apparatus-sumner-la": "la"}


def sections(body):
    """(langkey, kind, text) for every section that carries text read off a plate.

    Three kinds, and the third asks a different question:
      "text"  — the transcription layers.
      "note"  — Sumner's own apparatus. His footnotes quote Hebrew and Greek as heavily as
                the text does (En 20's note 7 alone carries four Hebrew forms) and were read
                off the same plates, so they need the same check: does this match the page?
      "ours"  — ## apparatus-editorial. These are OUR claims about what a corrupt printed
                reading ought to be. §5c already marks them UNVERIFIED; they are the rows
                where a specialist is not confirming a transcription but judging an argument,
                and they are the ones that must not be published unconfirmed.
    """
    for m in re.finditer(r'\n## ([a-z0-9-]+)\n', body):
        key = m.group(1)
        nxt = body.find("\n## ", m.end())
        text = body[m.end(): nxt if nxt > 0 else len(body)]
        if key in SCANS:
            yield key, "text", text
        elif key in APPARATUS_LAYER:
            yield APPARATUS_LAYER[key], "note", text
        elif key == "apparatus-editorial":
            yield "editorial", "ours", text


def harvest():
    """{(script, token): [occurrence, ...]} — occurrence carries chunk, layer, printed page."""
    found = collections.defaultdict(list)
    for cid, meta, body in chunks():
        for layer, kind, text in sections(body):
            key_ = "la" if layer in ("la", "editorial") else "en"
            start = int(str(meta.get("pages_" + key_)).split("-")[0])
            page = start
            # text layers carry <!-- p.N --> markers; apparatus carries "(printed En p. N"
            splitter = (r'(<!-- p\.\d+ -->)' if kind == "text"
                        else r'((?:printed )?(?:En|La)\.? pp?\.\s*\d+)')
            for piece in re.split(splitter, text):
                pm = (re.match(r'<!-- p\.(\d+) -->', piece) if kind == "text"
                      else re.match(r'(?:printed )?(?:En|La)\.? pp?\.\s*(\d+)', piece))
                if pm:
                    page = int(pm.group(1)); continue
                for script, rx in (("Hebrew", HEB), ("Greek", GRK)):
                    for tok in rx.findall(piece):
                        found[(script, tok)].append((cid, layer, page, kind))
    return found


def plate_links(layer, page):
    if layer == "editorial":
        return '<span style="color:var(--ink-3)">see the rows above</span>'
    out = []
    for ident, off, label in SCANS.get(layer, []):
        out.append(f'<a href="https://archive.org/download/{ident}/page/n{page + off}.jpg" '
                   f'target="_blank" rel="noopener" title="{html.escape(label)}">'
                   f'n{page + off}</a>')
    return " · ".join(out)


CSS = """
:root{--paper:#FBFAF8;--card:#FFF;--rule:#E2DED7;--ink:#1A1D24;--ink-2:#4A5060;--ink-3:#767D8E;
 --accent:#3A4A7B;--accent-soft:#E7EAF3;--flag:#A33B2E;--flag-soft:#F7E7E4;--ok:#3F7A5E}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--paper:#14161C;--card:#1C1F28;
 --rule:#2C313D;--ink:#E9EAEE;--ink-2:#A8AEBE;--ink-3:#767D8E;--accent:#93A6DC;--accent-soft:#242A3C;
 --flag:#E08476;--flag-soft:#2E1D1B;--ok:#79BE9B}}
:root[data-theme=dark]{--paper:#14161C;--card:#1C1F28;--rule:#2C313D;--ink:#E9EAEE;--ink-2:#A8AEBE;
 --ink-3:#767D8E;--accent:#93A6DC;--accent-soft:#242A3C;--flag:#E08476;--flag-soft:#2E1D1B;--ok:#79BE9B}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-size:15px;line-height:1.5;
 font-family:"IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:40px 24px 72px}
h1{font-family:"EB Garamond",Georgia,serif;font-style:italic;font-weight:600;font-size:32px;margin:0}
.eyebrow{font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
header{border-bottom:2px solid var(--ink);padding-bottom:18px}
.lede{color:var(--ink-2);font-size:14px;margin-top:10px;max-width:70ch}
.warn{background:var(--flag-soft);border-left:3px solid var(--flag);border-radius:6px;
 padding:13px 15px;margin:20px 0;font-size:13.5px;color:var(--ink-2);max-width:78ch}
.warn b{color:var(--ink)}
h2{font-size:15px;letter-spacing:.02em;border-bottom:1px solid var(--rule);
 padding-bottom:7px;margin:34px 0 0}
.meta{font-size:12px;color:var(--ink-3);font-weight:400}
table{width:100%;border-collapse:collapse;font-size:13.5px}
th{text-align:left;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);
 font-weight:600;padding:12px 10px 8px;border-bottom:1px solid var(--rule);white-space:nowrap}
td{padding:11px 10px;border-bottom:1px solid var(--rule);vertical-align:top}
tr:hover{background:var(--accent-soft)}
.tok{font-size:30px;line-height:1.35;white-space:nowrap;
 font-family:"SBL Hebrew","Ezra SIL","Times New Roman",serif}
.grk .tok{font-size:26px;font-family:"New Athena Unicode","Gentium Plus","Times New Roman",serif}
.where{font-family:ui-monospace,Menlo,monospace;font-size:11.5px;color:var(--ink-2)}
.where b{color:var(--ink);font-weight:600}
a{color:var(--accent)}
.n{font-family:ui-monospace,Menlo,monospace;font-size:12px;color:var(--ink-3);text-align:right}
.q{background:var(--flag-soft);border-radius:4px;padding:1px 6px;font-size:11px;
 color:var(--flag);font-weight:600;white-space:nowrap}
footer{margin-top:44px;padding-top:16px;border-top:1px solid var(--rule);font-size:12px;color:var(--ink-3)}
code{font-family:ui-monospace,Menlo,monospace;font-size:.92em;background:var(--accent-soft);
 padding:1px 5px;border-radius:4px}
"""

# tokens we already know are in question — shown with a flag and a reason
QUERIED = {
    "אֶהֶיֶה":
        "Exod. 3:14 with SEGOL under the he. The same word appears elsewhere on this sheet with "
        "SHVA — that is not our inconsistency, it is the book's. The Latin volume points it segol "
        "in both its instances; the English volume points it shva, then segol, then shva. "
        "Transcribed per instance and never harmonised (CONVENTIONS §3, §8b).",
    "אֶהְיֶה":
        "Exod. 3:14 with SHVA under the he — the correct Masoretic form, and what the English "
        "volume prints in two of its three instances (including note 7). See the segol row: the "
        "two pointings are both printed, in the same chapter, and are kept apart deliberately.",
    "אֱלֹהִים־בָּרִים":
        "Matches neither Psalm cited (vii. 10 / lxxxvi. 10), identically in BOTH volumes. "
        "Consonants confirmed at the plate. Probable error in the source — not mended in either layer.",
    "בְּרוּבָה":
        "Printed in the ENGLISH volume only (En 594) and is not a word; the Latin volume is sound here. "
        "Carried with an editorial note, per §5c.",
    "בִּדֵּו":
        "Printed in the ENGLISH volume only (En 594) and is not a word; the Latin volume is sound here. "
        "Carried with an editorial note, per §5c.",
}


def main():
    found = harvest()
    o = []
    A = o.append
    A('<title>Script check — De Doctrina Christiana</title>')
    A('<link rel="preconnect" href="https://fonts.googleapis.com">')
    A('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    A('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=EB+Garamond:ital,wght@0,400..600;1,400..600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">')
    A(f'<style>{CSS}</style>')
    A('<div class="wrap"><header>')
    A('<div class="eyebrow">Wroot Press · verification sheet</div>')
    A('<h1>Hebrew and Greek in the 1825 text</h1>')
    A('<p class="lede">Every non-Latin-script word we have transcribed from Sumner\'s 1825 '
      '<i>De Doctrina Christiana</i>, with the volume and printed page it comes from and a direct '
      'link to that page\'s scan. <b>We read these off the plates; we are not specialists in either '
      'script.</b> Nothing here has been corrected toward what the grammar expects — the 1825 is '
      'reproduced as printed, errors included.</p>')
    A('</header>')
    A('<div class="warn"><b>What is being asked.</b> For each row: does our transcription match the '
      'plate, character for character and point for point? Rows marked <span class="q">QUERIED</span> '
      'are ones we already believe the <i>printed source</i> is wrong — there the question is what the '
      'page actually says, not what it ought to say.<br><br>'
      '<b>Why we are asking rather than guessing.</b> The Greek below contains the cautionary case. '
      'Two words would not resolve in our scan, so we set them with standard accentuation and flagged '
      'them unverified. A cleaner scan later showed the book prints a <i>grave on the ultima</i> in '
      'both — our reconstruction from the grammar was simply wrong. The flag prevented a false claim; '
      'it did not prevent a false reading.</div>')

    for script, cls in (("Hebrew", ""), ("Greek", "grk")):
        rows = sorted(((t, occ) for (s, t), occ in found.items() if s == script),
                      key=lambda r: (-len(r[1]), r[0]))
        n_occ = sum(len(o2) for _, o2 in rows)
        A(f'<h2>{script} <span class="meta">— {len(rows)} distinct, '
          f'{n_occ} occurrence{"s" if n_occ != 1 else ""}</span></h2>')
        A(f'<table class="{cls}"><thead><tr><th>As we read it</th><th>Where it is printed</th>'
          f'<th class="n">×</th></tr></thead><tbody>')
        for tok, occ in rows:
            note = QUERIED.get(tok)
            where = []
            for cid, layer, page, kind in occ:
                tag = {"text": "", "note": ' <span style="color:var(--ink-3)">(in a footnote)</span>',
                       "ours": ' <span class="q">OUR CLAIM</span>'}[kind]
                where.append(f'<b>{LAYER_NAME[layer]} p.{page}</b>{tag} '
                             f'<span style="color:var(--ink-3)">{cid}</span> — {plate_links(layer, page)}')
            A('<tr><td class="tok" dir="rtl">' if script == "Hebrew" else '<tr><td class="tok">')
            A(html.escape(tok))
            if note:
                A('</td><td><span class="q">QUERIED</span> '
                  f'<span style="font-size:12.5px;color:var(--ink-2)">{html.escape(note)}</span>'
                  '<div class="where" style="margin-top:7px">' + '<br>'.join(where) + '</div>')
            else:
                A('</td><td><div class="where">' + '<br>'.join(where) + '</div>')
            A(f'</td><td class="n">{len(occ)}</td></tr>')
        A('</tbody></table>')

    A('<footer>Source text public domain (Sumner, Cambridge 1825). '
      'Generated from <code>chunks/</code> by <code>./tools/build-script-check.py</code> — '
      'regenerate after each chapter; nothing on this page is hand-kept.</footer>')
    A('</div>')
    out = os.path.join(ROOT, "script-check.html")
    io.open(out, "w", encoding="utf-8").write("\n".join(o))
    heb = sum(len(v) for (s, _), v in found.items() if s == "Hebrew")
    grk = sum(len(v) for (s, _), v in found.items() if s == "Greek")
    print(f"wrote {out}  ({os.path.getsize(out)//1024} KB)  "
          f"Hebrew {heb} occ / {sum(1 for s,_ in found if s=='Hebrew')} distinct · "
          f"Greek {grk} occ / {sum(1 for s,_ in found if s=='Greek')} distinct")


if __name__ == "__main__":
    main()
