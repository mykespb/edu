#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2026-04-22 2026-04-26 1.0
# code-phrase.py
# шифрование текста по кодовой фразе (слову)

import string

abc = string.ascii_letters + string.digits
print(f"alfabet: {abc}")


def encode(text : str, word : str, way : bool = True) -> str:
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


def check(text, word):

    print(80 * "=")
    print(f"{text=}, {word=}")

    one = encode(text, word, True)
    print(f"{one=}")
    
    two = encode(one, word, False)
    print(f"{two=}")
    

def main():

    check("Secret text for agent 007", "secret")
    check("Here we go again, and again, see us go!", "fake")

    print(80 * "=")


main()
