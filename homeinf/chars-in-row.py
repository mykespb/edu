#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-03 2025-04-03 1.2
# chars-in-rows.py

# ~ Даётся массив из строк, необходимо вернуть те строки из массива, которые могут быть набраны лишь при использовании знаков из одного ряда клавиатуры.
# ~ (Для простоты берём только латиницу (заглавные).
# ~ Слова=строки заданы в смешанном регистре.)

# keyboard:

kbd = "QWERTYUIOP ASDFGHJKL ZXCVBNM" .split()


# tests:

words1 = ["Hello", "Alaska", "Dad", "Peace"]
words2 = ["omg", 'gosh', 'devil', 'hell']


# solution:

skbd = list(map(set, kbd))


def check(words):
    """check all words"""
    
    # ~ goods = []
    # ~ for word in words:
        # ~ if good(word):
            # ~ goods.append(word)

    goods = [ word for word in words if good(word) ] 

    print(f"{words} => {goods}")


def good(word):
    """check one word"""

    # ~ sword = set(word.upper())

    # ~ for row in skbd:
        # ~ if sword <= row:
            # ~ return True

    # ~ return False

    return any( [set(word.upper()) <= row for row in skbd] )
    

check(words1)
check(words2)

# ~ result:
# ~ ['Hello', 'Alaska', 'Dad', 'Peace'] => ['Alaska', 'Dad']
# ~ ['omg', 'gosh', 'devil', 'hell'] => []
