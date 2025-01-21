#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-26 2021-11-27 1.2
# longstr.py

print ("""
Привет!
Давай поиграем в игру!

Человек и машина играют в слова так:
человек вводит строку,
а машина определяет,
какое слово в ней самое длинное
(если таких несколько, подойдёт любое).
Игра идёт по кругу, пока человек не введёт пустую строку
или строку из одной точки.""")

while True:
    human = input("\nВведи строку: ")
    if human == "" or human == ".":
        break

    maxlen = 0
    maxword = ""
    for word in human.split():
        thislen = len(word)

        if thislen > maxlen:
            maxlen = thislen
            maxword = word

    print (f"Самое длинное слово: '{maxword}' с длиной {maxlen}")

print ("\nПока...")
