#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-05-01 2.0
# rev-array.py
# переворот списка

from random import randint as ri
a = [ri(-100, 100) for _ in range(10)]

print("\n\n-------------------- version 1 ---------------------\n\n")

# правильно
print(a)

lena = len(a)
for i in range(lena // 2):
    a[i], a[lena-1-i] = a[lena-1-i], a[i]

print(a)

# ~ [-29, 55, -8, 90, 60, 35, -52, -89, -83, -83]
# ~ [-83, -83, -89, -52, 35, 60, 90, -8, 55, -29]

# типичная ошибка

print(a)

for i in range(lena):
    a[i], a[lena-1-i] = a[lena-1-i], a[i]

print(a)
# ~ [20, 92, 2, 44, -81, -29, 70, 66, -71, -23]
# ~ [20, 92, 2, 44, -81, -29, 70, 66, -71, -23]

print("\n\n-------------------- version 2 ---------------------\n\n")

print(a)

left  = 0
right = len(a)-1

while left < right:
    a[left], a[right] = a[right], a[left]
    left  += 1
    right -= 1

print(a)

# ~ -------------------- version 2 ---------------------


# ~ [-94, -69, 36, -90, 26, 23, -97, 57, -79, 20]
# ~ [20, -79, 57, -97, 23, 26, -90, 36, -69, -94]
