#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-08 2023-02-08 1.1
# ya-astones-jewels.py

# ~ Задача из яндекса.
# ~ Задача A. Камни и украшения
# ~ Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются «драгоценностями». Проще говоря, нужно проверить, какое количество символов из S входит в J.

# ~ 1. генерация строк

from random import choice

import string

CHARS = string.ascii_letters

def gen(lJ = 5, lS = 20):
    """даёт 2 строки, J, S"""

    return ( "".join(  list(set([choice(CHARS) for _ in range(lJ) ] )) ),
    "".join([choice(CHARS) for _ in range(lS)]) )

# ~ 2. решение

def solve1(j, s):
    """find common chars"""

    count = 0
    for e in s:
        if e in j:
            count += 1

    return count

def solve2(j, s):
    """find common chars"""

    return sum( map( lambda x: x in j, s)) 

# ~ 3. запуск тестов

def run_tests(times = 10):
    """run times tests"""

    for test in range(times):
        J, S = gen()
        print(f"{test=}, {J=}, {S=}, count=", solve1(J, S), ",", solve2(J, S))

run_tests(10)

# ~ test=0, J='WGxEQ', S='njTeCSBcPRHubsoFNTjy', count= 0 , 0
# ~ test=1, J='BvufF', S='oRxbLXWIIWYlnjbCULvp', count= 1 , 1
# ~ test=2, J='SRFQP', S='SYZcrbvfjbuiwdULJJBn', count= 1 , 1
# ~ test=3, J='GfFoj', S='WinvlAoxwdOMuwHgveln', count= 1 , 1
# ~ test=4, J='oqGh', S='ZVxPYowojufGwjbMnbkx', count= 3 , 3
# ~ test=5, J='SbRXx', S='kbawEjZRyzljAehQfSZR', count= 4 , 4
# ~ test=6, J='ehJFy', S='oXvoRPPuIOcrwsMsPJuy', count= 2 , 2
# ~ test=7, J='ZagQC', S='kaUezTPuWfVDXlampiIi', count= 2 , 2
# ~ test=8, J='GzxgI', S='GtrYaqFjxgzDQChhmSPY', count= 4 , 4
