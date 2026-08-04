#!/bin/bash
# Render page-FOOT crops of the Latin volume for the Book II footnote sweep (§9b).
#
# Crops the bottom 60% of each page at 200 dpi -- enough to catch a note that runs
# high up the page (La 454's fills half of it) while staying small enough that the
# note's own type is still legible when the image is read. Do NOT tile these into
# contact sheets: stacking 4 pages makes a 1496x4680 image that gets downscaled
# past the point where a footnote's superscript number can be read, which is the
# one thing the sweep exists to record.
#
# Usage:
#   ./tools/sweep-feet.sh 387 428          # a printed-page range
#   ./tools/sweep-feet.sh 431 454 447      # or an explicit list of printed pages
#
# Output: raw/plates/foot-la-<printed>.jpg   (raw/ is gitignored and regenerable)
set -euo pipefail

OFFSET=16          # la_pdf = la_printed + 16  (M0, measured)
DPI=200
Y=780              # top of the crop band: 40% down a 1950px page at 200 dpi
H=1170             # to the foot of the page

cd "$(dirname "$0")/.."
mkdir -p raw/plates

if [ "$#" -eq 2 ] && [ "$1" -le "$2" ] 2>/dev/null; then
  PAGES=$(seq "$1" "$2")
else
  PAGES="$*"
fi

n=0
for printed in $PAGES; do
  pdf=$((printed + OFFSET))
  out="raw/plates/foot-la-${printed}"
  pdftoppm -f "$pdf" -l "$pdf" -r "$DPI" -jpeg -y "$Y" -H "$H" raw/la.pdf "$out"
  # pdftoppm appends -<pdfpage>; normalise to a name keyed by PRINTED page, since
  # that is what the ledger and the runbook talk about.
  mv "${out}-${pdf}.jpg" "${out}.jpg"
  n=$((n + 1))
done
echo "rendered $n foot crops -> raw/plates/foot-la-<printed>.jpg"
