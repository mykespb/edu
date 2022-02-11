#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-01-29 2022-02-11 1.1
# pihalf.py

# ~ расчёт пи пополам как
# ~ 2*2 / (1*3)   *  4*4 / (3*5)  ...

import math

def calc(eps=1e-1):
    """посчитать с заданной точностью"""

    pi = 1
    maxtimes = 1000000

    for i in range(1, maxtimes, 2):
        mem = (i+1)*(i+1) / (i*(i+2))
        if mem < eps: return pi
        pi *= mem

    return pi


print("\nсчитаем пи пополам.\nдолжно получиться", math.pi / 2)

print("получилось число:", calc(1e-10))
