#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-03 2025-04-04 1.2
# has-double.py

# ~ Проверить, есть ли в данном списке дубли (одинаковые натуральные числа).
# ~ да = есть

from random import randint


def make(leng = 15, diap = 99):
    """make a list"""

    return [ randint(-diap, +diap) for _ in range(leng)]


def check(arr):
    """check array"""

    return len(arr) != len(set(arr))


def runner(times = 1, leng = 15, diap = 99):
    """run maky tests"""

    for test in range(1, times+1):
        arr = make(leng, diap)
        print(f"test {test}: array is {arr}, check is { 'negative positive' .split() [ check(arr) ] }")

runner(5)


# ~ test 1: array is [47, -87, -46, 4, 48, -46, -70, -26, 44, -58, 60, -86, 82, -88, 73], check is positive
# ~ test 2: array is [75, -83, 54, 65, 67, 54, 82, -83, -10, -59, 9, -39, 70, 32, -67], check is positive
# ~ test 3: array is [-32, -55, 55, 14, -27, 55, -46, -26, -6, 64, -41, 10, 66, -3, 94], check is positive
# ~ test 4: array is [-28, -92, -2, 81, 98, 97, 42, 29, -36, -78, -47, -13, 24, 18, 63], check is negative
# ~ test 5: array is [28, 82, -35, -50, 50, 32, 44, -97, 86, 62, -96, -30, 15, 68, 3], check is negative
