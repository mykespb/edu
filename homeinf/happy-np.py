#!/usr/bin/env python

# (C) Mikhail Kolodin, 2021
# 2021-12-23 2021-12-23 3.0
# счастливые билеты

LIMIT = 12

import itertools
import numpy as np

def happy(half = 3):
    """ считаем количество счастливых билетов
    для номера длиной half*2 цифр """

    kol = np.zeros(9*half+1, dtype=np.int64)
    num = np.zeros(half, dtype=np.int8)

    for it in range(10**half):

        summa = np.sum(num)
        kol [summa] += 1
        # ~ print (num, summa)
        
        for pos in range(half):
            num [pos] += 1
            if num [pos] <= 9:
                break
            for i in range(pos+1):
                num [i] = 0
        

    mul = sum([n*n for n in kol])

    return mul


def org(n):
    """органайзер """
    print(f"Счастливые билеты для номеров из {n:2} цифр. Их {happy(n//2):_}.")


def main():
    """считаем всё"""

    for n in range(2, LIMIT+1, 2):
        org(n)

main()


# Счастливые билеты для номеров из  2 цифр. Их 10
# Счастливые билеты для номеров из  4 цифр. Их 670
# Счастливые билеты для номеров из  6 цифр. Их 55_252
# Счастливые билеты для номеров из  8 цифр. Их 4_816_030
# Счастливые билеты для номеров из 10 цифр. Их 432_457_640
# Счастливые билеты для номеров из 12 цифр. Их 39_581_170_420
