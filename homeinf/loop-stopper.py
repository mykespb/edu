#!/usr/bin/env python
# myke 2026-04-05 2026-04-05 3.0
# loop-stopper.py

seq1 = 1, 4, 7, 10
seq2 = 2, 4, 6, 8
seq3 = 0, 10, 100, 1000

def sl1():
    for i1 in seq1:
        for i2 in seq2:
            for i3 in seq3:
                print(i1, i2, i3, "=>", i1+i2+i3)

# ~ sl1()

def sl2():
    for i1 in seq1:
        for i2 in seq2:
            for i3 in seq3:
                print(i1, i2, i3, "=>", i1+i2+i3)
                if (i1+i2+i3) % 7 == 0:
                    print("BREAK!")
                    break

def sl3():
    stop = False
    for i1 in seq1:
        if stop:
            break
        for i2 in seq2:
            if stop:
                break
            for i3 in seq3:
                if stop:
                    break
                print(i1, i2, i3, "=>", i1+i2+i3)
                if (i1+i2+i3) % 7 == 0:
                    print("BREAK!")
                    stop = True
                    break

class StopIt(Exception): pass

def sl4():
    try:
        for i1 in seq1:
            for i2 in seq2:
                for i3 in seq3:
                    print(i1, i2, i3, "=>", i1+i2+i3)
                    if (i1+i2+i3) % 7 == 0:
                        print("BREAK!")
                        raise StopIt
    except StopIt:
        pass

from itertools import product

def sl5():
    for it in product(seq1, seq2, seq3):
        print(*it, "=>", sit := sum(it))
        if sit % 7 == 0:
            print("BREAK!")
            break


sl1()
sl2()
sl3()
sl4()
sl5()

