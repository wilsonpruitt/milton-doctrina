"""Builds the 50-chapter La/En crosswalk table for STRUCTURE.md.
Page numbers are the PRINTED page numbers of the 1825 Sumner editions,
taken from each volume's own table of contents and verified by direct
plate check (pdftotext -f <pdf_page>) at multiple anchors per volume.
Offsets (rock-stable across the whole of each volume, verified 2026-08-03):
  Latin:   pdf_page = printed_page + 16
  English: pdf_page = printed_page + 56
"""

LA_OFFSET = 16
EN_OFFSET = 56

# (chapter_no, latin_title, la_printed_start)
LA_BOOK1 = [
    (1, "Quid sit Doctrina Christiana, quotque ejus partes", 7),
    (2, "De Deo", 10),
    (3, "De Divino Decreto", 22),
    (4, "De Praedestinatione", 31),
    (5, "De Filio Dei", 57),
    (6, "De Spiritu Sancto", 110),
    (7, "De Creatione", 124),
    (8, "De Providentia Dei seu rerum Gubernatione Communi", 140),
    (9, "De Gubernatione Speciali Angelorum", 154),
    (10, "De Gubernatione Speciali Hominis ante lapsum; de Sabbatho et Conjugio", 160),
    (11, "De Lapsu primorum Parentum, et de Peccato", 180),
    (12, "De Poena Peccati", 187),
    (13, "De Morte quae dicitur Corporali", 192),
    (14, "De Hominis Restitutione et Christo Redemptore", 203),
    (15, "De Officio Mediatorio ejusque triplici munere", 214),
    (16, "De Redemptionis Administratione", 221),
    (17, "De Renovatione; ubi et de Vocatione", 234),
    (18, "De Regeneratione", 242),
    (19, "De Resipiscentia", 247),
    (20, "De Fide Salvifica", 253),
    (21, "De Insitione in Christum, ejusque Effectis", 259),
    (22, "De Justificatione", 267),
    (23, "De Adoptione", 276),
    (24, "De Unione et Communione cum Christo ejusque Membris; de Ecclesia Mystica", 280),
    (25, "De Glorificatione Inchoata; de Certitudine Salutis, et Perseverantia", 283),
    (26, "De Manifestatione Foederis Gratiae; ubi et de Lege Dei", 294),
    (27, "De Evangelio et Libertate Christiana", 299),
    (28, "De Sigillatione Foederis Gratiae Externa", 309),
    (29, "De Ecclesia Visibili", 332),
    (30, "De Scriptura Sacra", 342),
    (31, "De Ecclesiis Particularibus", 354),
    (32, "De Disciplina Ecclesiastica", 366),
    (33, "De Glorificatione Perfecta; de secundo Christi Adventu, Resurrectione, Conflagratione", 372),
]
LA_BOOK1_END = 386  # Liber Secundus opens 387

LA_BOOK2 = [
    (1, "De Bonis Operibus", 387),
    (2, "De Bonorum Operum Causis Proximis", 395),
    (3, "De Virtutibus ad Dei Cultum pertinentibus", 404),
    (4, "De Cultu Externo", 413),
    (5, "De Jurejurando et Sorte", 429),
    (6, "De Zelo", 440),
    (7, "De Tempore Cultus divini; ubi de Sabbatho, Die Dominica, et Festis", 446),
    (8, "De Officiis erga Homines praestandis, et quae huc pertinent Virtutes Generales", 455),
    (9, "De Prima Specie Virtutum Specialium quae ad officium pertinent Hominis erga se", 462),
    (10, "De Secunda Specie Virtutum ad officia Hominis erga se pertinentium", 474),
    (11, "De Officiis Hominis erga Proximum, et quae Virtutes eo pertineant", 477),
    (12, "De Virtutibus sive Officiis Specialibus erga Proximum", 487),
    (13, "De Secunda Specie Officiorum Specialium erga Proximum", 492),
    (14, "Adhuc de Secunda Specie Officiorum Specialium erga Proximum", 504),
    (15, "De Officiis erga Proximum Mutuis, et speciatim Privatis", 511),
    (16, "De Altera Specie Officiorum Privatorum", 520),
    (17, "De Officiis Publicis erga Proximum", 524),
]
LA_BOOK2_END = 536  # MEASURED: "TOTIUS OPERIS FINIS" at printed 536 (pdf 552); Index follows ~537

