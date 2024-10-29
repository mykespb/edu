#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2024-10-30 2024-10-30 1.0
# calc.py

# ~ вер.1. простой калькулятор
# ~ пользователь вводит строку вида
# ~ 1 + 2
# ~ а программа вычисляет выражение

from operator import add, sub, mul, floordiv

def dialog1():
    """организует диалог, версия 1"""

    print("Введите арифметическое выражение (вида 1 + 2, т.е. всё через пробел), а я его посчитаю")

    opers = add, sub, mul, floordiv
    opsigns = list("+-*/")

    while (stroka := input("Что считать? ")):
        n1, op, n2 = stroka.strip().split()
        res = opers[opsigns.index(op)](int(n1), int(n2))
        print(n1, op, n2, '=', res)        

    print("Счастливо!")


dialog1()

# ~ Что считать? 1 + 2
# ~ 1 + 2 = 3
# ~ Что считать? 3 * 4
# ~ 3 * 4 = 12
# ~ Что считать? 4 / 2
# ~ 4 / 2 = 2
# ~ Что считать? 5 - 2
# ~ 5 - 2 = 3
# ~ Что считать? 
# ~ Счастливо!
