#!/usr/bin/env python

# sort-extern.py
# external sorting
# Mikhail (myke) Kolodin, 2024-2025
# 2024-10-02 2025-09-16 1.0
# внешняя сортировка

import random

a1 = [random.randint(-99, 99) for _ in range(10)]
a2 = [random.randint(-99, 99) for _ in range(10)]
a1.sort()
a2.sort()

print("исходные списки")

print(f"{a1=}")
print(f"{a2=}")

# а теперь
# типа a3 = a1 + a2
# но так, чтобы a3 тоже был отсортирован

print("неразрушающая сортировка")

a3 = []

p1 = p2 = 0

while p1 < len(a1) and p2 < len(a2):

    if a1[p1] < a2[p2]:
        a3.append(a1[p1])
        p1 += 1
    else:
        a3.append(a2[p2])
        p2 += 1

if p1 < len(a1):
    a3.extend(a1[p1:])

if p2 < len(a2):
    a3.extend(a2[p2:])

print(f"{a3=}")

print("разрушающая сортировка")

a3 = []

while a1 and a2:
    if a1[0] < a2[0]:
        a3.append(a1.pop(0))
    else:
        a3.append(a2.pop(0))

if a1:
    a3.extend(a1)
if a2:
    a3.extend(a2)

print(f"{a3=}")

