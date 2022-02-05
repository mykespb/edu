#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-05 2022-02-05 1.0
# guess-half.py

MAX = 100

def help():
    ...

def guess_iter():
    """машина угадывает"""
    low = 1
    high = 100
    while low != high:
        mid = low + (high - low) // 2
        yn = input(f"ваше число больше {mid}?  ")
        if not yn: continue
        yn = yn[0].lower() == "д"
        if yn:
            low = mid+1
        else:
            high = mid
    print("вы загадали", low)

guess_iter()
