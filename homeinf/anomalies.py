#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-26 2025-02-26 1.1
# anomalies.py

# ~ Есть ряд данных (неотрицательных).
# ~ Все, кроме крайних, могут быть ошибочными - аномальными.
# ~ Это так, если они не находятся по величине между своими соседями.
# ~ Найти и устранить аномалии.

# параметры задачи
IFROM = 0       # нижняя граница
ITO   = 100     # верхняя граница
MANY  = 100     # сколько элементов в данных


from itertools import compress
import random


def generate(many = MANY):
    """создать набор данных"""

    return [ random.randint(IFROM, ITO) for _ in range(many) ]


def improve(arr):

    # array to compress
    comp = [1]

    for i in range(1, len(arr) - 1):
        comp.append(
            arr[i-1] <= arr[i] <= arr[i+1]
            or
            arr[i-1] >= arr[i] >= arr[i+1]
            )

    comp.append(1)

    return compress(arr, comp)


def main():
    """запуск всего"""

    arr = generate(10)
    print("исходные данные:", arr)
    imp = list(improve(arr))
    print("лучшие данные:  ", imp)
    
    
main()


# ~ исходные данные: [30, 84, 37, 18, 16, 35, 25, 11, 98, 10]
# ~ лучшие данные:   [30, 37, 18, 25, 10]

# ~ исходные данные: [56, 28, 43, 22, 93, 15, 29, 56, 98, 65]
# ~ лучшие данные:   [56, 29, 56, 65]

# ~ исходные данные: [48, 28, 89, 95, 54, 72, 86, 40, 69, 100]
# ~ лучшие данные:   [48, 89, 72, 69, 100]
