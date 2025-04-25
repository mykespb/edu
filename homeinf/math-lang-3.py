#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-20 2025-04-25 3.3
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
# ~ Двух или более.
# ~ Разрешить смешанные выражения: переменные и числа.

# ~ Распечатать значения всех переменных после выполнения программы.

# ----------------- data

prog1 = """
A=1
B = A
B =23
C= 5 + 11
D=C+C
E = A+2
FAN =    56+A
ANSWER  =   42
NOOB = 5 + 15
VAR = B+NOOB
K=57
K=K+1
"""

prog2 = """
A=1
B = A
B =23
C= A + 5 + 11
D=C+C
E = 1+2   +3  +4
FAN =    56+A
ANSWER  =   42 + A + B + C + D +1 + 11
NOOB = 5 + 15 + 20 + 10
VAR = B+NOOB
K=57
K=K+1
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
        
        # ~ rp = right.split('+')
        # ~ right = sum( map(
            # ~ lambda x:
                # ~ dex[x] if x in dex else int(x),
            # ~ rp) )
        # ~ dex[left] = right

        dex[left] = right = sum( map( lambda x: dex[x] if x in dex else int(x), right.split('+')) )

    print("\nрезультат:")

    width = max( [ len(x) for x in dex ] )

    for k in sorted(dex):
        print(f"{k:{width}} : {dex[k]}")


calc(prog1)

# ~ результат:
# ~ A      : 1
# ~ ANSWER : 42
# ~ B      : 23
# ~ C      : 17
# ~ D      : 34
# ~ E      : 10
# ~ FAN    : 57
# ~ NOOB   : 50
# ~ VAR    : 73
