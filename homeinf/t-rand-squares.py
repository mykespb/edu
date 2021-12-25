#!/usr/bin/env python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-12-25 2021-12-25 0.1
# t-rand-squares.py

# ~ рисование квадратов черепашкой

from random import randint as ri
import turtle

TIMES = 20

t = turtle.Turtle()

for rept in range(TIMES):

    x0 = ri(10, 100)
    y0 = ri(10, 100)
    xp = ri(10, 50)
    yp = ri(10, 50)

    t.up()
    t.goto(x0, y0)
    t.down()
    
    for side in range(2):
        t.fd(xp)
        t.rt(90)
        t.fd(yp)
        t.rt(90)

input()
