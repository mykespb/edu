#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2026-04-22 2026-04-26 3.0
# code-phrase.py
# шифрование текста по кодовой фразе (слову)

import string

abc = string.ascii_letters + string.digits
# ~ abc = string.ascii_letters + string.digits + " "

print(f"alfabet: {abc}")


def encode1(text : str, word : str, way : bool = True) -> str:
    out = ""
    for i, c in enumerate(text):
        if c in abc:
            if way:
                out += abc[ (abc.index(c) + abc.index( word[ i % len(word) ] ) ) % len(abc) ]
            else:
                out += abc[ (abc.index(c) - abc.index( word[ i % len(word) ] ) ) % len(abc) ]
        else:
            out += c
    return str(out)


def encode2(text : str, word : str, way : bool = True) -> str:
    out = ""
    for i, c in enumerate(text):
        try:
            if c in abc:
                if way:
                    out += abc[ (abc.index(c) + abc.index( word[ i % len(word) ] ) ) % len(abc) ]
                else:
                    out += abc[ (abc.index(c) - abc.index( word[ i % len(word) ] ) ) % len(abc) ]
            else:
                out += c
        except:
            out += c
    return str(out)

encode = encode2


def check(text, word):

    print(80 * "=")
    print(f"{text=}\n{word=}")

    one = encode(text, word, True)
    print(f"!{one=}")
    
    two = encode(one, word, False)
    print(f"!{two=}")
    

def main():

    check("Secret text for agent 007", "secret")
    check("Here we go again, and again, see us go!", "fake")
    check("Скажи мне, кто ты такой, SeeGull", "goer")
    check("Jonathan Livingston Seagull is an allegorical fable in novella form written by American author Richard Bach and illustrated with black-and-white photographs", "lets start with horizontal flight")

    print(80 * "=")


main()
