#!/usr/bin/env python

# 2 arrays merge sort 2022-06-07 2022-06-07 1.0
# merge-sort-1.py (C) M.Kolodin 2022

# ~ simple template for program itself and tester

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
    c = a + b
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
    if mysorter(a, b) == ideal(a, b):
        print("yes, it is correct")
    else:
        print("no, it is wrong")

test()
