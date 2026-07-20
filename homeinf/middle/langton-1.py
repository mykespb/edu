#!/usr/bin/env python
# -*- coding: utf-8 -*-

# icmp1.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-11 2022-01-11 2.1

# ~ https://habr.com/ru/post/599275/
# ~ Муравей Лэнгтона — загадочный клеточный автомат

# ~ Математическая абстракция, модель для описания поведения динамической системы.
# ~ Он живёт на бесконечной плоскости, состоящей из белых клеток.
# ~ У него есть два неиссякаемых ведёрка — одно с белой краской, другое с чёрной.
# ~ Муравей перемещается по клеткам плоскости от одной клетки к другой.
# ~ При этом он выполняет несложный алгоритм:
# ~ Если клетка белая, то муравей перекрашивает её в чёрный цвет,
# ~ поворачивает на 90° направо (по часовой стрелке) и делает шаг вперёд.
# ~ Если клетка чёрная, то муравей перекрашивает её в белый цвет,
# ~ поворачивает на 90° налево (против часовой стрелки) и делает шаг вперёд.

# ~ Здесь модификация:
# ~ муравей всегда поворачивает в случайном направлении

# ~ http://www.langtonant.com/
# ~ https://josephpetitti.com/ant

import random
import turtle

ri = random.randint

STEPS = 150

t = turtle.Turtle()
t.speed(0)
print(t._mode)
t.home()

OFX = -100
OFY = -100

blacks = set()
napr   = 'north'

SIZE = 5
alldirs = "left", "right"

x, y = 0, 0

def randots(times=100):
    for i in range(times):
        x, y = ri(-200, 200), ri(-200, 200)
        t.up()
        t.goto(x, y)
        t.down()
        t.dot()


def turn(to):
    global napr, x, y
    if napr == 'north':
        if to == 'right':
            napr = 'east'
            x += SIZE
        else:
            napr = 'west'
            x -= SIZE
    elif napr == 'east':
        if to == 'right':
            napr = 'south'
            y -= SIZE
        else:
            napr = 'west'
            y += SIZE
    elif napr == 'south':
        if to == 'right':
            napr = 'west'
            x -= SIZE
        else:
            napr = 'east'
            x += SIZE
    elif napr == 'west':
        if to == 'right':
            napr = 'north'
            y += SIZE
        else:
            napr = 'south'
            y -= SIZE
        

def ant(times=100):
    global blacks, x, y, napr
    t.home()
    x = y = 0
    napr = 'north'
    for i in range(times):
        pos = x, y
        if pos in blacks:
            blacks.remove(pos)
            # ~ print(blacks)
            t.goto(x, y)
            t.dot(SIZE, "white")
            newdir = random.choice(alldirs)
            turn(newdir)
            # ~ turn('left')
        else:
            blacks |= {pos}
            # ~ print(blacks)
            t.goto(x, y)
            t.dot(SIZE, "black")
            newdir = random.choice(alldirs)
            turn(newdir)
            # ~ turn('right')

ant(STEPS)

input()
