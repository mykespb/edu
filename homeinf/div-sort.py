#!/usr/bin/env python
# myke 2022-04-26 2022-04-26 1.0
# div-sort.py 

# Первые 100 натуральных чисел упорядочить по количеству их делителей.

from math import isqrt

def primes(lim=100):
    """получить таблицу простых чисел до lim"""
    pt = []
    for num in range(2, lim):
        for diver in range(2, isqrt(num)):
            if num % diver == 0:
                break
        else:
            pt.append(num)
    return pt
    
pt = primes(100)
print("primes:", pt)

def devs(num):
    """сколько делителей"""
    res = 0
    while num>1:
        for diver in pt:
            if num % diver == 0:
                # ~ print(num , diver)
                res += 1
                num //= diver
    return res
    
def order(num=100):
    """упорядочиваем"""
    nums = [x for x in range(2, num+1)]
    nums.sort(key = devs)
    return nums
    
print("divisors:", order())
