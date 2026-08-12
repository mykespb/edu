#!/usr/bin/env python
# Miklhail (myke) Kolodin
# simple / snaky.py
# 2026-07-11 2026-08-12 1.3
# Заполнить числовой квадрат змейкой натуральными числами.

def filler(size: int = 1) -> list[list[int]]:
    """make kvadrat"""
    
    # ~ assert type(size) == int and size > 0, "Число раз должно быть натуральным!"

    # ~ kva = []

    # ~ for row_num in range(size):
        # ~ row = [ i+1 for i in range(row_num * size, (row_num+1) * size) ][::(-1)**row_num]
        # ~ kva.append(row)

    # ~ return kva

    # ~ kva = [
        # ~ [ i+1 for i in range(row_num * size, (row_num+1) * size) ][::(-1)**row_num]
        # ~ for row_num in range(size)
        # ~ ]

    # ~ return kva

    return [
        [ i+1 for i in range(row_num * size, (row_num+1) * size) ][::(-1)**row_num]
        for row_num in range(size)
        ]


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

    assert type(times) == int and 0 < times < 11, "Число раз должно быть натуральным и не более 10!"
    
    for time in range(1, times+1):
        print()
        one(time)

    print()
    

main()


def fake():
    print("""
 1 

 1  2 
 4  3 

 1  2  3 
 6  5  4 
 7  8  9 

 1  2  3  4 
 8  7  6  5 
 9 10 11 12 
16 15 14 13 

 1  2  3  4  5 
10  9  8  7  6 
11 12 13 14 15 
20 19 18 17 16 
21 22 23 24 25 
    """)

fake()
