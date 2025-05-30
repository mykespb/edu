#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-06 2025-04-10 2.1
# ~ lyshrel-196-stat.py
# ~ Проблема 196 (см. описание внизу)
# ~ Только считаем, не выводим, но мнго узнаём.

# предел числа обращений и сложений (шагов алгоритма)
LIMIT = 1000


def test(num: int) -> int:
    """проверить число на палиндромную схлжимость
    и сказать, на каком шаге получен палиндром;
    предел = LIMIT
    """

    for step in range(LIMIT):
        
        if palin(num):
            return step

        rev = int( str(num)[::-1] )
        num += rev

    else:
        return -1


def palin(num: int) -> bool:
    """проверить, палиндром ли данное число
    """

    snum = str(num)                 # в строку его!
    srev = str(int(snum[::-1]))     # так сложно - это для чисел на 0   :)

    return snum == srev
    

def tester(upto: int = 1, begin : int = 1, doprint : bool = True) -> None:
    """протестировать все числа от begin до upto,
    печатать все (True) или только найденные непалиндромы (False).
    """

    nopals = 0

    if not doprint:
        print(f"No palindromes (up to {upto} with max steps {LIMIT}):")
    for i in range(begin, upto+1):
        # ~ print(f"\n-------------------------------\n\nnumber: {i}")
        res = test(i)
        if doprint:
            print(f"number: {i},steps:  {res if res>0 else "No steps" if res == 0 else "No palindrome!"}")
        else:
            if res == -1:
                print(i, end=", ")
                nopals += 1

    print(f"\nTotal #no palindromes: {nopals}\n")


tester(2000, 1, False)


# ~ Проблема числа 196 — условное название нерешённой математической задачи: неизвестно, приведёт ли операция «перевернуть и сложить», применённая к числу 196 какое-то количество раз, к палиндрому.
# ~ Число Лишрел (англ. Lychrel number) — это натуральное число, которое не может стать палиндромом с помощью итеративного процесса «перевернуть и сложить» в десятичной системе счисления. Этот процесс называется 196-алгоритмом. Название «Lychrel», придуманное Уэйдом ВанЛэндингемом (англ. Wade VanLandingham), — неточная анаграмма имени его подруги, Шерил (англ. Cheryl). Строго доказанных чисел Лишрел не существует (для десятичной системы счисления; для некоторых других систем счисления доказанные числа Лишрел существуют), но многие числа предполагаются таковыми, причём наименьшее из них — число 196.
# ~ https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0_196#:~:text=%D0%9F%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B0%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20196%20%E2%80%94%20%D1%83%D1%81%D0%BB%D0%BE%D0%B2%D0%BD%D0%BE%D0%B5%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5,%D0%A7%D0%B8%D1%81%D0%BB%D0%BE%20%D0%9B%D0%B8%D1%88%D1%80%D0%B5%D0%BB%20(%D0%B0%D0%BD%D0%B3%D0%BB.
# ~ https://en.wikipedia.org/wiki/Lychrel_number

# ~ No palindromes (up to 1000 with max steps 1000):
# ~ 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986, 
# ~ Total #no palindromes: 13

# ~ No palindromes (up to 10000 with max steps 1000):
# ~ 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986, 1495, 1497, 1585, 1587, 1675, 1677, 1765, 1767, 1855, 1857, 1945, 1947, 1997, 2494, 2496, 2584, 2586, 2674, 2676, 2764, 2766, 2854, 2856, 2944, 2946, 2996, 3493, 3495, 3583, 3585, 3673, 3675, 3763, 3765, 3853, 3855, 3943, 3945, 3995, 4079, 4169, 4259, 4349, 4439, 4492, 4494, 4529, 4582, 4584, 4619, 4672, 4674, 4709, 4762, 4764, 4799, 4852, 4854, 4889, 4942, 4944, 4979, 5078, 5168, 5258, 5348, 5438, 5491, 5493, 5528, 5581, 5583, 5618, 5671, 5673, 5708, 5761, 5763, 5798, 5851, 5853, 5888, 5941, 5943, 5978, 5993, 6077, 6167, 6257, 6347, 6437, 6490, 6492, 6527, 6580, 6582, 6617, 6670, 6672, 6707, 6760, 6762, 6797, 6850, 6852, 6887, 6940, 6942, 6977, 6992, 7059, 7076, 7149, 7166, 7239, 7256, 7329, 7346, 7419, 7436, 7491, 7509, 7526, 7581, 7599, 7616, 7671, 7689, 7706, 7761, 7779, 7796, 7851, 7869, 7886, 7941, 7959, 7976, 7991, 8058, 8075, 8079, 8089, 8148, 8165, 8169, 8179, 8238, 8255, 8259, 8269, 8328, 8345, 8349, 8359, 8418, 8435, 8439, 8449, 8490, 8508, 8525, 8529, 8539, 8580, 8598, 8615, 8619, 8629, 8670, 8688, 8705, 8709, 8719, 8760, 8795, 8799, 8809, 8850, 8868, 8885, 8889, 8899, 8940, 8958, 8975, 8979, 8989, 8990, 9057, 9074, 9078, 9088, 9147, 9164, 9168, 9178, 9237, 9254, 9258, 9268, 9327, 9344, 9348, 9358, 9417, 9434, 9438, 9448, 9507, 9524, 9528, 9538, 9597, 9614, 9618, 9628, 9687, 9704, 9708, 9718, 9777, 9794, 9798, 9808, 9867, 9884, 9888, 9898, 9957, 9974, 9978, 9988, 
# ~ Total #no palindromes: 246
