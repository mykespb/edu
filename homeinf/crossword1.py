#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-11-15 2024-11-5 1.1
# crossword1.py

# Даны 2 слова. Построить кроссворд из этих 2 слов,
# т.е. вписать их в пересечённом виде на 2-мерной таблице.

vocab = 'alfa bravo charlie delta echo foxtrot golf hotel india juliett kilo lima mike november oscar ' \
    'papa quebec romeo sierra tango uniform victor whiskey xray yankee zulu'

print(vocab)

from random import choice

def isect(w1, w2):
    """найти пересечение слов, если оно есть, иначе False"""
    
    for i1 in range(len(w1)):
        for i2 in range(len(w2)):
            if w1[i1] == w2[i2]:
                return True, i1, i2
    
    return False, -1, -1


def draw(w1, w2, p1, p2):
    """отрисовать на плоскости слова с пересечением в указанных позициях"""
    
    # первое слово пишем горизонтально, второе через него вертикально.
    # надо len(w1) столбцов и len(w2) строк
    
    l1, l2 = len(w1), len(w2)
    mat = [ [' ' for j in range(l1)] for i in range(l2) ] 
           
    for i in range(l1):
        mat[p2][i] = w1[i]
        
    for i in range(l2):
        mat[i][p1] = w2[i]

    print()    
    for i1 in range(l2):
        for i2 in range(l1):
            print(mat[i1][i2], end="")
        print()


def main():
    """диспетчер"""
    
    words = vocab.split()
    w1, w2 = choice(words), choice(words)
    res, p1, p2 = isect(w1, w2)
    
    print(f"for {w1=} and {w2=} result is:", 
          f"{p1=} and {p2=} => '{w1[p1]}'" if res else "no intersection" )

    if res:
        draw(w1, w2, p1, p2)

    
main()


# s    
# india
# e    
# r    
# r    
# a  

#    v   
# juliett
#    c   
#    t   
#    o   
#    r  
   
# for w1='lima' and w2='echo' result is: no intersection
