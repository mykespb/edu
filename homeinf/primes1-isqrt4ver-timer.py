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
def primes1a(limit=100):
    """печать простых до limit"""
    for test in range(2, limit+1):
        for tester in range(2, math.isqrt(test)+1):
            if test % tester == 0:
                break
        else:
            ...
            # ~ print(test, end=", ")

@timer
def primes1b(limit=100):
    """печать простых до limit"""
    print(2, end=' ')
    for test in range(3, limit+1, 2):
        for tester in range(2, math.isqrt(test)+1):
            if test % tester == 0:
                break
        else:
            ...
            # ~ print(test, end=", ")

@timer
def primes2list(limit=100):
    """печать простых до limit"""
    ps = []
    for tested in range(2, limit+1):
        for tester in ps:
            if tested % tester == 0:
                break
        else:
            ps.append(tested)
            # ~ print(tested, end=", ")

@timer
def primes2dict(limit=100):
    """печать простых до limit"""
    ps = {}
    for tested in range(2, limit+1):
        for tester in ps:
            if tested % tester == 0:
                break
        else:
            ps[tested]=1
            # ~ print(tested, end=", ")

@timer
def primes2set(limit=100):
    """печать простых до limit"""
    ps = set()
    for tested in range(2, limit+1):
        for tester in ps:
            if tested % tester == 0:
                break
        else:
            ps.add(tested)
            # ~ print(tested, end=", ")

limit = 200_000

# вызов функции 1

print("\n------------------------------------------------\n")

print("\nisqrt-a 100:")
primes1a()
print()

print("\nisqrt-a 1000:")
primes1a()
print()

print("\nisqrt-b 100:")
primes1b(100)
print()

print("\nisqrt-b 1000:")
primes1b(100)
print()

print(f"\nisqrt {limit}:")
primes1a(limit)
print()

print(f"\nisqrt {limit}:")
primes1b(limit)
print()

# вызов функции 2

print("\nlist:")
primes2list(limit)

print("\ndict:")
primes2dict(limit)

print("\nset:")
primes2set(limit)
print()

# ~ primes2(1000)
# ~ print()

# ~ ------------------------------------------------


# ~ isqrt-a 100:
# ~ fun primes1a((), {}) took 0.0000 seconds.

# ~ isqrt-a 1000:
# ~ fun primes1a((), {}) took 0.0000 seconds.

# ~ isqrt-b 100:
# ~ 2 fun primes1b((100,), {}) took 0.0000 seconds.

# ~ isqrt-b 1000:
# ~ 2 fun primes1b((100,), {}) took 0.0000 seconds.

# ~ isqrt 200000:
# ~ fun primes1a((200000,), {}) took 0.2436 seconds.

# ~ isqrt 200000:
# ~ 2 fun primes1b((200000,), {}) took 0.2292 seconds.


# ~ list:
# ~ fun primes2list((200000,), {}) took 5.2287 seconds.

# ~ dict:
# ~ fun primes2dict((200000,), {}) took 6.1273 seconds.

# ~ set:
# ~ fun primes2set((200000,), {}) took 6.5563 seconds.
