#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-24 2022-03-24 1.1
# q2592.py

# ~ 2592 = 2**5 * 9**2
# ~ верно ли, что это единственный способ -- да
# ~ а если не умножение, а сложение? -- нет, не выходит

def amult():
    """вариант с умножением"""

    print("умножение")
    num = 0
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i**j * k**l == i*1000 + j*100 + k*10 + l:
                        num += 1
                        print(f"{num=} : {i}{j}{k}{l}")
    print(f"total: {num}")

amult()

# ~ умножение
# ~ num=1 : 2592
# ~ total: 1


def asum():
    """вариант со сложением"""

    print("сложение")
    num = 0
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i**j + k**l == i*1000 + j*100 + k*10 + l:
                        num += 1
                        print(f"{num=} : {i}{j}{k}{l}")
    print(f"total: {num}")

asum()
# ~ сложение
# ~ total: 0
