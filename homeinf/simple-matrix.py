#!/usr/bin/env python
# Mikhail Kolodin, 2024
# simple-matrix.py
# 2024-10-15 2024-10-18 4.3
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

# ~ 1. Перевернуть список (1-мерный). Операцией [::-1] и функцией list.reverse() не пользоваться.
# ~ Обратить внимание на не- и разрушающие преобразования.

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

# 1.3
def t13(a):
    print("source:", a)
    r = []

    while a:
        r.append(a.pop())
    
    print("result:", r)

# ~ t13(a)

# ~ 2. Матрица заполнена натуральными числами до 10. Сколько каких?
# ~ Counter не использовать.

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
    mprint(a)

    r = copy.deepcopy(a)

    for i in range(len(r)):
        for j in range(i):
            r[i][j], r[j][i] = r[j][i], r[i][j]

    print("result:")
    mprint(r)

# ~ trans(a)

# ~ source:
  # ~ 58  76 -92  89  53  14  15  52 -54  88
 # ~ -21 -83 -58 -92   6 -81  10   0  30 -81
  # ~ 82 -35  -8  12  65  62 -36  -6  89  11
 # ~ -23  34  20  92  83  63  87  21 -26 -13
 # ~ -37  93 -58 -50   7 -77   8  29  32  92
  # ~ 72  78 -76 -35 -29 -75 -43  31  91 -20
 # ~ -65 -59  73  -6 -81 -90 -13 -47  99 -14
  # ~ 33 -90 -93  26 -93 -93 -10  67 -57 -95
  # ~ 94  84  -3 -34 -62 -63 -28 -80  18 -19
 # ~ -36  73  38 -73 -85  88 -60  41  86 -87
# ~ result:
  # ~ 58 -21  82 -23 -37  72 -65  33  94 -36
  # ~ 76 -83 -35  34  93  78 -59 -90  84  73
 # ~ -92 -58  -8  20 -58 -76  73 -93  -3  38
  # ~ 89 -92  12  92 -50 -35  -6  26 -34 -73
  # ~ 53   6  65  83   7 -29 -81 -93 -62 -85
  # ~ 14 -81  62  63 -77 -75 -90 -93 -63  88
  # ~ 15  10 -36  87   8 -43 -13 -10 -28 -60
  # ~ 52   0  -6  21  29  31 -47  67 -80  41
 # ~ -54  30  89 -26  32  91  99 -57  18  86
  # ~ 88 -81  11 -13  92 -20 -14 -95 -19 -87


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

# ~ countseq(a)

# ~ source: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
# ~ result: 5 sequences
# ~ source: [0, 0, 1, 1, 1, 0, 0, 1, 0, 1]
# ~ result: 3 sequences
# ~ source: [0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
# ~ result: 2 sequences

# ~ 5. След матрицы

def make1dim(elems=3, bottom=0, top=9):
    return [ random.randint(bottom, top) for c in range(elems) ] 
    
def make2dim(rows=3, cols=3, bottom=0, top=9):
    return [ [ random.randint(bottom, top) for c in range(cols) ] for r in range(rows) ]
    
def trace1(a):
    summa = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == j:
                summa += a[i][j]
    return summa

def trace2(a):
    summa = 0
    for i in range(len(a)):
        summa += a[i][i]
    return summa

def trace3(a):
    return sum(a[i][i] for i in range(len(a)))

def test_trace():
    a = make2dim()
    mprint(a)
    print("след матрицы равен", trace1(a), trace2(a), trace3(a))

test_trace()

   # ~ 3   8   7
   # ~ 0   5   0
   # ~ 3   2   7
# ~ след матрицы равен 15 15 15
