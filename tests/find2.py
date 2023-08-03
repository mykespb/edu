#!/usr/bin/env python
# find2.py 2023-08-03 2023-08-03 2.0
# (C) Mikhail Kolodin, 2023

# A list of integers is  given.
# One and only one number occurs there exactly 1 time, others occur 2 times.
# Find that sole number.

# -------------------- functions --------------------

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


# -------------------- simple test  --------------------

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

# -------------------- time test  --------------------

import time

# how many times to run
TIMES = 100

# data
LENGTH = 1000
data = [i for i in range(LENGTH)]
data = data + [LENGTH] + list(reversed(data))

# functions
funcs = find1, find2, find3, find4, find5, find6

# prepare and run test

def tester(func):
    """test 1 function TIMES times"""

    res= []
    for rept in range(TIMES):
        start = time.time()
        _ = func(data)
        duration = time.time() - start
        res.append(duration)

    return sum(res) / len(res)


def testall():
    """test all functions"""

    print(f"\nTesting all functions {TIMES=} and {LENGTH=}.")

    for func in funcs:
        print(f"function {func.__name__} : {tester(func)}")

testall()

# Testing all functions TIMES=100 and LENGTH=100.
# function find1 : 7.3170661926269534e-06
# function find2 : 1.3375282287597657e-05
# function find3 : 3.0469894409179686e-06
# function find4 : 7.941722869873047e-06
# function find5 : 8.04424285888672e-06
# function find6 : 7.762908935546876e-06

# Testing all functions TIMES=100 and LENGTH=1000.
# function find1 : 7.423877716064453e-05
# function find2 : 0.0001326751708984375
# function find3 : 3.721475601196289e-05
# function find4 : 8.836030960083008e-05
# function find5 : 6.613492965698242e-05
# function find6 : 6.479263305664062e-05

# Testing all functions TIMES=100 and LENGTH=10000.
# function find1 : 0.0007916474342346191
# function find2 : 0.0012323784828186036
# function find3 : 0.00039081335067749025
# function find4 : 0.0009427404403686523
# function find5 : 0.0006291747093200683
# function find6 : 0.0006306266784667969

# Testing all functions TIMES=100 and LENGTH=100000.
# function find1 : 0.006879312992095947
# function find2 : 0.012329652309417724
# function find3 : 0.0037445926666259764
# function find4 : 0.008820950984954834
# function find5 : 0.006835203170776367
# function find6 : 0.0069159364700317385

# the end.
