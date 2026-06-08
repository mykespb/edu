#!/usr/bin/env python
# myke 2026-06-08 2026-06-08 1.0
# gamma.py

# ~ Простая гамма

# ~ Частота (высота) ноты ля (А) 1 октавы равна 440 Гц.
# ~ Каждая следующая нота больше, а предыдущая - меньше ровно на корень 12 степени из 2.
# ~ Напечатать таблицу отношений между всеми нотами 1 октавы (а также до 2 октавы).

mul = 2**(1/12)

notes = "C C# D D# E F F# G G# A B H C2".split()

freqs = {}
freqs['A'] = 440.

nf = 440.
for note in "C C# D D# E F F# G G#".split()[::-1]:
    freqs[note] = nf / mul
    nf /= mul
nf = 440.
for note in "B H C2".split():
    freqs[note] = nf * mul
    nf *= mul

print("частоты:", freqs, "\n")

print("%12s" % "", end="")
for second in notes:
    print("%-8s" % second, end="")
print()
for first in notes:
    print("%8s" % first, end="")
    for second in notes:
        print("%8.2f" % (freqs[second] / freqs[first]), end="")
    print()        

print()
