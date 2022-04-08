#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-08 1.0
# rev-array.py

from random import randint as ri
a = [ri(-100, 100) for _ in range(10)]

print(a)

lena = len(a)
for i in range(lena // 2):
    a[i], a[lena-1-i] = a[lena-1-i], a[i]

print(a)

# ~ [-29, 55, -8, 90, 60, 35, -52, -89, -83, -83]
# ~ [-83, -83, -89, -52, 35, 60, 90, -8, 55, -29]
