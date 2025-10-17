#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-10-17 2025-10-17 1.0
# same-num-matrices.py

# ~ Даны 2 матрицы целых чисел.
# ~ Верно ли, что они составлены из одних и тех же чисел
# ~ (в произвольном порядке)?


from random import random, randint, shuffle
from pprint import pp, pprint

# размеры, но это неизвестно
L1, C1, L2, C2 = 2, 6, 3, 4
# вероятность сбоя
PROB = 0.3
# верхнее число
LIMIT = 100

def make():
    """make 2 matrices"""

    src1 = [randint(1, LIMIT) for _ in range(L1*C1)]
    src2 = src1[:]
    shuffle(src2)

    if random() < PROB:
        src1[0] = 77
        shuffle(src1)

    m1 = [[0 for _ in range(C1)] for _ in range(L1)]
    m2 = [[0 for _ in range(C2)] for _ in range(L2)]

    for i in range(L1):
        for j in range(C1):
            m1[i][j] = src1.pop()
    for i in range(L2):
        for j in range(C2):
            m2[i][j] = src2.pop()
            
    return m1, m2


def compare(m1, m2):
    """compare 2 matrices"""

    # linearize
    rm1 = [ m1[j][i] for i in range(len(m1[0])) for j in range(len(m1)) ] 
    rm2 = [ m2[j][i] for i in range(len(m2[0])) for j in range(len(m2)) ]

    # ~ print(f"{rm1=}")
    # ~ print(f"{rm2=}")

    return sorted(rm1) == sorted(rm2)
    

def main():
    """run it"""

    m1, m2 = make()
    pp(m1)
    pp(m2)

    print("матрицы", "одинаковые" if compare(m1, m2) else "разные")


main()


# ~ результат:

# ~ [[39, 78, 73, 60, 80, 98], [69, 73, 56, 77, 81, 23]]
# ~ [[60, 56, 78, 23], [81, 39, 63, 73], [80, 98, 69, 73]]
# ~ матрицы разные

# ~ [[47, 31, 46, 55, 100, 65], [40, 28, 87, 94, 74, 59]]
# ~ [[28, 74, 100, 59], [55, 40, 87, 65], [46, 47, 31, 94]]
# ~ матрицы одинаковые
