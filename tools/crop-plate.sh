#!/bin/bash
# crop-plate.sh <la|en> <printed-page> <dpi> <y0-fraction> <y1-fraction> <name>
#
# Renders one printed page at an arbitrary dpi and saves a full-width horizontal
# band of it to raw/crops/<name>.jpg. This is the tool for CONVENTIONS §2's
# "doubtful characters get a 400 dpi crop" — 600 dpi settles citation digits,
# 900 dpi settles a single wrong sort (En 639's `justiee`).
#
# The y-fractions are of the whole page height; eyeball them off the 200 dpi
# plate in raw/plates/ first. Offsets are M0's, measured and exact.
#
#   ./tools/crop-plate.sh la 482 600 0.50 0.64 la482-prov
#   ./tools/crop-plate.sh en 639 900 0.42 0.48 en639-justice
#
# raw/ is gitignored and everything here is regenerable; don't commit the output.
set -e
V=$1; P=$2; DPI=$3; Y0=$4; Y1=$5; N=$6
if [ $# -ne 6 ]; then sed -n '2,3p' "$0"; exit 1; fi
cd "$(dirname "$0")/../raw"
mkdir -p crops
case "$V" in
  la) PDF=la.pdf; PG=$((P+16)) ;;   # la_pdf = la_printed + 16
  en) PDF=en.pdf; PG=$((P+56)) ;;   # en_pdf = en_printed + 56
  *)  echo "first argument must be la or en"; exit 1 ;;
esac
pdftoppm -jpeg -r "$DPI" -f "$PG" -l "$PG" "$PDF" "crops/.full-$N"
F=$(ls crops/.full-$N-*.jpg | head -1)
python3 - "$F" "$Y0" "$Y1" "crops/$N.jpg" <<'PY'
import sys
from PIL import Image
f, y0, y1, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
im = Image.open(f); w, h = im.size
im.crop((0, int(h * y0), w, int(h * y1))).save(out, quality=92)
print(out, Image.open(out).size)
PY
rm -f crops/.full-$N-*.jpg
