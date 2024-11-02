#!/usr/bin/env python
# myke 2024-10-31 2024-10-31 1.1
# check.py

# ~ проверка допустимости различных данных.

# ~ 1. даты (YYYY-MM-DD, DD.MM.YYYY)
# ~ 2. ipv4-адреса
# ~ 3. целые числа

# ~ везде есть 3 функции:
# ~ - порождающие случайные не всегда корректные данные
# ~ - проверяющие 1 элемент данных
# ~ - организующие цикл проверки по некоторому принципу

from random import randint as ri
from random import choice as rc
import re

# -----------------------------------------

def make_date():
    ...


def check_date(d):
    ...


def test_check_date(times=10):
    ...

# ~ test_check_date()

# -----------------------------------------

def make_ipv4():
    
    i1, i2, i3, i4 = ri(0, 300), ri(0, 300), ri(0, 300), ri(0, 300)
    sig = rc("................,:+")

    return f"{i1}{sig}{i2}{sig}{i3}{sig}{i4}"


def check_ipv4(ip):

    if re.sub(r'[.0-9]+', '', ip):
        return False

    i1, i2, i3, i4 = map(int, ip.split('.'))

    return (
        0 <= i1 <= 255 and
        0 <= i2 <= 255 and
        0 <= i3 <= 255 and
        0 <= i4 <= 255)


def test_check_ipv4(times=10):

    for rept in range(times):
        ip = make_ipv4()
        res = check_ipv4(ip)
        print(rept, ": ip", ip, "=>", res)

test_check_ipv4()

# ~ 0 : ip 274.173.162.276 => False
# ~ 1 : ip 226,69,263,73 => False
# ~ 2 : ip 81,55,128,197 => False
# ~ 3 : ip 115.91.273.164 => False
# ~ 4 : ip 69.104.127.258 => False
# ~ 5 : ip 275.234.125.223 => False
# ~ 6 : ip 212.44.82.271 => False
# ~ 7 : ip 129+159+37+180 => False
# ~ 8 : ip 242.66.248.167 => True
# ~ 9 : ip 5.288.286.30 => False


# -----------------------------------------

def make_integer():
    ...


def check_integer(inum):
    ...


def test_check_integer(times=10):
    ...

test_check_integer()

# -----------------------------------------
