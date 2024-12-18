#!/usr/bin/env python
# myke 2022-04-27 2024-12-18 2.1
# loopexcept.py

# ~ демонстрация выхода из вложенных циклов через исключения

def testbad():
    """проверим выход из цикла"""

    print("begin test")
    
    for i in range(1, 10):
        for j in range(1, 10):
            print((i, j), end=", ")
            if i*j == 15:
                break

    print("end test")

testbad()

# --------------------------------------

def testsoso():
    """проверим выход из цикла через флажки"""

    print("begin test")

    goon = True

    for i in range(1, 10):
        for j in range(1, 10):
            print((i, j), end=", ")
            if i*j == 15:
                goon = False
                break
        if not goon:
            break

    print("end test")

testsoso()

# --------------------------------------

class ex (Exception): pass

def testexgood():
    """проверим исключения в циклах"""

    print("begin test")

    try:
        for i in range(1, 10):
            for j in range(1, 10):
                print((i, j), end=", ")
                if i*j == 15:
                    raise ex
    except:
        print("\nend of loop")

    print("end test")

# ~ testexgood()
