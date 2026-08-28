#!/bin/bash
# fetch-jt.sh — pull the Junius–Tremellius Old Testament into raw/jt/ (gitignored, regenerable).
#
# ★ THIS IS THE BIBLE MILTON CITED. CONVENTIONS §3 records that the two 1825 volumes diverge on
# citation digits because Milton cites Junius–Tremellius versification and Sumner adjusts toward
# the KJV. M4-RUNBOOK §6b settled the Ecclesiastes cases from the corpus — by finding per-chapter
# offsets that repeat — and §10.8 asks whether eight more rows in II.xvii's "silently corrected
# error" table are the same thing. That question is not an inference problem. It is a lookup, and
# this is the book to look it up in.
#
# Hanau 1603, typis Wechelianis. 1252 pp. Public domain. The Old Testament only — Tremellius and
# Junius did the OT from the Hebrew; the NT in the same family is Beza's, and Milton's NT
# citations are a separate question this volume does not answer.
#
# ⚠ OCR of 1603 printing: long-s, ligatures, marginal scholia bleeding into the text column, and
# VERSE NUMBERS SET IN THE MARGIN, which is exactly the material OCR loses first. Same rule as the
# Milton volumes (CONVENTIONS §2) and the loci (fetch-loci.sh): a FINDING AID ONLY. Use it to find
# the leaf; read the numbers off the PAGE IMAGE at 300 dpi or better, never off this text.
#
# Page images:  https://archive.org/download/testamentiveteri00trem/page/n<LEAF>.jpg
# ⚠ The leaf offset is NOT calibrated. Calibrate it before citing a page (STRUCTURE.md), and
#   record the calibration there next to the two Sumner volumes'.
set -e
cd "$(dirname "$0")/../raw"
mkdir -p jt && cd jt

id=testamentiveteri00trem
if [ -s jt-ot-1603.txt ]; then
  echo "  have  jt-ot-1603"
else
  curl -sL --max-time 300 -o jt-ot-1603.txt "https://archive.org/download/$id/${id}_djvu.txt"
  [ -s jt-ot-1603.txt ] || { rm -f jt-ot-1603.txt; echo "  FAIL  jt-ot-1603 ($id)"; exit 1; }
  echo "  got   jt-ot-1603  $(du -h jt-ot-1603.txt | cut -f1)  <- $id"
fi
