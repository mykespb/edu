#!/usr/bin/env python
# primes2-erato.py (c) Mikhail Kolodin
# 2025-03-05 2025-04-30 2.2
# Расчёт простых чисел.
# ~ Решето Эратосфена = Sieve of Eratosthenes
# ~ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

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
def primes(limit=100):
    """печать простых до limit"""

    seive = [1 for _ in range(limit)]
    seive[0] = seive[1] = 0

    for elem in range(2, limit):
        if seive[elem]:
            # ~ print(elem, end=", ")
            for mult in range(2, limit // elem):
                seive[elem * mult] = 0

    print()

# вызов функции
primes()
# должно напечатать простые до 100
primes(1000)
# должно напечатать простые до 1000
primes(10000)
# должно напечатать простые до 10000
primes(100000)
# должно напечатать простые до 100000

# ----------------------------------------------------

# ~ fun primes((), {}) took 0.0000 seconds.

# ~ fun primes((1000,), {}) took 0.0001 seconds.

# ~ fun primes((10000,), {}) took 0.0011 seconds.
