#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# paint-area-que.py
# 2025-09-17 2025-09-17 0.1

# ~ Закрашивание области карты
# ~ --------------------------------------

# ~ Дана карта. Отмечены области на ней.
# ~ Дана точка внутри некоторой области.
# ~ Закрасить карту вокруг этой точки с учётом границ.
# ~ Алгоритм с очередью.


map1 = """
************************************************************
*                                                          *
*                                                          *
*                                                          *
*                                                          *
*                                                          *
*                                                          *
*                                                          *
*                                                          *
*                                                          *
************************************************************
"""

map2 = """
************************************************************
*     *                          *                         *
*     *                          *                         *
*     *                          *                         *
*     *                          *                         *
*     *                          *                         *
*     ****************************                         *
*     *                          *                         *
*     *                          *                         *
*     *                          *                         *
************************************************************
"""

map3 = """
****   *****************************************************
*                *                                         *
*         ***************                                  *
*         *             *                                  *
*         *     * ****************                         *
*         ***  **                *                         *
*               ******************                         *
*                 *                                        *
*                 *                                        *
*                 *                                        *
************************************************************
"""


def paint(mapa, x, y, color):
    """paint one area"""

    if x < 0: return
    if y < 0: return
    if x >= len(mapa): return
    if x >= len(mapa[0]): return

    if mapa[x][y] != " ": return

    mapa[x][y] = color

    paint(mapa, x-1, y-1, color)
    paint(mapa, x-1, y, color)
    paint(mapa, x-1, y+1, color)
    paint(mapa, x, y-1, color)
    paint(mapa, x, y+1, color)
    paint(mapa, x-1, y+1, color)
    paint(mapa, x+1, y-1, color)
    paint(mapa, x+1, y, color)
    paint(mapa, x+1, y+1, color)
    

def dopaint(mapa, x, y, color):
    """paint area"""

    print(mapa)

    lapa = []
    for line in mapa.strip().splitlines():
        aline = list(line)
        lapa.append(aline)

    paint(lapa, x, y, color)

    tapa = ""
    for line in lapa:
        aline = "" .join(line)
        tapa += aline + "\n"

    print(tapa)
    

def main():
    """start all"""
    
    dopaint(map1, 3, 3, '#')
    dopaint(map2, 3, 10, '~')
    dopaint(map2, 3, 40, '%')
    dopaint(map3, 5, 26, '.')


main()
