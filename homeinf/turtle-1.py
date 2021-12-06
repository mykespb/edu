#!/python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-12-07 2021-12-07 1.0
# turtle-1.py

# ~ простые рисунки черепашкой

import random
import turtle

t = turtle.Turtle()

t.penup()
t.setpos(0, 0)
t.width(10)
t.pendown()

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
    ...

pic2()

turtle.update()
turtle.done()
