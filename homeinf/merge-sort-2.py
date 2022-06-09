#!/usr/bin/env python

# 2 arrays merge sort 2022-06-07 2022-06-07 2.0
# merge-sort-2.py (C) M.Kolodin 2022

# ~ ready sorter and manual tester

from random import randint as ri

def prep_data():
    """prepare data"""
    a = [ri(-100, 100) for _ in range(10)]
    b = [ri(-100, 100) for _ in range(10)]
    a.sort()
    b.sort()
    return a, b

# sort it all
def mysorter(a, b):
    """my own sorter"""

    if not a: return b
    if not b: return a

    c = []
    ai = bi = 0
    lena = len(a)
    lenb = len(b)

    while ai < lena and bi < lenb:
        if a[ai] <= b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1

    if ai < lena:
        c += a[ai:]
    elif bi < lenb:
        c += b[bi:]

    print(f"mysorter is: {c=}")
    return c

# ideal sorter
def ideal(a, b):
    """iedeal sorter fro comparison"""
    c = a + b
    c.sort()
    print(f"ideal sort:  {c=}")
    return c

# make experiment
def test():
    a, b = prep_data()
    print(f"{a=}")
    print(f"{b=}")
    if (result := (mysorter(a, b) == ideal(a, b))):
        print("yes, it is correct")
    else:
        print("no, it is wrong")
    print(f"{result=}")
    return result

test()
