#!/usr/bin/env python3
"""build-status.py — generate the project status register from live repo data.

Reads tools/chapters.tsv and chunks/*.md and writes status.html, a self-contained
page showing where the edition stands: every chapter, its extent, its paragraph
alignment, the footnote numbers it carries, and what is still open.

    ./tools/build-status.py            # writes status.html
    ./tools/build-status.py --check    # print a summary, write nothing

Everything except OPEN_ITEMS is derived from the repo, so the page cannot drift
from the corpus. OPEN_ITEMS is the one hand-kept list; edit it here.
"""
import re, glob, os, sys, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- the one hand-kept list -------------------------------------------------
OPEN_ITEMS = [
    ("next", "ddc-1-03 — De Divino Decreto",
     "La 22–30 / En 30–43. Its first English note must be 8 (I.ii closed at 7), and the "
     "English chapter opens at En 30, plate-confirmed. Book I is split-dominated: expect "
     "Sumner to break Milton's paragraphs, not weld them."),
    ("watch", "crosswalk-output.txt is superseded",
     "The chapter-start audit's discrepancies now stand at 7 for 7 against the crosswalk's 0. "
     "chapters.tsv is the only source for page ranges; treat a ratio outside 1.05-1.85 as a "
     "boundary suspicion, since 1.27's 2.20 and 1.28's 0.96 were both real errors."),
    ("watch", "sweep-book1.tsv is unreliable",
     "The Latin-footnote detector missed BOTH notes in I.ii (La 12, La 20). "
     "It may suggest where to look in Book I; it cannot decide. Read every Latin foot."),
    ("watch", "PLAN §6.2 records conclusions, not arguments",
     "Two claims now mislocated: II.xv's divorce material is Sumner's apparatus, and "
     "the Arian argument is made in I.ii, not only I.v. Check I.vii and I.xiii the same way."),
    ("watch", "Hebrew pointing is UNVERIFIED",
     "Read by us, not a specialist (§5c). אֱלֹהִים־בָּרִים at La 18 / En 26 matches neither "
     "Psalm cited, identically in both volumes — probable error in the source."),
    ("watch", "A 2nd scan exists; use it before writing \'unresolvable\'",
     "archive.org bwb_T5-ARK-705 is a cleaner Latin volume, leaf = printed + 17. It settled the "
     "Theotes/Theiotes accents our own scan could not -- and showed the standard-accentuation "
     "fallback we had used was WRONG. See STRUCTURE.md."),
    ("watch", "Anchors can exist with no definition",
     "ddc-1-02 shipped its Latin layer with [^la1] and [^la2] anchored and no "
     "apparatus-sumner-la section at all, and it was not on the owed list. Check every "
     "anchor resolves before calling a layer complete."),
]

BOOK_TITLES = {1: "De Cognitione Dei", 2: "De Dei Cultu"}


def read_chapters():
    rows = []
    for line in open(os.path.join(ROOT, "tools/chapters.tsv"), encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        f = line.rstrip("\n").split("\t")
        if f[0] == "book":
            continue
        rows.append(dict(book=int(f[0]), ch=int(f[1]),
                         la_start=int(f[2]), la_pp=int(f[3]),
                         en_start=int(f[4]), en_pp=int(f[5]),
                         flag=f[6], title_la=f[7]))
    return rows


def read_chunks():
    by = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "chunks/ddc-*.md"))):
        t = open(path, encoding="utf-8").read()
        fm = t.split("---")[1]
        def g(k):
            m = re.search(rf'^{k}:\s*"?(.*?)"?\s*$', fm, re.M)
            return m.group(1) if m else None
        book, ch = int(g("book")), int(g("chapter"))
        la = t.split("## la")[1].split("## en-sumner")[0] if "## en-sumner" in t else ""
        en = t.split("## en-sumner")[1].split("## apparatus")[0] if "## en-sumner" in t else ""
        seq = []
        for n in re.findall(r"^\[\^s([0-9]+(?:-[0-9]+)?)\]:", t, re.M):
            if n not in seq:
                seq.append(n)
        rec = by.setdefault((book, ch), dict(ids=[], status=set(), la_par=0, en_par=0,
                                             notes=[], la_notes=[], title_en=None))
        rec["ids"].append(g("id"))
        rec["status"].add(g("status"))
        rec["la_par"] += len(re.findall(r"^\{¶", la, re.M))
        rec["en_par"] += len(re.findall(r"^\{¶", en, re.M))
        rec["notes"] += seq
        rec["la_notes"] += re.findall(r"^\[\^la([0-9]+)\]:", t, re.M)
        rec["title_en"] = rec["title_en"] or g("title_en")
    return by


