#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2025-10-01 2025-10-01 0ю1
# max-three.py

# ~ Есть 3-мерный массив (куб) целых чисел.
# ~ Найти 3 максимальных и напечатать их в порядке убывания.


from random import randint
from pprint import pp, pprint

# parameters
min_val = -100
max_val = 100


def make(size = 3):
    """create integer cube"""
    return [[[ randint(min_val, max_val) for _ in range(size) ] for _ in range(size) ] for _ in range(size) ]


def find1(arr):
    """find 3 max numbers, ver.1"""

    size = len(arr)
    mv = []
    
    for i1 in range(size):
        for i2 in range(size):
            for i3 in range(size):
                cur = arr[i1][i2][i3]
                mv.append(cur)
                mv.sort(reverse=True)
                mv = mv[:3]                    

    return mv


def find2(arr):
    """find 3 max numbers, ver.2"""

    size = len(arr)
    mv = []
    

find = find1

cube = make()
pp(cube)

vals = find(cube)
print(f"max values= {vals}")
