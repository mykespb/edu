#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-06 2025-01-10 1.1
# ~ lyshrel-196.py
# ~ Проблема 196 (см. описание внизу)

LIMIT = 100

def test(num: int) -> int:
    """проверить число на палиндромную схлжимость
    и сказать, на каком шаге получен палиндром;
    предел = LIMIT
    """

    print("next:   ", end="")
    go = 0

    for step in range(LIMIT):
        if go > 0:
            print(num, end=", ")
        go = 1
        
        if palin(num):
            print("ready")
            return step

        rev = int( str(num)[::-1] )
        num += rev

    else:
        print("stop")
        return -1

    print("stop")


def palin(num: int) -> bool:
    """проверить, палиндром ли данное число
    """

    snum = str(num)                 # в строку его!
    srev = str(int(snum[::-1]))     # так сложно - это для чисел на 0   :)

    return snum == srev
    

def tester(upto: int = 1) -> None:
    """протестировать все числа от 1 до upto
    """

    for i in range(1, upto+1):
        print(f"\n-------------------------------\n\nnumber: {i}")
        res = test(i)
        print(f"steps:  {res if res>0 else "No steps" if res == 0 else "No palindrome!"}")


tester(200)


# ~ Проблема числа 196 — условное название нерешённой математической задачи: неизвестно, приведёт ли операция «перевернуть и сложить», применённая к числу 196 какое-то количество раз, к палиндрому.
# ~ Число Лишрел (англ. Lychrel number) — это натуральное число, которое не может стать палиндромом с помощью итеративного процесса «перевернуть и сложить» в десятичной системе счисления. Этот процесс называется 196-алгоритмом. Название «Lychrel», придуманное Уэйдом ВанЛэндингемом (англ. Wade VanLandingham), — неточная анаграмма имени его подруги, Шерил (англ. Cheryl). Строго доказанных чисел Лишрел не существует (для десятичной системы счисления; для некоторых других систем счисления доказанные числа Лишрел существуют), но многие числа предполагаются таковыми, причём наименьшее из них — число 196.
# ~ https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0_196#:~:text=%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20196%20%E2%80%94%20%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5,%D0%A7%D0%B8%D1%81%D0%BB%D0%BE%20%D0%9B%D0%B8%D1%88%D1%80%D0%B5%D0%BB%20(%D0%B0%D0%BD%D0%B3%D0%BB.
# ~ https://en.wikipedia.org/wiki/Lychrel_number
