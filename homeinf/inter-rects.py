#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-28 2024-12-28 0.1
# inter-rects.py

# ~ На бесконечной плоскости размещены квадраты с указанной длиной стороны,
# ~ указаны также координаты нижных левых углов квадратов.
# ~ Квадраты занимают целые ячейки,
# ~ позиционирование идёт по левым нижним углам.
# ~ Определить, какие квадраты пересекаются (вывести их координаты).

from random import randint

SIZE = 10    # размер квадратов


def make(, number=20):
    """разместить квадраты на плоскости"""

    global plane    # плоскость
    plane = []

    for num in range(number):
        plane.append(( randint(-30, 30), randint(-30, 30)))

    print("получены квадраты:\n", plane)
    

def solve():
    """решить задачу о пересечениях"""

    global plane, inters

    inters = []

    for one in range(len(plane) - 1):
        for two in range(one, len(plane)):
            if inter(one, two):
                print("intersection:", one, two)

    print("все пересечения:", inters)


def inter(one, two):
    """пересекаются ли"""

    global plane

    # ~ mnemonics:
    # ~ o = one, t = two
    # ~ l = left, r = right
    # ~ b = bottom, t = top
    # ~ x = x-coordinate (to right), y = t-coordinate (to up) 

    olbx, olby = one
    oltx, olty = (one[0], one[1]+SIZE-1)
    orbx, orby = (one[0]+SIZE-1, one[1])
    ortx, orty = (one[0]+SIZE-1, one[1]+SIZE-1)

    tlbx, tlby = two
    tltx, tlty = (two[0], two[1]+SIZE-1)
    trbx, trby = (two[0]+SIZE-1, two[1])
    trtx, trty = (two[0]+SIZE-1, two[1]+SIZE-1)

    yes = (
        (olbx ...
        )


def main():
    """запуск"""

    global plane    # плоскость

    make()
    solve()


main()

