#!/usr/bin/env python
# timer-decor.py (c) Mikhail Kolodin
# 2025-03-05 2025-05-06 3.3
# Расчёт простых чисел.
# ~ Решето Эратосфена = Sieve of Eratosthenes
# ~ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# ~ Версия с 2 списками.
# ~ Изучение декораторов.

import math
from time import time

# 1. собственно просые числа

# определение функции
def primes(limit=100):
    """печать простых до limit"""

    ready = [2]
    todo = [ x for x in range(3, limit) ]

    while todo:
        elem = todo.pop(0)
        ready.append(elem)
        todo = [ x for x in todo if x % elem ]

    return ready


# вызов функции
# ~ print(primes(50))
# должно напечатать простые до 50
# ~ print(primes(1000))
# должно напечатать простые до 1000

# ~ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 

# 2. как бы измерить затраченное время?

def timer1(fun):
    """простой таймер"""

    start = time()
    fun()
    finish = time()
    print(f"время: { finish - start } секунд.")


timer1(primes)

# ~ ок, но не совсем удобно:
# ~ только с 1 заданным значением. без параметров, их трудно передать

# чуток подправим:

def timer2(fun, limit):
    """простой таймер"""

    print(f"выполняем для предела: {limit}")
    start = time()
    fun(limit)
    finish = time()
    print(f"время: { finish - start } секунд.")


timer2(primes, 100)


# 3. с обёрткой

# ~ def wrap(fun)
