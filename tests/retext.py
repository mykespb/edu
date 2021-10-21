#!/python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-10-21 2021-10-21 1.0
# retext.py
# Заменить во входном тексте указанное слово на случайный вариант
# из предложенного набора заменителей.
# Параметры - в командной строке.

import re, random, sys

fin = 'retext-in.txt'
fot = 'retext-out.txt'

t1 = """
here we go again and we know:
here we do the same
"""

def redo(text: str, aword: str, subs: list) -> str:
    """ заменятель """
    return re.sub(f'(\W{aword}\W)', " "+random.choice(subs)+" ", text)

def test1():
    """ тестировщик """
    w = "we"
    s = ["they", "he", "she"]
    print(w, "->", s, "\n", t1, "\n", redo(t1, w, s))

#test1()

def main():
    """ запуск """
    print("got params:", sys.argv)
    argc = len(sys.argv)
    if argc < 3:
        print("Not enough parameters")
        return
    w, *subs = sys.argv[2:]
    #print(w, subs)
    with open(fin) as fi:
        text = fi.read()
    out = redo(text, w, subs)
    with open(fot, 'w') as fo:
        fo.write(out)

main()
