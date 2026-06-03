#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-27 2026-06-03 1.1
# summa7.py

# ~ Найти сумму всех 3-значных чисел, сумма цифр которых делится на 7.

raz = summa = 0

for i in range(100, 1000):
    if (i // 100 + i // 10 % 10 + i % 10) % 7 == 0:
        summa += i
        raz += 1

print(f"{raz=}, {summa=}")
