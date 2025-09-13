#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-27 2025-09-11 2.4
# knight-order-que.py
# На шахматной доске стоит конь (по умолчанию - на А1 = [0, 0]). Это позиция 0.
# (Можно изменить и посчитать для другого начального поля.)
# Отметить числами клетки доски в соответствии с тем, на каком минимальном ходу конь может оказаться на соотв. клетке.
# Решить рекурсивно вширь, т.е. с очередью.

SIZE  = 4
EMPTY = -1

# позиция на главной диагонали доски, где в board[START][START] изначально стоит конь
START = 0


def pp():
    """печать доски"""
    
    for i in range(SIZE-1, -1, -1):
        print()
        for j in range(SIZE):
            print(f"{board[i][j]:3d}", end="")
    print()
    

def mark():
    """отметить ход"""
    
    global board, queue

    i, j, move = queue.pop(0)
    
    board[i][j] = move

    enqueue(i-2, j-1, move+1)
    enqueue(i-2, j+1, move+1)
    enqueue(i+2, j-1, move+1)
    enqueue(i+2, j+1, move+1)
    enqueue(i-1, j-2, move+1)
    enqueue(i-1, j+2, move+1)
    enqueue(i+1, j-2, move+1)
    enqueue(i+1, j+2, move+1)
    

def enqueue(i, j, m):
    """добавить в очередь для обхода"""

    global queue

    if i < 0 or i >= SIZE or j < 0 or j >= SIZE or board[i][j] != EMPTY:
        return

    queue.append((i, j, m))
                    
                
def main():
    """решить всё"""
    
    global board, queue

    print(f"\n{SIZE=}")
    
    board = [ [ EMPTY  for i in range(SIZE) ] for j in range(SIZE) ]
    
    queue = []

    enqueue(START, START, 0)

    while queue:
        mark()
    
    pp()
    print()
    
    
main()


# ~ SIZE=2

 # ~ -1 -1
  # ~ 0 -1

# ~ SIZE=3

# ~ 2  1  4
# ~ 3 -1  1
# ~ 0  3  2

# ~ SIZE=4

# ~ 5  2  3  2
# ~ 2  1  4  3
# ~ 3  4  1  2
# ~ 0  3  2  5

# ~ SIZE=5

# ~ 2  3  2  3  4
# ~ 3  2  3  2  3
# ~ 2  1  4  3  2
# ~ 3  4  1  2  3
# ~ 0  3  2  3  2

# ~ SIZE=6

# ~ 3  4  3  4  3  4
# ~ 2  3  2  3  4  3
# ~ 3  2  3  2  3  4
# ~ 2  1  4  3  2  3
# ~ 3  4  1  2  3  4
# ~ 0  3  2  3  2  3

# ~ SIZE=7

# ~ 4  3  4  3  4  5  4
# ~ 3  4  3  4  3  4  5
# ~ 2  3  2  3  4  3  4
# ~ 3  2  3  2  3  4  3
# ~ 2  1  4  3  2  3  4
# ~ 3  4  1  2  3  4  3
# ~ 0  3  2  3  2  3  4

# ~ SIZE=8

#  5  4  5  4  5  4  5  6
#  4  3  4  3  4  5  4  5
#  3  4  3  4  3  4  5  4
#  2  3  2  3  4  3  4  5
#  3  2  3  2  3  4  3  4
#  2  1  4  3  2  3  4  5
#  3  4  1  2  3  4  3  4
#  0  3  2  3  2  3  4  5

# ~ SIZE=9

# ~ 4  5  4  5  4  5  6  5  6
# ~ 5  4  5  4  5  4  5  6  5
# ~ 4  3  4  3  4  5  4  5  6
# ~ 3  4  3  4  3  4  5  4  5
# ~ 2  3  2  3  4  3  4  5  4
# ~ 3  2  3  2  3  4  3  4  5
# ~ 2  1  4  3  2  3  4  5  4
# ~ 3  4  1  2  3  4  3  4  5
# ~ 0  3  2  3  2  3  4  5  4

# ~ SIZE=10

# ~ 5  6  5  6  5  6  5  6  7  6
# ~ 4  5  4  5  4  5  6  5  6  7
# ~ 5  4  5  4  5  4  5  6  5  6
# ~ 4  3  4  3  4  5  4  5  6  5
# ~ 3  4  3  4  3  4  5  4  5  6
# ~ 2  3  2  3  4  3  4  5  4  5
# ~ 3  2  3  2  3  4  3  4  5  6
# ~ 2  1  4  3  2  3  4  5  4  5
# ~ 3  4  1  2  3  4  3  4  5  6
# ~ 0  3  2  3  2  3  4  5  4  5
