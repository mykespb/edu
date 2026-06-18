#!/usr/bin/env python
# myke 2026-06-18 2026-06-18 1.0
# rot-array-shift.py

# ~ Даны 2 (случайных) списка целых чисел.
# ~ Определить, являются ли сдвинутыми по кругу копиями друг друга.
# ~ Если да, указать величину сдвига, или -1, если нет.

from random import randint

# ------------------------- make random ---------------------

def make(size : int = 10) -> tuple[list]:
    """make 2 arrays"""

    l1 = [ randint(-10, 10) for _ in range(size) ]
    randpoint = randint(1, size-1)
    l2 = l1[randpoint:] + l1[:randpoint]
    if randint(0,1):
        l2.reverse()

    return l1, l2

# ~ print(make())

# ------------------------- solve ---------------------

def solve(l1, l2):
    """solve it"""

    if len(l1) != len(l2):
        return -1

    if l1 == l2 == []:
        return 0

    size = len(l1)

    for shift in range(size):
        for pos in range(size):
            if l1[pos] != l2[ (pos+shift) % size ]:
                break
        else:
            return shift

    return -1

# ------------------------- test ---------------------

l1, l2 = make()
how = solve(l1, l2)

print(f"""
first:  {l1}
second: {l2}
result: {how}
""")



# ~ first:  [1, -3, -1, -8, -4, 0, 8, -10, -8, 3]
# ~ second: [0, 8, -10, -8, 3, 1, -3, -1, -8, -4]
# ~ result: True

# ~ first:  [5, -1, -9, -10, 7, 7, 0, -4, 8, 0]
# ~ second: [-10, -9, -1, 5, 0, 8, -4, 0, 7, 7]
# ~ result: False
