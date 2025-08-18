#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-08-16 2025-08-17 1.1

# ~ grow-stat.py

# ~ Статистика растущих чисел

# ~ Назовём натуральное число растущим, если в его записи каждая последующая цифра
# ~ строго больше предыдущей.

# ~ Подсчитать, сколько растущих чисел есть среди 1-значных, 2-значных, и т.п.


import random


def is_grow(x):
    """check if number x is growing"""

    seq = str(x)

    for i in range(len(seq) - 1):
        if seq[i] > seq[i+1]:
            return False

    return True
    

def main():
    """solve all"""

    for size in range(1, 9):
        nmin = 10**(size-1)
        nmax = 10**size

        how_many = 0
        for i in range(nmin, nmax):
            if is_grow(i):
                how_many += 1

        print(f"{size=:3} => from {nmin:10} to {nmax-1:10} : {how_many=:5}")
        

main()


# results:

# ~ size=  1 => from          1 to          9 : how_many=    9
# ~ size=  2 => from         10 to         99 : how_many=   45
# ~ size=  3 => from        100 to        999 : how_many=  165
# ~ size=  4 => from       1000 to       9999 : how_many=  495
# ~ size=  5 => from      10000 to      99999 : how_many= 1287
# ~ size=  6 => from     100000 to     999999 : how_many= 3003
# ~ size=  7 => from    1000000 to    9999999 : how_many= 6435
# ~ size=  8 => from   10000000 to   99999999 : how_many=12870
