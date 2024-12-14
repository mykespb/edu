#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-14 2024-12-14 1.0
# knight-order.py
# На шахматной доске стоит конь (по умолчанию - на А1 = [0, 0]). Это позиция 0.
# Отметить числами клетки доски в соответствии с тем, на каком минимальном ходу конь может оказаться на соотв. клетке.

# from pprint import pp

SIZE = 8


def pp(width=3):
    """печать доски"""
    
    for i in range(SIZE):
        print()
        for j in range(SIZE):
            print(f"{board[i][j]:3d}", end="")
        
    print()
    

def mark(i, j):
    """отметить ход"""
    
    global board, marked, move
    
    if 0 <= i < SIZE and 0 <= j < SIZE and board[i][j] == -1:
        board[i][j] = move + 1
        marked += 1
        

def markall():
    """разметить доску"""

    global board, marked, move
    
    while marked < SIZE*SIZE:
        
        for i in range(SIZE):
            for j in range(SIZE):
                
                if board[i][j] == move:
                    mark(i-2, j-1)
                    mark(i-2, j+1)
                    mark(i+2, j-1)
                    mark(i+2, j+1)
                    mark(i-1, j-2)
                    mark(i-1, j+2)
                    mark(i+1, j-2)
                    mark(i+1, j+2)
                    
        move += 1
                    
                
def main():
    """решить всё"""
    
    global board, marked, move
    
    board = [ [ -1  for i in range(SIZE)] for j in range(SIZE)]
    # pp(board)
    
    board[0][0] = 0
    marked = 1
    move = 0

    markall()
    
    pp(board)
    
    
main()
