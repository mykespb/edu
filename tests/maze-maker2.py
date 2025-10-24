#!/usr/bin/env python3
# maze-maker1.py
# (C) Mikhail Kolodin, 2025
# 2025-10-24 2025-10-24 2.0

# Сгенерировать проходимый лабиринт заданного размера.
# Идём с (0, 0) до (край, край) сверху-слева вниз-вправо.

# Обозначения:  0 = пусто, 1 = стена.

# ~ Идея:
# ~ разбиваем массив на квадраты 2х2,
# ~ в каждом отмечаем как стену ровно 1 случайную клетку.
# ~ Это (почти, практически) заведомо проходимо.

from random import randint
from itertools import product


def maker(size : int = 6) -> list[list[int]]:
    """make maze"""

    # array itself
    a = [ [ 0  for _ in range(size) ] for _ in range(size) ]

    # fill 1 cell in 2x2
    for l in range(0, len(a), 2):
        for c in range(0, len(a[0]), 2):
            a[l+randint(0, 1)][c+randint(0, 1)] = 1

    # make empty start and finish cells
    a[0][0] = 0
    a[len(a)-1][len(a[0])-1] = 0

    # answer:
    return a
    

def mprint(a, width=4):
    """напечатать матрицу"""
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"%{width}d" % a[i][j], end="")
        print()
    

def main():
    a = maker()
    mprint(a)

    
main()


# result:

   # ~ 0   1   0   0   0   1
   # ~ 0   0   0   1   0   0
   # ~ 1   0   0   1   0   0
   # ~ 0   0   0   0   1   0
   # ~ 0   0   0   0   0   0
   # ~ 0   1   1   0   1   0
