#!/usr/bin/env python
# # Mikhail (myke) Kolodin

# 2022-05-05 2022-05-05 1.0
# arot1.py 

# ~ есть случайный список (м.б. 10 элементов, натуральные до 99),
# ~ сдвинуть все элементы по кругу, 
# ~ 0ой становится 1ым, 1ый - 2ым и т.д., 9ый -- 0ым.

from random import randint

arr = [randint(1, 99) for _ in range(10)]
print(arr)

arr = arr[-1:] + arr[:-1]
print(arr)

# ~ пример

# ~ [53, 48, 23, 67, 63, 7, 50, 15, 43, 90]

# ~ [90, 53, 48, 23, 67, 63, 7, 50, 15, 43]
