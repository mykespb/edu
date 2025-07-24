#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# sub-dc.py 2025-07-24 2025-07-24 1.0

# ~ Подутилита dc

# ~ dc -e "1 2 + 3 - p "  =>  0
# ~ Смоделировать подмножество утилиты dc,
# ~ являющейся калькулятором в полизе,
# ~ только для операций + и  -.

exprs = """
1 p
1 2 + p
1 1 - p
1 2 + 3 - p
1 2 3 + + 4 - 2 + p
-
1 -
p
"""


def tests():
    """make all tests"""

    for ex in exprs.strip().splitlines():
        try:
            print(f"{ex} => ", end="")
            test(ex)
        except:
            print(f"Bad expression: {ex}")


def test(ex):
    """calculate 1 expression in RPN"""

    stack = []

    for e in ex.strip().split():
        match e:
            case 'p':
                assert len(stack) >= 1
                print(stack.pop())
            case '+':
                assert len(stack) >= 2
                stack.append(stack.pop() + stack.pop())
            case '-':
                assert len(stack) >= 2
                stack.append(-stack.pop() + stack.pop())
            case _:
                stack.append(int(e))


tests()
