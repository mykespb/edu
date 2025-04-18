#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# rainbow.py
# 2025-02-01 2025-02-02 1.2

# ~ Про радугу

# ~ Даны 7 названий цветов.
# ~ Верно ли, что они образуют радугу (в любом порядке, но по порядку цветов радуги).
# ~ Т.е.
# ~ а) верно ли, что все слова соответствуют радуге, причём обязательно в прямом либо обратном порядке
# ~ (и все по 1 разу)?
# ~ б) ... но порядок произвольный, но все по 1 разу?
# ~ в) среди данных слов есть в т.ч.и цвета радуги, в любом порядке... в прямом либо обратном порядке... по 1 разу?

colors = "красный оранжевый жёлтый зелёный голубой синий фиолетовый"

data = [
"красный оранжевый жёлтый зелёный голубой синий фиолетовый",
" ".join("красный оранжевый жёлтый зелёный голубой синий фиолетовый".split()[::-1]),
"чёрный белый оранжевый жёлтый красный зелёный голубой синий фиолетовый",
"оранжевый жёлтый красный зелёный голубой синий фиолетовый",
"красный зелёный голубой сюзюлевый синий фиолетовый",
"красненький зелёненький голубенький сюзюлевый синенький серенький фиолетовый",
"серый оранжевый жёлтый зелёный",
]

# -----------------------------------------------------------

from collections import Counter
from pprint import pprint

# -----------------------------------------------------------
# предобработка

def prepare() -> None:
    """приводим строки к спискам
    """

    global colors, data

    colors = colors.strip().split()

    for idata in range(len(data)):
        data[idata] = data[idata].strip().split()

    # ~ print(data)

# -----------------------------------------------------------

def test1(t: list[str]) -> bool:
    """проверка а.
    верно ли, что все слова соответствуют радуге, причём обязательно в прямом порядке?
    """

    return t == colors

# -----------------------------------------------------------

def test2(t: list[str]) -> bool:
    """проверка б. 
    ... но порядок произвольный, но все по 1 разу?
    """

    c1 = Counter(colors)
    c2 = Counter(t)
    
    return c1 == c2

# -----------------------------------------------------------

def test3(t: list[str]) -> bool:
    """проверка в. 
    ... причём обязательно в прямом порядке, но все по 1 разу?
    """

    proc = [ c for c in t if c in colors ]
    
    return proc == colors

# -----------------------------------------------------------

def test4(t: str) -> bool:
    """проверка г. 
    среди данных слов есть в т.ч. и все цвета радуги, в любом порядке...?
    """

    proc = [ c for c in t if c in colors ]

    return set(colors) == set(proc)

# -----------------------------------------------------------

def test5(t: str) -> bool:
    """проверка д. 
    среди данных слов есть в т.ч. и все цвета радуги, в прямом либо обратном порядке... по 1 разу?
    """

    proc = [ c for c in t if c in colors ]
    
    return proc == colors or proc == colors[::-1]

# -----------------------------------------------------------
# все тесты

tests = test1, test2, test3, test4, test5

# -----------------------------------------------------------

def run_tests() -> None:
    """запустить все тесты надо всеми данными.
    построить таблицу из результатов.
    """

    print("%-20s" % "данные \\ тест", end="")
    
    for itest, test in enumerate(tests):
        print("%-15s" % names[itest], end="")
    print()

    for idata, dset in enumerate(data, 1):
        print("набор %2d            " % idata, end="")

        for test in tests:
            res =  test(dset)
            res = ["нет", "да"] [res]
            print("%-15s" % res, end="")
        
        print()

# -----------------------------------------------------------

def desc_tests() -> None:
    """распечатать описания тестов
    """

    global names
    names = []
    
    print("\nОписания тестов\n")

    for test in tests:
        desc = test.__doc__.strip().replace("\n", "")

        name, info = desc.split('.', maxsplit=1)

        names.append(name)

        print(f"{name} : {info}")
        
# -----------------------------------------------------------

def main() -> None:
    """главный запуск
    """

    prepare()

    print(f"""
==========================================================================================
                       Задача про радугу
==========================================================================================

Исходные данные

Цвета радуги:
""")

    print(*colors, sep=", ", end="\n")

    print(f"""
Наборы данных для тестирования:
""")

    # ~ pprint(data)

    for i, s in enumerate(data, 1):
        print("набор", i, ": ", end="")
        print(*s, sep=", ")

    desc_tests()

    print("""
==========================================================================================
""")

    run_tests()

    print("""
==========================================================================================

""")


main()

# -----------------------------------------------------------
# результаты

# ~ ==================================================================
                       # ~ Задача про радугу
# ~ ==================================================================

# ~ Исходные данные

# ~ Цвета радуги:

# ~ красный, оранжевый, жёлтый, зелёный, голубой, синий, фиолетовый

# ~ Наборы данных для тестирования:

# ~ набор 1 : красный, оранжевый, жёлтый, зелёный, голубой, синий, фиолетовый
# ~ набор 2 : фиолетовый, синий, голубой, зелёный, жёлтый, оранжевый, красный
# ~ набор 3 : чёрный, белый, оранжевый, жёлтый, красный, зелёный, голубой, синий, фиолетовый
# ~ набор 4 : оранжевый, жёлтый, красный, зелёный, голубой, синий, фиолетовый
# ~ набор 5 : красный, зелёный, голубой, сюзюлевый, синий, фиолетовый
# ~ набор 6 : красненький, зелёненький, голубенький, сюзюлевый, синенький, серенький, фиолетовый
# ~ набор 7 : серый, оранжевый, жёлтый, зелёный

# ~ Описания тестов

# ~ проверка а : верно ли, что все слова соответствуют радуге, причём обязательно в прямом порядке?
# ~ проверка б :  ... но порядок произвольный, но все по 1 разу?
# ~ проверка в :  ... причём обязательно в прямом порядке, но все по 1 разу?
# ~ проверка г :  среди данных слов есть в т.ч. и все цвета радуги, в любом порядке...?
# ~ проверка д :  среди данных слов есть в т.ч. и все цвета радуги, в прямом либо обратном порядке... по 1 разу?

# ~ ==================================================================

# ~ данные \ тест       проверка а     проверка б     проверка в     проверка г     проверка д     
# ~ набор  1            True           True           True           True           True           
# ~ набор  2            False          True           False          True           True           
# ~ набор  3            False          False          False          True           False          
# ~ набор  4            False          True           False          True           False          
# ~ набор  5            False          False          False          False          False          
# ~ набор  6            False          False          False          False          False          
# ~ набор  7            False          False          False          False          False  

# ~ ==================================================================

# -----------------------------------------------------------
