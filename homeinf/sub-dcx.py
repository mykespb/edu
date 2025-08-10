#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# sub-dcx.py 2025-07-24 2025-08-10 2.1

# ~ Подутилита dc

# ~ dc -e "1 2 + 3 - p "  =>  0
# ~ Смоделировать подмножество утилиты dc,
# ~ являющейся калькулятором в полизе,
# ~ для операций + - * /.
# ~ Добавлены * и / .

exprs = """
1 p
1 2 + p
1 1 - p
1 2 + 3 - p
1 2 3 + + 4 - 2 + p
-
1 -
p
1 p 2 p 3 p
2 -1 + p
21 20 - p
100500 -100499 + p
2 2 * p
100 25 / p
1 0 / p
"""


def tests():
    """make all tests"""

    for ex in exprs.strip().splitlines():
        try:
            print(f"\n{ex} => ", end="")
            test(ex)
        except:
            print(f"Bad expression: {ex}")
    print()


def test(ex):
    """calculate 1 expression in RPN"""

    stack = []

    for e in ex.strip().split():
        match e:
            case 'p':
                assert len(stack) >= 1
                print(stack.pop(), end=" ")
            case '+':
                assert len(stack) >= 2
                stack.append(stack.pop() + stack.pop())
            case '-':
                assert len(stack) >= 2
                stack.append(-stack.pop() + stack.pop())
            case '*':
                assert len(stack) >= 2
                stack.append(stack.pop() * stack.pop())
            case '/':
                assert len(stack) >= 2
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(int(x1 / x2))
            case _:
                stack.append(int(e))


tests()


# ~ 1 p => 1 
# ~ 1 2 + p => 3 
# ~ 1 1 - p => 0 
# ~ 1 2 + 3 - p => 0 
# ~ 1 2 3 + + 4 - 2 + p => 4 
# ~ - => Bad expression: -
# ~ 1 - => Bad expression: 1 -
# ~ p => Bad expression: p
# ~ 1 p 2 p 3 p => 1 2 3
# ~ 2 -1 + p => 1 
# ~ 21 20 - p => 1 
# ~ 100500 -100499 + p => 1 
# ~ 2 2 * p => 4 
# ~ 100 25 / p => 4 
