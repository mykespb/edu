#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-03 2025-04-03 1.0
# has-double.py

# ~ Проверить, есть ли в данном списке дубли (одинаковые натуральные числа).

from random import randint


def make(leng = 15, diap = 99):
    """make a list"""

    return [ randint(-diap, +diap) for _ in range(leng)]


def check(arr):
    """check array"""

    return len(arr) == len(set(arr))


def runner(times = 1, leng = 15, diap = 99):
    """run maky tests"""

    for test in range(1, times+1):
        arr = make(leng, diap)
        print(f"test {test}: array is {arr}, check is {check(arr)}")


runner(5)


# ~ test 1: array is [88, 90, 98, -85, 92, 32, -38, -59, -6, -98, 92, 92, 38, -80, -8], check is False
# ~ test 2: array is [-8, -56, -23, -32, -78, -85, -51, 70, 70, -19, -8, 23, 6, -16, -48], check is False
# ~ test 3: array is [26, -50, -47, 23, -72, 59, 7, 39, -1, 75, -41, 54, -12, 13, -89], check is True
# ~ test 4: array is [-35, 89, 2, -49, 32, 27, -74, -99, 73, -48, 48, -85, -9, -12, -64], check is True
# ~ test 5: array is [-97, -32, -56, 66, -74, -50, -4, 3, -69, -21, 0, 70, -34, -4, -43], check is False
