#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-15 2022-04-15 1.1
# howmany-vars-match.py

# ~ ДЗ2. Сколько каких?
# ~ Дан случайный список вида
# ~ from random import randint as ri
# ~ a = [ri(0, 10) for _ in range(10)]
# ~ Определить, сколько каких чисел в нём.

from random import randint as ri

# задание
a = [ri(0, 10) for _ in range(10)]
print("вход:", a, "\n")

# решение на отдельных переменных
n0 = n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n10 = 0

print("число сколько")

for e in a:
    match e:
        case 0:
            n0 += 1
        case 1:
            n1 += 1
        case 2:
            n2 += 1
        case 3:
            n3 += 1
        case 4:
            n4 += 1
        case 5:
            n5 += 1
        case 6:
            n6 += 1
        case 7:
            n7 += 1
        case 8:
            n8 += 1
        case 9:
            n9 += 1
        case 10:
            n10 += 1

# печать результата
if n0 > 0:
    print(f"{0:3}   {n0:4}")
if n1 > 0:
    print(f"{1:3}   {n1:4}")
if n2 > 0:
    print(f"{2:3}   {n2:4}")
if n3 > 0:
    print(f"{3:3}   {n3:4}")
if n4 > 0:
    print(f"{4:3}   {n4:4}")
if n5 > 0:
    print(f"{5:3}   {n5:4}")
if n6 > 0:
    print(f"{6:3}   {n6:4}")
if n7 > 0:
    print(f"{7:3}   {n7:4}")
if n8 > 0:
    print(f"{8:3}   {n8:4}")
if n9 > 0:
    print(f"{9:3}   {n9:4}")
if n10 > 0:
    print(f"{10:3}   {n10:4}")
