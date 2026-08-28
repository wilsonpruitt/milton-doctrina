#!/bin/bash
# prep-chapter.sh — stage the mechanical inputs for one DDC chapter.
#
# Renders both plate sets at 200 dpi and both pdftotext drafts, so a transcription
# session spends its (expensive) tokens on reading plates, not on shell setup.
# Costs no model tokens. Safe to re-run: pdftoppm overwrites in place.
#
#   ./tools/prep-chapter.sh 2 3        # Book II, chapter 3
#   ./tools/prep-chapter.sh 2 3 2 9    # a range: Book II chapters 3 through 9
#
# Offsets (measured at M0, do not guess): la_pdf = printed + 16 · en_pdf = printed + 56
# Renders ONE page past the computed chapter end on both layers, so the chapter
# boundary can be confirmed off the plate rather than trusted from the crosswalk.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RAW="$ROOT/raw"
TSV="$ROOT/tools/chapters.tsv"
LA_OFFSET=16
EN_OFFSET=56

[ -f "$RAW/la.pdf" ] || { echo "FATAL: $RAW/la.pdf missing (raw/ is gitignored — re-fetch)"; exit 1; }
[ -f "$RAW/en.pdf" ] || { echo "FATAL: $RAW/en.pdf missing (raw/ is gitignored — re-fetch)"; exit 1; }
mkdir -p "$RAW/plates"

prep_one() {
  local book="$1" ch="$2"
  local row
  row=$(awk -F'\t' -v b="$book" -v c="$ch" '!/^#/ && $1==b && $2==c {print; exit}' "$TSV")
  [ -n "$row" ] || { echo "FATAL: no row for book $book chapter $ch in chapters.tsv"; exit 1; }

  local la_start la_pp en_start en_pp flag title
  la_start=$(echo "$row" | cut -f3); la_pp=$(echo "$row" | cut -f4)
  en_start=$(echo "$row" | cut -f5); en_pp=$(echo "$row" | cut -f6)
  flag=$(echo "$row" | cut -f7);     title=$(echo "$row" | cut -f8)

  # +1 page past the end on each layer, to confirm the boundary off the plate.
  local la_f=$((la_start + LA_OFFSET))
  local la_l=$((la_start + LA_OFFSET + la_pp))
  local en_f=$((en_start + EN_OFFSET))
  local en_l=$((en_start + EN_OFFSET + en_pp))

  local tag
  tag=$(printf "%d-%02d" "$book" "$ch")

  echo "=== ddc-$tag  $title"
  echo "    La printed $la_start-$((la_start + la_pp - 1))  (pdf $la_f-$((la_l - 1)), +1 = $la_l)"
  echo "    En printed $en_start-$((en_start + en_pp - 1))  (pdf $en_f-$((en_l - 1)), +1 = $en_l)"
  if [ "$flag" = "suspect" ]; then
    echo "    !!  EXTENT FLAGGED 'suspect' — confirm the chapter boundary off the plate"
    echo "    !!  BEFORE transcribing, and correct chapters.tsv when you do."
  fi

  # Render one page at a time and name the file by PRINTED page, matching
  # sweep-feet.sh and every ledger, runbook and chunk in the project. Naming these
  # by PDF page (as this script did until 2026-08-04) puts `la-474.jpg` on printed
  # 458 and invites transcribing the wrong sixteen pages.
  # ⚠ pdftoppm ZERO-PADS its output filename to the width of the PDF's page count,
  # so page 23 of a 572-page scan is written `la-7-023.jpg`, not `la-7-23.jpg`.
  # Book II never exposed this (its pdf pages are already 3 digits); every Book I
  # chapter does. Do not reconstruct the produced name — glob for it.
  render_one() {
    local pdf="$1" out="$2" printed="$3" src="$4"
    rm -f "$out"-*.jpg                       # clear stale renders before globbing
    pdftoppm -jpeg -r 200 -f "$pdf" -l "$pdf" "$src" "$out"
    local produced
    produced=$(ls "$out"-*.jpg 2>/dev/null | head -1)
    [ -n "$produced" ] || { echo "FATAL: pdftoppm produced nothing for printed $printed (pdf $pdf)"; exit 1; }
    mv "$produced" "$out.jpg"
  }

  local p pdf
  for ((p = la_start; p <= la_start + la_pp; p++)); do
    pdf=$((p + LA_OFFSET)); render_one "$pdf" "$RAW/plates/la-$p" "$p" "$RAW/la.pdf"
  done
  for ((p = en_start; p <= en_start + en_pp; p++)); do
    pdf=$((p + EN_OFFSET)); render_one "$pdf" "$RAW/plates/en-$p" "$p" "$RAW/en.pdf"
  done
  pdftotext -f "$la_f" -l "$la_l" -layout "$RAW/la.pdf" "$RAW/la-ch$tag.txt"
  pdftotext -f "$en_f" -l "$en_l" -layout "$RAW/en.pdf" "$RAW/en-ch$tag.txt"

  echo "    plates: raw/plates/la-{$la_start..$((la_start + la_pp))}.jpg  raw/plates/en-{$en_start..$((en_start + en_pp))}.jpg  (PRINTED pages)"
  echo "    drafts: raw/la-ch$tag.txt  raw/en-ch$tag.txt"
  echo
}

if [ $# -eq 2 ]; then
  prep_one "$1" "$2"
elif [ $# -eq 4 ]; then
  b1="$1"; c1="$2"; b2="$3"; c2="$4"
  [ "$b1" = "$b2" ] || { echo "FATAL: range must stay within one book"; exit 1; }
  for ((c = c1; c <= c2; c++)); do prep_one "$b1" "$c"; done
else
  echo "usage: $0 <book> <chapter>"
  echo "       $0 <book> <from-ch> <book> <to-ch>"
  exit 1
fi

echo "Disk used by plates: $(du -sh "$RAW/plates" | cut -f1)"
