#!/usr/bin/env python

# 2025-07-18 2025-07-18 1.0
# random-square.py (C) M.Kolodin 2025

# ~ Дано натуральное число n.
# ~ Заполнить квадрат n x n натуральными числами 1..n^2 в случайном порядке.

from random import randint, shuffle

N = 20       # размер стороны квадрата

def make1(n):
    """1 решение"""

    a = [ i for i in range(1, N*N+1) ]
    shuffle(a)

    s = [ [a.pop() for j in range(N)]  for i in range(N)]
    return s


make = make1

def test():
    """запуск"""

    print(f"\nслучайный квадрат со стороной {N}\n")

    s = make(N)

    for i in range(N):
        for j in range(N):
            print(f"{s[i][j]:4}", end="")
        print()

    print()

test()