CSS = """
:root{
  --paper:#FBFAF8; --sunk:#F2F0EC; --card:#FFFFFF; --rule:#E2DED7;
  --ink:#1A1D24; --ink-2:#4A5060; --ink-3:#767D8E;
  --accent:#3A4A7B; --accent-soft:#E7EAF3;
  --ok:#3F7A5E; --ok-soft:#E4EFE9;
  --work:#A8741A; --work-soft:#F6EEDD;
  --flag:#A33B2E; --flag-soft:#F7E7E4;
  --idle:#9AA0AE; --idle-soft:#EFEFF1;
  --shadow:0 1px 2px rgba(20,22,28,.05),0 8px 24px -12px rgba(20,22,28,.12);
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#14161C; --sunk:#191C24; --card:#1C1F28; --rule:#2C313D;
    --ink:#E9EAEE; --ink-2:#A8AEBE; --ink-3:#767D8E;
    --accent:#93A6DC; --accent-soft:#242A3C;
    --ok:#79BE9B; --ok-soft:#1B2A24;
    --work:#DCA94E; --work-soft:#2A2317;
    --flag:#E08476; --flag-soft:#2E1D1B;
    --idle:#6B7285; --idle-soft:#232630;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -12px rgba(0,0,0,.6);
  }
}
:root[data-theme="dark"]{
  --paper:#14161C; --sunk:#191C24; --card:#1C1F28; --rule:#2C313D;
  --ink:#E9EAEE; --ink-2:#A8AEBE; --ink-3:#767D8E;
  --accent:#93A6DC; --accent-soft:#242A3C;
  --ok:#79BE9B; --ok-soft:#1B2A24;
  --work:#DCA94E; --work-soft:#2A2317;
  --flag:#E08476; --flag-soft:#2E1D1B;
  --idle:#6B7285; --idle-soft:#232630;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 8px 24px -12px rgba(0,0,0,.6);
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font-family:"IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;
  font-size:15px; line-height:1.5; -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1120px; margin:0 auto; padding:40px 24px 72px}
.mono{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace; font-variant-numeric:tabular-nums}
.lat{font-family:"EB Garamond",Iowan Old Style,Palatino,Georgia,serif}

/* masthead */
header{display:flex; flex-wrap:wrap; gap:20px; align-items:flex-end;
  justify-content:space-between; padding-bottom:20px; border-bottom:2px solid var(--ink)}
h1{font-family:"EB Garamond",Georgia,serif; font-weight:600; font-size:34px;
  letter-spacing:-.01em; margin:0; text-wrap:balance; font-style:italic}
.sub{color:var(--ink-2); font-size:13.5px; margin-top:4px}
.eyebrow{font-size:11px; letter-spacing:.13em; text-transform:uppercase;
  color:var(--ink-3); font-weight:600}
.stamp{text-align:right; font-size:12px; color:var(--ink-3)}

/* summary */
.summary{display:grid; grid-template-columns:repeat(auto-fit,minmax(168px,1fr));
  gap:14px; margin:26px 0 8px}
.stat{background:var(--card); border:1px solid var(--rule); border-radius:8px;
  padding:14px 16px; box-shadow:var(--shadow)}
.stat .n{font-family:"IBM Plex Mono",monospace; font-size:26px; font-weight:500;
  letter-spacing:-.02em; font-variant-numeric:tabular-nums}
.stat .k{font-size:11px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--ink-3); font-weight:600; margin-top:2px}
.stat .note{font-size:12px; color:var(--ink-2); margin-top:6px}

/* progress bars */
.bookbar{margin:22px 0 6px}
.bookbar h2{font-size:14px; margin:0 0 8px; display:flex; gap:10px; align-items:baseline}
.bookbar h2 .t{font-family:"EB Garamond",Georgia,serif; font-style:italic;
  font-size:17px; color:var(--ink-2); font-weight:500}
.track{height:9px; border-radius:99px; background:var(--idle-soft);
  display:flex; overflow:hidden; border:1px solid var(--rule)}
.track i{display:block; height:100%}
.legend{display:flex; flex-wrap:wrap; gap:14px; margin-top:8px; font-size:12px; color:var(--ink-2)}
.legend b{font-weight:500}
.dot{width:9px;height:9px;border-radius:3px;display:inline-block;margin-right:5px;vertical-align:-1px}

/* register */
section{margin-top:34px}
.sechead{display:flex; align-items:baseline; justify-content:space-between;
  gap:16px; border-bottom:1px solid var(--rule); padding-bottom:7px; margin-bottom:2px}
.sechead h2{margin:0; font-size:15px; letter-spacing:.02em}
.sechead .meta{font-size:12px; color:var(--ink-3)}
.tablewrap{overflow-x:auto}
table{width:100%; border-collapse:collapse; font-size:13.5px}
thead th{text-align:left; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--ink-3); font-weight:600; padding:10px 10px 8px; white-space:nowrap;
  border-bottom:1px solid var(--rule)}
tbody td{padding:9px 10px; border-bottom:1px solid var(--rule); vertical-align:baseline}
tbody tr:hover{background:var(--sunk)}
td.ch{white-space:nowrap; padding-left:14px; position:relative; width:1%}
td.ch::before{content:""; position:absolute; left:0; top:6px; bottom:6px;
  width:3px; border-radius:99px; background:var(--stripe,var(--idle))}
.num{font-family:"IBM Plex Mono",monospace; color:var(--ink-3); font-size:12.5px}
.title{font-family:"EB Garamond",Georgia,serif; font-size:16px; line-height:1.3}
.title .en{display:block; font-family:"IBM Plex Sans",sans-serif; font-size:11.5px;
  color:var(--ink-3); line-height:1.35; margin-top:1px}
td.r{text-align:right; white-space:nowrap}
.chip{display:inline-block; font-size:10.5px; font-weight:600; letter-spacing:.07em;
  text-transform:uppercase; padding:3px 8px; border-radius:99px; white-space:nowrap}
.c-ok{background:var(--ok-soft); color:var(--ok)}
.c-work{background:var(--work-soft); color:var(--work)}
.c-flag{background:var(--flag-soft); color:var(--flag)}
.c-idle{background:var(--idle-soft); color:var(--ink-3)}
.ratio{font-family:"IBM Plex Mono",monospace; font-size:12.5px}
.ratio.warn{color:var(--work)}
.notes{font-family:"IBM Plex Mono",monospace; font-size:12px; color:var(--ink-2)}
.notes .none{color:var(--ink-3); font-style:italic; font-family:"IBM Plex Sans",sans-serif}
.la-note{display:inline-block; margin-left:5px; font-size:10px; font-weight:700;
  color:var(--accent); border:1px solid var(--accent); border-radius:3px;
  padding:0 3px; vertical-align:1px}
tr.next td{background:var(--accent-soft)}
tr.next td.ch::before{background:var(--accent)}

/* ledger ribbon */
.ribbon{background:var(--card); border:1px solid var(--rule); border-radius:8px;
  padding:16px 18px; box-shadow:var(--shadow)}
.cyc{display:flex; flex-wrap:wrap; gap:3px; margin-top:12px}
.cyc span{font-family:"IBM Plex Mono",monospace; font-size:11px; width:20px; height:20px;
  display:grid; place-items:center; border-radius:4px; background:var(--sunk);
  color:var(--ink-3); border:1px solid var(--rule)}
.cyc span.on{background:var(--accent); color:#fff; border-color:var(--accent); font-weight:600}
:root[data-theme="dark"] .cyc span.on{color:#14161C}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .cyc span.on{color:#14161C}}
.cyc .brk{width:auto; background:none; border:none; color:var(--ink-3); padding:0 4px}

/* open items */
.items{display:grid; gap:10px; margin-top:4px}
.item{display:flex; gap:12px; align-items:flex-start; background:var(--card);
  border:1px solid var(--rule); border-left:3px solid var(--stripe,var(--idle));
  border-radius:6px; padding:12px 14px}
.item h3{margin:0 0 2px; font-size:13.5px; font-weight:600}
.item p{margin:0; font-size:12.5px; color:var(--ink-2); line-height:1.45}
footer{margin-top:40px; padding-top:16px; border-top:1px solid var(--rule);
  font-size:12px; color:var(--ink-3); display:flex; flex-wrap:wrap; gap:6px 18px}
code{font-family:"IBM Plex Mono",monospace; font-size:.92em;
  background:var(--sunk); padding:1px 5px; border-radius:4px}
"""


