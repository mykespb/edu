#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-03 2025-04-04 1.5
# hill-top.py

# ~ Верно ли, что в данном массиве натуральных чисел
# ~ числа сначала монотонно возрастают (это высоты до вершины горы - на подъёме),
# ~ а потом монотонно убывают (на спуске)?

from random import randint


def make_hill(leng=20, top=99):
    """generate a hill"""

    left, right = leng // 4, leng * 3 // 4
    summit = randint(left, right)

    hill = (
        sorted( [randint(1, top) for _ in range(summit) ] ) +
        sorted( [randint(1, top) for _ in range(leng - summit) ], reverse=True )
        )

    if randint(0, 1):
        hill[left], hill[right] = hill[right], hill[left]

    return hill


def test_hill(hill):
    """test if hill is OK"""

    up = True
    
    for pos in range(1, len(hill)):
        if up and hill[pos-1] > hill[pos]:
            up = False
        elif not up and hill[pos-1] < hill[pos]:
            return False

    return True


hill = make_hill() 
# ~ print(f"{hill} => { test_hill(hill) }")        
print(f"{hill} => { 'нет да' .split() [ test_hill(hill) ] }")        


# ~ [6, 32, 47, 49, 60, 36, 96, 94, 92, 88, 82, 77, 60, 43, 36, 98, 34, 13, 6, 5] => нет
# ~ [14, 20, 33, 50, 66, 81, 83, 95, 96, 99, 74, 59, 26, 21, 17, 13, 12, 11, 2, 2] => да
