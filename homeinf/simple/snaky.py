#!/usr/bin/env python
# Miklhail (myke) Kolodin
# simple / snaky.py
# 2026-07-11 2026-08-11 1.1
# Заполнить числовой квадрат змейкой.

def filler(size: int = 1) -> list[list[int]]:
    """make kvadrat"""
    
    assert size > 0

    kva = []

    for row_num in range(size):
        row = [ i for i in range(row_num * size, (row_num+1) * size) ][::(-1)**row_num]
        kva.append(row)

    return kva


def printer(kva: list[list[int]], width: int = 2) -> None :
    """print kvadrat"""

    size = len(kva)

    for row_num in range(size):
        for col_num in range(size):
            print(f"{kva[row_num][col_num]:{width}}", end=" ")
        print()


def one(size: int = 1):
    """test it"""

    qua = filler(size)
    printer(qua)


def main(times: int = 5):
    """many tests"""

    assert 0 < times < 11
    
    for time in range(1, times+1):
        print()
        one(time)

    print()
    

main()


def fake():
    print("""
 0 

 0  1 
 3  2 

 0  1  2 
 5  4  3 
 6  7  8 

 0  1  2  3 
 7  6  5  4 
 8  9 10 11 
15 14 13 12 

 0  1  2  3  4 
 9  8  7  6  5 
10 11 12 13 14 
19 18 17 16 15 
20 21 22 23 24 
    """)

fake()
