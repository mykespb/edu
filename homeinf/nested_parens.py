#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-07-21 1.0

# ~ nested_parens.py

# ~ Дана строка, состяощая из пробелов и скобок разного типа ()[]{}<> .
# ~ Определить, правильно ли вложены скобки.

# тесты

tests = """
()
()[]
({})
([{}])
)(
(
)
(]
([{<      >}])
    ( ) [ ] { } < >
<>{}[]()
"""

# программа

def test(t):
    """проверка 1 строки"""

    what = []
    count = []
    para = {')': '(', ']': '[', '}': '{', '>': '<'}

    for c in t:
        if c in "([{<":
            if what and c == what[-1]:
                count[-1] += 1
            else:
                what.append(c)
                count.append(1)
        elif c in ")]}>":
            if not what:
                return False
            if para[c] != what[-1]:
                return False
            count[-1] -= 1
            if count[-1] == 0:
                count.pop()
                what.pop()

    return not what and not count

# запуск теста

def do_tests():
    """все тесты"""

    for t in tests.strip().split('\n'):
        print(f"{t} -> {test(t)}")
    

do_tests()


# результаты:

# ~ () -> True
# ~ ()[] -> True
# ~ ({}) -> True
# ~ ([{}]) -> True
# ~ )( -> False
# ~ ( -> False
# ~ ) -> False
# ~ (] -> False
# ~ ([{<      >}]) -> True
    # ~ ( ) [ ] { } < > -> True
# ~ <>{}[]() -> True

