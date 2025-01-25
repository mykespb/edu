#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-11 2025-01-25 1.2
# names-ordered.py


# ~ Имена по порядку

# ~ Дан набор имён.
# ~ Определить, идут ли они в алфавитном порядке.

# --------------------------------
# исходные данные

names1 = """
Акулина Амбруазий Аникей Бажена Вилена Виссарион Галактион Ёлка Иннокентий Лукерья
Мэлс Нектарий Пафнутий Савва Севериан Терентий Феодор Филарет Флюра Шурик Эльбрус
"""

names2 = """
Акулина Амбруазий Аникей Бажена Вилена Виссарион Галактион Иннокентий Лукерья
Ратибор Элемир Огнеслав Волямир Велес Баян Добрыня Рада Электра Анри Оскар
Мэлс Нектарий Пафнутий Савва Севериан Терентий Феодор Филарет Флюра Шурик Эльбрус
"""

# --------------------------------
# программы

myorder = "0123456789abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def good_order(text):
    """
    проверить порядок
    """

    # ~ text = text.strip().split()
    # ~ return text == sorted(text)

    # ~ return (txt := text.strip().split()) == sorted(txt)

    return (txt := text.strip().split()) == sorted(txt,
        key = lambda x: [ myorder.find(y.lower()) for y in x ] 
        )
    

def test(text):
    """
    одна проверка
    """

    print("\nтекст:\n", text, "\n=>", "в порядке" if good_order(text) else "не в порядке\n")


def main():
    """
    главный запуск
    """
    
    test(names1)
    test(names2)

main()

# --------------------------------
# тесты

# ~ текст:
 
# ~ Акулина Амбруазий Аникей Бажена Вилена Виссарион Галактион Иннокентий Лукерья
# ~ Мэлс Нектарий Пафнутий Савва Севериан Терентий Феодор Филарет Флюра Шурик Эльбрус
 
# ~ => в порядке

# ~ текст:
 
# ~ Акулина Амбруазий Аникей Бажена Вилена Виссарион Галактион Иннокентий Лукерья
# ~ Ратибор Элемир Огнеслав Волямир Велес Баян Добрыня Рада Электра Анри Оскар
# ~ Мэлс Нектарий Пафнутий Савва Севериан Терентий Феодор Филарет Флюра Шурик Эльбрус
 
# ~ => не в порядке

# --------------------------------
