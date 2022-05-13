#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-14 3.0
# howmany-counter.py

# ~ ДЗ2. Сколько каких?
# ~ Дан случайный список вида
# ~ from random import randint as ri
# ~ a = [ri(0, 10) for _ in range(10)]
# ~ Определить, сколько каких чисел в нём.

from random import randint as ri
from collections import Counter

# задание
a = [ri(0, 10) for _ in range(10)]
print("вход:", a, "\n")

# решение

print("число сколько")

cnt = Counter(a)

for e in sorted(cnt):
    print(f"{e:3}   {cnt[e]:4}")
