#!/usr/bin/env python
# myke 2022-05-06 2022-05-06 1.0
# set-list.py 

# ~ есть случайный список из целых чисел.
# ~ убрать из него все дубликаты (повторяющиеся элементы),
# ~ а оставшиеся упорядочить по убыванию

from random import randint

arr = [randint(1, 20) for _ in range(10)]
print(arr)

arr = sorted(set(arr), reverse=True)
print(arr)

# ~ пример работы
# ~ [5, 4, 5, 15, 11, 11, 1, 11, 18, 10]
# ~ [18, 15, 11, 10, 5, 4, 1]
