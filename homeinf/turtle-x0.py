#!/usr/bin/env python
# 2024-11-18 
# turtle-x0.py

#рисование черепашкой "red", "magenta", "blue","cyan","green","yellow","white"]

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
