#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2026-03-12 2026-03-12 1.1
# bad-habits.py
# Плохие идеи для питона

from datetime import date, time

# -------------------------------------------------------
sepa = 80 * "="
subsepa = 80 * "-"

def part(name):
    print(f"{sepa}\n{name}\n{sepa}")

def subpart(name):
    print(f"{subsepa}\n{name}\n{subsepa}")

# -------------------------------------------------------
part("Bools")

subpart("Assignment")

# bad

year = date.today().year

def fun3():

    if year == 2026:
        go = True
    else:
        go = False
    print(go)

    # good

    go = year == 2026
    print(go)

    print(year == 2026)

    subpart("Comparison")

    # bad

    if go == True:
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

fun6a(1)
fun6b(1)

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
part("Print")

subpart("Manual / auto formatting")

def fun2a():
    print("The answer for 2*2 is", 2*2, "and for 3*3 is", 3*3)

def fun2b():
    print(f"The answer for 2*2 is {2*2} and for 3*3 is {3*3}")

# ~ fun2a()
# ~ fun2b()

# -------------------------------------------------------
part("Files")

subpart("Manual / auto file open / close")

fname = "nytree.py"

def fun4a():
    f = open(fname)
    print(f.read())
    f.close()

def fun4b():
    with open(fname) as f:
        print(f.read())

# ~ fun4a()
# ~ fun4b()

# -------------------------------------------------------
part("Mutables")

subpart("Default mutables as parameters")

def fun5a(value, arr=[]):
    arr.append(value)
    return arr

def fun5b(value, arr=None):
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

# ~ fun50()
# ~ fun51()

# -------------------------------------------------------
part("The End.")
# -------------------------------------------------------
