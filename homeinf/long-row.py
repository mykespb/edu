#!/usr/bin/env python
# myke 2022-05-13 2022-05-13 1.0
# long-row.py 

# ~ 1. заполнить 2-мерный массив числами 0..9, рандомно.
# ~ 2. найти самую длинную гориз. или верт. поледовательность из одинаковых цифр.

from random import randint as ri
from pprint import pp

def fill(size=10):
    """заполнитель"""
    
    size = size if size else ri(5, 10)
    arr = [[ri(0, 9) for i in range(size)] for j in range(size)]
    return arr

def find(arr):
    """искатель"""
    
    size = len(arr)
    lines = []
    
    for i in range(size):
        for j in range(size):
            lines.append(( calc(arr, i, j, 'hor'),  arr[i][j], i, j, 'hor'  ))
            lines.append(( calc(arr, i, j, 'vert'), arr[i][j], i, j, 'vert' ))
    
    lines.sort(reverse=True)
    best = lines[0][0]
    
    return [x for x in lines if x[0] == best]

def calc(arr, xi, xj, direct):
    """найти длину последовательности из данной клетки"""
    
    size = len(arr)
    item = arr[xi][xj]
    
    xl = 0
    if direct == 'hor':
        for j in range(xj, size):
            if arr[xi][j] == item:
                xl += 1
            else:
                break
                
    else:
        for i in range(xi, size):
            if arr[i][xj] == item:
                xl += 1
            else:
                break
        
    return xl

def show(best):
    """показ лучшего"""
    print(f"\nЛучшие результаты. Длина наидлиннейшая {best[0][0]}. Всего ответов: {len(best)}.")
    for num in range(len(best)):
        print(f"Результат номер {num+1:2}. Цифра {best[num][1]}. Координаты {best[num][2]}, {best[num][3]}",
            "горизонтально." if best[num][4] == 'hor'  else "вертикально.")

# запуск
arr = fill()
pp(arr)
best = find(arr)
show(best)

# ~ [[6, 6, 6, 9, 6, 8, 7, 1, 6, 2],
 # ~ [4, 3, 9, 8, 5, 0, 0, 4, 6, 4],
 # ~ [3, 3, 3, 2, 7, 8, 0, 2, 4, 9],
 # ~ [5, 7, 0, 4, 7, 1, 2, 0, 3, 2],
 # ~ [9, 1, 3, 5, 3, 3, 0, 7, 2, 1],
 # ~ [3, 7, 0, 3, 6, 5, 0, 2, 4, 3],
 # ~ [7, 0, 2, 6, 8, 8, 7, 7, 7, 6],
 # ~ [2, 9, 3, 4, 3, 8, 1, 1, 9, 2],
 # ~ [5, 0, 9, 4, 7, 8, 6, 6, 8, 5],
 # ~ [1, 7, 4, 5, 3, 8, 6, 3, 4, 1]]

# ~ Лучшие результаты. Длина наидлиннейшая 4. Всего ответов: 1.
# ~ Результат номер  1. Цифра 8. Координаты 6, 5 вертикально.
