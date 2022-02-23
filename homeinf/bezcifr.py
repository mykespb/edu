#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-23 2022-02-23 1.0
# bezcifr.py

# ~ Считаем до 100…

# ~ Часть 1. 
# ~ Напечатать натуральные числа до 100 включительно через запятую.

def ver_aa():
    """просто 1..100"""

    for i in range(1, 101):
        print(i, end=", ")

# ~ ver_aa()

def ver_ab():
    """просто 1..100"""

    print(*(i for i in range(1, 101)), sep=", ")

# ~ ver_ab()

# ~ Часть 2. 
# ~ Напечатать натуральные числа до 100 включительно через запятую.
# ~ не используя в программе ни одной цифры.

import math, random

def ver_bc():
    """и без цифр"""

    sa = len("a")
    sb = len("aaaaaaaaaa")
    sb *= sb
    sb += sa

    for i in range(sa, sb):
        print(i, end=", ")

# ~ ver_bc()

def ver_ba():
    """и без цифр"""

    zero     = int()
    one      = int(math.pi // math.e)

    szero    = str(zero)
    sone     = str(one)
    sstoodin = sone + szero + sone
    stoodin  = int(sstoodin)

    for i in range(one, stoodin):
        print(i, end=", ")

# ~ ver_ba()

def ver_bb():
    """и без цифр"""

    na, nb = random.random(), random.random()
    zero = int(min(na, nb) // max(na, nb))
    one  = int(round(math.cos(zero)))
    two  = one + one

    mdg = int(math.degrees(one) - math.tau) * two - one

    for i in range(one, mdg):
        print(i, end=", ")

ver_bb()































