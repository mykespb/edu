#!/usr/bin/env python
# Mikhail Kolodin, 2023-01-16 1.0 2023-01-16
# testing string interns

# https://www.youtube.com/watch?v=SJxgQFKp2qc

# выдать последовательности натуральных чётных чисел до заданного предела

def giveseq(limit: int = 10) -> list[int]:
    return [x for x in range(2, limit+1, 2)]

def test_giveseq() -> None:

    print(giveseq(1))
    print(giveseq(2))
    print(giveseq(3))
    print(giveseq(10))

    assert(giveseq(1) == [])
    assert(giveseq(2) == [2])
    assert(giveseq(3) == [2])
    assert(giveseq(10) == [2, 4, 6, 8, 10])
    print("All tests OK")

test_giveseq()

# https://www.youtube.com/watch?v=VeDc_eUnjuU

def subs(s1: str, s2: str) -> str:
    # subtract strings s1-s2, if possible
    if s1.startswith(s2):
        return s1[len(s2):]
    else:
        return s1

def test_subs():

    print(subs('hello world', 'hello'))
    print(subs('hello world', 'llo'))
    print(subs('hello world', ''))
    print(subs('hello world', 'with hello'))

# test_subs()

class DifString(str):
    def __init__(self, stroka: str) -> None:
        self.stroka = stroka

    def __sub__(self, difa: str):
        if self.stroka.startswith(difa):
            return DifString(self.stroka[len(difa):])
        else:
            return DifString(self.stroka)

def testDifString():
    s1 = DifString("stroka")
    s2 = DifString("st")
    print(f"{s1=}", f"{s2=}")
    s3 = s1 - s2
    print(f"{s1=}, {s2=}, {s3=}")
    print(type(s1), type(s2), type(s3))

testDifString()

# /myke/pro/pytests/etc/hwtest1.py 
# s1='stroka' s2='st'
# s1='stroka', s2='st', s3='roka'
# <class '__main__.DifString'> <class '__main__.DifString'> <class '__main__.DifString'>

def test0():
    a = "Hello World"
    a0 = a
    a1 = "Hello World"
    b = "Hello Worl"
    c = 'd'
    d = b + c

    print(f"{a=}, {b=}, {c=}")
    print(id(a), id(a0), id(a1), id(b), id(c))
    print(a == b)
    print(a is b)

    print(dir(str))

    import sys

    x = 15
    print(sys.getsizeof(x))

    print(70*'=')

    a = "helwol"
    a0 = a
    a1 = "helwol"
    b = "helwo"
    c = 'l'
    d = b + c

    print(f"{a=}, {b=}, {c=}, {d=}")
    print('a',  id(a), 'a0', id(a0), 'a1', id(a1), 'b', id(b), 'c', id(c), 'd', id(d))
    print(a == b+c, a is b)
    print(a == d, a is d)

# test0()
