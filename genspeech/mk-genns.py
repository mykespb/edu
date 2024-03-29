#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-16 2022-03-17 1.1
# mk-genns.py

#Ученый приходит в офис и говорит: "Я совершил открытие". В ответ слышит "Нам такие не нужны". С тех пор это закон.

who   = "Учёный;Больной;Пикачу;Кот;Никто;Террорист;Сантехник;Динозавр;Мама;Менеджер" .split(";")

comes = "в офис;в небытие;в больницу;драться;в лабораторию;на вызов;в парк юрского периода;на родительское собрание;к кошке;в метро" .split(";")

says  = "Я совершил открытие!;Пика-пика!;(мысленно) Привет, ничто!;У меня болит голова.;Давай заведём котят!;Я мама Вовочки.;Я увольняюсь!;Аллах акбар!;Возьмите меня есть туристов!;Какой серьёзный засор!" .split(";")

ands  = "кошка отвечает;учительница;небытие ему в ответ;доктор ему;тут по громкоговорителю;учёное сообщество;в ответ слышит;из трубы голос;начальник ему;бульбазавр на это" .split(";")

words = "Ты не пикачу, ты сантехник!;Я не доктор, я динозавр!;Давай лучше мышат!;Привет, ничтожество!;Следующая станция Бесконечная;Вы не мама, вы папа!;Нам такие не нужны!;Ты же на пенсию вышел!;Ты новый Эйнштейн!;Ну хочешь шутку расскажу?" .split(";")

sends = "Энтропия нарастала;И уехали в Казахстан;Динозавр всё равно съел туристов;Держите зачётку;И все стали танцевать;Вот и сказочке конец;Так появилась Вселенная;С тех пор это закон;И немедленно выпил;)))" .split(";")

from random import choice

def gena():
    """генератор расказов"""

    return (
        choice(who) +
        " приходит " + choice(comes) +
        " и говорит: '" + choice(says) +
        "'. А " + choice(ands) +
        ": '" + choice(words) +
        "'. " + choice(sends) + ".")

def pgena():
    print(gena())

pgena()

# ~ Мама приходит к кошке и говорит: 'У меня болит голова.'. А кошка отвечает: 'Я не доктор, я динозавр!'. Энтропия нарастала.

# ~ Пикачу приходит в офис и говорит: 'Какой серьёзный засор!'. А в ответ слышит: 'Следующая станция Бесконечная'. И все стали танцевать.

# ~ Динозавр приходит к кошке и говорит: 'У меня болит голова.'. А бульбазавр на это: 'Ты новый Эйнштейн!'. С тех пор это закон.

# ~ Никто приходит в лабораторию и говорит: '(мысленно) Привет, ничто!'. А тут по громкоговорителю: 'Я не доктор, я динозавр!'. Так появилась Вселенная.

# ~ Террорист приходит на вызов и говорит: 'Я увольняюсь!'. А начальник ему: 'Следующая станция Бесконечная'. ))).

# ~ Динозавр приходит в парк юрского периода и говорит: 'Давай заведём котят!'. А тут по громкоговорителю: 'Я не доктор, я динозавр!'. Динозавр всё равно съел туристов.
