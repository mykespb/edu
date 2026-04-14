#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-04-15 2026-04-15 1.1
# yabeda.py

# ~ В рассказе есть имена (они записаны заглавными или дан список имён).
# ~ Заменить все имена на следующие по списку (циклически).

names_eng = "Ann Bob Charlie Dasha Eva Harris Ira Jane Koko Lena Marfa Nick Olga Parasha Qwen Roger Sarah Tina Uma Venera Wolfen Xenia Yoda Zena"

story_eng = "Ann did bad thing. Zena didn't."

names_rus = "Анька Бориска Верка Данька"

story_rus = "Анька говорит, что бяку делает Бориска и не надо так. А Бориска не делает, это Верка делает. Вовсе не Верка а Данька таую бяку делает, а Анька буку делает, вот так!"


def klyauza(names, story):
    out_story = ""
    names = names.split()
    story = story.split()

    for word in story:
        if word in names:
            out_story += names[(names.index(word) + 1) % len(names)] + " "
        else:
            out_story += word + " "

    return out_story


print(klyauza(names_eng, story_eng))
print(klyauza(names_rus, story_rus))


# ~ Bob did bad thing.
# ~ Бориска говорит, что бяку делает Верка и не надо так. А Верка не делает, это Данька делает. Вовсе не Данька а Анька таую бяку делает, а Бориска буку делает, вот так!
