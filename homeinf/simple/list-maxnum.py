#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-07 2022-03-07 1.0
# list-maxnum.py

# ~ Сколько раз встречается в списке максимальное значение?
# ~ (функцию max не использовать)

import random
spisok = [random.randint(1, 3) for _ in range(10)]

print("исходный список:", spisok)

maxnum = spisok[0]
maxtimes = 1

for e in spisok[1:]:
    if e == maxnum:
        maxtimes += 1
    elif e> maxnum:
        maxnum = e
        maxtimes = 1

print("максимум", maxnum, "встречается", maxtimes, "раз(а)")
