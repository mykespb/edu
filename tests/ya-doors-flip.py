#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-06 2023-02-07 1.0
# ya-doors-flip.py

# ~ Есть сто дверей, 1..100.
# ~ При каждом проходе человек меняет состояние дверей с номерами, кратными номеру прохода
# ~ (от 1 до 100).
# ~ Какие двери останутся открытыми после всех 100 проходов?

LEN = 100

doors = [False for _ in range(LEN+1)]

def runs():
    for run in range(1, LEN+1):
        for door in range(1, LEN+1):
            if door % run == 0:
                doors[door] = not doors[door]

def runs():
    for run in range(1, LEN+1):
        for door in range(1, LEN+1):
            if door % run == 0:
                doors[door] = not doors[door]

runs()

for n, e in enumerate(doors[1:], start=1):
    if e:
        print(n, end=' ')

# ~ 1 4 9 16 25 36 49 64 81 100 

# это квадраты
