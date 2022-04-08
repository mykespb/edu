#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-08 1.1
# howmany-int.py

# ~ ДЗ2. Сколько каких?
# ~ Дан случайный список вида
# ~ from random import randint as ri
# ~ a = [ri(0, 10) for _ in range(10)]
# ~ Определить, сколько каких чисел в нём.

from random import randint as ri

# задание
a = [ri(0, 10) for _ in range(10)]
print("вход:", a, "\n")

# решение
a.sort()
print("сорт:", a, "\n")

print("число сколько")
what = many = -1

for e in a:
    if what == -1:
        what = e
        many = 1
        continue
    if what == e:
        many += 1
        continue
    print(f"{what:3}   {many:4}")
    what = e
    many = 1

print(f"{what:3}   {many:4}")
