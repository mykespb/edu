#!/usr/bin/env python
# timer-decor.py (c) Mikhail Kolodin
# 2025-03-05 2025-05-06 3.5
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
    print(f"для {limit:10} чисел нужно: { finish - start : 10f} секунд.")


def test(order=5):
    for i in range(1, order+1):
        timer(10**i)

test()
