#!/usr/bin/env python

# Mikhail (myke) Kolodin 2025-01-16 2025-01-19 2.1
# rev-strings.py

# ~ Перевернуть все слова внутри строки,
# ~ не используя функцию reverse
# ~ и м.б. и все слова тоже поставить в обратном порядке

# -------------------------------------------

def revstr1(s : str, words : bool = False) -> str:
    """reverse string"""

    pre = [word[::-1] for word in s.strip().split()]

    if words:
        out = " " .join (pre[::-1])
    else:
        out = " " .join (pre)
    
    return out


def revstr2(s : str, words : bool = False) -> str:
    """reverse string"""

    if words:
        return s[::-1]

    return " " .join ([word[::-1] for word in s.strip().split()])


def revstr2(s : str, words : bool = False) -> str:
    """reverse string"""

    if words:
        return s[::-1]

    return " " .join ([word[::-1] for word in s.strip().split()])


revstr = revstr2

# -------------------------------------------

def test(s : str, words : bool = False) -> None:
    """test reverser"""

    print(f"\nстрока '{s}' \nпревращается в строку '{revstr(s, words)}'")

# -------------------------------------------

test("по городу ходила большая крокодила")
test("взвейтесь кострами, синие ночи!")
test("понедельник начинается в субботу")
test("Мы сами знаем, что эта задача не имеет решения. Мы хотимм знать, как её решать!")
test("Cogito ergo sum")
test("1234567890 это десятичные цифры 0987654321")
test("1234567890987654321")

test("по городу ходила большая крокодила", words=True)
test("взвейтесь кострами, синие ночи!", words=True)
test("понедельник начинается в субботу", words=True)
test("Cogito ergo sum", words=True)

# результаты:

# ~ строка 'по городу ходила большая крокодила' 
# ~ превращается в строку 'оп удорог алидох яашьлоб алидокорк'

# ~ строка 'взвейтесь кострами, синие ночи!' 
# ~ превращается в строку 'ьсетйевзв ,имартсок еинис !ичон'

# ~ строка 'понедельник начинается в субботу' 
# ~ превращается в строку 'киньледеноп ястеаничан в утоббус'

# ~ строка 'Мы сами знаем, что эта задача не имеет решения. Мы хотимм знать, как её решать!' 
# ~ превращается в строку 'ыМ имас ,меанз отч атэ ачадаз ен тееми .яинешер ыМ ммитох ,ьтанз как ёе !ьташер'

# ~ строка 'Cogito ergo sum' 
# ~ превращается в строку 'otigoC ogre mus'

# ~ строка '1234567890 это десятичные цифры 0987654321' 
# ~ превращается в строку '0987654321 отэ еынчитясед ырфиц 1234567890'

# ~ строка '1234567890987654321' 
# ~ превращается в строку '1234567890987654321'

# ~ строка 'по городу ходила большая крокодила' 
# ~ превращается в строку 'алидокорк яашьлоб алидох удорог оп'

# ~ строка 'взвейтесь кострами, синие ночи!' 
# ~ превращается в строку '!ичон еинис ,имартсок ьсетйевзв'

# ~ строка 'понедельник начинается в субботу' 
# ~ превращается в строку 'утоббус в ястеаничан киньледеноп'

# ~ строка 'Cogito ergo sum' 
# ~ превращается в строку 'mus ogre otigoC'

# -------------------------------------------
