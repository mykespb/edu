#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-25 2026-04-25 1.0
# exbrace.py

# ~ Есть строка, в которой есть скобки типа ()[]{}<>.
# ~ Развернуть все скобки в обратную сторону,
# ~ остальные символы не трогать.

from random import choice
import string

bra = "()[]{}<>"

# ~ syms = bra + " "
syms = bra + " .,"
# ~ syms = bra + " .,/?!%^&*-_=+$6"
# ~ syms = bra + " " + string.ascii_letters


def make(size : int = 10) -> str:
    """make random string of syms"""

    return "".join ( [ choice(syms) for _ in range(size) ] )


def subst(s : str) -> str:
    """make substitutions"""

    # prepare
    pat = {}
    for i in range(len(bra)):
        pat[bra[i]] = bra[i+1] if i%2==0 else bra[i-1]
    # ~ print(pat)

    # run
    out = "".join( [ pat[c] if c in bra else c for c in s ] )

    return out


def main(times : int = 3, size : int = 10) -> None:
    """run tests"""

    for test in range(1, times+1):
        problem = make(size)
        result = subst(problem)
        print(f"{test=:2}, {problem=}, {result=}")


main(10)
