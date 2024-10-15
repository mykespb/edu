#!/usr/bin/env python
# Mikhail Kolodin, 2024
# simple-matrix.py
# 2024-10-15 2024-10-15 0.1
# простые задачи по работе со списками и матрицами

import random
from pprint import pp

# ~ 1. Перевернуть список (1-мерный). Операцией [::-1] и функцией reverse не пользоваться.

a = [random.randint(-99, 99) for _ in range(10)]

# ~ source: [27, -86, 52, 9, 98, 35, -95, -31, 13, -62]
# ~ result: [-62, 13, -31, -95, 35, 98, 9, 52, -86, 27]

# 1.1
def t11(a):
    print("source:", a)
    r = []
    for i in range(len(a)):
        r = [a[i]] + r
    
    print("result:", r)

# ~ t11(a)

# 1.2
def t12(a):
    print("source:", a)
    r = a[:]

    for i in range(len(r) // 2):
        r[i], r[len(r) - i - 1] = r[len(r) - i -1], r[i]
    
    print("result:", r)

# ~ t12(a)

# ~ 2. Матрица заполнена натуральными числами до 10. Сколько каких?

a = [random.randint(0, 9) for _ in range(10)]

def t21(a):
    print("source:", a)
    r = [0 for _ in range(len(a))]

    for e in a:
        r[e] += 1
    
    print("result:", r)

t21(a)

# ~ source: [8, 7, 8, 8, 7, 4, 8, 6, 0, 4]
# ~ result: [1, 0, 0, 0, 2, 0, 1, 2, 4, 0]

# ~ 3. Транспонирование матрицы.

# ~ 4. Список заполнен нулями и единицами. Сколько там последовательностей из единиц (идущих подряд и разделённых нулями)?
