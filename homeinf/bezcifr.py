#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-23 2022-03-31 1.11
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

import math

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

import random

def ver_bb():
    """и без цифр"""

    zero = int(random.random())
    one  = int(round(math.cos(zero)))
    two  = one + one

    mdg = int(math.degrees(one) - math.tau) * two - one

    for i in range(one, mdg):
        print(i, end=", ")

# ~ ver_bb()

def ver_bd():
    """и без цифр все числа от 1 до 100"""

    saa, saaa = len("aa"), len("aaa")
    ifrom, ito = ver_bd.__doc__.split()[-saaa::saa]

    for i in range(int(ifrom), int(ito)+int(ifrom)):
        print(i, end=", ")        

# ~ ver_bd()

def ver_be():
    """и без цифр все числа от 1 до 100"""

    saa, saaa = len("aa"), len("aaa")
    ifrom, ito = map(int, ver_be.__doc__.split()[-saaa::saa])

    for i in range(ifrom, ito + ifrom):
        print(i, end=", ")        

# ~ ver_be()

def ver_bf():
    """и без цифр"""

    for i in range(ord('B')-ord('A'), ord('e')):
        print(i, end=", ")        

# ~ ver_bf()        

import string

def ver_bg():
    """и без цифр"""

    ten     = len(string.digits)
    hundred = ten *  ten
    one     = ten // ten

    for i in range(one, hundred + one):
        print(i, end=", ")        

# ~ ver_bg()

import datetime

def ver_bh():
    """и без цифр"""

    s, saaa, saaaa = len(""), len("aaa"), len("aaaa")
    d       = datetime.date.today().ctime()[-saaaa:]
    da, db  = int(d[:saaa]), int(d[s])
    one     = da // da
    hundred = da // db
    
    for i in range(one, hundred):
        print(i, end=", ")        

ver_bh()

import sys

def ver_bi():
    """и без цифр"""

    tri     = sys.version_info.major
    odin    = tri // tri
    desat   = tri * tri + odin
    sto     = desat * desat
    stoodin = sto + odin

    for i in range(odin, stoodin):
        print(i, end=", ")

# ~ ver_bi()

def ver_bj():
    """и без цифр"""

    one     = int(... is ...)
    zero    = one - one
    stoodin = int(str(one) + str(zero) + str(one))

    for i in range(one, stoodin):
        print(i, end=", ")

# ~ ver_bj()

import string

def ver_bk():
    """и без цифр"""

    digs    = list(map(int, [c for c in string.digits]))
    zero    = min(digs)
    nine    = max(digs)
    one     = nine // nine
    stoodin = nine * nine + nine + nine + one + one

    for i in range(one, stoodin):
        print(i, end=", ")

# ~ ver_bk()

def ver_bl():
    """и без цифр"""

    one  = int(True)
    text = ("Печать натуральных чисел до ста включительно через запятую, "
        "не используя в программе ни одной цифры.")
    
    for i in range(one, len(text) + one):
        print(i, end=", ")

# ~ ver_bl()


























