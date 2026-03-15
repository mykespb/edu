#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-03-15 2026-03-15 2.0
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
                wow = elem in arr
                print(f"look for {elem} => {ok} (really: {wow}, so: {"YES!" if ok == wow else "NEE!"} )")
                

def find1(arr : list[int], elem : int) -> bool:
    """find the element in the array: simple builtin operation `in`"""
    return elem in arr

def find2(arr : list[int], elem : int) -> bool:
    """find the element in the array: bisect"""

    left = 0
    right = len(arr) - 1
    wasmed = -1

    while left <= right:
        med = left + (right - left) // 2
        if med == wasmed:
            break
        curr = arr[med]
        if curr == elem:
            return True
        elif curr < elem:
            left = med
        else:
            right = med
        wasmed = med

    return False


find = find2

allrun()
