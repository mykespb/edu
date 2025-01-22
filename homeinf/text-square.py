#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-22 2025-01-22 1.0
# text-square.py

# ------------------------------------------
# задание

# ~ Дан текст.
# ~ Записать его построчно в квадрат наименьшего размера.

# ------------------------------------------
# примеры для тестирования

texts = """
Дан текст. Записать его построчно в квадрат наименьшего размера.
Бывший президент США отправился (https://www.rbc.ru/wine/news/6790a04b9a79473c8eb00504) в долину Санта-Инес, чтобы отпраздновать выход на пенсию. Эта долина известна своими винодельческими производствами.
В Лос-Анджелесе продолжаются пожары, с которыми не справляются — ни фактически, ни политически. Огненная стихия уничтожает все на своем пути — от домов обычных людей до роскошных вилл голливудских звезд. 
"""

# ------------------------------------------
# определение размера

from pprint import pp

# макс размер стороны квадрата
MAX_SIZE    = 100

# делать ли пробелы между буквами при выводе
WITH_SPACES = True
# ~ WITH_SPACES = False

def det_size(text):
    tl = len(text)

    if not tl:
        return 0

    for i in range(MAX_SIZE):
        if tl <= i*i:
            return i

    return 0

# ------------------------------------------
# вписывание текста

def place_text(text, size):

    sq = [ [ "" for j in range(size) ] for i in range(size) ]
    tl = len(text)

    for i in range(size):
        for j in range(size):
            pos = i*size + j
            if tl > pos:
                sq[i][j] = text[pos]
            else:
                sq[i][j] = ""

    return sq

# ------------------------------------------
# все тесты

def print_square(text, size):
    tl = len(text)

    pp(text)
    print()
    
    for i in range(size):
        for j in range(size):
            print(text[i][j], end=" " if WITH_SPACES else "")
        print()

    print()


def tests():

    for one in texts.strip().splitlines():
        size = det_size(one)
        print(f"\nтекст: {one}\nдлина: {len(one)}\nразмер: {size}\n\nквадрат:\n")
        if size:
            print_square(place_text(one, size), size)
        else:
            print("невозможен")


tests()

# ------------------------------------------
# результаты

# ------------------------------------------
