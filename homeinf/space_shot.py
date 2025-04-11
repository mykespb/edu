#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2025
# 2025-04-11 2025-04-11 1.1
# space_shot.py

# ~ Считаем объекты на космоснимке

# ~ Есть как бы космический снимок (2-мерный список).
# ~ На нём буквами (a..z, A..Z) и цифрами (0..9) отмечены разные прямоугольные объекты (каждый своей буквой);
# ~ объекты могут касаться друг друга произвольным образом, накладываться, пересекаться и т.п.
# ~ Подсчитать количество объектов.
# ~ (Пустые места - любые не алфавитно-цифровые знаки).

ROWS = 20
COLS = 30

from math import isqrt

SPARSE = isqrt(ROWS * COLS)

from pprint import pp
from random import randint, choice, shuffle
from string import ascii_letters, digits

good_chars = list(ascii_letters + digits)
shuffle(good_chars)
bad_chars  = "`~!@#$%^&*()_+-={}[];:'<>?,./"

def show(mapa):
    for i in range(ROWS):
        for j in range(COLS):
            print(mapa[i][j], end=" ")
        print()

def make():
    my_good_chars = good_chars[:]
    mapa = [ [ choice(bad_chars) for j in range(COLS) ] for i in range(ROWS) ]
    num_rects = randint(1, ROWS * COLS // SPARSE)
    print("\nArea:\n")
    for rect in range(num_rects):
        from_i = randint(0, ROWS-1)
        from_j = randint(0, COLS-1)
        to_i = randint(from_i + 1, from_i + ROWS // 2 + 1)
        to_j = randint(from_j + 1, from_j + COLS // 2 + 1)
        filler = my_good_chars.pop()
        for i in range(from_i, to_i):
            for j in range(from_j, to_j):
                mapa[i % ROWS][j % COLS] = filler
    return mapa

def count(mapa):
    cs = set()
    for i in range(ROWS):
        for j in range(COLS):
            if (c:=mapa[i][j]) in good_chars:
                cs |= {c}
    print(f"\nTotal number of figures: {len(cs)}\n(with letters: { ", " . join ( sorted(list(cs)) ) if cs else "None"})\n")

mapa = make()
show(mapa)
count(mapa)

# ~ Area:

# ~ ~ & * $ , - 2 2 2 2 2 2 2 2 2 2 ; ` ; # + ! ~ & ] ! - { ? ( 
# ~ - [ : * < ( 2 2 2 2 2 2 2 2 2 2 ~ @ : & ) + @ ? ? * ; - = ; 
# ~ _ - $ % & ] 2 2 2 2 2 2 2 2 2 2 ! , [ _ } * ? ! [ ! ) + : . 
# ~ < ) % ^ _ ] 2 2 2 2 2 2 2 2 2 2 ; - _ [ & < ~ % ? # ' + ; [ 
# ~ v v v v v v 2 2 1 1 1 1 1 1 1 1 1 L L L L L L L L L ) { # ^ 
# ~ v v v v v v 2 2 1 1 1 1 1 1 1 1 1 L L L L L L L L L ! . ' ] 
# ~ v v v v v v 2 2 Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y ? - ' ' 
# ~ v v v v v v 2 2 Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y : ~ * > 
# ~ v v v v v v 2 2 Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y [ . ' [ 
# ~ v v v v v v 2 2 Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y ~ , , ; 
# ~ v v v l l l 2 2 Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y [ + ) - 
# ~ v v v v v v 2 2 Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y ^ / { ) 
# ~ v v v v v v v i Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y % : , ) 
# ~ v v v v v v v i i i i i > = ; > ` ) ~ % + { ' * = ' ) & # . 
# ~ v v v v v v v i i i i i } * - & : ! + $ @ ? - ^ # _ ; ` * # 
# ~ v v v v v v v i i i i i % * & < ! > } ~ + % = . [ % . % . . 
# ~ v v v v v v v i i i i i ^ & & + [ ! - } ] @ ' } . = > ^ & [ 
# ~ & _ @ [ ( + + i i i i i { ( ] % ( ( + @ ] & - ] ^ ` - + > } 
# ~ ( { ] - ` , : # ] > : & + > * . ( . ` > ) ` % ; + , _ ~ # > 
# ~ ( < @ - = ! $ $ ^ - - - < > { , # > / + @ - ` * . > ? / = < 

# ~ Total number of figures: 7
# ~ (with letters: 1, 2, L, Y, i, l, v)
