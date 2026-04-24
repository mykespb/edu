#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-23 2026-04-24 1.3
# anagram2.py

# ~ Есть две строки, в них тексты на английском из слов, разделённых пробелами, где также возможны знаки препинания.
# ~ Возможно, в этих 2 строках есть слова-анаграммы,
# ~ т.е. слово в 1ой строке является анаграммой слова из 2ой строки.
# ~ Найти их.
# ~ Анаграммы в одной и той же строке не считать.
# ~ Регистром букв при проверке пренебречь.
# ~ Одинаковые слова не считаются, нужны только с перестановками.


# text1 =   "God knows all?"
# text2 =   "No dog here!"
# answer:   "God <-> dog"

text1 = "Listen to me in the night, no evil, only care of heart."
text2 = "Silent wood is live. No race, one thing is our Earth!"


import string
good = string.ascii_letters + " "


def ana(t1 : str, t2 : str) -> list[str]:
    loa = set()

    t1 = "".join ( filter( lambda x: x in good, t1) )
    t2 = "".join ( filter( lambda x: x in good, t2) )
    s1 = t1.split()
    s2 = t2.split()

    for w1 in s1:
        w1l = w1.lower()
        for w2 in s2:
            w2l = w2.lower()            
            if w1l != w2l and set(w1l) == set(w2l):
                loa.add((w1, w2))

    return loa


def main():

    print()
    print(text1)
    print(text2)

    anas = ana(text1, text2)
    if anas:
        print(f"\nWe found {len(anas)} anagram pairs.\n")
        for p1, p2 in anas:
            print(f"{p1:>10} <-> {p2:<10}")
        print()
    else:
        print("\nNo anagrams found.\n")


main()
