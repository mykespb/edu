#!/usr/bin/env python
# fibo-rec.py (c) Mikhail Kolodin
# 2025-05-12 2025-05-12 0.1
# Числа Фибоначчи рекурсивно -- просто и с декоратором

from functools import wraps
from time import time

LIMIT = 20

print("\n=================================== Recursion ==============================\n")

def timing(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print(f"выполняем для параметров: {args=}, {kwargs=}")
        start = time()
        res = fun(*args, **kwargs)
        finish = time()
        print(f"время: { finish - start } секунд.")
        return res
    return wrapper
    

#@timing
def fib(n: int) -> int:
    """вычислить n-ое число Фибоначчи"""

    if n < 2:
        return 1

    return fib(n-2) + fib(n-1)


def test(n: int) -> None:
    """посчитать и показать все числа Фионаччи до n"""

    for i in range(1, n+1):
        print("\n-------------------------------------------------\n")
        start = time()
        print(f"fib({i}) = {fib(i)}")
        finish = time()
        print(f"время: { finish - start } секунд.")


test(LIMIT)

print("\n=================================== LRU decorator ==============================\n")

#Using least recently used cache function in Python to limit the no. of items in cache
from functools import lru_cache

@lru_cache
def fib(n: int) -> int:
    """вычислить n-ое число Фибоначчи"""

    if n < 2:
        return 1

    return fib(n-2) + fib(n-1)


def test(n: int) -> None:
    """посчитать и показать все числа Фионаччи до n"""

    for i in range(1, n+1):
        print("\n-------------------------------------------------\n")
        start = time()
        print(f"fib({i}) = {fib(i)}")
        finish = time()
        print(f"время: { finish - start } секунд.")


test(LIMIT)
