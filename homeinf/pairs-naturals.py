#!/usr/bin/env python

# 2025-06-25 2025-06-27 2.1
# pairs-naturals.py (C) M.Kolodin 2025

# ~ Парочки натуралов
# ~ ----------------------------------------------

# ~ Дан список случайных 2-значных натуральных чисел.
# ~ Найти пары чисел, состящих из одинаковых цифр,
# ~ записанных в обратном порядке.

# ~ Напр., для 11, 35, 45, 53, 88, 67, 54
# ~ это (35 и 53), (45 и 54)

lon = 11, 35, 45, 53, 88, 67, 54

slon = list(map(str, lon))


def doit1():
    """решаем всё"""

    for left in range(len(lon)-1):
        for right in range(left+1, len(lon)):
            if same(lon[left], lon[right]):
                print(lon[left], lon[right])


def doit2():
    """решаем всё"""

    for left in range(len(slon)-1):
        for right in range(left+1, len(slon)):
            if slon[left] ==  slon[right][::-1]:
                print(slon[left], slon[right])


def same(x, y):
    """сравниваем"""

    # версия 1
    # ~ return set(str(x)) == set(str(y))

    # версия 2
    # ~ return sorted(str(x)) == sorted(str(y))

    # версия 3
    # ~ return x == y or str(x) == str(y)[::-1]
    
    # версия 4
    return str(x) == str(y)[::-1]
    

doit1()
doit2()


# ~ 35 53
# ~ 45 54
