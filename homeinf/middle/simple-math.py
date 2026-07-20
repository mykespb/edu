#!/usr/bin/env python
# Mikhail Kolodin, 2024
# simple-matrix.py
# 2024-10-15 2024-10-29 4.0
# простые задачи по математике

import random
from pprint import pp
import copy
import math

ri = random.randint

# ============================================================================
# 0. Создание и печать матрицы
# ============================================================================

def make1dim(elems=3, bottom=0, top=9):
    """создать вектор"""
    
    return [ random.randint(bottom, top) for c in range(elems) ] 

    
def make2dim(rows=3, cols=3, bottom=0, top=9):
    """создать матрицу"""
    
    return [ [ random.randint(bottom, top) for c in range(cols) ] for r in range(rows) ]

    
def mprint(a, width=4):
    """напечатать матрицу"""
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"%{width}d" % a[i][j], end="")
        print()
# ~ a = [random.randint(-99, 99) for _ in range(10)]


# ============================================================================
# ~ 1. Нахождение НОД по Евклиду
# ============================================================================

def gcd1(a, b):
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


def gcd2(a, b):
    """соптимизированный вариант"""
    
    while b:
        a, b = b, a % b
    return a


def gcd_tests():
    tests = ((1, 1), (1, 2), (2, 4), (3, 9), (6, 8), (7, 13), (1024, 2048), (6, 4096))

    for test in tests:
        a, b = test
        print(f"GCD of {a} and {b} is {gcd1(a,b)}, {gcd2(a,b)}, {math.gcd(a,b)}")

# ~ gcd_tests()

# ~ GCD of 1 and 1 is 1, 1, 1
# ~ GCD of 1 and 2 is 1, 1, 1
# ~ GCD of 2 and 4 is 2, 2, 2
# ~ GCD of 3 and 9 is 3, 3, 3
# ~ GCD of 6 and 8 is 2, 2, 2
# ~ GCD of 7 and 13 is 1, 1, 1
# ~ GCD of 1024 and 2048 is 1024, 1024, 1024
# ~ GCD of 6 and 4096 is 2, 2, 2

# ============================================================================
# ~ 2. Простые обмены
# ============================================================================

# ~ Поменять местами значения 2 переменных
# ~ a -> b -> a

a, b = ri(1, 9), ri(1, 9)
print(f"{a=}, {b=}")

a, b = b, a
print(f"{a=}, {b=}")

# ~ Поменять местами значения 3 переменных
# ~ a -> b -> c-> a

a, b, c = ri(1, 9), ri(1, 9), ri(1, 9)
print(f"{a=}, {b=}, {c=}")

a, b, c = c, a, b
print(f"{a=}, {b=}, {c=}")

# ============================================================================
