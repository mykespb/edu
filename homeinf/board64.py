#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# board64.py
# 2025-01-31 2025-01-31 0.1

# ~ Доска-64, или A1-H8
# ~ -----------------------------------------------

# ~ а. Разными способами сформровать набор текстовых строк вида A1, A2, ..A8, B1, ... H1, ...H8.
# ~ б. Красиво напечатать это.

from pprint import pp

chars  = 'ABCDEFGH'
digits = '12345678'

# ~ ------------------- ver. 1 ----------------------------

def ver1():
    board = []
    for c in chars:
        for d in digits:
            board.append(c+d)

    # ~ pp(board, width=100)
    print(board)

# ~ ver1()

# ~ ------------------- ver. 2 ----------------------------

from itertools import product

def ver2():
    board = []
    for c, d in product(chars, digits):
        board.append(c+d)

    # ~ pp(board, width=100)
    print(board)

ver2()
    
# ~ -----------------------------------------------

# ~ ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8']


# ~ -----------------------------------------------
