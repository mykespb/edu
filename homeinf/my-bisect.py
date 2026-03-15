#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-03-15 2026-03-15 1.0
# my-bisect.py

# ~ Проба бинарного поиска в отсортированном массиве. Разными способами.

MIN : int = 1
MAX : int = 1000

from random import randint

# ~ import bisect
# ~ https://docs.python.org/3/library/bisect.html


def allrun(number : int = 10) -> None:
    """run all tests"""

    sizes = 10, 100, 1_000  #, 10_000

    for test_num in range(number):
        for size in sizes:
            arr = [randint(MIN, MAX) for _ in range(size)]
            arr.sort()
            print(f"----------------------------\narray of {len(arr)} elements\n")
            elems = arr[0], arr[1], 1, 2, arr[size // 4 + 1], arr[size // 2], arr[size // 2 + 1], 99, 100, 500
            for elem in elems:
                ok = find(arr, elem)
                print(f"look for {elem} => {ok}")
                

def find1(arr : list[int], elem : int) -> bool:
    """find the element in the array: simple builtin operation `in`"""
    return elem in arr


find = find1

allrun()
