#!/usr/bin/env python
# Mikhail Kolodin, 2024
# list-search-simple.py
# 2024-10-08 2024-10-11 1.2
# найти целое значение в списке

import random

a = [random.randint(0, 9) for _ in range(10)]

def find1(lst, val):
    """ищем число val в списке lst.
    возвращает True/ Fasle"""
    
    if not lst: return False

    return val in lst


def find2(lst, val):
    """ищем число val в списке lst.
    возвращает True/ Fasle"""
    
    if not lst: return False

    for e in lst:
        if e == val:
            return True

    return False
    

def find3(lst, val):
    """ищем число val в списке lst.
    возвращает True/ Fasle"""
    
    if not lst: return False

    for i in range(len(lst)):
        if lst[i] == val:
            return True, i

    return False, -1
    
                
    
print(f"{a=},  0 => \t{find1(a, 0)}\t{find2(a, 0)}\t{find3(a, 0)}")
print(f"{a=}, -1 => \t{find1(a, -1)}\t{find2(a, -1)}\t{find3(a, -1)}")
print(f"{a=},  1 => \t{find1(a, 1)}\t{find2(a, 1)}\t{find3(a, 1)}")

# ~ a=[9, 1, 1, 8, 5, 3, 9, 6, 8, 3],  0 =>     False   False   (False, -1)
# ~ a=[9, 1, 1, 8, 5, 3, 9, 6, 8, 3], -1 =>     False   False   (False, -1)
# ~ a=[9, 1, 1, 8, 5, 3, 9, 6, 8, 3],  1 =>     True    True    (True, 1)

