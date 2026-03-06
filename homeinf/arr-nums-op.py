#!/usr/bin/env python
# arr-nums-op.py
# (C) Mikhail Kolodin, 2026
# 2026-03-06 2026-03-06 1.0

# ~ Дан случайный список вида ['9', ' ', '5', '2', '3', ' ', ' ', ' ', '9', '2'].
# ~ Считая это 1 строкой, найти наибольшее натуральное число.


from random import randint


def make(size=10):
    """make array"""

    return [ (str(randint(1, 9)) if randint(0, 9) > 4 else " ") for _ in range(size) ]


def solve(arr):
    """find max int"""

    return max(map(int, "".join(arr) . split() ))
    

def main(size=10):
    """dispatcher"""

    arr = make()
    print("array:", arr)
    print("max int is", solve(arr))


main()
