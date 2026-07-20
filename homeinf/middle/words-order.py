#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-05-02 2026-05-02 1.1
# words-order.py

# ~ Порядок слов

# ~ Дан список слов и список чисел.
# ~ Выбрать и напечатать слова в соответствии с их номерами в списке чисел.

# ~ Пример: 
# ~ words = "хорошо стране жить советской в эх"
# ~ order = [5, 0, 4, 1, 3, 2]
# ~ вывод: "эх хорошо в стране советской жить"

# ~ (возможно повторное использование слов:
# ~ words = "понимаешь это странно очень"
# ~ order = 0, 1, 2, 3, 2
# ~ )

# ~ об ошибках сообщать, а не ломаться.

success = "Failure Success".split()


def reasm(what : str, how : list[int]):
    try:
        what = what.split()
        return True, [ what[num] for num in how ]
    except:
        return False, "Cannot reassemble it!"
        

words = "хорошо стране жить советской в эх"
order = [5, 0, 4, 1, 3, 2]

good, result = reasm(words, order)

print(success[good], ":", *result)

words = "понимаешь это странно очень"
order = 0, 1, 2, 3, 2

good, result = reasm(words, order)

print(success[good], ":", *result)

words = "Alas it fails"
order = 0, 5

good, result = reasm(words, order)

print(success[good], ":", *result)


# ~ Success : эх хорошо в стране советской жить
# ~ Success : понимаешь это странно очень странно
# ~ Failure : C a n n o t   r e a s s e m b l e   i t !
