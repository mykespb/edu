#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-12-25 2021-12-25 0.1
# t-squares.py

# ~ рисование квадратов черепашкой

import turtle

ANGLE = 20
TIMES = 18

t = turtle.Turtle()

for rept in range(TIMES):
    for side in range(4):
        t.fd(100)
        t.rt(90)
    t.rt(ANGLE)

input()
