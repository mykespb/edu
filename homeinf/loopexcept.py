#!/usr/bin/env python
# myke 2022-04-27 2022-04-27 1.1
# loopexcept.py

# ~ демонстрация выхода из вложенных циклов через исключения

class ex (Exception): pass

def testexgood():
    """проверим исключения в циклах"""

    print("begin test")
    try:
        for i in range(1, 100):
            for j in range(1, 100):
                print((i, j), end=", ")
                if i*j == 15:
                    raise ex
    except:
        print("\nend of loop")
    print("end test")

testexgood()

def testexbad():
    """проверим исключения в циклах"""

    print("begin test")
    for i in range(1, 100):
        for j in range(1, 100):
            print((i, j), end=", ")
            if i*j == 15:
                break
    print("end test")

# ~ testexbad()
