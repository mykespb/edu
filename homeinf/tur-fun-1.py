#!/usr/bin/env python

# tur-fun-1.py.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-11 2022-01-11 1.0

# ~ несколько черепашьих картинок с функциями

# ~ доки: https://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()
t.speed(0)

def square(size, cx, cy):
    """нарисовать квадрат со стороной size и центром в точке cx, cy"""
    t.penup()
    half = size//2
    t.goto(cx-half, cy-half)
    t.pendown()
    t.seth(0)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)


def manysq():
    """много квадратов"""
    for i in  range(10):
        for j in range(10):
            square(40, i*50, j*50)


manysq()

input()