def esc(s):
    return html.escape(s or "")


def status_of(ch, done):
    """(chip label, css class, stripe var) for one chapter row."""
    if done:
        st = ch["k"]["status"]
        if any(x and x != "verified" for x in st):      # la-verified, draft, ...
            return ("one layer", "c-work", "var(--work)")
        return ("verified", "c-ok", "var(--ok)") if ch["flag"] == "verified" \
               else ("drafted", "c-work", "var(--work)")
    if ch["flag"] == "suspect":
        return ("suspect", "c-flag", "var(--flag)")
    return ("not started", "c-idle", "var(--idle)")


def build():
    chaps, chunks = read_chapters(), read_chunks()
    for c in chaps:
        c["k"] = chunks.get((c["book"], c["ch"]))
        c["done"] = c["k"] is not None
    full = lambda c: c["done"] and all(x == "verified" for x in c["k"]["status"])
    done_all = [c for c in chaps if full(c)]
    partial = [c for c in chaps if c["done"] and not full(c)]
    nxt = next((c for c in chaps if not c["done"]), None)

    # ---- masthead + summary
    pct = round(100 * len(done_all) / len(chaps))
    la_pp = sum(c["la_pp"] for c in done_all)
    la_tot = sum(c["la_pp"] for c in chaps)
    notes_ct = sum(len(c["k"]["notes"]) for c in done_all)
    la_notes_ct = sum(len(c["k"]["la_notes"]) for c in done_all)
    suspects = [c for c in chaps if c["flag"] == "suspect"]

    o = []
    A = o.append
    A('<div class="wrap">')
    A('<header><div>')
    A('<div class="eyebrow">Wroot Press · transcription register</div>')
    A('<h1>De Doctrina Christiana</h1>')
    A('<div class="sub">Milton\'s systematic theology, Sumner 1825 — Latin and English '
      'in parallel, transcribed against the plates.</div>')
    A('</div><div class="stamp">generated '
      + datetime.date.today().isoformat()
      + '<br>from <span class="mono">chapters.tsv</span> + <span class="mono">chunks/</span></div></header>')

    A('<div class="summary">')
    A(f'<div class="stat"><div class="n">{len(done_all)}<span style="color:var(--ink-3);font-size:16px">/{len(chaps)}</span></div>'
      f'<div class="k">chapters verified</div><div class="note">{pct}% of the work'
      + (f' · {len(partial)} part-done' if partial else '') + '</div></div>')
    A(f'<div class="stat"><div class="n">{la_pp}<span style="color:var(--ink-3);font-size:16px">/{la_tot}</span></div>'
      f'<div class="k">Latin pages read</div><div class="note">every page against its plate</div></div>')
    A(f'<div class="stat"><div class="n">{notes_ct}</div>'
      f'<div class="k">Sumner notes</div><div class="note">{la_notes_ct} of them in the Latin volume</div></div>')
    A(f'<div class="stat"><div class="n">{len(suspects)}</div>'
      f'<div class="k">extents unresolved</div><div class="note">'
      + (", ".join(f"I.{c['ch']}" for c in suspects) if suspects else "none outstanding")
      + '</div></div>')
    A('</div>')

    # ---- per-book progress
    for b in (2, 1):
        bc = [c for c in chaps if c["book"] == b]
        d = [c for c in bc if c in done_all]
        s = [c for c in bc if c["flag"] == "suspect" and not c["done"]]
        A('<div class="bookbar">')
        A(f'<h2>Liber {"Primus" if b==1 else "Secundus"} '
          f'<span class="t">{BOOK_TITLES[b]}</span> '
          f'<span style="margin-left:auto;color:var(--ink-3);font-weight:400">'
          f'{len(d)} of {len(bc)}</span></h2>')
        A('<div class="track">')
        pa = [c for c in bc if c["done"] and c not in d]
        w = len(bc) - len(d) - len(s) - len(pa)
        for n, col in ((len(d), "var(--ok)"), (len(pa), "var(--work)"),
                       (len(s), "var(--flag)"), (w, "transparent")):
            if n:
                A(f'<i style="width:{100*n/len(bc)}%;background:{col}"></i>')
        A('</div></div>')

    A('<div class="legend">'
      '<span><i class="dot" style="background:var(--ok)"></i><b>verified</b> — both layers, plate-confirmed</span>'
      '<span><i class="dot" style="background:var(--flag)"></i><b>suspect extent</b> — boundary unresolved</span>'
      '<span><i class="dot" style="background:var(--idle-soft);border:1px solid var(--rule)"></i><b>not started</b></span>'
      '</div>')
    return o, chaps, nxt, done_all


