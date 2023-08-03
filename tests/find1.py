#!/usr/bin/env python
# find1.py 2023-08-03 2023-08-03 3.0
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
    """find 1, ver.2"""

    res = 0    
    for n in arr:
        res ^= n

    return res


def test(arr: list[int]) -> int:
    """run 1 test"""

    print(f"{arr=} -> {find1(arr)}")
    print(f"{arr=} -> {find2(arr)}")
    print(f"{arr=} -> {find3(arr)}")

test([1, 2, 2, 8, 1, 8, 3, 4, 4])
test([1])

# arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# arr=[1, 2, 2, 8, 1, 8, 3, 4, 4] -> 3
# arr=[1] -> 1
# arr=[1] -> 1
# arr=[1] -> 1