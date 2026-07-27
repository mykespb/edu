#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-08-24 2025-08-24 1.0
# ~ num-digits.py

# ~ Числа с цифрами
# ~ ------------------------------

# ~ Дан набор (случайных) чисел.
# ~ Вывести:
# ~ сколько чисел начинаются на 1, сколько на 2, и т.д., сколько нулей.


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

    cnt = defaultdict(int)

    for num in nums:
        cnt[ str(num)[0] ] += 1

    print("result:")
    for k in sorted(cnt.keys()):
        print(f"1st digit: {k}, number of numbers: {cnt[k]}")


def main():
    """start it"""

    nums = make(10)
    solve(nums)


main()


# ~ numbers:
# ~ 161, 507, 427, 391, 285, 6, 329, 999, 103, 649
# ~ result:
# ~ 1st digit: 1, number of numbers: 2
# ~ 1st digit: 2, number of numbers: 1
# ~ 1st digit: 3, number of numbers: 2
# ~ 1st digit: 4, number of numbers: 1
# ~ 1st digit: 5, number of numbers: 1
# ~ 1st digit: 6, number of numbers: 2
# ~ 1st digit: 9, number of numbers: 1
