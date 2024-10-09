#!usr/bin/env python
# Mikhail Kolodin, 2024
# list-info.py
# 2024-10-09 2024-10-09 1.0
# получение информации по спискам и прочие спецштучки

import random

#1. Задача: узнать, верно ли, что в заданном случайном списке целых чисел все числа больше нуля

def p1():
    for _ in range(10):
        a = [random.randint(0, 9) for _ in range(10)]
        print( ["не", ""][all( [ e > 0 for e in a ] )],
            "все элементы списка", a, "положительны")

# ~ p1()

 # ~ все элементы списка [6, 2, 6, 8, 1, 3, 3, 7, 3, 7] положительны
# ~ не все элементы списка [6, 1, 8, 8, 6, 5, 2, 8, 0, 8] положительны
 # ~ все элементы списка [6, 4, 2, 3, 2, 3, 2, 4, 7, 5] положительны
 # ~ все элементы списка [7, 9, 2, 3, 2, 6, 9, 4, 7, 1] положительны
# ~ не все элементы списка [2, 5, 4, 0, 8, 6, 0, 9, 9, 5] положительны
 # ~ все элементы списка [4, 5, 5, 2, 6, 9, 6, 9, 6, 5] положительны
# ~ не все элементы списка [9, 5, 5, 5, 3, 4, 0, 7, 8, 4] положительны
# ~ не все элементы списка [9, 0, 0, 7, 4, 1, 5, 2, 9, 8] положительны
 # ~ все элементы списка [4, 6, 6, 9, 1, 9, 1, 5, 7, 3] положительны
# ~ не все элементы списка [3, 1, 6, 4, 0, 1, 4, 1, 7, 8] положительны

#2. Задача: узнать, верно ли, что в заданном случайном списке целых чисел есть хотя бы одно число, кратное 5

def p2():

    elems = [1, 2, 3, 4, 6, 7, 8, 9, 0]
    for _ in range(10):
        a = [random.choice(elems) for _ in range(10)]
        print( "есть такие элементы," if any([ e % 5 == 0 for e in a ] ) else "нет таких элементов,",
            "чтобы на 5 нацело делились в списке", a)

p2()

