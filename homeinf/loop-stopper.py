#!/usr/bin/env python
# myke 2026-04-05 2026-04-13 3.2
# loop-stopper.py

# ~ Даны (пока) 3 последовательности чисел.
# ~ Перебрав все их сочетания, напечатать их вместе с суммой чисел.
# ~ Решение оформить как функцию.
# ~ А теперь: прекратить вычисления, если сумма чисел делится на 7.

# ~ Примерно так:
# ~ 1 2 0 => 3
# ~ 1 2 10 => 13
# ~ 1 2 100 => 103
# ~ 1 2 1000 => 1003
# ~ 1 4 0 => 5
# ~ 1 4 10 => 15
# ~ 1 4 100 => 105


seq1 = 1, 4, 7, 10
seq2 = 2, 4, 6, 8
seq3 = 0, 10, 100, 1000


def sl1():
    print("\n*** SL1 ***\n")
    for i1 in seq1:
        for i2 in seq2:
            for i3 in seq3:
                print(i1, i2, i3, "=>", i1+i2+i3)


def sl2():
    print("\n*** SL2 ***\n")
    for i1 in seq1:
        for i2 in seq2:
            for i3 in seq3:
                print(i1, i2, i3, "=>", i1+i2+i3)
                if (i1+i2+i3) % 7 == 0:
                    print("break!")
                    break


def sl3():
    print("\n*** SL3 ***\n")
    stop = False
    for i1 in seq1:
        if stop:
            break
        for i2 in seq2:
            if stop:
                break
            for i3 in seq3:
                # ~ if stop:
                    # ~ break
                print(i1, i2, i3, "=>", i1+i2+i3)
                if (i1+i2+i3) % 7 == 0:
                    print("BREAK!")
                    stop = True
                    break


class StopIt(Exception): pass

def sl4():
    print("\n*** SL4 ***\n")
    try:
        for i1 in seq1:
            for i2 in seq2:
                for i3 in seq3:
                    print(i1, i2, i3, "=>", i1+i2+i3)
                    if (i1+i2+i3) % 7 == 0:
                        print("BREAK!")
                        raise StopIt
    except StopIt:
        print("поймали исключение")
        # ~ pass


from itertools import product

def sl5():
    print("\n*** SL5 ***\n")
    for it in product(seq1, seq2, seq3):
        print(*it, "=>", sit := sum(it))
        if sit % 7 == 0:
            print("BREAK!")
            break


# ~ sl1()
# ~ sl2()
# ~ sl3()
sl4()
sl5()