EN_BOOK1 = [
    (1, "Of the Christian Doctrine, and the Number of its Divisions", 9),
    (2, "Of God", 13),
    (3, "Of the Divine Decrees", 30),
    (4, "Of Predestination", 44),
    (5, "Of the Son of God", 81),
    (6, "Of the Holy Spirit", 153),
    (7, "Of the Creation", 172),
    (8, "Of the Providence of God, or of his General Government of the Universe", 199),
    (9, "Of the Special Government of Angels", 217),
    (10, "Of the Special Government of Man before the Fall; Sabbath and Marriage", 226),
    (11, "Of the Fall of our first Parents, and of Sin", 260),
    (12, "Of the Punishment of Sin", 272),
    (13, "Of the Death of the Body", 278),
    (14, "Of Man's Restoration, and of Christ as Redeemer", 294),
    (15, "Of the Functions of the Mediator, and of his threefold Office", 308),
    (16, "Of the Ministry of Redemption", 316),
    (17, "Of Man's Renovation, including his Calling", 332),
    (18, "Of Regeneration", 342),
    (19, "Of Repentance", 347),
    (20, "Of Saving Faith", 353),
    (21, "Of being planted in Christ, and its effects", 360),
    (22, "Of Justification", 369),
    (23, "Of Adoption", 379),
    (24, "Of Union and Fellowship with Christ and His Members; the Mystical Church", 382),
    (25, "Of Imperfect Glorification; Assurance and Final Perseverance", 386),
    (26, "Of the Manifestation of the Covenant of Grace, including the Law of God", 400),
    (27, "Of the Gospel, and of Christian Liberty", 407),
    (28, "Of the External Sealing of the Covenant of Grace", 429),
    (29, "Of the Visible Church", 451),
    (30, "Of the Holy Scriptures", 465),
    (31, "Of Particular Churches", 481),  # OCR-mangled "381" in scan; verify on plate
    (32, "Of Church Discipline", 497),
    (33, "Of Perfect Glorification; Second Advent, Resurrection, General Conflagration", 505),
]
EN_BOOK1_END = 526  # Book II opens 527

EN_BOOK2 = [
    (1, "Of Good Works", 527),
    (2, "Of the Proximate Causes of Good Works", 537),
    (3, "Of the Virtues belonging to the Service of God", 547),
    (4, "Of External Service", 557),
    (5, "Of Oaths and the Lot", 579),
    (6, "Of Zeal", 598),  # OCR-mangled "59S" in scan; verify on plate
    (7, "Of the Time for Divine Worship; Sabbath, Lord's Day, Festivals", 600),
    (8, "Of our Duties towards Man, and the general Virtues belonging thereto", 613),
    (9, "Of the first Class of Special Virtues re: Duty of Man towards himself", 621),
    (10, "Of the second Class of Virtues re: Duty of Man towards himself", 636),  # OCR "6*36"
    (11, "Of the Duties of Man towards his Neighbour, and the Virtues therein", 639),
    (12, "Of the Special Virtues or Duties which regard our Neighbour", 650),
    (13, "Of the second Class of Special Duties towards our Neighbour", 655),
    (14, "The second Class of Special Duties towards our Neighbour, continued", 672),
    (15, "Of the Reciprocal Duties of Man towards his Neighbour; Private Duties", 680),
    (16, "Of the remaining Class of Private Duties", 691),  # OCR "69J"
    (17, "Of Public Duties towards our Neighbour", 696),
]
EN_BOOK2_END = 711  # MEASURED: "THE END." at printed 711 (pdf 767); Addenda et Corrigenda follows immediately


def sizes(rows, end):
    out = []
    for i, (n, title, p) in enumerate(rows):
        nxt = rows[i + 1][2] if i + 1 < len(rows) else end
        out.append((n, title, p, nxt - p))
    return out


def report(label, la_rows, la_end, en_rows, en_end):
    la = sizes(la_rows, la_end)
    en = sizes(en_rows, en_end)
    print(f"\n## {label}\n")
    print(f"| Ch | La p. (pdf) | La pp | En p. (pdf) | En pp | Title (La) |")
    print(f"|---|---|---|---|---|---|")
    for (n, lt, lp, lsz), (_, et, ep, esz) in zip(la, en):
        print(f"| {n} | {lp} ({lp+LA_OFFSET}) | {lsz} | {ep} ({ep+EN_OFFSET}) | {esz} | {lt} |")


if __name__ == "__main__":
    report("Liber I / Book I — De Cognitione Dei / Of the Knowledge of God", LA_BOOK1, LA_BOOK1_END, EN_BOOK1, EN_BOOK1_END)
    report("Liber II / Book II — De Dei Cultu / Of the Service of God", LA_BOOK2, LA_BOOK2_END, EN_BOOK2, EN_BOOK2_END)
