#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-06-03 2026-06-05 1.2
# semerysh.py

# ~ Сделать список из 10 случайных 3-значных чисел.
# ~ Напечатать все семёрышные числа из этого списка.
# ~ "Семёрышным" называется число, если хотя бы одна перестановка его цифр
# ~ даёт 3-значное число, делящееся на 7 без остатка.

from random import randint
from itertools import permutations


def make():
    return sorted([ randint(100, 999) for _ in range(10) ])


def solve(arr):
    return sorted([ x for x in arr if is_sem(x) ])


def is_sem(x):
    global divs
    sx = list(str(x))
    for sn in permutations(sx):
        if sn[0] == '0':
            continue
        n = int("".join(sn))
        if n % 7 == 0:
            divs[x] = (n, n/7)
            return True
    return False
        

def main():
    global divs
    divs = {}
    # ~ arr = make()
    arr = [123, 226, 343, 350, 356, 378, 602, 647, 715, 893]
    sol = solve(arr)
    print("problem: ", arr, "=>",  sol)
    print("divisors:", divs)


main()


# ~ problem:  [226, 231, 347, 407, 502, 796, 838, 896, 899, 971] => [231, 796, 896, 971]
# ~ divisors: {231: (231, 33.0), 796: (679, 97.0), 896: (896, 128.0), 971: (917, 131.0)}

# ~ https://docs.python.org/3/library/itertools.html#itertools.permutations

https://docs.python.org/3/library/functions.html#int
https://docs.python.org/3/library/stdtypes.html
https://www.w3schools.com/python/ref_func_str.asp
