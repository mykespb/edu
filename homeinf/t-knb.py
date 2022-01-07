#!/usr/bin/env python3.10

# Mikhail (myke) Kolodin, 2021
# 2022-01-08 2022-01-08 1.2
# камень - ножницы - бумага

from random import choice

help = """
давай поиграем в знаменитую игру "камень - ножницы - бумага"!

будем по очереди называть эти предметы, и кто-то выиграет:

камень сильнее ножниц,
ножницы сильнее бумаги.
бумага сильнее камня.

когда надоест, просто нажми ВВОД.

поехали!
"""

def play():
    """один раунд"""
    
    human = input("\nну введи же своё слово (можно только 1ую букву) -- ")

    if not human:
        return False

    if human[0] not in "кнб":
        print("не знаю такого предмета! повтори!")
        return True

    comp = choice("камень ножницы бумага".split())
    print(f"у меня {comp}.") 

    who = compwin(comp[0], human[0])
    
    if who == 1:
        print("я выиграл!")
    elif who == -1:
        print("ты выиграл!")
    else:
        print("ничья!")

    return True


def compwin(c, h):
    """сравнение"""

    if c == h:
        return 0

    elif ((c=="к" and h=="н") or
        (c=="н" and h=="б") or
        (c=="б" and h=="к")):
        return 1

    else:
        return -1


def main():
    """главная"""

    print(help)
    while play(): pass
    print("\nпока!..")

main()
