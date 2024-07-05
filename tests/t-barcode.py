#!/usr/bin/env python

# calculate control digit for ISBN
# Mikhail Kolodin, 2024
# 2024-07-04 2024-70-05 2.0
# https://w.wiki/ABfs

def cd1(n):
    """method 1"""

    if type(n) == str:
        n = n.replace("-", "")
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


def cd2(n):
    """method 2"""
    
    if type(n) == str:
        n = n.replace("-", "")
        n = int(n, 0)

    summa = 0
    mult = 3

    while n:
        ld = n % 10
        n //= 10

        ld *= mult
        mult = 4 - mult
        summa += ld

    summa %= 10

    return summa if summa == 0 else 10 - summa


def test(n):
    """test for a number"""

    print(n, "-> method 1: ", cd1(n), ", method 2: ", cd2(n))


test(226611156)
# -> 6, 8
test("978-5-93286161")
# -> 1, 5


#https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9_%D0%BD%D0%BE%D0%BC%D0%B5%D1%80
