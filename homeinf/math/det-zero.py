#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-08-12 2026-08-12 1.0
# det-zero.py

# ~ Содержит ли данная (случайная) матрица 3 порядка хотя бы одну подматрицу с нулевым определителем
# ~ (включая саму исходную матрицу).

# ~ Нахождение определителя матрицы 1x1, 2х2 или 3х3.
# ~ https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C

from random import randint


# range of numbers in random matrix
RANGE_FROM = 1
RANGE_TO   = 4


def det1(m):
    """det matrix x1"""

    return m[0][0]


def det2(m):
    """det matrix x2"""

    return m[0][0] * m[1][1] - m[0][1] * m [1][0]


def det3(m):
    """det matrix x3"""

    return (m[0][0] * m[1][1] * m[2][2]
        - m[0][0] * m[1][2] * m[2][1]
        - m[0][1] * m[1][0] * m[2][2]
        + m[0][1] * m[1][2] * m[2][0]
        + m[0][2] * m[1][0] * m[2][1]
        - m[0][2] * m[1][1] * m[2][0]
        )


def gen_matrix():
    """generate random matrix"""

    return [
        [ randint(RANGE_FROM, RANGE_TO) for _ in range(3) ]
        for _ in range(3)
        ]

# ~ print(gen_matrix())


def solve(m):
    """solve for given matrix"""

    return any( [has_1(m), has_2(m), has_3(m)] )


def has_1(m):
    """if m has zero determinator"""

    for i in range(3):
        for j in range(3):
            if det1( [[m[i][j]]] ) == 0:
                return True

    return False


def has_2(m):
    """if m has zero determinator"""

    for i in range(3-1):
        for j in range(3-1):
            sm = [ [ m[i][j], m[i][j+1] ],
                   [ m[i+1][j], m[i+1][j+1] ] ]
            
            if det2(sm) == 0:
                return True

    return False

    
def has_3(m):
    """if m has zero determinator"""

    return det3(m) == 0

    
def main():
    """do all"""

    mat = gen_matrix()
    res = solve(mat)
    print(f"{mat=} => {res}")


main()
