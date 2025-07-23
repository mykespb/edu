#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-07-23 2.0

# ~ numinlists.py

# ~ Есть глубоко вложенный список (кортеж).
# ~ Определить, есть ли в нём заданное число.

# примеры для проверки
lex = (
    (1,),
    (1, 2),
    (1, 2, 3),
    (1, (2, 3)),
    (1, (2, (3, (4, 5, 6), 7), 8), 9)
)

# решалка
def find(lst, num):
    """найти num в lst"""

    for e in lst:
        if e == num:
            return True

        if type(e) == tuple and find(e, num):
            return True

    return False

# решалка
def findall(lst, num):
    """найти num в lst"""

    for seq in lst:
        print("tuple = ", seq, ", number=", num, ", result = ", find(seq, num))
    
# запуски
findall(lex, 1)
findall(lex, 4)
findall(lex, 0)
findall(lex, 100500)


# ~ tuple =  (1,) , number= 1 , result =  True
# ~ tuple =  (1, 2) , number= 1 , result =  True
# ~ tuple =  (1, 2, 3) , number= 1 , result =  True
# ~ tuple =  (1, (2, 3)) , number= 1 , result =  True
# ~ tuple =  (1, (2, (3, (4, 5, 6), 7), 8), 9) , number= 1 , result =  True
# ~ tuple =  (1,) , number= 4 , result =  False
# ~ tuple =  (1, 2) , number= 4 , result =  False
# ~ tuple =  (1, 2, 3) , number= 4 , result =  False
# ~ tuple =  (1, (2, 3)) , number= 4 , result =  False
# ~ tuple =  (1, (2, (3, (4, 5, 6), 7), 8), 9) , number= 4 , result =  True
# ~ tuple =  (1,) , number= 0 , result =  False
# ~ tuple =  (1, 2) , number= 0 , result =  False
# ~ tuple =  (1, 2, 3) , number= 0 , result =  False
# ~ tuple =  (1, (2, 3)) , number= 0 , result =  False
# ~ tuple =  (1, (2, (3, (4, 5, 6), 7), 8), 9) , number= 0 , result =  False
# ~ tuple =  (1,) , number= 100500 , result =  False
# ~ tuple =  (1, 2) , number= 100500 , result =  False
# ~ tuple =  (1, 2, 3) , number= 100500 , result =  False
# ~ tuple =  (1, (2, 3)) , number= 100500 , result =  False
# ~ tuple =  (1, (2, (3, (4, 5, 6), 7), 8), 9) , number= 100500 , result =  False