def register(o, chaps, nxt):
    A = o.append
    for b in (2, 1):
        bc = [c for c in chaps if c["book"] == b]
        A('<section>')
        A('<div class="sechead"><h2>Liber ' + ("Primus" if b == 1 else "Secundus")
          + ' <span style="color:var(--ink-3);font-weight:400">— '
          + f'{len(bc)} chapters, La {bc[0]["la_start"]}–'
          + f'{bc[-1]["la_start"]+bc[-1]["la_pp"]-1}</span></h2>'
          '<div class="meta">¶ counts are Latin → English; the ratio is English pages ÷ Latin pages</div></div>')
        A('<div class="tablewrap"><table><thead><tr>'
          '<th>Ch.</th><th>Title</th><th>Latin</th><th>English</th>'
          '<th class="r">¶ → ¶</th><th class="r">ratio</th><th>Sumner notes</th><th class="r">state</th>'
          '</tr></thead><tbody>')
        for c in bc:
            label, cls, stripe = status_of(c, c["done"])
            k = c["k"]
            is_next = nxt is not None and c is nxt
            A(f'<tr class="{"next" if is_next else ""}">')
            A(f'<td class="ch" style="--stripe:{stripe}"><span class="mono">'
              f'{"I" if b==1 else "II"}.{c["ch"]}</span></td>')
            A('<td class="title">' + esc(c["title_la"])
              + (f'<span class="en">{esc(k["title_en"])}</span>' if k and k["title_en"] else "")
              + '</td>')
            A(f'<td class="num">{c["la_start"]}–{c["la_start"]+c["la_pp"]-1}'
              f'<span style="opacity:.6"> · {c["la_pp"]}pp</span></td>')
            A(f'<td class="num">{c["en_start"]}–{c["en_start"]+c["en_pp"]-1}'
              f'<span style="opacity:.6"> · {c["en_pp"]}pp</span></td>')
            if k and k["en_par"] == 0 and k["la_par"]:
                A(f'<td class="r ratio">{k["la_par"]} → <span style="color:var(--work)">owed</span></td>')
            elif k:
                same = k["la_par"] == k["en_par"]
                A(f'<td class="r ratio">{k["la_par"]} → {k["en_par"]}'
                  + ('<span style="color:var(--ok)"> ≡</span>' if same else '')
                  + '</td>')
            else:
                A('<td class="r ratio" style="color:var(--ink-3)">—</td>')
            r = c["en_pp"] / c["la_pp"]
            warn = "" if 1.05 <= r <= 1.85 else " warn"
            A(f'<td class="r ratio{warn}">{r:.2f}</td>')
            if k and k["en_par"] == 0:
                A('<td class="notes"><span style="color:var(--work)">owed</span>'
                  + (f'<span class="la-note">La {", ".join(k["la_notes"])}</span>' if k["la_notes"] else "")
                  + '</td>')
            elif k:
                if k["notes"]:
                    A('<td class="notes">' + " · ".join(k["notes"])
                      + (f'<span class="la-note" title="Latin-volume note">La {", ".join(k["la_notes"])}</span>'
                         if k["la_notes"] else "") + '</td>')
                else:
                    A('<td class="notes"><span class="none">none — number passes through</span>'
                      + (f'<span class="la-note">La {", ".join(k["la_notes"])}</span>' if k["la_notes"] else "")
                      + '</td>')
            else:
                A('<td class="notes" style="color:var(--ink-3)">—</td>')
            A(f'<td class="r"><span class="chip {cls}">{label}</span></td></tr>')
        A('</tbody></table></div></section>')


