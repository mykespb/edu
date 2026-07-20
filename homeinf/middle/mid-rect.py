#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-27 2025-02-27 1.0
# mid-rect.py

# ~ Середина прямоугольника

# ~ На плоскости (2-мерный массив (список)) проведены знаками "+" 2 вертикальные линии
# ~ и 2 горизонтальные так, что между ними образовался прямоугольник
# ~ с нечётными длинами строк и столбцов.
# ~ Поставить в центр этого прямоугольника знак "*".

from random import randint, choice


def make(hei=20, wid=20):
    """сделать матрицу с 4 линиями"""

    left   = randint(0, wid-4)
    right  = choice( [ j for j in range(left+2, wid-1, 2) ] )
    top    = randint(0, hei-4)
    bottom = choice( [ j for j in range(top+2, hei-1, 2) ] )

    mat = [ [ " " for j in range(wid) ] for i in range(hei) ]

    for j in range(wid):
        mat[top][j] = mat[bottom][j] = "+"
    for i in range(hei):
        mat[i][left] = mat[i][right] = "+"

    return mat


def center(mat):
    """поставить * """

    hei = len(mat)
    wid = len(mat[0])
    
    left = top = -1
    row  = col = 0
    
    if mat[0][1] == "+": row = 1
    if mat[1][0] == "+": col = 1

    for j in range(wid):
        if mat[row][j] == "+":
            if left > -1:
                right = j
                break
            left = j

    for i in range(hei):
        if mat[i][col] == "+":
            if top > -1:
                bottom = i
                break
            top = i

    lev = (top + bottom) // 2
    mid = (left + right) // 2

    mat[lev][mid] = "*"

    # ~ return mat
    

def show(mat):
    """показать"""

    print()
    hei = len(mat)
    wid = len(mat[0])

    for i in range(hei):
        for j in range(wid):
            print(mat[i][j], end=" ")
        print()

    print()
        

def main():
    """запустить"""

    mat = make()
    show(mat)
    center(mat)
    show(mat)
   

main()


#                      +           +     
#                      +           +     
#                      +           +     
#                      +           +     
#                      +           +     
#                      +           +     
#                      +           +     
#                      +           +     
#                      +           +     
#                      +           +     
#+ + + + + + + + + + + + + + + + + + + + 
#                      +           +     
#                      +           +     
#                      +     *     +     
#                      +           +     
#                      +           +     
#+ + + + + + + + + + + + + + + + + + + + 
#                      +           +     
#                      +           +     
#                      +           +
#
