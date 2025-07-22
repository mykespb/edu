#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# divide55.py 2025-07-22 225-07-22 1.0

# numinlists.py
# ~ Делимость
# ~ Переставьте цифры 3, 4, 5, 6, чтобы число делилось на 55.
# ~ (Задача со ЛШЮП-2025)

from itertools import permutations

digs = [3, 4, 5, 6]

for p in permutations(digs):
    num = p[0] * 1000  + p[1] * 100 + p[2] * 10 + p[3]
    if num % 55 == 0:
        print(num)
        break

# 33465
