#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2025
# 2025-04-11 2025-04-11 1.0
# space_shot.py

# ~ Считаем объекты на космоснимке

# ~ Есть как бы космический снимок (2-мерный список).
# ~ На нём буквами (a..z, A..Z) и цифрами (0..9) отмечены разные прямоугольные объекты (каждый своей буквой);
# ~ объекты могут касаться друг друга произвольным образом, накладываться, пересекаться и т.п.
# ~ Подсчитать количество объектов.
# ~ (Пустые места - любые не алфавитно-цифровые знаки).

ROWS = 20
COLS = 30

from pprint import pp
from random import randint, choice, shuffle
from string import ascii_letters, digits

good_chars = list(ascii_letters + digits)
shuffle(good_chars)
bad_chars  = "`~!@#$%^&*()_+-={}[];:'<>?,./"


def show(mapa):
    rows = len(mapa)
    cols = len(mapa[0])
    for i in range(rows):
        for j in range(cols):
            print(mapa[i][j], end=" ")
        print()


def make():
    my_good_chars = good_chars[:]
    mapa = [ [ choice(bad_chars) for j in range(COLS) ] for i in range(ROWS) ]
    num_rects = randint(1, ROWS * COLS // 15)
    print("\nArea:\n")
    for rect in range(num_rects):
        from_i = randint(0, ROWS-2)
        from_j = randint(0, COLS-2)
        to_i   = randint(from_i+1, ROWS-1)
        to_j   = randint(from_j+1, COLS)
        filler = my_good_chars[0]
        my_good_chars = my_good_chars[1:]
        for i in range(from_i, to_i):
            for j in range(from_j, to_j):
                mapa[i][j] = filler
    return mapa


def count(mapa):
    cs = set()
    rows = len(mapa)
    cols = len(mapa[0])
    for i in range(rows):
        for j in range(cols):
            if (c:=mapa[i][j]) in good_chars:
                cs |= {c}
    print(f"\nTotal number of figures: {len(cs)}\n(with letters: { " " . join ( sorted(list(cs)) ) })\n")
        

mapa = make()
show(mapa)
count(mapa)

# ~ Area:

# ~ + ` ' % & } ^ . f f f f f f f f f f f f f f f f f % = ` + # 
# ~ ? I I I I I I I f f f f f f f f f f f f f f f f f v v v C C 
# ~ ~ I I I I I I I f f f f f f f f f f f f f f f f f v v v C C 
# ~ ] I I I I I I I f f f f f f f f f f f f f f f f f v v v C C 
# ~ ! I I I I I I I f f f f f f f f f f f f f f f f f v v v y y 
# ~ $ I I I I I I I f f f f f f f f f f f f f f f f f v v v y y 
# ~ + I I I I I I I f f f f f f f f f f f f f f f f f v v v y y 
# ~ { I I U U U U U U U U U U U U U U U U U U U U U U v v v y y 
# ~ ! I I U U U U U U U U U U U U U U U U U U U U U U z z z z y 
# ~ ~ I I U U U U U U U U U U U U U U U U U U U U U U z z z z y 
# ~ ` I I U U U U U U U U U U U U U U U U U U U U U U o o o z y 
# ~ ] I I U U U U U U U U U U U U U U U U U U U U U U o o o z y 
# ~ ! I I U U U U U U U U U U U U U U U U U U U U U U o o o z y 
# ~ > I I U U U U U U U U U U U U U U U U U U U U U U o o o $ _ 
# ~ ! I I U U U U U U U U U U U U U U U U U U U U U U o o o < ? 
# ~ < ` > U U U U U U U U U U U U U U U U U U U U U U o o o . / 
# ~ < + ' U U U U U U U U U U U U U U U U U U U U U U o o o ] ` 
# ~ & ( & 9 a a a V V V V V V V V 5 V V V V > , = $ - o o o * ' 
# ~ / ~ , 9 a a a V V V V V V V V 5 V V V V 4 4 4 4 4 o o o 4 ( 
# ~ > * ' ^ } : > * , $ - - ( ! : - = , ` ] ' : + { ! _ ` } ) [ 

# ~ Total number of figures: 13
# ~ (with letters: 4 5 9 C I U V a f o v y z)
