#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# acronims.py
# 2025-02-15 2025-02-15 1.0

# ~ Акронимы

# ~ Есть набор имён вида
# ~ (((
# ~ Ахматова, Анна Андреевна
# ~ Визбор, Юрий Иосифович
# ~ Маяковский, Владимир Владимирович
# ~ )))

# ~ переформатировать их как
# ~ (((
# ~ А.А. Ахматова
# ~ Ю.И. Визбор
# ~ В.В. Маяковский
# ~ )))

# ~ т.е.
# ~ И.О._Фамилия

# ~ Несоответствия обнаруживать и сообщать о них.

# -------------------------------------------

names = """
Ахматова, Анна Андреевна
Визбор, Юрий Иосифович
Маяковский, Владимир Владимирович
сэр Конан Дойль, Артур
"""

# -------------------------------------------

def main1():
    """прокрутить все тесты"""
    
    for inum, name in enumerate(names.strip().splitlines(), 1):
        print(f"имя #{inum}: {name} -- {test(name)}")


def main2():
    """прокрутить все тесты"""
    
    for inum, name in enumerate(names.strip().splitlines(), 1):
        try:
            print(f"имя #{inum}: {name} -- {test(name)}")
        except AssertionError as e:
            print(f"Ошибка в имени '{name}'")


def test(name):
    """проверить одного писателя"""

    parts = name.strip().split()

    assert len(parts) == 3
    assert parts[0][-1] == ","

    result = parts[1][0] + '.' + parts[2][0] + '. ' + parts[0][:-1]

    return result


main = main2
main()
