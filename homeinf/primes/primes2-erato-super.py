#!/usr/bin/env python
# primes2-erato-opt.py (c) Mikhail Kolodin
# 2025-03-05 2025-04-30 2.2
# Расчёт простых чисел.
# ~ Решето Эратосфена = Sieve of Eratosthenes
# ~ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# ~ Оптимизированная версия.
# ~ Суперпростые числа.
# ~ Суперпросты́е чи́сла (также известны как простые числа высшего порядка) — подмножество простых чисел, стоящих в списке простых чисел на позициях, являющихся простыми числами (то есть это 2-е, 3-е, 5-е, 7-е, 11-е, 13-е, 17-е и т.д. по счёту простые числа).
# ~ Первые члены последовательности суперпростых чисел:
# ~ 3, 5, 11, 17, 31, 41, 59, 67, 83, 109, 127, 157, … (последовательность A006450 в OEIS).

import math

# определение функции
def primes(limit=100):
    """список простых до limit"""

    seive = [1 for _ in range(limit)]
    seive[0] = seive[1] = 0

    for elem in range(2, limit-1):
        if seive[elem]:
            for mult in range(2, limit // elem):
                seive[elem * mult] = 0

    result = [ n for n in range(len(seive)-1) if seive[n]]

    return result

def supper(seive):
    """печать суперпростых"""

    result = []
    
    for i, p in enumerate(seive, 1):
        if p < len(seive):
            result.append(seive[p-1])

    return result

# вызов функции
pt = primes(1500)
# ~ print(pt)
print(*supper(pt), sep=", ")

# ~ 3, 5, 11, 17, 31, 41, 59, 67, 83, 109, 127, 157, 179, 191, 211, 241, 277, 283, 331, 353, 367, 401, 431, 461, 509, 547, 563, 587, 599, 617, 709, 739, 773, 797, 859, 877, 919, 967, 991, 1031, 1063, 1087, 1153, 1171, 1201, 1217, 1297, 1409, 1433, 1447, 1471

# ~ https://oeis.org/A006450
# ~ A006450 Prime-indexed primes: primes with prime subscripts.
# ~ 3, 5, 11, 17, 31, 41, 59, 67, 83, 109, 127, 157, 179, 191, 211, 241, 277, 283, 331, 353, 367, 401, 431, 461, 509, 547, 563, 587, 599, 617, 709, 739, 773, 797, 859, 877, 919, 967, 991, 1031, 1063, 1087, 1153, 1171, 1201, 1217, 1297, 1409, 1433, 1447, 1471

# ~ A000040 The prime numbers.
# ~ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271
