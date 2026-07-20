#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2025-09-18 2025-09-18 1.0
# calc-expr.py

# ~ вер.2. непростой калькулятор
# ~ Дана строка с выражением. Посчитать значение выражения и напечатать.
# ~ Числа целые.
# ~ Операции 3 приоритетов: +, -; *, /; ^.
# ~ В конце стоит точка.
# ~ Операнды и операции разделены пробелами.
# ~ Проверка на ошибки - минимальная.
# ~ Решение на 3 стеках.
# ~ Примеры в коде.
# ~ Запуск сразу для нескольких примеров.


exprs = """
1 .
1 + 2 .
1 + 2 + 3 + 4 .
1 + 2 * 3 .
2 * 3 - 1 .
1 + 2 * 3 ^ 2 - 11 .
"""

def calc(expr):
    """calc 1 expr"""

    # stacks:
    snums = []   # numbers
    soper = []   # operations
    sprio = []   # op.priorities

    # dict of priorities:
    prios = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '.': 0}

    # process elements of expression:
    
    for elem in expr.strip().split():

        # operations:
        if elem in "+-*/^.":

            if not soper:
                soper.append(elem)
                sprio.append(prios[elem])

            else:
                prio = prios[elem]

                # process previous operations:
                while sprio and sprio[-1] >= prio:
                    woper = soper.pop()
                    wprio = sprio.pop()

                    match woper:
                        case '+':
                            snums.append( snums.pop() + snums.pop() )
                        case '-':
                            snums.append( -snums.pop() + snums.pop() )
                        case '*':
                            snums.append( snums.pop() * snums.pop() )
                        case '/':
                            y = snums.pop()
                            x = snums.pop()
                            if y == 0:
                                print("error(zdiv)")
                                snums.append(0)
                            else:
                                snums.append( x // y )
                        case '^':
                            y = snums.pop()
                            x = snums.pop()
                            snums.append( x**y )
                        case '.':
                            ...

                # process new operation: put it onto stacks
                soper.append( elem )
                sprio.append( prios[elem] )

        # numbers:
        else:
            try:
                i = int(elem)
            except:
                print(f"error({elem})")
                i = 0
            snums.append(i)        

    if snums:
        return snums.pop()
    else:
        print("error(no data)")
        

def main():
    """main starter"""

    for num, expr in enumerate(exprs.strip().splitlines()):
        print(num+1, ':', expr, end=" => ")
        res = calc(expr)
        print(res)


main()


# results:
# ~ 1 : 1 . => 1
# ~ 2 : 1 + 2 . => 3
# ~ 3 : 1 + 2 + 3 + 4 . => 10
# ~ 4 : 1 + 2 * 3 . => 7
# ~ 5 : 2 * 3 - 1 . => 5
# ~ 6 : 1 + 2 * 3 ^ 2 - 11 . => 8
