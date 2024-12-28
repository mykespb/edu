#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-28 2024-12-28 OK 1.0 
# inter-rects.py

# ~ На бесконечной плоскости размещены квадраты с указанной длиной стороны,
# ~ указаны также координаты нижных левых углов квадратов.
# ~ Квадраты занимают целые ячейки,
# ~ позиционирование идёт по левым нижним углам.
# ~ Определить, какие квадраты пересекаются (вывести их координаты).

from random import randint
from pprint import pprint

# ~ DEBUG = True
DEBUG = False

SCOPE = 20   # на каком расстоянии по х, у от начала координат находятся квадраты


def make(size, number):
    """разместить квадраты на плоскости"""

    global plane, SIZE
    
    SIZE = size

    print(f"\nРасставляем квадраты со сторонами {SIZE} \
на плоскости с удалением от начала координат \
их левых нижних углов равным {SCOPE}.\n")
    
    plane = []

    for num in range(number):
        plane.append(( randint(-SCOPE, SCOPE), randint(-SCOPE, SCOPE)))

    print("Получены квадраты:")
    pprint(list(enumerate(plane, 1)))
    

def solve():
    """решить задачу о пересечениях"""

    global plane, inters

    inters = []

    for one in range(len(plane) - 1):
        for two in range(one+1, len(plane)):
            if inter(one, two):
                if DEBUG: print("intersection:", one, two)
                inters.append((one, two))

    print("\nВсе пересечения:", inters, "\n")


def inter(onep, twop):
    """пересекаются ли"""

    global plane, SIZE

    one = plane[onep]
    two = plane[twop]

    # ~ mnemonics:
    # ~ O = one, T = two
    # ~ L= left, R = right, T = top, B = bottom

    OL = one[0]
    OR = one[0] + SIZE - 1
    OB = one[1]
    OT = one[1] + SIZE - 1

    TL = two[0]
    TR = two[0] + SIZE - 1
    TB = two[1]
    TT = two[1] + SIZE - 1

    yes = (
        TL <= OL <= TR and TB <= OB <= TT or
        TL <= OR <= TR and TB <= OB <= TT or
        TL <= OL <= TR and TB <= OT <= TT or
        TL <= OR <= TR and TB <= OT <= TT 
        )

    return yes


def main(size=5, number=20):
    """запуск
    size=10   = размер квадратов
    number=20 = сколько их поставить
    """

    make(size, number)
    solve()


main()
# ~ size=10   = размер квадратов
# ~ number=20 = сколько их поставить
