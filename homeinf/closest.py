#!/usr/bin/env python

# Mikhail Kolodin
# 2022-04-22 2022-04-22 v.1.1

# ~ Дан список случайных натуральных чисел.
# ~ Найти пару ближайших чисел.
# ~ (Если их несколько, показать все).

from random import randint as ri

# параметры
MAX = 100     # макс. нат. число
LEN = 10      # длина списка

# формируем случайный список
lon = [ri(1, MAX) for _ in range(LEN)]
print("исходный список:\n", lon)

# находим ближайшие

# упорядочиваем список
lon.sort()
print("упорядоченный список:\n", lon)

# строим список расстояний
lod = [(lon[i] - lon[i-1], lon[i-1], lon[i]) for i in range(1, len(lon))]
print("список расстояний:\n", lod)

# сортируем список расстояний
lod.sort()
print("упорядоченный список расстояний:\n", lod)

# находим мин. расстояние
mindist = lod[0][0]
print("\nрезультат:\nмин. расстояние равно", mindist)

# распечатываем все пары с минимальным расстоянием
for element in lod:
    if element[0] == mindist:
        print("пара: от", element[1], "до", element[2])
    else:
        break

# прощаемся
print("\nконец. спасибо всем...")


# ~ исходный список:
 # ~ [11, 3, 80, 27, 48, 93, 12, 70, 69, 10]
# ~ упорядоченный список:
 # ~ [3, 10, 11, 12, 27, 48, 69, 70, 80, 93]
# ~ список расстояний:
 # ~ [(7, 3, 10), (1, 10, 11), (1, 11, 12), (15, 12, 27), (21, 27, 48), (21, 48, 69), (1, 69, 70), (10, 70, 80), (13, 80, 93)]
# ~ упорядоченный список расстояний:
 # ~ [(1, 10, 11), (1, 11, 12), (1, 69, 70), (7, 3, 10), (10, 70, 80), (13, 80, 93), (15, 12, 27), (21, 27, 48), (21, 48, 69)]

# ~ результат:
# ~ мин. расстояние равно 1
# ~ пара: от 10 до 11
# ~ пара: от 11 до 12
# ~ пара: от 69 до 70

# ~ конец. спасибо всем...
