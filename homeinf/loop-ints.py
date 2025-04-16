#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2025
# 2025-04-14 2025-04-16 1.1
# loop-ints.py

# ~ Цепочка чисел

# ~ Дана последовательность целых чисел (список целых).
# ~ Верно ли, что каждое следующее число начинается с последней цифры предыдущего.
# ~ (Есть нули и отрицательные).

from random import randint

def make(long = 10):
    arr = []
    prev = 1
    for _ in range(long):
        nova = (-1)**(randint(0, 1)) * (prev*100 + randint(0, 99))
        prev = abs(nova) % 10
        arr.append(nova)
    return arr

def test(arr):
    long = len(arr)
    print(arr, end = ' -> ')
    arr = list(map(abs, arr))
    
    old = arr[0] % 10
    for i in range(1, long):
        num = arr[i]
        last = num % 10
        while num > 9:
            num //= 10
        if old != num:
            print("no chain")
            return
        old = last
    print("has chain")


arr = make()
test(arr)
# ~ print(arr)

# ~ [-158, 841, -113, -380, -74, -418, 813, 378, -815, 582] -> no chain
# ~ [103, -345, -542, 229, 933, 385, -578, 857, -778, -848] -> has chain
