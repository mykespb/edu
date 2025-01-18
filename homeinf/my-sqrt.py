#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-18 2025-01-18 1.0
# my-sqrt.py

# ~ Корень

# ~ Найти квадратный корень методом половинного деления.

EPS = 1e-8
TIMES = 1_000

from math import isqrt, sqrt

# ------------------------------------
# мой квадратный корень

def mysqrt(x = 1.0):

    if 0 <= x <= 1:
        left, right = 0., 1.
    else:
        left, right = 1., x
    test0 = 1e10
    test = left  + (right - left) / 2

    rept = 0
    while abs(test - test0) > EPS and rept < TIMES:
        rept += 1
        if test*test > x:
            right = test
        else:
            left = test
        test0 = test
        test = left  + (right - left) / 2

    return test

# ------------------------------------
# всё протестировать

def main():
    """всё запускаем и смотрим
    """

    print("""
----------------------------------------------------------------------------------------
number          our sqrt        std sqrt        number          our sqrt        std sqrt
----------------------------------------------------------------------------------------
""")

    for x in range(10):
        x1 = x / 10.
        x2 = x * 10.
        print(f"{x1:10.8f}\t{mysqrt(x1):10.8f}\t{sqrt(x1):10.8f}\t{x2:10.8f}\t{mysqrt(x2):10.8f}\t{sqrt(x2):10.8f}\t")

main()

# ------------------------------------


# ------------------------------------
