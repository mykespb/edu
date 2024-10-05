#!usr/bin/env python
# Mikhail Kolodin, 2024
# 2024-10-05 2024-10-05 1.0
# list bubble sorter 

import random

arr = [random.randint(-99, 99) for _ in range(10)]
print("old:", arr)

def sorter(arr):
    if not arr: return []

    need = True
    while need:
        need= False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                need = True

sorter(arr)

print("new:", arr)

# ~ old: [-28, -67, 18, -21, -37, -65, 59, -56, 96, -99]
# ~ new: [-99, -67, -65, -56, -37, -28, -21, 18, 59, 96]
