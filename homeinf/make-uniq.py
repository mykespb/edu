#!/usr/bin/env python
# myke 2022-05-13 2022-05-13 3.0
# make-uniq.py 

# ~ Дан список. Удалить из него повторяющиеся элементы
# ~ (оставить всех по одному).

from random import randint

def make(size=9):
    """создать список"""
    
    return [randint(1, 9) for _ in range(size)]

def proc1(arr):
    """обработка. версия 1"""
    
    return list(set(arr))
    
def proc2(arr):
    """обработка. версия 2"""
    
    nova = []
    for elem in arr:
        if elem not in nova:
            nova.append(elem)
            
    return nova

from collections import Counter

def proc3(arr):
    """обработка. версия 3"""
    
    cnt = Counter(arr)
    nova = []
    for k in cnt.keys():
        nova.append(k)    
    return nova
        
def proc4(arr):
    """обработка. версия 4"""
    
    cnt = Counter(arr)
    return list(cnt.keys())

def proc5(arr):
    """обработка. версия 5"""
    
    a = arr[:]
    nova = []
    while a:
        elem = a.pop(0)
        nova.append(elem)
        num = a.count(elem)
        for i in range(num):
            a.remove(elem)
        
    return nova
    
def tests(proc, times=3, size=9):
    print("\ntesting:", proc.__name__)
    for test in range(times):
        arr = make(size)
        print(f"\nwas ({len(arr)}):", arr)
        uniq = sorted(proc(arr))
        print(f"now ({len(uniq)}):", uniq)
        
tests(proc1)
tests(proc2)
tests(proc3)
tests(proc4)
tests(proc5)

# examples of work

# ~ testing: proc1

# ~ was (9): [9, 4, 4, 2, 4, 8, 6, 6, 9]
# ~ now (5): [2, 4, 6, 8, 9]

# ~ was (9): [9, 3, 4, 4, 7, 1, 1, 6, 9]
# ~ now (6): [1, 3, 4, 6, 7, 9]

# ~ was (9): [6, 4, 3, 5, 1, 1, 5, 2, 6]
# ~ now (6): [1, 2, 3, 4, 5, 6]

# ~ testing: proc2

# ~ was (9): [1, 1, 1, 8, 2, 4, 2, 7, 6]
# ~ now (6): [1, 2, 4, 6, 7, 8]

# ~ was (9): [3, 2, 8, 2, 2, 6, 4, 9, 3]
# ~ now (6): [2, 3, 4, 6, 8, 9]

# ~ was (9): [1, 5, 4, 1, 4, 3, 8, 8, 5]
# ~ now (5): [1, 3, 4, 5, 8]

# ~ testing: proc3

# ~ was (9): [8, 5, 4, 9, 8, 1, 3, 6, 6]
# ~ now (7): [1, 3, 4, 5, 6, 8, 9]

# ~ was (9): [3, 4, 4, 3, 6, 1, 4, 9, 4]
# ~ now (5): [1, 3, 4, 6, 9]

# ~ was (9): [5, 4, 2, 3, 9, 1, 5, 1, 7]
# ~ now (7): [1, 2, 3, 4, 5, 7, 9]

# ~ testing: proc4

# ~ was (9): [3, 3, 6, 2, 4, 4, 7, 9, 9]
# ~ now (6): [2, 3, 4, 6, 7, 9]

# ~ was (9): [2, 6, 7, 1, 7, 4, 6, 8, 6]
# ~ now (6): [1, 2, 4, 6, 7, 8]

# ~ was (9): [6, 6, 4, 2, 2, 4, 8, 3, 2]
# ~ now (5): [2, 3, 4, 6, 8]

# ~ testing: proc5

# ~ was (9): [5, 5, 1, 2, 6, 6, 9, 5, 7]
# ~ now (6): [1, 2, 5, 6, 7, 9]

# ~ was (9): [1, 4, 4, 5, 1, 8, 3, 8, 3]
# ~ now (5): [1, 3, 4, 5, 8]

# ~ was (9): [3, 9, 2, 4, 2, 5, 8, 6, 4]
# ~ now (7): [2, 3, 4, 5, 6, 8, 9]
