#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2024-10-30 2024-10-30 1.0
# sequences.py

# ~ работа с пследовательностями

import random
from pprint import pp
import copy

# ============================================================================
# 0. Создание и печать матрицы
# ============================================================================

def make1dim(elems=3, bottom=0, top=9):
    """создать вектор"""
    
    return [ random.randint(bottom, top) for c in range(elems) ] 

    
def make2dim(rows=3, cols=3, bottom=0, top=9):
    """создать матрицу"""
    
    return [ [ random.randint(bottom, top) for c in range(cols) ] for r in range(rows) ]

    
def mprint(a, width=4):
    """напечатать матрицу"""
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"%{width}d" % a[i][j], end="")
        print()


# ============================================================================
# 1. проверка и правка
# ============================================================================

# ~ 1.1. Сглаживание.
# ~ В некоторой заданной натуральной последовательности 
# ~ заменить элементы на среднее арифм. их соседей.
# ~ (Не считать для крайних элементов).

def deltas(seq, proc=50):
    """подсчёт и правка"""

    a = seq[:]
    for i in range(1, len(seq)-1):
        neibmed = (seq[i-1] + seq[i+1]) / 2
        a[i] = int(neibmed + .5)

    return a


def deltas_test(times=10):
    """запуск тестов"""

    for raz in range(1, times+1):
        a = make1dim(10, 80, 90)
        for i in range(1, len(a)):
            if random.random() > .9:
                a[i] *= 2
        print("\nбыло: ", a)
        b = deltas(a)
        print("стало:", b)

deltas_test()

# ~ было:  [81, 85, 90, 400, 82, 83, 83, 400, 83, 89]
# ~ стало: [81, 86, 243, 86, 242, 83, 242, 83, 245, 89]

# ============================================================================
