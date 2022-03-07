#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-07 2022-03-07 0.1
# list-max.py

# ~ Найти макс и мин в списке (без использования встроенных функций max, min).

import random
spisok = [random.randint(-100, 100) for _ in range(10)]

print("исходный список:", spisok)

amin = amax = spisok[0]

for e in spisok[1:]:
    if e > amax:
        amax = e
    if e < amin:
        amin = e

print("минимум:", amin, ", максимум:", amax)
