#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-15 2022-03-15 1.0
# allsquares.py

# ~ Дан текст. В нём есть целые числа.
# ~ Скажите, все ли эти числа являются квадратами.

text1 = """
3 - очень постоянное число.
Жили в квартире 44 весёлых чижа.
"""

text2 = """
Мой номер - 4.
Твой номер - 16.
Мы встретимся в 9 часов.
"""

import math

def myint(t):
    try:
        n = int(t)
    except:
        n = 1
    return n

def issq(n):
    sq = math.isqrt(n)
    return n == sq*sq

def check(text):
    """проверить текст"""

    print(all([issq(x) for x in [myint(word) for word in text.split()] ] ))

check(text1)
check(text2)

# ~ False
# ~ True
