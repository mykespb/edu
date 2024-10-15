#!/usr/bin/env python
# Mikhail Kolodin, 2024
# simple-matrix.py
# 2024-10-15 2024-10-15 1.1
# простые задачи по математике

import random
from pprint import pp
import copy

# 0. Печать матрицы

def mprint(a, width=4):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"%{width}d" % a[i][j], end="")
        print()

# ~ a = [random.randint(-99, 99) for _ in range(10)]

# ~ 1. Нахождение НОД по Евклиду

def gcd(a, b):
    """find GCD of a and b"""

    assert type(a) == int
    assert type(b) == int
    assert a > 0
    assert b > 0

    while True:
        if a > b:
            a -= b
        elif a < b:
            b -= a
        else:
            return a

def gcd_tests():
    tests = ((1, 1), (1, 2), (2, 4), (3, 9), (6, 8), (7, 13), (1024, 2048), (6, 4096))

    for test in tests:
        a, b = test
        print(f"GCD of {a} and {b} is {gcd(a,b)}")

# ~ GCD of 1 and 1 is 1
# ~ GCD of 1 and 2 is 1
# ~ GCD of 2 and 4 is 2
# ~ GCD of 3 and 9 is 3
# ~ GCD of 6 and 8 is 2
# ~ GCD of 7 and 13 is 1
# ~ GCD of 1024 and 2048 is 1024
# ~ GCD of 6 and 4096 is 2

gcd_tests()
