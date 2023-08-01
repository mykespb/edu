#!/usr/bin/env python
# countzeros.py 2023-07-27 2023-07-27 1.3
# (C) Mikhail Kolodin, 2023

# Даётся квадратная матрица из отсортированных по ситрокам и столбцм нулей и единиц.
# Посчитать в ней нули.

def count_zeros1(mat):
    size = len(mat)
    summa = sum( [sum(mat[i])  for i in range(size) ] )
    zeros = size*size - summa
    return zeros

def count_zeros2(mat):
    size = len(mat)
    summa = sum(sum(l) for l in mat)
    zeros = size*size - summa
    return zeros

def count_zeros3(mat):
    size = len(mat)
    num = 0
    pos = size-1
    for i in range(size):
        for j in range(pos, -1, -1):
            if mat[i][j] == 0:
                num += j + 1
                pos = j
                break
    return num

m = [ [0, 0, 1],
      [0, 0, 1],
      [0, 1, 1]]

print(count_zeros3(m))

m = [ [0, 0, 0, 1],
      [0, 0, 0, 1],
      [0, 0, 1, 1]]

print(count_zeros3(m))
