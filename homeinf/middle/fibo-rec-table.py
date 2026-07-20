#!/usr/bin/env python
# fibo-rec-table.py (c) Mikhail Kolodin
# 2025-05-12 2025-05-16 2.3
# Числа Фибоначчи рекурсивно -- просто и с декоратором
# и даже со своим (почти настоящим) декоратором

from functools import wraps
from time import time

LIMIT = 36

# -------------------------------------------------

table = [[0, 0] for _ in range(LIMIT+1) ] 

def fib1(n: int) -> int:
    """вычислить n-ое число Фибоначчи"""

    if n < 2:
        return 1

    return fib1(n-2) + fib1(n-1)


def test1(n: int) -> None:
    """посчитать n чисел Фибоначчи"""
    # ~ global table

    for i in range(1, n+1):
        start = time()
        x = fib1(i)
        finish = time()

        table[i][0] = finish - start

test1(LIMIT)

from functools import lru_cache, cache

# ~ @lru_cache
@cache
def fib2(n: int) -> int:
    """вычислить n-ое число Фибоначчи"""

    if n < 2:
        return 1

    return fib2(n-2) + fib2(n-1)


def test2(n: int) -> None:
    """посчитать n чисел Фибоначчи"""
    # ~ global table

    for i in range(1, n+1):
        start = time()
        x = fib2(i)
        finish = time()

        table[i][1] = finish - start

test2(LIMIT)


def show():
    print(f"{'number':6}   {'simple':10} {'lru_cache':10}")
    for i in range(len(table)):
        print(f"{i:6} {table[i][0]:10f} {table[i][1]:10f}")

show()

# -------------------------------------------------

# ~ from functools import cache

# ~ @lru_cache
@cache
def fib3(n: int) -> int:
    """вычислить n-ое число Фибоначчи"""

    if n < 2:
        return 1

    return fib3(n-2) + fib3(n-1)


def test3(n: int) -> None:
    """посчитать n чисел Фибоначчи"""
    # ~ global table

    for i in range(1, n+1):
        start = time()
        x = fib3(i)
        finish = time()
        print(f"fib({i}), время: { finish - start :10f} секунд.")

# ~ test3(LIMIT)

# -------------------------------------------------

def my_lru(fun):
    def wrapper(num):
        if num not in my_lru.cache:
            res = fun(num)
            my_lru.cache[num] = res
        return my_lru.cache[num]
    return wrapper
my_lru.cache = {}


@my_lru
def fib4(n: int) -> int:
    """вычислить n-ое число Фибоначчи"""

    if n < 2:
        return 1

    return fib4(n-2) + fib4(n-1)


def test4(n: int) -> None:
    """посчитать n чисел Фибоначчи"""

    for i in range(1, n+1):
        start = time()
        x = fib4(i)
        finish = time()
        print(f"fib({i}), время: { finish - start :10f} секунд.")

test4(LIMIT)
print(my_lru.cache)

# -------------------------------------------------

