#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2024-11-04 2024-11-04 0.1
# ack-pairs.py

Даны пары ребят, знакомых друг с другом.
Но указаны не все пары.
А дружба - симметрична.
Определить, все ли ребята дружат между собой.

import random

def prepare():
    ...

def solve(data):
    ...

def main():
    data = prepare()
    print("Дано:", data)
    res  = solve(data)
    print("Все знакомы:", "да" if solve(data) else "нет")

main()
 
