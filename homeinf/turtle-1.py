#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-12-07 2022-01-08 1.1
# turtle-1.py

# ~ простые рисунки черепашкой
# ~ работает и можно ещё много экспериментировать

# ~ https://realpython.com/beginners-guide-python-turtle/
# ~ https://docs.python.org/3/library/turtle.html
# ~ https://gvard.github.io/py/turtle/

# ~ https://www.youtube.com/watch?v=Z6FKGQcjTOk
# ~ Getting Started With Turtle in Python
# ~ 1 788 просмотров17 дек. 2020 г.

from random import randint as ri
import turtle

t = turtle.Turtle()

t.penup()
t.setpos(0, 0)
t.width(2)
t.pendown()
t.speed(10)

def pic1():

    for size in 100, 150, 200:

        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)

def pic2():

    for size in 100, 200, 300, 400:

        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.left(90)

def pic3():
    for cir in range(10):
        x = ri(-450, 450)
        y = ri(-450, 450)
        r = ri(35, 55)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.circle(r)

pic1()
# ~ pic2()
# ~ pic3()

turtle.update()
turtle.done()
