#!/usr/bin/env python
# Mikhail Kolodin, 2024
# list-chessboard.py
# 2024-10-08 2024-10-08 1.0
# Сделать 2-мерный список - “шахматную доску”

from pprint import pp

SIZE = 8

board = [ [ (i+j) % 2 for j in range(SIZE) ]  for i in range(SIZE) ]

pp(board)

# ~ [[0, 1, 0, 1, 0, 1, 0, 1],
 # ~ [1, 0, 1, 0, 1, 0, 1, 0],
 # ~ [0, 1, 0, 1, 0, 1, 0, 1],
 # ~ [1, 0, 1, 0, 1, 0, 1, 0],
 # ~ [0, 1, 0, 1, 0, 1, 0, 1],
 # ~ [1, 0, 1, 0, 1, 0, 1, 0],
 # ~ [0, 1, 0, 1, 0, 1, 0, 1],
 # ~ [1, 0, 1, 0, 1, 0, 1, 0]]
