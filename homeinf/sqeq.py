#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-02-09 2025-02-09 1.0
# sqeq.py

# ~ Решение квадратных уравнений.

# ~ a, b, c -> x / x1, x2 / {}

# --------------------------------
# solver

from math import sqrt

def solve(a, b, c):
    """решить квадратное уравнение
    с выдачей кортежа решений
    в вещ. числах
    """

    assert a != 0

    d = b*b - 4*a*c

    if d > 0:
        x1 = (-b - sqrt(d)) / (2*a)
        x2 = (-b + sqrt(d)) / (2*a)
        return x1, x2

    elif d == 0:
        x = -b / (2*a)
        return x,

    else:
        return ()

# --------------------------------
# tests

def test(a, b, c):
    print(f"квадратное уравнение с коэффициентами {a=}, {b=}, {c=} ", end="")
    match solve(a, b, c):
        case x1, x2:
            print(f"имеет 2 корня: {x1=}, {x2=}")
        case x,:
            print(f"имеет 1 корень: {x=}")
        case _:
            print(f"не имеет корней в действительных числах")
            

test(1, 2, 3) 
test(1, -4, 0)           
test(3, -10, 1)           
test(-1, 0, 100)           
test(10, -150, 15)           
test(1, -1, 0) 
test(1, 0, 0) 
test(1, 1, 0) 
# ~ test(0, 0, 0) 

# --------------------------------
# results

# ~ квадратное уравнение с коэффициентами a=1, b=2, c=3 не имеет корней в действительных числах
# ~ квадратное уравнение с коэффициентами a=1, b=-4, c=0 имеет 2 корня: x1=0.0, x2=4.0
# ~ квадратное уравнение с коэффициентами a=3, b=-10, c=1 имеет 2 корня: x1=0.10319474672552342, x2=3.23013858660781
# ~ квадратное уравнение с коэффициентами a=-1, b=0, c=100 имеет 2 корня: x1=10.0, x2=-10.0
# ~ квадратное уравнение с коэффициентами a=10, b=-150, c=15 имеет 2 корня: x1=0.10067570652562949, x2=14.89932429347437
# ~ квадратное уравнение с коэффициентами a=1, b=-1, c=0 имеет 2 корня: x1=0.0, x2=1.0
# ~ квадратное уравнение с коэффициентами a=1, b=0, c=0 имеет 1 корень: x=0.0
# ~ квадратное уравнение с коэффициентами a=1, b=1, c=0 имеет 2 корня: x1=-1.0, x2=0.0

# ~ квадратное уравнение с коэффициентами a=0, b=0, c=0 Traceback (most recent call last):
  # ~ File "/home/myke/pro/edu/homeinf/sqeq.py", line 60, in <module>
    # ~ test(0, 0, 0)
    # ~ ~~~~^^^^^^^^^
  # ~ File "/home/myke/pro/edu/homeinf/sqeq.py", line 43, in test
    # ~ match solve(a, b, c):
          # ~ ~~~~~^^^^^^^^^
  # ~ File "/home/myke/pro/edu/homeinf/sqeq.py", line 22, in solve
    # ~ assert a != 0
           # ~ ^^^^^^
# ~ AssertionError

# --------------------------------
