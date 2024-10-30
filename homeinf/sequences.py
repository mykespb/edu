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

