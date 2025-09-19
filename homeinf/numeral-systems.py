#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-09-19 2025-09-19 1.0
# numeral-systems.py

# ~ Напечатать таблицы сложения и умножения в системах счисления: 2, 8, 10, 16.

from operator import add, mul


def table(base, oper):
    """print table for base with oper"""

    width = 4
    basechar = {2:'b', 8:'o', 10:'d', 16:'X'}

    for i in range(base):
        for j in range(base):
            print( "{value:{width}{baza}}" .format(value = oper(i, j), baza=basechar[base], width=width), end="")
        print()


def print_all():
    """print all tables"""

    for base in 2, 8, 10, 16:
        for oper in add, mul:
            print(f"\n-------------------------------{base} {oper} ---------------------\n")
            table(base, oper)
    print()


print_all()
