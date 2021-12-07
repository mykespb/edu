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
