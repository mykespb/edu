#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-23 2025-02-23 0.1
# expr-simple.py

# ~ Упрощение выражения и общее приведение подобных
# ~ вида
# ~ 5x- 6 +7 -11x
# ~ или со многими переменными
# ~ 5x- 6 +7 -11x +y -x +78z

exprs = """
5x- 6 +7 -11x
-5x- 6 +7 -11x +y -x +78z
"""


# ~ import re
from collections import defaultdict


def oneExpr(ex: str) -> str:
    """одно выражение"""

    ex = ex.replace(' ', '')

    if not ex.startswith('-'):
        ex = '+' + ex

    print(f"{ex=}")

    ex = ex.replace('-', ' -')
    ex = ex.replace('+', ' +')

    subs = ex.split()

    print(f"{subs=}")

    terms = defaultdict(list)

    for isub, sub in enumerate(subs):
        print(f"{isub=}, {sub=}")
        if sub.endswith(tuple(list('1234567890'))):
            terms[''] += int(sub)
        elif len(sub) == 2:
            sub = sub[0] + '1' + sub[1]
            terms[sub[-1]] += int(sub[:-1])
        else:
            terms[sub[-1]] == int(sub[:-1])

    print(f"{list(terms)=}")


def allExprs(exs: str) -> None:
    """все выражения"""

    for iexpr, expr in enumerate(exprs.strip().splitlines(), 1):
        print(f"\nвыражение {iexpr}: '{expr}'")
        oneExpr(expr)


def main() -> None:
    """запуск"""

    print("\nВыполняем упрощение выражений с переменными.")
    allExprs(exprs)
    print("\nВсё выполнено.\n")

main()
