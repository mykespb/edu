#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-27 2026-04-27 1.0
# summa7.py

# ~ Найти сумму всех 3-значных чисел, сумма цифр которых делится на 7.

from itertools import permutations

digits = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

summa = 0

for a, b, c in permutations(digits, 3):
    
    if a and (a + b + c) % 7 == 0:
        summa += a*100 + b*10 + c

print(f"{summa=}")
