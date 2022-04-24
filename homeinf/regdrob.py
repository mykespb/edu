#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-23 2022-04-24 1.1
# regdrob.py

# ~ Дан список натуральных чисел.
# ~ Найти минимальную и максимальную правильные дроби,
# ~ которые можно составить из попарно взятых разных чисел из заданного списка.

from random import randint as ri

# параметры задачи

MAX = 100     # макс число
LEN = 20      # количество чисел

# задаём список

lon = [ri(1, MAX) for _ in range(LEN)]
print("числа:", lon)

# решаем

# строим список допустимых дробей
lod = []

for a in lon:
    for b in lon:
        if a >= b:
            continue
        q = a / b
        lod.append((q, a, b))

# сортируем
lod.sort()

# результат

print(f"""
итого:
минимум:  {lod[0][0] : 10.6} при {lod[0][1]} / {lod[0][2]}
максимум: {lod[-1][0] : 10.6} при {lod[-1][1]} / {lod[-1][2]}
""")


# ~ пример расчёта:

# ~ числа: [51, 46, 43, 29, 100, 69, 72, 68, 14, 95, 11, 71, 11, 90, 34, 31, 4, 56, 3, 29]

# ~ итого:
# ~ минимум:        0.03 при 3 / 100
# ~ максимум:   0.986111 при 71 / 72

# ~ пример расчёта:

# ~ числа: [49, 49, 35, 25, 9, 13, 40, 86, 24, 77, 21, 37, 90, 88, 4, 28, 85, 67, 51, 80]

# ~ итого:
# ~ минимум:   0.0444444 при 4 / 90
# ~ максимум:   0.988372 при 85 / 86
