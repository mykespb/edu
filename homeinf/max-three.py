#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2025-10-01 2025-10-01 1.1
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
    assert size > 2
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

    lst = [ x for xss in arr for xs in xss for x in xs ]
    lst.sort(reverse=True)
    return lst[:3]
    

cube = make()
pp(cube)

# ~ find = find2
vals1 = find1(cube)
vals2 = find2(cube)
print(f"max values: {vals1=}, {vals2=}")


# ~ [[[39, 66, -83], [-76, 31, 33], [64, 12, -92]],
 # ~ [[-90, -49, -23], [-83, -53, -53], [-1, 37, -55]],
 # ~ [[80, -49, -58], [-39, 28, 47], [-75, 51, 18]]]
# ~ max values= vals1=[80, 66, 64], vals2=[80, 66, 64]
