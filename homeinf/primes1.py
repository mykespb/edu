#!/usr/bin/env python
# primes1.py (c) Mikhail Kolodin
# 2022-02-12 2022-02-12 1.0

import math

# определение функции
def primes(limit=100):
    """печать простых до limit"""
    for test in range(2, limit+1):
        for tester in range(2, math.isqrt(test)):
            if test % tester == 0:
                break
        else:
            print(test, end=", ")

# вызов функции
#primes()
# должно напечатать простые до 100
primes(2500)
# должно напечатать простые до 1000
