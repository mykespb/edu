#!/usr/bin/env python
# fizbuzz.py 2023-07-27 2023-07-27 0.1
# (C) Mikhail Kolodin, 2023

# Напишите программу, которая выводит на экран чис-
# ла от 1 до 100. При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz», а вместо
# чисел, кратных пяти — слово «Buzz». Если число
# кратно и 3, и 5, то программа должна выводить сло-
# во «FizzBuzz». Это программная реализация детской
# игры, в которой игроки должны по очереди называть
# числа или слова «Fizz», «Buzz» и «FizzBuzz» по тем
# же правилам.

def fizbuzz1():
    for i in range(1,101):
        if i % 15 == 0:
            print("FizBuzz", end=" ")
        elif i % 3 == 0:
            print("Fiz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# fizbuzz1()

def fizbuzz2():
    for i in range(1, 101):
        out = ""
        if i % 3 == 0:
            out += "Fiz"
        if i % 5 == 0:
            out += "Buzz"
        if len(out):
            print(out, end=" ")
        else:
            print(i, end=" ")
        
fizbuzz2()

