#!isr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.0
# list sorter by recollecting array

import random

arr = [random.randint(-99, 99) for _ in range(10)]
print("old:", arr)

newarr = []
while arr:
    elem = min(arr)
    newarr.append(elem)
    arr.remove(elem)

print("new:", newarr)
