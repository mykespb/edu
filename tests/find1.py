#!/usr/bin/env python
# find1.py 2023-08-03 2023-08-03 7.0
# (C) Mikhail Kolodin, 2023

# Дан список целых чисел.
# Найти в нём число, которое встречается 1 раз (остальные - по 2 раза; всё честно).

def find1(arr: list[int]) -> int:
    """find 1, ver.1"""
    times = set()

    for n in arr:
        if n in times:
            times.remove(n)
        else:
            times.add(n)

    return times.pop()


def find2(arr: list[int]) -> int:
    """find 1, ver.2"""
    times = set()
    
    for n in arr:
        times ^= {n}

    return times.pop()


def find3(arr: list[int]) -> int:
    """find 1, ver.3"""

    res = 0    
    for n in arr:
        res ^= n

    return res


from functools import reduce

def find4(arr: list[int]) -> int:
    """find 1, ver.4"""

    return reduce(lambda x, y: x^y, arr)


from collections import Counter

def find5(arr: list[int]) -> int:
    """find 1, ver.5"""

    cnt = Counter(arr)
    ones = [k for k, v in cnt.items() if v == 1]   # slower

    return ones[0]


def find6(arr: list[int]) -> int:
    """find 1, ver.5"""

    cnt = Counter(arr)
    for k, v in cnt.items():
        if v == 1:
            return k     # faster


def test(arr: list[int]) -> int:
    """run 1 test"""

    print(f"ver.1: {arr=} -> {find1(arr)}")
    print(f"ver.2: {arr=} -> {find2(arr)}")
    print(f"ver.3: {arr=} -> {find3(arr)}")
    print(f"ver.4: {arr=} -> {find4(arr)}")
    print(f"ver.5: {arr=} -> {find5(arr)}")
    print(f"ver.6: {arr=} -> {find6(arr)}")

test([1, 2, 2, 8, 1, 8, 3, 4, 4])
test([1])

# ver.1: arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# ver.2: arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# ver.3: arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# ver.4: arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# ver.5: arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# ver.6: arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# ver.1: arr=[1] -> 1
# ver.2: arr=[1] -> 1
# ver.3: arr=[1] -> 1
# ver.4: arr=[1] -> 1
# ver.5: arr=[1] -> 1
# ver.6: arr=[1] -> 1
