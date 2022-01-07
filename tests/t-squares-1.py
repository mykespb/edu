#!/usr/bin/env python

# t-squares-1-1.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-08 2022-01-08 1.2

# ~ нарисовать рамку квадрата с заданной стороной
# ~ нарисовать несколько таких квадратов


def square(size):
    """рисуем 1 квадрат со стороной size"""

    if size < 1:
        print()
        return
    elif size == 1:
        print("*\n")
        return

    stars  = size * "*"
    blanks = "*" + (size-2) * " " + "*"

    print(stars)
    for line in range(size-2):
        print(blanks)
    print(stars)
    print()


def main():
    """главная - запуск тестов"""

    for test in range(10):
        square(test)


main()



# ~ *

# ~ **
# ~ **

# ~ ***
# ~ * *
# ~ ***

# ~ ****
# ~ *  *
# ~ *  *
# ~ ****

# ~ *****
# ~ *   *
# ~ *   *
# ~ *   *
# ~ *****

# ~ ******
# ~ *    *
# ~ *    *
# ~ *    *
# ~ *    *
# ~ ******

# ~ *******
# ~ *     *
# ~ *     *
# ~ *     *
# ~ *     *
# ~ *     *
# ~ *******

# ~ ********
# ~ *      *
# ~ *      *
# ~ *      *
# ~ *      *
# ~ *      *
# ~ *      *
# ~ ********

# ~ *********
# ~ *       *
# ~ *       *
# ~ *       *
# ~ *       *
# ~ *       *
# ~ *       *
# ~ *       *
# ~ *********
