#!/usr/bin/env python3
"""Insert stdin verbatim before a unique marker line in a chunk file.

Guards CONVENTIONS/M3-RUNBOOK §10's rule that every string replace assert a
match count of 1, so a paragraph can never be spliced into the wrong place
(e.g. into the chunk's own ## Notes, which quotes the apparatus).
"""
import io, sys
path, marker = sys.argv[1], sys.argv[2]
body = sys.stdin.read().rstrip('\n')
s = io.open(path, encoding='utf-8').read()
n = s.count(marker)
if n != 1:
    sys.exit('ERROR: marker %r occurs %d times in %s (need exactly 1)' % (marker, n, path))
s = s.replace(marker, body + '\n\n' + marker)
io.open(path, 'w', encoding='utf-8').write(s)
print('ok: %d chars inserted before %s' % (len(body), marker))