def ribbon(o, chaps, done_all):
    """The 1–9 footnote cycle, the project's checksum, drawn as it actually runs."""
    A = o.append
    seq, marks = [], []
    for c in sorted(done_all, key=lambda c: (c["book"], c["ch"])):
        for n in c["k"]["notes"]:
            seq.append((n, f'{"I" if c["book"]==1 else "II"}.{c["ch"]}'))
    A('<section><div class="sechead"><h2>The footnote cycle</h2>'
      '<div class="meta">Sumner numbers his notes 1–9 and wraps; a break means a note was missed</div></div>')
    A('<div class="ribbon">')
    A('<div style="font-size:12.5px;color:var(--ink-2);max-width:66ch">'
      'The run begins in Sumner\'s own preface (English pp. 1–8 carry notes 1–8), passes through '
      'Book I, and continues into Book II — one unbroken cycle across the whole volume. '
      'Every number below was predicted from its predecessor before the plate was read.</div>')
    A('<div class="cyc">')
    for n in "12345678":
        A(f'<span class="on" title="Sumner\'s preface">{n}</span>')
    A('<span class="brk">preface ┊ I.i none ┊</span>')
    for n, where in seq:
        A(f'<span class="on" title="{where}">{esc(n)}</span>')
    A('</div>')
    A('<div style="margin-top:10px;font-size:12px;color:var(--ink-3)">'
      f'{len(seq)} notes transcribed in the treatise text, unbroken. '
      'Book II is closed; Book I is live from I.ii.</div>')
    A('</div></section>')


