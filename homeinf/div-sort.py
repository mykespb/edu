#!/usr/bin/env python
# myke 2022-04-26 2022-04-26 1.1
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


# ~ primes: [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# ~ divisors: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 4, 6, 8, 9, 10, 14, 15, 21, 22, 25, 26, 27, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 12, 16, 18, 20, 24, 28, 30, 36, 40, 42, 44, 45, 50, 52, 54, 56, 63, 64, 66, 68, 70, 75, 76, 78, 81, 88, 92, 98, 99, 32, 48, 60, 72, 80, 84, 90, 100, 96]
