#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-10-19 2025-10-19 2.0
# super-seven.py

# ~ Есть список целых чисел.
# ~ Напечатать максимальное, в состав которого входит цифра 7.

from random import randint

MIN, MAX = 10, 99
#MIN, MAX = 100_000, 999_999
# ~ MIN, MAX = 100_000_000, 999_999_999


def make():
    """make list"""

    return [ randint(MIN, MAX) for _ in range(10) ]


def main():
    """run it"""

    m = make()    # normal test
    # ~ m = [1]   # spec bad test
    print("list:", m)

    # version 1
    sub7 = [n for n in m if "7" in str(n)]
    if sub7:
        print("best:", max(sub7))
    else:
        print("alas, no 7s")

    # version 2
    print("лучшее: " + str(max(семёрки)) if (семёрки := [n for n in m if "7" in str(n)]) else "увы, без семёрок")

main()

# ~ list: [37, 30, 50, 75, 85, 31, 74, 15, 91, 50]
# ~ best: 75
# ~ лучшее: 75
