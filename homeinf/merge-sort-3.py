#!/usr/bin/env python

# 2 arrays merge sort 2022-06-07 2022-06-09 3.2
# merge-sort-3.py (C) M.Kolodin 2022

# ~ good sorter and autotester

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
    """ideal sorter for comparison"""
    c = a + b
    c.sort()
    print(f"ideal sort:  {c=}")
    return c

# make experiment
def test():
    """tester"""
    a, b = prep_data()
    print(f"{a=}")
    print(f"{b=}")
    if (result := (mysorter(a, b) == ideal(a, b))):
        print("yes, it is correct")
    else:
        print("no, it is wrong")
    print(f"{result=}\n")
    return result

# ~ test()

def autotest(times=10):
    """make automatic tests 'times' times"""

    print(f"\nrunning autotests {times=}\n")

    ok = 0
    for num in range(times):
        print(f"тест номер {num+1}")
        ok += int(test())

    print(f"tested {times=}, result is {ok * 100 / times}%\n")

autotest()
