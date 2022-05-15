#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-15 2022-04-15 1.1
# howmany-bigvar.py

# ~ ДЗ2. Сколько каких?
# ~ Дан случайный список вида
# ~ from random import randint as ri
# ~ a = [ri(0, 10) for _ in range(10)]
# ~ Определить, сколько каких чисел в нём.

from random import randint as ri

# задание
a = [ri(0, 9) for _ in range(10)]
print("вход:", a, "\n")

# решение на большом числе
big = 0

print("число сколько")

for e in a:
    big += 10**e

# печать результата
for i in range(10):
    num = big % 10
    big //= 10
    if num:
        print(f"{i:3}   {num:4}")


# ~ вход: [9, 0, 6, 3, 0, 1, 5, 0, 3, 5] 

# ~ число сколько
  # ~ 0      3
  # ~ 1      1
  # ~ 3      2
  # ~ 5      2
  # ~ 6      1
  # ~ 9      1
