#!/usr/bin/env python
# Mikhail Kolodin, 2024
# list-search-simple.py
# 2024-10-08 2024-10-11 1.1
# найти целое значение в списке

import random

a = [random.randint(0, 9) for _ in range(10)]

def find1(lst, val):
    """ищем число val в списке lst.
    возвращает True/ Fasle"""
    
    if not lst: return False

    return val in lst


print(f"{a=}, 0 => {find1(a, 0)}")
print(f"{a=}, -1 => {find1(a, -1)}")
print(f"{a=}, 1 => {find1(a, 1)}")

# ~ a=[0, 3, 4, 8, 0, 2, 1, 6, 2, 2], 0 => True
# ~ a=[0, 3, 4, 8, 0, 2, 1, 6, 2, 2], -1 => False
# ~ a=[0, 3, 4, 8, 0, 2, 1, 6, 2, 2], 1 => True