def items(o):
    A = o.append
    A('<section><div class="sechead"><h2>What is open</h2>'
      '<div class="meta">hand-kept — edit <span class="mono">OPEN_ITEMS</span> in build-status.py</div></div>')
    A('<div class="items">')
    for kind, head, body in OPEN_ITEMS:
        stripe = "var(--flag)" if kind == "blocked" else "var(--work)"
        A(f'<div class="item" style="--stripe:{stripe}"><div>'
          f'<h3>{esc(head)}</h3><p>{esc(body)}</p></div></div>')
    A('</div></section>')


def main():
    o, chaps, nxt, done_all = build()
    register(o, chaps, nxt)
    ribbon(o, chaps, done_all)
    items(o)
    o.append('<footer><span>Source text public domain (Sumner, Cambridge 1825).</span>'
             '<span>Encoding, apparatus and headnotes CC BY-NC 4.0.</span>'
             '<span>Regenerate with <code>./tools/build-status.py</code></span></footer>')
    o.append('</div>')

    page = ('<title>De Doctrina Register</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=EB+Garamond:ital,wght@0,400..700;1,400..600&'
            'family=IBM+Plex+Mono:wght@400;500;600&'
            'family=IBM+Plex+Sans:wght@400;500;600&display=swap">\n'
            f'<style>{CSS}</style>\n' + "\n".join(o))
    if "--check" in sys.argv:
        print(f"{len(done_all)}/{len(chaps)} chapters done; next = "
              + (f'{nxt["book"]}.{nxt["ch"]}' if nxt else "none"))
        return
    out = os.path.join(ROOT, "status.html")
    open(out, "w", encoding="utf-8").write(page)
    print(f"wrote {out}  ({len(page)//1024} KB)  "
          f"{len(done_all)}/{len(chaps)} chapters; next = "
          + (f'{nxt["book"]}.{nxt["ch"]}' if nxt else "none"))


if __name__ == "__main__":
    main()
