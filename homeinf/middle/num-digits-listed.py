#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-08-24 2025-08-24 1.0
# ~ num-digits-listed.py

# ~ Числа с цифрами
# ~ ------------------------------

# ~ Дан набор (случайных) чисел.
# ~ Вывести:
# ~ сколько чисел начинаются на 1, сколько на 2, и т.д., сколько нулей.
# ~ и показать (отсортированные любым способом) списки таких чисел по группам по 1 цифре.


import random
from collections import defaultdict


def make(num = 10):
    """make numbers"""

    nums = [ random.randint(1, 1_000) for _ in range(num) ]
    print("numbers:")
    print(*nums, sep=", ")
    return nums


def solve(nums):
    """print number of numbers by 1st digit"""

    cnt = defaultdict(list)

    for num in nums:
        cnt[ str(num)[0] ] .append(num)

    print("result:")
    for k in sorted(cnt.keys()):
        print(f"1st digit: {k}, number of numbers: {len(cnt[k])}, numbers: ", end="")
        print(*(sorted(cnt[k])), sep=", ")


def main():
    """start it"""

    nums = make(10)
    solve(nums)


main()


# ~ numbers:
# ~ 125, 897, 845, 582, 597, 952, 701, 660, 851, 77
# ~ result:
# ~ 1st digit: 1, number of numbers: 1, numbers: 125
# ~ 1st digit: 5, number of numbers: 2, numbers: 582, 597
# ~ 1st digit: 6, number of numbers: 1, numbers: 660
# ~ 1st digit: 7, number of numbers: 2, numbers: 701, 77
# ~ 1st digit: 8, number of numbers: 3, numbers: 897, 845, 851
# ~ 1st digit: 9, number of numbers: 1, numbers: 952
