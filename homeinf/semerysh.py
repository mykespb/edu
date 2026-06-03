#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-06-03 2026-06-03 1.0
# semerysh.py

# ~ Сделать список из 10 случайных 3-значных чисел.
# ~ Напечатать все семёрышные числа из этого списка.
# ~ "Семёрышным" называется число, если хотя бы одна 3-значная перестановка его цифр
# ~ даёт число, делящееся на 7 без остатка.

from random import randint
from itertools import permutations


def make():
    return [ randint(100, 999) for _ in range(10) ]


def solve(arr):
    return [ x for x in arr if is_sem(x) ]


def is_sem(x):
    # ~ global d
    sx = list(str(x))
    for sn in permutations(sx, 3):
        if sn[0] == '0':
            continue
        n = int("".join(sn))
        if n % 7 == 0:
            # ~ print(n)
            # ~ d.append(n)
            return True
    return False
        

def main():
    # ~ global d
    # ~ d = []
    arr = make()
    sol = solve(arr)
    print(arr, "=>",  sol)
    # ~ print(d)


main()
