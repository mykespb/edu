#!/usr/bin/env python
# primes1-isqrt.py (c) Mikhail Kolodin
# 2022-02-12 2025-04-30 1.2
# Расчёт простых чисел.

import math, time
from functools import wraps

# decorator
def timer(fun):
    @wraps(fun)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fun(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"fun {fun.__name__}({args}, {kwargs}) took {total_time:.4f} seconds.")
        return result
    return timeit_wrapper
    
# определение функции
@timer
def primes1(limit=100):
    """печать простых до limit"""
    for test in range(2, limit+1):
        for tester in range(2, test):
            if test % tester == 0:
                break
        else:
            ...
            # ~ print(test, end=", ")

# определение функции
@timer
def primes2(limit=100):
    """печать простых до limit"""
    for test in range(2, limit+1):
        for tester in range(2, math.isqrt(test)+1):
            if test % tester == 0:
                break
        else:
            ...
            # ~ print(test, end=", ")

# вызов функции 1

primes1(100)
print()

primes1(1000)
print()

primes1(10000)
print()

primes1(100000)
print()

# вызов функции 2

primes2(100)
print()

primes2(1000)
print()

primes2(10000)
print()

primes2(100000)
print()


# ~ fun primes1((100,), {}) took 0.0000 seconds.

# ~ fun primes1((1000,), {}) took 0.0027 seconds.

# ~ fun primes1((10000,), {}) took 0.2140 seconds.

# ~ fun primes1((100000,), {}) took 17.4030 seconds.

# ~ fun primes2((100,), {}) took 0.0000 seconds.

# ~ fun primes2((1000,), {}) took 0.0003 seconds.

# ~ fun primes2((10000,), {}) took 0.0047 seconds.

# ~ fun primes2((100000,), {}) took 0.0917 seconds.


