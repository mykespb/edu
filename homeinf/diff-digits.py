#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-10-17 2025-10-17 1.2
# diff-digits.py

# ~ Есть список чисел.
# ~ Показать те, которые состоят из макс. количества разных цифр.

from random import randint

MIN, MAX = 100_000, 999_999
# ~ MIN, MAX = 10, 99
# ~ MIN, MAX = 100_000_000, 999_999_999


def make():
    """make list"""

    return [ randint(MIN, MAX) for _ in range(10) ]


def main():
    """run it"""

    m = make()
    print("list:", m)

    m = [( len( set( str(x) ) ) ,x ) for x in m]
    m.sort(reverse=True)

    dmax = m[0][0]
    print(f"max different digits: {dmax}")

    best = sorted([x[1] for x in m if x[0] == dmax])
    print("diff:", best)


main()


# ~ list: [501181, 325714, 785733, 593792, 659379, 443117, 319477, 107306, 430031, 604919]
# ~ max different digits: 6
# ~ diff: [325714]

# ~ list: [887936, 285015, 827387, 124047, 333995, 357703, 978958, 870032, 635269, 505193]
# ~ max different digits: 5
# ~ diff: [124047, 285015, 505193, 635269, 870032, 887936]
