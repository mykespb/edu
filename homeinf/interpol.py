#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-17 2025-05-18 1.1
# interpol.py
# ~ Интерполяция
# ~ Дан список с данными (м.б. давление или температура),
# ~ это всё положительные вещ. числа.
# ~ Некоторые значения испорчены, там нули или отрицательные числа.
# ~ Иногда это одно число, иногда несколько подряд.
# ~ Заполнить пропуски равномерно.

import math, random

def make(size = 10):
    """make list"""

    # ~ lof = [ random.random() * 99 + 1e-6 for _ in range(size)]

    # ~ for bad in range(random.randint(0, int(math.isqrt(size)))):
        # ~ start = random.randint(1, int(math.isqrt(size)))
        # ~ finish = random.randint(start+1, min(size, start+1+random.randint(1,5)))
        # ~ for i in range(start, finish):
            # ~ lof[i] = - random.random() * 100

    lof = [1., 2., 0., 4., 0., 0., 7., 0., 0., 0., 3.]

    doprint("old", lof)
    return lof

def solve(lof):
    """solve it"""

    # ~ start = 0
    normal = True
    for i in range(1, len(lof)):
        if normal:
            if lof[i] <= 0.:
                start = i - 1
                normal = False
        else:
            if lof[i] > 0.:
                diff = lof[i] - lof[start]
                step = diff / (i - start)
                # ~ print(f"{start=}, {i=}, {diff=}, {step=}")
                for j in range(start+1, i):
                    lof[j] = lof[start] + (j - start) * step
                normal = True

    return lof


def test():
    """test it"""
    lof  = make()
    clof = solve(lof)

    doprint("new", clof)


def doprint(title, lof):
    """print it"""

    print(title, end=": ")
    for f in lof:
        print(f"{f:.2f}", end=", ")
    print()

test()


# ~ old: 1.00, 2.00, 0.00, 4.00, 0.00, 0.00, 7.00, 0.00, 0.00, 0.00, 3.00, 
# ~ new: 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 6.00, 5.00, 4.00, 3.00, 
