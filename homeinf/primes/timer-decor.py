#!/usr/bin/env python
# timer-decor.py (c) Mikhail Kolodin
# 2025-03-05 2025-05-06 3.5
# Расчёт простых чисел.
# ~ Решето Эратосфена = Sieve of Eratosthenes
# ~ https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# ~ Версия с 2 списками.
# ~ Изучение декораторов.

import math
from time import time

# 1. собственно простые числа

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
print(primes(100))
# ~ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
# ~ print(primes(1000))


# 2. как бы измерить затраченное время?

def timer1(fun):
    """простой таймер"""

    start = time()
    fun()
    finish = time()
    print(f"время: { finish - start } секунд.")


timer1(primes)

# ~ ок, но не совсем удобно:
# ~ только с 1 заданным значением, без параметров, их трудно передать


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

print('\nс обёрткой:')

def decor(fun, limit=10):
    def wrapper():
        print(f"выполняем для предела: {limit}")
        start = time()
        fun(limit)
        finish = time()
        print(f"время: { finish - start } секунд.")
    return wrapper

timer3 = decor(primes)
print(timer3())


# 4. обёртка - "синтаксический сахар" - декораторы

from functools import wraps

def timing(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        print(f"выполняем для параметров: {args=}, {kwargs=}")
        start = time()
        fun(*args, **kwargs)
        finish = time()
        print(f"время: { finish - start } секунд.")
    return wrapper

@timing
def decoprimes(limit=100):
    """печать простых до limit"""

    ready = [2]
    todo = [ x for x in range(3, limit) ]

    while todo:
        elem = todo.pop(0)
        ready.append(elem)
        todo = [ x for x in todo if x % elem ]

    return ready

decoprimes(100)
decoprimes(1_000)
decoprimes(10_000)
decoprimes(100_000)


# ~ https://www.geeksforgeeks.org/decorators-in-python/
# ~ https://realpython.com/primer-on-python-decorators/#simple-decorators-in-python


# ~ [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# ~ время: 1.9311904907226562e-05 секунд.
# ~ выполняем для предела: 100
# ~ время: 3.600120544433594e-05 секунд.

# ~ с обёрткой:
# ~ выполняем для предела: 10
# ~ время: 1.6689300537109375e-06 секунд.
# ~ None
# ~ выполняем для параметров: args=(100,), kwargs={}
# ~ время: 2.288818359375e-05 секунд.
# ~ выполняем для параметров: args=(1000,), kwargs={}
# ~ время: 0.000690460205078125 секунд.
# ~ выполняем для параметров: args=(10000,), kwargs={}
# ~ время: 0.03265118598937988 секунд.
# ~ выполняем для параметров: args=(100000,), kwargs={}
# ~ время: 2.0448899269104004 секунд.
