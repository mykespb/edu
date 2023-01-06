#!/usr/bin/env python3
# lc-rects1.py 2023-01-06 1.0 2023-01-06

# ~ https://leetcode.com/problems/rectangle-area/
# ~ Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
# ~ The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
# ~ The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

# ~ Chg: input =
# ~ сначала 1ый прям: axmin, aymin, axmax, aymax,
# ~ потом 2ой прям:   bxmin, bymin, bxmax, bymax.

axmin, aymin, axmax, aymax = -3, 0, 3, 4
bxmin, bymin, bxmax, bymax = 0, -1, 9, 2

def calc():
    sq = 0

    xmin = min(axmin, bxmin)
    xmax = max(axmax, bxmax)
    ymin = min(aymin, bymin)
    ymax = max(aymax, bymax)

    for x in range(xmin, xmax):
        if axmin <= x < axmax and bxmin <= x < bxmax:
            cmin = ymin
            cmax = ymax
            sq += cmax - cmin
        elif axmin <= x < axmax:
            cmin = aymin
            cmax = aymax
            sq += cmax - cmin
        elif bxmin <= x < bxmax:
            cmin = bymin
            cmax = bymax
            sq += cmax - cmin

    return sq

print(calc())

# ~ Площадь прямоугольников (https://leetcode.com/problems/rectangle-area/)

# ~ Сложность: Средняя

# ~ Условие задачи: на вход подаются координаты двух прямоугольников (левый нижний угол, а также правый верхний угол). 

# ~ Необходимо вычислить суммарную площадь, занимаемую двумя прямоугольниками. 

# ~ Пример:

# ~ Ввод: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# ~ Вывод: 45
