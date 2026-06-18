#!/usr/bin/env python
# myke 2026-06-18 2026-06-18 1.0
# array-max3.py

# ~ Дан случайный список целых чисел.
# ~ Верно ли, что три самых больших числа в нём находятся рядом?

from random import randint, shuffle

# --------------------- make ---------------------

def make(size : int = 10) -> list[int]:
    """make random array"""

    a = [ randint(-99, 99) for _ in range(size) ]
    a.sort()

    randpoint = randint(1, size-1)
    a = a[randpoint:] + a[:randpoint]

    if randint(0, 1):
        shuffle(a)

    return a


# --------------------- solve ---------------------

# ~ from itertools import permutations

def solve(a : list[int]) -> bool:
    """solve task"""

    m3s = sum(sorted(a)[-3:])

    for pos in range(len(a) - 3):
        if sum(a[pos:pos+3]) == m3s:
            return True

    return False


# --------------------- test ---------------------

a   = make()
res = solve(a)

print(f"""
list:   {a}
result: {res}
""")

# --------------------- end ---------------------
