#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-15 2025-02-15 1.1
# kergudu.py

# ~ Бамбарбия кергуду

# ~ Некий тип прикидывается местным жителем и говорит с туристом на типа своём местном языке.
# ~ Турист знает, что в языке все слова заканчиваются на гласную,
# ~ а если число слогов чётное, то и предпоследняя буква тоже гласная.
# ~ Проверить, не врёт ли типа местный тип.


speach = """
Бамбарбия кергуду
Пара мара тура мама папа
Хавала мапала туркая муркая
Глокая Куздра кудрячила бокрёнка
Кырлая Мырлая бра мра пра фыркая
Тудысь сюдысь тут не садись
"""


def test(slova):
    """одна проверка"""

    vowels = "уеЁыаоэяию"

    for slovo in slova.strip().lower().split():
        if slovo[-1] not in vowels:
            return False
        vc = 0
        for c in slovo:
            if c in vowels:
                vc += 1
        if vc % 2 == 0 and slovo[-2] not in vowels:
            return False

    return True


def main():
    """всё проверяем"""

    for slova in speach.strip().splitlines():
        print("\n", slova, "=>",
            ["плохой", "хороший"] [test(slova)])
    print()

    
main()
