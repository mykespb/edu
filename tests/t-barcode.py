#!/usr/bin/env python

# calculate control digit for ISBN
# Mikhail Kolodin, 2024
# 2024-07-04 1.0
# https://w.wiki/ABfs

def cd(n):
    """calculate digit"""

    if type(n) == str:
        n = int(n, 0)

    pos = 2
    summa = 0
    while n:
        ld = n % 10
        n //= 10

        term = pos * ld
        summa += term

        #print(f"{ld=}, {n=}, {pos=}, {term=}, {summa=}")

        pos += 1

    summa %= 11
    summa = 11 - summa

    return summa

def test(n):
    """test for a number"""

    print(n, "->", cd(n))


test(226611156)
# -> 6

#https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9_%D0%BD%D0%BE%D0%BC%D0%B5%D1%80
