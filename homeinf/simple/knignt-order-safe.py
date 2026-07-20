#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-14 2025-09-16 1.5
# knight-order-safe.py
# На шахматной доске стоит конь (по умолчанию - на А1 = [0, 0]). Это позиция 1.
# (Можно изменить и посчитать для другого начального поля и для любого (натурального) размера доски.)
# Отметить числами клетки доски в соответствии с тем, на каком минимальном ходу конь может оказаться на соотв. клетке.

SIZE  = 8
EMPTY = 0

# позиция на главной диагонали доски, где в board[START][START] изначально стоит конь
START = 0

def pp():
    """печать доски"""
    
    for i in range(SIZE-1, -1, -1):
        print()
        for j in range(SIZE):
            print(f"{board[i][j]:3d}", end="")
    print()
    

def mark(i, j):
    """отметить ход"""
    
    global board, marked, move, done
    
    if 0 <= i < SIZE and 0 <= j < SIZE and board[i][j] == EMPTY:
        board[i][j] = move + 1
        marked += 1
        done = True
        

def markall():
    """разметить доску"""

    global board, marked, move, done
    
    while marked < SIZE*SIZE:

        done = False
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

        if not done:
            print("Failed...")
            break
        
                    
                
def main():
    """решить всё"""
    
    global board, marked, move
    
    board = [ [ EMPTY  for i in range(SIZE)] for j in range(SIZE)]
    
    board[START][START] = 1
    marked = 1
    move = 1

    markall()
    
    pp()
    
    
main()


  # ~ 6  5  6  5  6  5  6  7
  # ~ 5  4  5  4  5  6  5  6
  # ~ 4  5  4  5  4  5  6  5
  # ~ 3  4  3  4  5  4  5  6
  # ~ 4  3  4  3  4  5  4  5
  # ~ 3  2  5  4  3  4  5  6
  # ~ 4  5  2  3  4  5  4  5
  # ~ 1  4  3  4  3  4  5  6


