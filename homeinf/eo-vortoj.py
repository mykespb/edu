#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-12-25 2021-12-25 1.0
# eo-vortoj.py

# ~ Дан текст на эсперанто, состоящий из существительных,
# ~ прилагательных, производных наречий и глаголов.
# ~ Определить, сколько в тексте каких частей речи.

eo = """
Imagu: homaj estas bonaj, vortoj estas klaraj, domoj estas blankaj.
Kompreneble, birdoj ĉiele flugadas, fiŝoj enakve naĝas.
"""

import string

print("Шаг 0.\n", eo)

eo = eo.lower()
eo = eo.replace("\n", " ")
eox = ""
for c in eo:
    if c in string.ascii_lowercase + " ĉĝĥĵŝŭ":
        eox += c

eo = eox
print("Шаг 1.\n\n", eo)

print("\nШаг 2.\n")

eox = ""
for vorto in eo.split():
    if vorto.endswith("n"):
        vorto = vorto[:-1]
    if vorto.endswith("j"):
        vorto = vorto[:-1]
    eox += " " + vorto
print(eox)

print("\nШаг 3.\n")

nouns = adjs = verbs = prons = 0

for vorto in eox.split():
    if vorto.endswith("o"):
        nouns += 1
    elif vorto.endswith("a"):
        adjs += 1
    elif vorto.endswith("e"):
        prons += 1
    elif vorto.endswith(("i", "s", "u")):
        verbs += 1

print(f"""
Результат:
существительных:  {nouns:3}
прилагательных:   {adjs:3}
наречий:          {prons:3}
глаголов:         {verbs:3}
всего:            {nouns + adjs + prons + verbs :3}
""")
