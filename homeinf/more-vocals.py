#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-08 1.1
# more-vocals.py

# ~ ДЗ3. Больше гласности!
# ~ Определение. Назовём “гласностью” слова количество гласных букв в нём.
# ~ Дана некая строка, состоящая из слов, разделённых пробелами (других символов нет).
# ~ Напечатать её в порядке уменьшения гласности её слов.
# ~ Сделать это программой в 1 строку :)


strs = """
Какая славная погода
Как хорошо хоть песню пой
Над границей тучи ходят хмуро
"""

def tests():
    for test in strs.strip().split("\n"):
        show(test)

def show(s):
    print(" -->", s, "\n", "<--", 
        " ".join(sorted(s.split(), key=lambda k: sum(map(int, [c.lower() in "eyuioaуеыаоэяию" for c in k])), reverse=True)),
        "\n")

tests()

# --> какая славная погода
# <-- какая славная погода

# --> как хорошо хоть песню пой
# <-- хорошо песню как хоть пой

# --> над границей тучи ходят хмуро
# <-- границей тучи ходят хмуро над

