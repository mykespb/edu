#!/usr/bin/env python3.9
# sotni.py
# (C) Mikhail Kolodin, 2021
# ver. 2021-08-26 2021-08-26 1.2

# дано натуральное число (задаётся случайным образом) от 1 до 999.
# напечатать его словами

import random

def slovami(n):
    """ печать словами """

    edinicy = {
    0: "",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять"
    }

    desatki = {
    0: "",
    1: "десять",
    2: "двадцать",
    3: "тридцать",
    4: "сорок",
    5: "пятьдесят",
    6: "шестьдесят",
    7: "семьдесят",
    8: "восемьдесят",
    9: "девяносто"
    }

    sotni = {
    0: "",
    1: "сто",
    2: "двести",
    3: "триста",
    4: "четыреста",
    5: "пятьсот",
    6: "шестьсот",
    7: "семьсот",
    8: "весемьсот",
    9: "девятьсот"
    }

    spec = {
    0:  "нуль",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать"
    }

    if n == 0:
        return "нуль"

    soten = n // 100
    desatkov = (n // 10) % 10
    edinic = n % 10
    des1 = n % 100

    result = sotni[soten] + " " if soten else ""

    if desatkov == 1:
        result += spec[des1]
    else:
        result += desatki[desatkov] + " " if desatkov else ""
        result += edinicy[edinic]

    result = result.strip()

    return result

def tests1():
    """ проверка печать """

    nabor = 0, 1, 2, 10, 11, 20, 21, 35, 99, 100, 101, 110, 111, 150, 500, 999

    for i in nabor:
        print("%3d" % i, "->", slovami(i))

def tests2():
    """ проверка печать """

    nabor = [random.randint(1, 999) for _ in range(20)]

    for i in nabor:
        print("%3d" % i, "->", slovami(i))

#
tests1()
tests2()

  # ~ 0 -> нуль
  # ~ 1 -> один
  # ~ 2 -> два
 # ~ 10 -> десять
 # ~ 11 -> одиннадцать
 # ~ 20 -> двадцать
 # ~ 21 -> двадцать один
 # ~ 35 -> тридцать пять
 # ~ 99 -> девяносто девять
# ~ 100 -> сто
# ~ 101 -> сто один
# ~ 110 -> сто десять
# ~ 111 -> сто одиннадцать
# ~ 150 -> сто пятьдесят
# ~ 500 -> пятьсот
# ~ 999 -> девятьсот девяносто девять

# ~ 228 -> двести двадцать восемь
# ~ 684 -> шестьсот восемьдесят четыре
# ~ 542 -> пятьсот сорок два
# ~ 926 -> девятьсот двадцать шесть
# ~ 320 -> триста двадцать
# ~ 709 -> семьсот девять
# ~  13 -> тринадцать
# ~ 921 -> девятьсот двадцать один
# ~ 376 -> триста семьдесят шесть
# ~ 370 -> триста семьдесят
# ~ 123 -> сто двадцать три
# ~ 335 -> триста тридцать пять
# ~ 197 -> сто девяносто семь
# ~ 715 -> семьсот пятнадцать
# ~ 670 -> шестьсот семьдесят
# ~ 389 -> триста восемьдесят девять
# ~  70 -> семьдесят
# ~ 519 -> пятьсот девятнадцать
# ~ 994 -> девятьсот девяносто четыре
# ~ 949 -> девятьсот сорок девять
