#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-03 2025-04-04 1.1
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
        print(f"test {test}: array is {arr}, check is {check(arr)}")


runner(5)


# ~ test 1: array is [33, -74, 66, 62, 78, -72, -64, -72, 30, -70, 36, -86, -12, 64, 2], check is True
# ~ test 2: array is [17, -13, -38, 17, 56, 77, -45, 60, -17, -83, -35, 47, 54, -40, -93], check is True
# ~ test 3: array is [84, -73, -65, -34, -3, -68, 0, -82, -61, -7, -39, 71, 45, -15, 53], check is False
# ~ test 4: array is [-11, 22, 83, -16, 43, 81, -3, -5, -6, -95, 7, 75, -99, 11, -54], check is False
# ~ test 5: array is [-45, -85, -58, 36, 70, 99, 41, 39, 72, -56, 35, -35, -50, 92, -33], check is False
