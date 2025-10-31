#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-10-17 2025-10-31 2.0
# has-ada.py

# ~ Есть список слов, разделённых пробелами.
# ~ Найти слова, в которых есть заданные буквы (напр., "ада").
# ~ Регистры произвольны.

words = """
адажио илиада рвакля шмакля дракля коррида Арамис
арахна хорда Ада адамант кандалы аркада Арканар Канада
"""

#def with_word(what, words):
def with_word(what: str, words: str) -> list:
    """find 'em"""

    return [word for word in words.strip().split() if what.lower() in word.lower()]


def main():
    """run it!"""

    print("\nдано:\n", words.strip())
    print("\nвывод:\n", ", ".join(with_word("ада", words)), "\n")


main()
