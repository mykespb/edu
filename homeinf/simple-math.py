#!/usr/bin/env python
# Mikhail Kolodin, 2024
# simple-matrix.py
# 2024-10-15 2024-10-15 0.1
# простые задачи по математике

import random
from pprint import pp
import copy

# 0. Печать матрицы

def mprint(a, width=4):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"%{width}d" % a[i][j], end="")
        print()

# ~ 1. Перевернуть список (1-мерный). Операцией [::-1] и функцией list.reverse() не пользоваться.

a = [random.randint(-99, 99) for _ in range(10)]

