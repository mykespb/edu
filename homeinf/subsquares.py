#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-11 2025-01-11 1.0
# subsquares.py

# ~ Субквадратная матрица 

# ~ Дана матрица целых чисел.
# ~ Она "субквадратная", если сумма чисел в любом подквадрате 2х2 положительна.
# ~ Проверить!


from random import random

# ------------------------------------
# создать матрицу

def create(size = 10):
    """создать маторицу,
    вернуть её же
    """

    return [ [ (random()-0.125)*10 for j in range(size) ] for i in range(size) ]


# ------------------------------------
# напечатать матрицу

def show(mat):
    """
    печатаем как таблицу, аккуратно, с округлением
    """

    size = len(mat)

    for i in range(size):
        for j in range(size):
            print( "%10.5f" % mat[i][j] , end=" ")
        print()


# ------------------------------------
# проверить матрицу

def test(mat):
    """
    тестируем матрицу на субквадратность
    """

    size = len(mat)

    for i in range(size-1):
        for j in range(size-1):
            if (minus := mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1]) <= 0:
                return False, minus

    return True,
    

# ------------------------------------
# всё протестировать

def main():
    """
    всё запускаем и смотрим
    """

    mat = create()
    show(mat)

    match test(mat):
        case (True,):
            print("OK, матрица субквадратная")
        case (False, minus):
            print(f"Не OK, матрица не субквадратная, с  минусом {minus}")
        

main()

# ------------------------------------
