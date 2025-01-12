#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-12 2025-01-12 1.0
# boxing-all.py

# ~ Разложить всё!

# ~ Есть набор предметов (указаны их размеры) и набор коробок (указаны их размеры).
# ~ Разложить предметы по 1 в каждую коробку (количества коробок и предметов равны) так, чтобы каждый
# ~ предмет поместился в своей коробке,
# ~ либо сказать, что такая раскладка невозможна.

# ----------------------------------------------
# настройки

LIMIT = 10    # количество коробок и предметов

# ----------------------------------------------
#  импорты

from random import randint as ri

# ----------------------------------------------
# создание всего

def make_all():
    """
    сделать наборы коробок и предметов
    """

    boxes    = [ ri(1, 9) for _ in range(LIMIT) ]
    subjects = [ ri(1, 9) for _ in range(LIMIT) ]

    return boxes, subjects

# ----------------------------------------------
# проверка

def test(boxes, subjects):
    """
    проверка набора
    """

    boxes.sort(reverse = True)
    subjects.sort(reverse = True)
    
    mess = tuple(zip(boxes, subjects))
    print(mess)

    # ~ print([x[0] > x[1] for x in mess ])
    
    result = all( [x[0] >= x[1] for x in mess ] )
    return result

def main():
    """
    запуск всего
    """

    boxes, subjects = make_all()
    result = test(boxes, subjects)
    print(f"Результат: {result}")

main()

# ----------------------------------------------
# результаты

# ~ ((9, 7), (9, 7), (8, 6), (7, 6), (7, 3), (7, 3), (5, 2), (4, 2), (2, 1), (1, 1))
# ~ Результат: True

# ~ ((9, 9), (9, 8), (7, 8), (7, 6), (7, 3), (5, 2), (5, 2), (3, 2), (3, 1), (2, 1))
# ~ Результат: False

# ----------------------------------------------
