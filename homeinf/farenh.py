#!/usr/bin/env python

# farenh.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-10 2022-01-10 1.1

# ~ перевод температуры между градусами Цельсия и Фаренгейта

def c2f(d):
    """celsius -> fahrenheit"""

    return 9/5*d+32

def f2c(d):
    """fahrenheit -> celsius"""

    return (d-32)*5/9

def test():
    """make tests"""

    print("Celsius Fahrenheit   Fahrenheit Celsius")
    for d in range(-30, 31, 10):
        print(f"{d:+06.2f} = {c2f(d):+06.2f}      {d:+06.2f} = {f2c(d):+06.2f}")

test()


# ~ Celsius Fahrenheit   Fahrenheit Celsius
# ~ -30.00 = -22.00      -30.00 = -34.44
# ~ -20.00 = -04.00      -20.00 = -28.89
# ~ -10.00 = +14.00      -10.00 = -23.33
# ~ +00.00 = +32.00      +00.00 = -17.78
# ~ +10.00 = +50.00      +10.00 = -12.22
# ~ +20.00 = +68.00      +20.00 = -06.67
# ~ +30.00 = +86.00      +30.00 = -01.11
