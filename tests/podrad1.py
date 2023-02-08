#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-08 2023-02-08 1.0
# podrad1.py

# ~ задача "Последовательно идущие единицы"

# 1. tests generator

from random import randint

def make(length: int = 20) -> list[int]:
    """generate list of 0..1"""
    arr = [randint(0, 1) for _ in range(length)]
    return arr

# 2. solver

def solver(arr: list[int]) -> int:
    """find longest sequence of 1's"""
    maxlen = thislen = 0

    for e in arr:
        if e:
            thislen += 1
        else:
            maxlen = max(maxlen, thislen)
            thislen = 0

    maxlen = max(maxlen, thislen)

    return maxlen    

# 3. run tests

def runtests(num: int =1) -> None:
    """rune 1 or more tests"""

    for test in range(num):
        arr = make()
        maxlen = solver(arr)
        print(f"test#{test+1}. {arr=}. {maxlen=}")

runtests(20)


# ~ test#1. arr=[0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1]. maxlen=2
# ~ test#2. arr=[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]. maxlen=12
# ~ test#3. arr=[1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]. maxlen=5
# ~ test#4. arr=[1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]. maxlen=4
# ~ test#5. arr=[0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]. maxlen=4
# ~ test#6. arr=[0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0]. maxlen=4
# ~ test#7. arr=[1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]. maxlen=6
# ~ test#8. arr=[0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0]. maxlen=6
# ~ test#9. arr=[1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0]. maxlen=4
# ~ test#10. arr=[1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1]. maxlen=2
# ~ test#11. arr=[0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1]. maxlen=9
# ~ test#12. arr=[0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1]. maxlen=4
# ~ test#13. arr=[1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]. maxlen=3
# ~ test#14. arr=[0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]. maxlen=4
# ~ test#15. arr=[1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]. maxlen=4
# ~ test#16. arr=[0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0]. maxlen=5
# ~ test#17. arr=[0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0]. maxlen=4
# ~ test#18. arr=[0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0]. maxlen=3
# ~ test#19. arr=[1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1]. maxlen=4
# ~ test#20. arr=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1]. maxlen=4
