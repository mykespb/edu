#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-26 2021-12-24 1.1
# whatword.py

print("""
Привет!
Давай поиграем в игру!

Человек и машина играют в слова так:
человек вводит слово,
а машина определяет, что это:
слово на русском языке,
слово на английском языке,
натуральное число,
ничего из перечисленного.
Игра идёт по кругу, пока человек не введёт пустую строку
или строку из одной точки.""")

eng = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
dig = "0123456789"

while True:
    human = input("\nвведи слово: ")
    if human == "" or human == ".":
        break

    iseng = all([ (c in eng) for c in human ])
    isrus = all([ (c in rus) for c in human ])
    isnum = all([ (c in dig) for c in human ])

    print ("это слово", "английское" if iseng else
        "русское" if isrus else
        "число" if isnum else
        "непонятно что")

print ("\nПока...")

