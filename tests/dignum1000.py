#!/usr/bin/env python
# dignum1000.py
# (C) Mikhail Kolodin, 2023
# ver. 2023-05-31 2023-05-31 1.0

#Task 1578. Определить количество повторений каждой из цифр 0,1,2,...,9 в числе N^N (N в степени N), N <= 1000

def cntdig(n: int) -> list[int]:
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while n:
        ld = n % 10
        cnt[ld] += 1
        n //= 10
    return cnt

def cnt1000(lim: int = 10) -> list[list[int]]:
    res = []
    for row in range(1, lim+1):
        res += [cntdig(row**row)]
    return res

def show(n: int = 1):
    print((0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    arr = cnt1000(n)
    for row in enumerate(arr, 1):
        print(row)

show(1000)
