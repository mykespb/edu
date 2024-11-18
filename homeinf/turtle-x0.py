#!/usr/bin/env python
# 

from turtle import *
bgcolor("black")
pensize(2)
speed(0)
for i in range(6):
    for colours in  ["red", "magenta", "blue","cyan","green","yellow","white"]:
        color(colours)
        circle(100)
        left(10)
hideturtle()
done()
# https://www.youtube.com/watch?v=w0LO0Ff7WRo
