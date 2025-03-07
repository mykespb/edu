#!/usr/bin/env python
# primes2-erato.py (c) Mikhail Kolodin
# 2025-03-05 2025-03-05 2.1
# Расчёт простых чисел.
# ~ Решето Эратосфена = Sieve of Eratosthenes
# ~ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math

# определение функции
def primes(limit=100):
    """печать простых до limit"""

    seive = [1 for _ in range(limit)]
    seive[0] = seive[1] = 0

    for elem in range(2, limit):
        if seive[elem]:
            print(elem, end=", ")
            for mult in range(2, limit // elem):
                seive[elem * mult] = 0

    print()

# вызов функции
primes()
# должно напечатать простые до 100
# ~ primes(2500)
# должно напечатать простые до 2500

# ~ Вопрос: можно ли оптимизировать этот алгоритм:?
# ~ Подсказка: домножать можно не на все натуральные числа, а только начиная с квадратов, и только нечётные, и т.п.


# ~ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 99, 
