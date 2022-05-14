#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-14 2022-04-14 3.1
# howmany-defdict.py

# ~ ДЗ2. Сколько каких?
# ~ Дан случайный список вида
# ~ from random import randint as ri
# ~ a = [ri(0, 10) for _ in range(10)]
# ~ Определить, сколько каких чисел в нём.

from random import randint as ri
from collections import defaultdict

# задание
a = [ri(0, 10) for _ in range(10)]
print("вход:", a, "\n")

# решение

print("число сколько")

d= defaultdict(int)

for e in a:
    d[e] += 1

for e in sorted(d):
    print(f"{e:3}   {d[e]:4}")
