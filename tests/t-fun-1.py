#!/usr/bin/env python

# t-fun-1.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-07 2022-01-07 1.2

# edu: работа с функциями

# ~ тема: линейные уравнения
# ~ определение: линейными называются уравнения вида ax+b=0
# ~ решение: x = -b/a
# ~ условие: a != 0


def lineq(a, b):
    """ решение линейных уравнений
    """

    return -b / a


def lineq_test(a, b):
    """ тестирование функции lineq
    без проверки на ошибки
    """

    print(f"дано {a=}, {b=}, корень равен {lineq(a, b)}")


def lineq_test1(a, b):
    """ тестирование функции lineq
    с проверкой на ошибки
    """

    try: 
        print(f"дано {a=}, {b=}, корень равен {lineq(a, b)}")
    except:
        print("ошибка была")


test = lineq_test1

def main():
    """ вызовы с разными данными
    """

    print("решаем линейные уравнения")
    test(1, 2)
    test(1, 3)
    test(1, 0)
    test(-5, 100500)
    test(0, 0)
    test(10, 20)
    print("закончили решать линейные уравнения")
    

main()


# ~ решаем линейные уравнения
# ~ дано a=1, b=2, корень равен -2.0
# ~ дано a=1, b=3, корень равен -3.0
# ~ дано a=1, b=0, корень равен 0.0
# ~ дано a=-5, b=100500, корень равен 20100.0
# ~ Traceback (most recent call last):
  # ~ File "/home/myke/pro/edu/tests/t-fun-1.py", line 56, in <module>
    # ~ main()
  # ~ File "/home/myke/pro/edu/tests/t-fun-1.py", line 52, in main
    # ~ test(0, 0)
  # ~ File "/home/myke/pro/edu/tests/t-fun-1.py", line 27, in lineq_test
    # ~ print(f"дано {a=}, {b=}, корень равен {lineq(a, b)}")
  # ~ File "/home/myke/pro/edu/tests/t-fun-1.py", line 19, in lineq
    # ~ return -b / a
# ~ ZeroDivisionError: division by zero

# ~ решаем линейные уравнения
# ~ дано a=1, b=2, корень равен -2.0
# ~ дано a=1, b=3, корень равен -3.0
# ~ дано a=1, b=0, корень равен 0.0
# ~ дано a=-5, b=100500, корень равен 20100.0
# ~ ошибка была
# ~ дано a=10, b=20, корень равен -2.0
# ~ закончили решать линейные уравнения
