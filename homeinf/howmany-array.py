#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-15 2022-04-15 1.1
# howmany-array.py

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
cnt = [0 for _ in range(11)]

print("число сколько")

for e in a:
    cnt[e] += 1

# печать результата
for i in range(10):
    e = cnt[i]
    if e == 0:
        continue
    print(f"{i:3}   {e:4}")

# ~ вход: [2, 6, 8, 4, 0, 5, 7, 0, 9, 5] 

# ~ число сколько
  # ~ 0      2
  # ~ 2      1
  # ~ 4      1
  # ~ 5      2
  # ~ 6      1
  # ~ 7      1
  # ~ 8      1
  # ~ 9      1
