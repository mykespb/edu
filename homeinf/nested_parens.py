#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-09-11 1.4

# ~ nested_parens.py

# ~ Дана строка, состоящая из пробелов и скобок разного типа ()[]{}<> .
# ~ Определить, правильно ли вложены скобки.

# тесты

tests = """
()
()[]
({})
([{}])
([{<>}])
)(
(
)
(]
([)]
([{)]}
([{<)]}>
([{<      >}])
    ( ) [ ] { } < >
<>{}[]()
1+(2)
(1)+(2)
(((1+2)*3/4)-5)
(abc-cde+ghi)*(qwe-rty*tyu/iou)
(((скажи)+(привет)))
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

def main():
    """все тесты"""

    for t in tests.strip().split('\n'):
        print(f"{t} -> {test(t)}")
    

main()


# результаты:

# ~ () -> True
# ~ ()[] -> True
# ~ ({}) -> True
# ~ ([{}]) -> True
# ~ ([{<>}]) -> True
# ~ )( -> False
# ~ ( -> False
# ~ ) -> False
# ~ (] -> False
# ~ ([)] -> False
# ~ ([{)]} -> False
# ~ ([{<)]}> -> False
# ~ ([{<      >}]) -> True
    # ~ ( ) [ ] { } < > -> True
# ~ <>{}[]() -> True
# ~ 1+(2) -> True
# ~ (1)+(2) -> True
# ~ (((1+2)*3/4)-5) -> True
# ~ (abc-cde+ghi)*(qwe-rty*tyu/iou) -> True
# ~ (((скажи)+(привет))) -> True
