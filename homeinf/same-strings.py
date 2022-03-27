#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-27 2022-03-27 1.0
# same-strings.py

# ~ даны 2 строки.
# ~ определить, состоят ли ли они из одинаковых слов
# ~ (хотя бы и в разном порядке;
# ~ каждое слово учитывается отдельно;
# ~ в строке только слова, без прочих символов).

def sames(s1, s2):
    """compares"""
    return sorted(s1.split()) == sorted(s2.split())

def test(s1, s2):
    """tests"""
    print(f"\n{s1=}\n{s2=}\nsames: {sames(s1, s2)}")
    

test("one two three", "one three two")
test("", "")
test("1 2 3", "4 5 6")


# ~ s1='one two three'
# ~ s2='one three two'
# ~ sames: True

# ~ s1=''
# ~ s2=''
# ~ sames: True

# ~ s1='1 2 3'
# ~ s2='4 5 6'
# ~ sames: False
