#!/usr/bin/env python
# timer-table-func.py (c) Mikhail Kolodin
# 2025-03-05 2025-05-12 5.1
# Расчёт простых чисел.
# ~ Решето Эратосфена = Sieve of Eratosthenes
# ~ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# ~ Версия с 2 списками.

from time import time

# 1. собственно простые числа

# определение функции
def primes(limit=100):
    """печать простых до limit"""

    ready = []
    todo  = [ x for x in range(2, limit) ]

    while todo:
        elem = todo.pop(0)
        ready.append(elem)
        todo = [ x for x in todo if x % elem ]

#    return ready

# 2. как бы измерить затраченное время?

def timer(limit):
    """простой таймер"""

    start = time()
    primes(limit)
    finish = time()
    print(f"для {limit:8_} чисел нужно {finish - start : 10f} секунд.")


def functimer(func, limit=100):
    """простой таймер"""

    start = time()
    func(limit)
    finish = time()
    print(f"functimer: для {limit:8_} чисел нужно {finish - start : 10f} секунд.")


functimer(primes, 10)

def test(order=4):
    for i in range(1, order+1):
        timer(10**i)

test()

def functest(func, order=4):
    for i in range(1, order+1):
        functimer(func, 10**i)

functest(primes, 4)

# ~ test(6)
# ~ для         10 чисел нужно   0.000004 секунд.
# ~ для        100 чисел нужно   0.000033 секунд.
# ~ для      1_000 чисел нужно   0.000510 секунд.
# ~ для     10_000 чисел нужно   0.026871 секунд.
# ~ для    100_000 чисел нужно   1.639403 секунд.
# ~ для  1_000_000 чисел нужно 133.756445 секунд.
