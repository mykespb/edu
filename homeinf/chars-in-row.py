#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-03 2025-04-03 1.0
# chars-in-rows.py

# ~ Даётся массив из строк, необходимо вернуть те строки из массива, которые могут быть набраны лишь при использовании знаков из одного ряда клавиатуры.
# ~ (Для простоты берём только латиницу (заглавные).
# ~ Слова=строки заданы в смешанном регистре.)

# keyboard:

kbd = "QWERTYUIOP ASDFGHJKL ZXCVBNM" .split()


# tests:
words1 = ["Hello", "Alaska", "Dad", "Peace"]
words2 = ["omg", 'gosh', 'devil', 'hell']


def check(words):
    """check all words"""
    
    out = []
    for word in words:
        if good(word):
            out.append(word)

    print(f"{words} => {out}")


def good(word):
    """check one word"""

    skbd = list(map(set, kbd))

    return any( set(word.upper()) <= row for row in skbd )
    

check(words1)
check(words2)

# ~ result:
# ~ ['Hello', 'Alaska', 'Dad', 'Peace'] => ['Alaska', 'Dad']
# ~ ['omg', 'gosh', 'devil', 'hell'] => []
