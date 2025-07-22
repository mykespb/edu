#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# divide55.py 2025-07-22 2025-07-22 2.0

# divide55.py
# ~ Делимость
# ~ Переставьте цифры 3, 4, 5, 6, чтобы число делилось на 55.
# ~ (Задача со ЛШЮП-2025)

# 1st method

from itertools import permutations

digs = [3, 4, 5, 6]

for p in permutations(digs):
    num = p[0] * 1000  + p[1] * 100 + p[2] * 10 + p[3]
    if num % 55 == 0:
        print(num)


# 2nd method

for p1 in digs:
    for p2 in digs:
        if p1 == p2: continue
        for p3 in digs:
            if p1 == p3 or p2 == p3: continue
            for p4 in digs:
                if p1 == p4 or p2 == p4 or p3 == p4: continue
                num = p1 * 1000 + p2 * 100 + p3 * 10 + p4
                if num % 55 == 0:
                    print(num)


# results:

# ~ 3465
# ~ 6435

# ~ 3465
# ~ 6435
