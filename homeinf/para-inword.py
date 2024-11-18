#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-12-04 2021-12-04 1.0
# para-inword.py

# ~ найти в строке все пары слов, одно из которых входит в другое
# ~ и распечатать
# ~ хорошо бы сразу прокрутить несколько примеров
# ~ регистр слов игнорировать

stroki = """ар арка аркан
тара таран тарантул рант
кило килограмм километр метраж кило лог
"""

for frase in stroki.split("\n"):
    frase = frase.strip().lower()
    if not frase:
        continue

    print ("фраза:", frase)

    for one in frase.split():
        for two in frase.split():
            if one != two and one in two:
                print (f"пара:  {one}, {two}")
