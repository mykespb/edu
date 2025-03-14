#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-12-03 2021-12-03 1.0
# bigroom.py

# ~ Юзер вводит пары чисел,
# ~ которые представляют собой размеры комнаты
# ~ (прямоугольник, длина и ширина, в метрах).
# ~ Когда перечисление комнат закончится,
# ~ юзер вводит пустую строку.
# ~ Найти самую большую комнату.

maxx = maxy = maxsq = 0

while True:
    s = input ("ещё комнату, пожалуйста: длину и ширину: ").strip()
    if not s:
        break

    x, y = s.split()
    x = int (x)
    y = int (y)

    sq = x * y

    if sq > maxsq:
        maxsq = sq
        maxx = x
        maxy = y

print (f"\nрезультат: самая большая комната со сторонами {maxx} и {maxy} "
    f"имеет размер {maxsq}")
