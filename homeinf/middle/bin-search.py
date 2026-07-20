#!/usr/bin/env python
# Mikhail Kolodin, 2024
# bin-search.py
# 2024-10-11 2024-10-11 1.0
# binary search in array

import random

def search(a, val):
    """search for val in a"""

    size = len(a)
    left = 0
    right = size - 1

    while right - left > 1:
        center = left + (right - left) // 2
        if val == a[center]:
            return True
        elif val < a[center]:
            right = center
        else:
            left = center

    return a[left] == val or a[right] == val


def make(size=10, diap=10):
    """ make random list[size] with values +-diap, perform search for random val"""

    a = sorted([ random.randint(-diap, diap) for _ in range(size) ])
    v = random.randint(-diap, diap) 

    print(f"searching in {a} for {v} is", search(a, v))


def tests(num=10):
    """make num tests"""

    for test in range(num):
        print("test", test, ":")
        make()


tests()

# ~ test 0 :
# ~ searching in [-9, -8, -5, -5, -2, -1, -1, 1, 5, 8] for -4 is False
# ~ test 1 :
# ~ searching in [-10, -9, -9, -7, -4, 2, 3, 4, 4, 9] for -9 is True
# ~ test 2 :
# ~ searching in [-9, -9, -4, 0, 0, 3, 4, 6, 6, 9] for 3 is True
# ~ test 3 :
# ~ searching in [-10, -10, -8, -8, -7, -4, -2, 8, 9, 10] for -7 is True
# ~ test 4 :
# ~ searching in [-7, -7, -6, -5, -2, 1, 5, 6, 6, 8] for -4 is False
# ~ test 5 :
# ~ searching in [-8, -6, -6, -4, -1, 0, 0, 1, 6, 7] for 9 is False
# ~ test 6 :
# ~ searching in [-10, -8, -7, -6, -3, -1, 0, 1, 2, 9] for -5 is False
# ~ test 7 :
# ~ searching in [-10, -6, -4, -1, 1, 3, 4, 5, 9, 10] for -1 is True
# ~ test 8 :
# ~ searching in [-9, -8, -5, -5, -1, 0, 1, 4, 5, 10] for 3 is False
# ~ test 9 :
# ~ searching in [-8, -7, -5, -3, 0, 0, 2, 3, 3, 5] for 5 is True

