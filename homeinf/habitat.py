#!/usr/bin/env python

# Mikhail (myke) Kolodin 
# 2025-01-13 2025-01-13 1.0
# habitat.py

# ~ Среда обитания

# ~ Даны наборы существ, живущих в определённых средах, напр.,
# ~ (((
# ~ море акула камбала медуза
# ~ река карась щука уклейка лещ подлещик
# ~ лес синица жаворонок кукушка
# ~ болото цапля лягушка жаба 
# ~ )))
# ~ и строка из некоторых из этих существ, типа
# ~ "щука мурена карась".
# ~ Определить, правильно ли собраны эти существа в тестовую строку,
# ~ если требуется, чтобы все они принадлежали к одной и той же среде обитания
# ~ (не сказано в каждом случае, к какой именно).


sdata = """
море акула нарвал камбала медуза скат кит кашалот
река карась щука уклейка лещ подлещик
лес синица жаворонок кукушка сокол
болото цапля лягушка жаба пиявка
"""

squeries = """
акула камбала медуза
кукушка синица жаба
кукла маня
скат кашалот нарвал
"""


def prepare():
    """всё подготовить"""

    global data, queries

    data = {}

    for row in sdata.strip().splitlines():
        where, *whos = row.strip().split()

        for who in whos:
            data[who] = where    
        
    queries = []

    for row in squeries.strip().splitlines():
        queries.append(row)

    print("data", data)
    print("queries", queries)


def testone(query):
    """протестировать 1 запрос"""

    beasts = query.strip().split()

    try:
        base = data[beasts[0]]
        
        for beast in beasts[1:]:
            if data[beast] != base:
                return False

    except KeyError as err:
        print(f"\nнедопустимый зверь {err}!")
        return False

    return True
    

def testall():
    """оттестировать всё"""

    for query in queries:
        print(f"\nзапрос '{query}' даёт ответ",
            ["отрицательный", "положительный"] [testone(query)]
            )


prepare()
testall()


# результат:

# ~ data {'акула': 'море', 'нарвал': 'море', 'камбала': 'море', 'медуза': 'море', 'скат': 'море', 'кит': 'море', 'кашалот': 'море', 'карась': 'река', 'щука': 'река', 'уклейка': 'река', 'лещ': 'река', 'подлещик': 'река', 'синица': 'лес', 'жаворонок': 'лес', 'кукушка': 'лес', 'сокол': 'лес', 'цапля': 'болото', 'лягушка': 'болото', 'жаба': 'болото', 'пиявка': 'болото'}

# ~ queries ['акула камбала медуза', 'кукушка синица жаба', 'кукла маня', 'скат кашалот нарвал']

# ~ запрос 'акула камбала медуза' даёт ответ положительный

# ~ запрос 'кукушка синица жаба' даёт ответ отрицательный

# ~ недопустимый зверь 'кукла'!

# ~ запрос 'кукла маня' даёт ответ отрицательный

# ~ запрос 'скат кашалот нарвал' даёт ответ положительный
