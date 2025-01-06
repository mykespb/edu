#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-01 2025-01-06 1.1
# ceasares.py

# ~ Вариации на тему шифра Цезаря
# ~ Работаем сразу с несколькими алфавитами,
# ~ кружим внутри каждого самого по себе,
# ~ а прочее вообще не трогаем, оставляем как есть...

digits = "0123456789"
lataz  = "abcdefghijklmnopqrstuvwxyz"
latAZ  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rusaya = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
rusAYA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

alfs = [digits, lataz, latAZ, rusaya, rusAYA]


def ceasar(text, shift):
    """shift string forward"""

    out = ""

    for char in text:
        for alf in alfs:
            if char in alf:
                out += alf [ (alf.index(char) + shift ) % len(alf) ]
                break
        else:
            out += char

    return out


def tests():

    text1 = "Hello to all! 2025"
    text2 = "Всем чмоки в этом чате! 2025"

    print(f"{text1=}")
    print(f"{text2=}")

    koded1 = ceasar(text1, 3)
    koded2 = ceasar(text2, 3)

    print(f"{koded1=}")
    print(f"{koded2=}")

    dekoded1 = ceasar(koded1, -3)
    dekoded2 = ceasar(koded2, -3)

    print(f"{dekoded1=}")
    print(f"{dekoded2=}")


tests()


# ~ text1='Hello to all! 2025'
# ~ text2='Всем чмоки в этом чате! 2025'
# ~ koded1='Khoor wr doo! 5358'
# ~ koded2='Ефзп ъпснл е ахсп ъгхз! 5358'
# ~ dekoded1='Hello to all! 2025'
# ~ dekoded2='Всем чмоки в этом чате! 2025'
