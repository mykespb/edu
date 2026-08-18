#!/usr/bin/env python
# Miklhail (myke) Kolodin
# math / factorion.py
# 2026-07-28 2026-08-14 1.1
# Факторион — натуральное число, которое равно сумме факториалов своих цифр.
# ~ Полный список факторионов
# ~ 1 = 1!
# ~ 2 = 2! 
# ~ 145 = 1! + 4! + 5!
# ~ 40585 = 4! + 0! + 5! + 8! + 5!
# ~ https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%BE%D0%BD

from functools import lru_cache

@lru_cache(maxsize=None)
def fact1(n):
    if n == 0:
        return 1
    if n <= 2:
        return n
    return n * fact(n-1)


@lru_cache(maxsize=None)
def fact2(n):
    if n == 0:
        return 1
    if n <= 2:
        return n
    p = 1
    for i in range(2, n+1):
        p *= i
    return p
    

fact = fact2


def facts():
    LIMIT = 50000

    for f in range(LIMIT):
        sf   = list(str(f))
        nsf  = map(int, sf)
        sumf = sum(fact(x) for x in nsf)

        if f == sumf:
            print(f"{f}! = ", end="")
            print(*sf, sep="! + ", end="!\n")


facts()


# ~ 1 ! = 1
# ~ 2 ! = 2
# ~ 145 ! = 1! + 4! + 5!
# ~ 40585 ! = 4! + 0! + 5! + 8! + 5!
