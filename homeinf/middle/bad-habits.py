#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2026-03-12 2026-03-18 1.3
# bad-habits.py
# Плохие идеи для питона

from datetime import date, time
from random import randint

# -------------------------------------------------------
sepa = 80 * "="
subsepa = 80 * "-"

def part(name):
    print(f"{sepa}\n{name}\n{sepa}")

def subpart(name):
    print(f"{subsepa}\n{name}\n{subsepa}")

# -------------------------------------------------------
part("Unnecessary steps")

subpart("String conversion")

# ~ value = str(input())
# ~ print("string is:", value)

# -------------------------------------------------------
part("Bools")

subpart("Assignment")

year = date.today().year

def fun3():

    # very bad

    if year == 2026:
        go = True
    print(go)

    # bad

    if year == 2026:
        go = True
    else:
        go = False
    print(go)

    # good

    go = year == 2026
    print(go)

    print(year == 2026)

    YEAR = 2026
    print(go == YEAR)

    subpart("Comparison")

    # bad

    if go == True:
        print("True")
    else:
        print("False")

    # better

    if go:
        print("True")
    else:
        print("False")

    # good

    print(go)

# ~ fun3()

subpart("Logical expressions")

def fun6a(value):
    if bool(value):
        print("it is good variant")
    else:
        print("it is bad variant")
    
def fun6b(value):
    if value:
        print("it is good variant")
    else:
        print("it is bad variant")

# ~ fun6a(1)
# ~ fun6b(1)
# ~ fun6a(0.0)
# ~ fun6b(0.0)

# -------------------------------------------------------
part("Branching")

subpart("break, continue, return, exit")

def fun1a():
    if year == 2026:
        print("This year")
        return
    else:
        print("Another year")
        return

def fun1b():
    if year == 2026:
        print("This year")
    else:
        print("Another year")

def fun1c():
    print( "This year" if year == 2026 else "Another year") 

# ~ fun1a()
# ~ fun1b()
# ~ fun1c()

# -------------------------------------------------------
part("Loops")

subpart("Explicit index")

data = [1, 2, 3, 11, 22, 33]

def fun7a(lst):

    for i in range(len(lst)):
        print(lst[i], end=", ")
    print()

def fun7b(lst):

    for elem in lst:
        print(elem, end=", ")
    print()

def fun7c(lst):

    for index, elem in enumerate(lst):
        print(f"{index=} => {elem=}")
    print()

# ~ fun7a(data)
# ~ fun7b(data)
# ~ fun7c(data)

# -------------------------------------------------------

part("Print")

subpart("Manual / auto formatting")

def fun2a():
    print("The answer for 2*2 is", 2*2, "and for 3*3 is", 3*3, "and year is", year)

def fun2b():
    print(f"The answer for 2*2 is {2*2} and for 3*3 is {3*3} and year is {year}")

# ~ fun2a()
# ~ fun2b()

# -------------------------------------------------------
part("Files")

subpart("Manual / auto file open / close")

fname = "nytree.py"
text  = "The new text"

def fun4a():
    print("Start files")
    f = open(fname, 'a')
    f.write(text)
    f.close()
    print("End files")

def fun4b():
    print("Start files")
    with open(fname, 'a') as f:
        f.write(text)
    print("End files")

def fun4c():
    print("Start files")
    try:
        with open(fname, 'a') as f:
            f.write(text)
    except:
        print("No file or other error, alas...")
    print("End files")

# ~ fun4a()
# ~ fun4b()
# ~ fun4c()

# -------------------------------------------------------
part("Mutables")

subpart("Default mutables as parameters, ver.1")

def fun5a(value=5, arr=[]):
    arr.append(value)
    return arr

def fun5b(value=6, arr=None):
    if arr is None:
        arr = []
    arr.append(value)
    return arr

def fun50():
    print("fun50")
    l1 = fun5a(0)
    print(l1)
    l2 = fun5a(1)
    print(l2)
    l3 = fun5a(2)
    print(l3)

def fun51():
    print("fun51")
    l1 = fun5b(0)
    print(l1)
    l2 = fun5b(1)
    print(l2)
    l3 = fun5b(2)
    print(l3)

fun50()
fun51()

subpart("Default mutables as parameters, ver.2")

def fun6a(arr=[]):
    arr.append(randint(1, 9))
    return arr

def fun6b(arr=None):
    if arr is None:
        arr = []
    arr.append(randint(1, 9))
    return arr

def fun60():
    print("fun60")
    l1 = fun6a()
    print(l1)
    l2 = fun6a()
    print(l2)
    l3 = fun6a()
    print(l3)

def fun61():
    print("fun61")
    l1 = fun6b()
    print(l1)
    l2 = fun6b()
    print(l2)
    l3 = fun6b()
    print(l3)

# ~ fun60()
# ~ fun61()

# -------------------------------------------------------
part("The End.")
# -------------------------------------------------------
