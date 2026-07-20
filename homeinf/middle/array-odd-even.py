#!/usr/bin/env python3
# array-odd-even.py
# (C) Mikhail Kolodin, 2025
# 2025-10-24 2025-10-24 3.0

# ~ Дан список.
# ~ Посчитать суммы чётных (по порядку) элементов, нечётных, найти положительную разность.

from random import randint

def make(size=10):
    """make array"""

    return [ randint(0, 99) for _ in range(size) ]


def solve1(arr):
    """solve the task and return 3 integer numbers"""

    evens = sum( arr[i] for i in range(len(arr)) if i%2 == 0)
    odds  = sum( arr[i] for i in range(len(arr)) if i%2 == 1)
    diff = abs(evens - odds)

    return evens, odds, diff


def solve2(arr):
    """solve the task and return 3 integer numbers"""

    evens = odds = 0

    for i, v in enumerate(arr):
        if i % 2:
            odds += v
        else:
            evens += v

    diff = abs(evens - odds)

    return evens, odds, diff


def main(size=10):
    """dispatcher"""

    arr = make()
    print("array:", arr)
    print("evens, odds, diff are", solve1(arr), solve2(arr))


main()


# ~ array: [65, 1, 30, 54, 10, 47, 96, 76, 25, 45]
# ~ evens, odds, diff are, 226, 223, 3

# ~ array: [48, 42, 43, 26, 22, 73, 88, 85, 10, 34]
# ~ evens, odds, diff are, 211, 260, 49

# ~ array: [19, 4, 64, 38, 39, 6, 18, 91, 88
# ~ evens, odds, diff are, 228, 187, 41
