#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# board64.py
# 2025-01-31 2025-01-31 0.1

# ~ Доска-64, или A1-H8
# ~ -----------------------------------------------

# ~ а. Разными способами сформровать набор текстовых строк вида A1, A2, ..A8, B1, ... H1, ...H8.
# ~ б. Красиво напечатать это.

# ~ from pprint import pp

chars  = 'ABCDEFGH'
digits = '12345678'

# ~ ------------------- ver. 1 ----------------------------

def ver1():
    board = []
    for c in chars:
        for d in digits:
            board.append(c+d)

    print(board)

# ~ ver1()

# ~ ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']

# ~ ------------------- ver. 2 ----------------------------

from itertools import product

def ver2():
    board = []
    for c, d in product(chars, digits):
        board.append(c+d)

    print(board)

# ~ ver2()

# ~ ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']
    
# ~ ------------------- ver. 3 ----------------------------

def ver3():
    for d in digits[::-1]:
        for c in chars:
            print(c+d, end = " ")
        print()

ver3()

# ~ A8 B8 C8 D8 E8 F8 G8 H8 
# ~ A7 B7 C7 D7 E7 F7 G7 H7 
# ~ A6 B6 C6 D6 E6 F6 G6 H6 
# ~ A5 B5 C5 D5 E5 F5 G5 H5 
# ~ A4 B4 C4 D4 E4 F4 G4 H4 
# ~ A3 B3 C3 D3 E3 F3 G3 H3 
# ~ A2 B2 C2 D2 E2 F2 G2 H2 
# ~ A1 B1 C1 D1 E1 F1 G1 H1 

# ~ -----------------------------------------------

