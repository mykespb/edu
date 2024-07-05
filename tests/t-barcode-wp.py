#!/usr/bin/env python

# calculate control digit for ISBN
# Mikhail Kolodin, 2024
# 2024-07-04 2024-70-05 2.1
# https://w.wiki/ABfs

def cd1(number):
    """method 1"""

    if type(number) == str:
        number = number.replace("-", "")
        number = int(number, 0)

    position = 2
    summa = 0
    while number:
        last_digit = number % 10
        number //= 10

        term = position * last_digit
        summa += term
        position += 1

    summa %= 11
    summa = 11 - summa

    return summa


def test(number):
    """test for a number"""

    print(number, "-> method 1: ", cd1(number))


test(226611156)
test("978-5-93286161")

# 226611156 -> method 1:  6 , method 2:  8
# 978-5-93286161 -> method 1:  1 , method 2:  5

#https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9_%D0%BD%D0%BE%D0%BC%D0%B5%D1%80
