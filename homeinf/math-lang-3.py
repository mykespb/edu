#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-20 2025-04-16 3.1
# math-lang-3.py

# ~ Язык математики

# ~ Есть простой язык программирования с командами вида
# ~ A = 1
# ~ или
# ~ B = A
# ~ устанавливающими зависимости между переменными и значениями,
# ~ возможно, с переприсваиваниями.

# ~ Дана программа из таких команд.
# ~ Команды исполняются сверху вниз, 
# ~ устанавливая зависимости между переменными.

# ~ Учесть, что значения переменных - целые числа.

# ~ Разрешить в правой части выражения с вычислением суммы целых чисел.

# ~ Распечатать значения всех переменных после выполнения программы.

# ----------------- data

prog1 = """
A=1
B = A
B =23
C= A
D=C
E = 1+2   +3  +4
FAN =    56
ANSWER  =   42
NOOB = 5 + 15 + 20 + 10
VAR = B
"""

# ----------------- calc

def calc(prog):
    """посчитать всё и распечатать словарь значений"""

    dex = {}

    for iexpr, expr in enumerate(prog.strip().splitlines(), 1):
        print(f"#{iexpr:3}: {expr}")

        assert '=' in expr
        
        expr = expr.replace(' ', '')

        left, right = expr.split('=')

        assert left
        assert right
        
        if right in dex:
            dex[left] = dex[right]
        else:
            rint = right.split('+')
            right = sum( map(int, rint) )
            dex[left] = right

    print("\nрезультат:")

    for k in sorted(dex):
        print(f"{k} : {dex[k]}")
        
    width = max( [ len(x) for x in dex] )

    for k in sorted(dex):
        print(f"{k:{width}} : {dex[k]}")


calc(prog1)

# ----------------- result

# ----------------- the end.
