#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# paint-area-que.py
# 2025-09-17 2025-09-17 1.0

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


def onepaint():
    
    global queue, lapa, color

    x, y = queue.pop(0)

    if x < 0: return
    if y < 0: return
    if x >= len(lapa): return
    if x >= len(lapa[0]): return

    if lapa[x][y] != " ": return

    lapa[x][y] = color

    queue.append( (x-1, y-1) )
    queue.append( (x-1, y) )
    queue.append( (x-1, y+1) )
    queue.append( (x, y-1) )
    queue.append( (x, y+1) )
    queue.append( (x+1, y-1) )
    queue.append( (x+1, y) )
    queue.append( (x+1, y+1) )
    

def dopaint(mapa, x, y, acolor):
    """paint area"""

    global queue, lapa, color
    color = acolor

    # print and  convert data to list
    print(mapa)

    lapa = []
    for line in mapa.strip().splitlines():
        aline = list(line)
        lapa.append(aline)

    # start work
    queue = []
    queue.append( (x, y) )

    # make loop
    while queue:
        onepaint()

    # convert data to strings and print them
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
