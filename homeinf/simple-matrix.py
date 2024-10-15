#!/usr/bin/env python
# Mikhail Kolodin, 2024
# simple-matrix.py
# 2024-10-15 2024-10-15 3.1
# простые задачи по работе со списками и матрицами

import random
from pprint import pp
import copy

# 0. Печать матрицы

def mprint(a, width=4):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"%{width}d" % a[i][j], end="")
        print()

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

# ~ t21(a)

# ~ source: [8, 7, 8, 8, 7, 4, 8, 6, 0, 4]
# ~ result: [1, 0, 0, 0, 2, 0, 1, 2, 4, 0]

# ~ 3. Транспонирование матрицы.

a = [[random.randint(-99, 99) for j in range(10)] for i in range(10)]

def trans(a):
    print("source:")
    # ~ pp(a)
    mprint(a)

    r = copy.deepcopy(a)

    for i in range(len(r)):
        for j in range(i):
            r[i][j], r[j][i] = r[j][i], r[i][j]

    print("result:")
    # ~ pp(r)
    mprint(r)

trans(a)

# ~ source:
# ~ [[-59, 15, -6, -16, 61, -56, 29, -26, -34, 75],
 # ~ [10, 21, -74, -60, 65, 37, -37, -48, 83, 27],
 # ~ [37, 95, 90, -12, -84, 32, 78, 62, -23, -89],
 # ~ [63, 53, 43, -53, -40, -56, 17, -6, -18, 20],
 # ~ [36, 95, 9, 17, -36, 80, -13, -11, -31, 41],
 # ~ [79, 69, -75, -9, 54, -97, 50, -69, 69, 22],
 # ~ [-98, 60, -29, 53, -35, -59, 84, 35, 96, -60],
 # ~ [-22, -36, -44, 7, 51, -63, -62, -81, -81, 1],
 # ~ [64, 54, 0, -11, -12, -52, -54, 97, 53, -22],
 # ~ [-6, 21, 3, -23, -39, -47, -41, 51, 89, 0]]
# ~ result:
# ~ [[-59, 10, 37, 63, 36, 79, -98, -22, 64, -6],
 # ~ [15, 21, 95, 53, 95, 69, 60, -36, 54, 21],
 # ~ [-6, -74, 90, 43, 9, -75, -29, -44, 0, 3],
 # ~ [-16, -60, -12, -53, 17, -9, 53, 7, -11, -23],
 # ~ [61, 65, -84, -40, -36, 54, -35, 51, -12, -39],
 # ~ [-56, 37, 32, -56, 80, -97, -59, -63, -52, -47],
 # ~ [29, -37, 78, 17, -13, 50, 84, -62, -54, -41],
 # ~ [-26, -48, 62, -6, -11, -69, 35, -81, 97, 51],
 # ~ [-34, 83, -23, -18, -31, 69, 96, -81, 53, 89],
 # ~ [75, 27, -89, 20, 41, 22, -60, 1, -22, 0]]

# ~ 4. Список заполнен нулями и единицами. Сколько там последовательностей из единиц (идущих подряд и разделённых нулями)?

a =  [random.randint(0, 1) for _ in range(10)]

def countseq(a):
    print("source:", a)
    
    nseq = 0
    inseq = 0
    
    for e in a:
        if e and not inseq:
            nseq += 1
            inseq = True
        elif not e:
            inseq = False

    print("result:", nseq, "sequences")

countseq(a)

# ~ source: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# ~ result: 5 sequences
# ~ source: [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
# ~ result: 3 sequences
# ~ source: [0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
# ~ result: 2 sequences
