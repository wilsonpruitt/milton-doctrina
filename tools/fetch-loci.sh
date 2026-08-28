#!/bin/bash
# fetch-loci.sh — pull the Wolleb and Ames compendia into raw/loci/ (gitignored, regenerable).
#
# PLAN §6.2: DDC's skeleton follows the Reformed scholastic loci tradition, and specifically
# these two. Milton's originality is visible as DEVIATION from a template he is otherwise
# following, so the loci panel needs both the Latin Milton would have known and the period
# English a reader can check.
#
# ⚠ These are OCR of 17th-century printing: long-s, broken sorts, heavy noise. Same rule as
# the Milton volumes (CONVENTIONS §2) — a FINDING AID ONLY. Use them to locate a locus and to
# read structure and sequence. §6.2's warning stands: assert a verbal dependence only where you
# have checked both texts at the page image, never off this OCR.
#
# Page images, when a claim needs one:  https://archive.org/download/<id>/page/n<LEAF>.jpg
# Leaf offsets are NOT calibrated for these four — calibrate before citing a page (STRUCTURE.md).
set -e
cd "$(dirname "$0")/../raw"
mkdir -p loci && cd loci

fetch () {  # fetch <local-name> <archive-identifier>
  local n=$1 id=$2
  [ -s "$n.txt" ] && { echo "  have  $n"; return; }
  curl -sL --max-time 120 -o "$n.txt" "https://archive.org/download/$id/${id}_djvu.txt"
  [ -s "$n.txt" ] || { rm -f "$n.txt"; echo "  FAIL  $n  ($id)"; return 1; }
  echo "  got   $n  $(du -h "$n.txt" | cut -f1)  <- $id"
}

echo "Wolleb, Compendium Theologiae Christianae"
fetch wolleb-la-1657 bim_early-english-books-1641-1700_compendium-theologi-chr_wolleb-johann_1657
fetch wolleb-en-1660 abridgmentofchri00woll        # Ross's English; §6.2 names the 1650, this is a later printing
echo "Ames, Medulla Theologica / The Marrow of Sacred Divinity"
fetch ames-la-1656   guilielamesiimed00ames
fetch ames-en-1639   marrowsacdi00ames             # §6.2 names the 1642; the 1639 is the same translation
echo "done — raw/loci/"
