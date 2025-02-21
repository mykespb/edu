#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-20 2025-02-21 1.4
# math-lang.py

# ~ Язык математики

# ~ Есть простой язык программирования с командами вида
# ~ A = 1
# ~ или
# ~ B = A
# ~ устанавливающими зависимости между переменными и значениями,
# ~ возможно, с перепи=рисваиваниями.

# ~ Дана программа из таких команд.
# ~ Команды исполняются сверху вниз, 
# ~ устанавливая зависимости между переменными.

# ~ Распечатать значения всех переменных после выполнения программы.

# ----------------- data

exprs = """
A=1
B = A
B =23
C= 1
D=B
FAN =    56
ANSWER  =   42
NOOB =   FAN
VAR = B
"""

# ----------------- calc

def calc():
    """посчитать всё и распечатать словарь значений"""

    dex = {}

    for iexpr, expr in enumerate(exprs.strip().splitlines(), 1):
        print(f"#{iexpr:3}: {expr}")

        assert '=' in expr
        
        expr = expr.replace(' ', '')

        left, right = expr.strip().split('=')
        
        if right in dex:
            dex[left] = dex[right]
        else:
            dex[left] = right

    print("\nрезультат:")

    width = max( [ len(x) for x in dex] )

    for k in sorted(dex):
        print(f"{k:{width}} : {dex[k]}")


calc()


# ----------------- resuilt

# ~ #  1: A=1
# ~ #  2: B = A
# ~ #  3: B =23
# ~ #  4: C= 1
# ~ #  5: D=B
# ~ #  6: FAN =    56
# ~ #  7: ANSWER  =   42
# ~ #  8: NOOB =   FAN
# ~ #  9: VAR = B
# ~ результат:
# ~ A      : 1
# ~ ANSWER : 42
# ~ B      : 23
# ~ C      : 1
# ~ D      : 23
# ~ FAN    : 56
# ~ NOOB   : 56
# ~ VAR    : 23

# ----------------- the end.
