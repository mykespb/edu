#!/usr/bin/env python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-11-26 2021-11-30 1.2
# isnumber.py

print("""
Привет!
Давай поиграем в игру!

Человек вводит строку,
а машина определяет,
является ли эта строка целым числом
(возможно, со знаком).

Игра идёт по кругу, пока человек не введёт пустую строку
или строку из одной точки.""")

digits = "0123456789"

while True:
    human = input("\nВведи слово: ")
    if human == "" or human == ".":
        break

    if human.startswith("-") or human.startswith("+"):
        human = human[1:]

    for c in human:
        if c not in digits:
            print ("Нет, это не целое число.")
            break
    else:
        print ("Да, это целое число.")

print ("\nПока...")

# ~ вариант:
    # ~ if human[0] == "+":
        # ~ human = human[1:]
    # ~ elif human[0] == "-":
        # ~ human = human[1:]
