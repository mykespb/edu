#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-07 2023-02-07 1.0
# make-parens.py

# ~ Сгенерировать случайную правильную последовательность вложенных скобок

from random import randint, choice

def make(ls: int =10) -> str:
    s = "   "
    for _ in range(ls):
        pc = [i for i in range(len(s)) if s[i] == " "]
        pos = choice(pc)
        s = s[:pos] + " ( ) " + s[pos:]
    s = list(filter(lambda c: c != ' ', s))
    so = ''.join(s)
    return so

def test(n: int =10) -> None:
    for i in range(n):
        print(make())

test()    

# ~ ()()()()()()(())()()
# ~ ()((())()()()())()()
# ~ (()()(())())()()(())
# ~ (()())(()()())(())()
# ~ (()()()())(())(())()
# ~ ()()(())(()())(())()
# ~ ()()()()()()()(())()
# ~ ()(())()()((()))()()
# ~ ()()()()()()(())()()
# ~ ()()(())(())(())()()
