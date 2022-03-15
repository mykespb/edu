#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-15 2022-03-15 1.1
# allsquares.py

# ~ Дан текст. В нём есть целые числа.
# ~ Скажите, все ли эти числа являются квадратами.

text1 = """
3 - очень постоянное число.
Жили в квартире 44 44 весёлых чижа.
"""

text2 = """
Мой номер - 4.
Твой номер - 16.
Мы встретимся в 9 часов.
"""

import math

def check(text):
    """проверить текст"""
    print(all([x == math.isqrt(x)**2 for x in [int(word if all([c in '0123456789' for c in word]) else 1) for word in text.split()] ] ))

check(text1)
check(text2)

# ~ False
# ~ True
