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
    for c in chars:
        for d in digits:
            board.append(c+d)

    # ~ pp(board, width=100)
    print(board)

ver2()
    
    
# ~ -----------------------------------------------


# ~ -----------------------------------------------
