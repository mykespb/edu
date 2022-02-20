#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-05 2022-02-20 1.1
# guess-half.py

def help():
    print("""
Человек и машина играют в такую игру:
человек загадывает натуральное число в некотором диапазоне (напр., от 1 до 100),
а машина пытается угадать это число.
При этом загадавший отвечает на вопросы только “да” или “нет”.
Нужно справиться с отгадыванием за наименьшее количество попыток.
""")

def guess_iter(high=100):
    """машина угадывает"""
    low = 1
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

help()
guess_iter()
