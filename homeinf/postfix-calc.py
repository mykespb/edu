#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# postfix-calc.py
# 2025-05-25 2025-05-25 1.0

# ~ Делаем постфиксный калькулятор.
# ~ На входе строка. Выход - число или сообщение об ошибке.
# ~ Числа челые, [+|-]\d+ .
# ~ Действия: + - * /

def calc(s: str) -> int:
    """посчитать строку"""

    print(s, '=>', end=" ")

    stack = []

    for e in s.strip().split():

        match e:
            case '+':
                stack.append( stack.pop() + stack.pop() )
            case '-':
                stack.append( - stack.pop() + stack.pop() )
            case '*':
                stack.append( stack.pop() * stack.pop() )
            case '/':
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append( x1 // x2 )
            case _:
                stack.append(int(e))

    print(stack.pop())


def run_tests(tests):
    """выполнить тесты"""

    for test in tests.strip().split('\n'):
        try:
            calc(test)
        except:
            print("error!")


good_tests = """
1
1 2 +
2 1 -
2 3 *
1 2 3 * +
2 -1 +
-1 -2 +
4 2 / 
"""

run_tests(good_tests)

bad_tests = """
1 0 /
+
2 -
"""

run_tests(bad_tests)

# ~ 1 => 1
# ~ 1 2 + => 3
# ~ 2 1 - => 1
# ~ 2 3 * => 6
# ~ 1 2 3 * + => 7
# ~ 2 -1 + => 1
# ~ -1 -2 + => -3
# ~ 4 2 / => 2

# ~ 1 0 / => error!
# ~ + => error!
# ~ 2 - => error!

