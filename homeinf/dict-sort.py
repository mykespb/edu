#!/usr/bin/env python
# myke 2022-05-06 2022-05-06 1.0
# dict-sort.py

# ~ """
# ~ — Голубчики, — сказал Фёдор Симеонович озабоченно, разобравшись в почерках. — Это же проблема Бен Бецалеля. Калиостро же доказал, что она не имеет решения.

# ~ — Мы сами знаем, что она не имеет решения, — сказал Хунта, немедленно ощетиниваясь. — Мы хотим знать, как её решать.

# ~ — Как-то странно ты рассуждаешь, Кристо… Как же искать решение, когда его нет? Бессмыслица какая-то…

# ~ — Извини, Теодор, но это ты очень странно рассуждаешь. Бессмыслица — искать решение, если оно и так есть. Речь идёт о том, как поступать с задачей, которая решения не имеет. Это глубоко принципиальный вопрос…

                 # ~ Аркадий и Борис Стругацкие. Понедельник начинается в субботу\

# ~ https://ru.wikibooks.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D1%8B_%D0%9A%D1%80%D0%B8%D1%81%D1%82%D0%BE%D0%B1%D0%B0%D0%BB%D1%8F_%D0%A5%D1%83%D0%BD%D1%82%D1%8B

# ~ """

# ~ Как известно, словари - неупорядоченные коллекции (в общем случае).
# ~ А как их отсортировать?

# ~ Пусть нам достался словарь, для которого мы знаем возможный порядок сортировки,
# ~ но в том, что у нас, ключи  значения идут перемешанными.

import random

# Пусть есть

abc = '''
A Alfa
B Bravo
C Charlie
D Delta
E Echo
F Foxtrot
G Golf
H Hotel
I India
J Juliett
K Kilo
L Lima
M Mike
N November
O Oscar
P Papa
Q Quebec
R Romeo
S Sierra
T Tango
U Uniform
V Victor
W Whiskey
X X-ray
Y Yankee
Z Zulu
'''

# получим словарь и всё перемешаем

s = [p.split() for p in abc.strip().split("\n")]
random.shuffle(s)
d = dict(s)
# ~ print(s)
print("\nбыло:\n", d)

# получили примерно такое:

# {'D': 'Delta', 'B': 'Bravo', 'F': 'Foxtrot', 'V': 'Victor', 'L': 'Lima', 'P': 'Papa', 'K': 'Kilo', 'T': 'Tango', 'S': 'Sierra', 'J': 'Juliett', 'W': 'Whiskey', 'Z': 'Zulu', 'I': 'India', 'O': 'Oscar', 'M': 'Mike', 'Q': 'Quebec', 'N': 'November', 'X': 'X-ray', 'E': 'Echo', 'C': 'Charlie', 'H': 'Hotel', 'R': 'Romeo', 'Y': 'Yankee', 'G': 'Golf', 'A': 'Alfa', 'U': 'Uniform'}

# а как теперь отсортировать?

# вот так:

sd = {}
for k in sorted(d.keys()):
    sd[k] = d[k]

# печатаем и радуемся
print("\n\nстало:\n", sd)
