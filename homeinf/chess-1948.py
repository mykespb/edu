#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-23 2025-01-23 1.0
# chess-1948.py

# ~ Дана турнирная таблица, 
# ~ Кто стал победителем турнира и чемпионом мира по шахматам 1948 года?

# -----------------------------------------------

turnir = """
Ботвинник ННВННВВВВПВНПВВВНВНН
Керес     ППППВВВНПНПНВПНВНВВВ
Решевский ПНВППННПННВНПВНВННВВ
Смыслов   ННПННППНВНННВННВВПВВ
Эйве      ПНПННППВПППНППППННПП
"""

# -----------------------------------------------
# 

def main():
    """запуск"""

    table = []
    values = { 'В': 2, 'Н': 1, 'П': 0 }

    for person in turnir.strip().splitlines():
        name, games = person.strip().split()
        # ~ print(f"игрок {name} играл так: {games}")

        table.append( (name,
            sum (map(
                lambda x: values[x], games
                ))
            ))

    table.sort(key = lambda x: x[1], reverse = True)

    print("все участники:", *table)
    print("победитель:", table[0][0], "с", table[0][1], "очками.")


main()

# -----------------------------------------------

# ~ все участники: ('Ботвинник', 28) ('Смыслов', 22) ('Керес', 21) ('Решевский', 21) ('Эйве', 8)
# ~ победитель: Ботвинник с 28 очками.

# -----------------------------------------------

# ~ Дана турнирная таблица вида
# ~ (фамилии указаны по алфавиту)

# ~ ===
# ~ Ботвинник ННВННВВВВПВНПВВВНВНН
# ~ Керес     ППППВВВНПНПНВПНВНВВВ
# ~ Решевский ПНВППННПННВНПВНВННВВ
# ~ Смыслов   ННПННППНВНННВННВВПВВ
# ~ Эйве      ПНПННППВПППНППППННПП
# ~ ===

# ~ где В=выигрыш (1 очко), Н=ничья (1/2 очка), П=поражение (0 очков).
# ~ Кто стал победителем турнира и чемпионом мира по шахматам 1948 года?

# ~ См. Матч-турнир за звание чемпиона мира по шахматам 1948
# ~ https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%82%D1%87-%D1%82%D1%83%D1%80%D0%BD%D0%B8%D1%80_%D0%B7%D0%B0_%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D1%87%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%B0_%D0%BC%D0%B8%D1%80%D0%B0_%D0%BF%D0%BE_%D1%88%D0%B0%D1%85%D0%BC%D0%B0%D1%82%D0%B0%D0%BC_1948
# ~ Михаил Ботвинник захватил лидерство с первых туров и выиграл турнир с заметным преимуществом, имея положительный баланс со всеми соперниками и проиграв лишь 2 партии (причём вторую — уже обеспечив себе победу в турнире). Он стал шестым (и первым советским) чемпионом мира по шахматам.

# ~ 1	Флаг СССР Михаил Ботвинник						½	½	1	½	½	1	1	1	1	0	1	½	0	1	1	1	½	1	½	½	10	2	8	14	1
# ~ 2	Флаг СССР Василий Смыслов	½	½	0	½	½						0	0	½	1	½	½	½	1	½	½	1	1	0	1	1	6	4	10	11	2
# ~ 3	Флаг СССР Пауль Керес	0	0	0	0	1	1	1	½	0	½						0	½	1	0	½	1	½	1	1	1	8	7	5	10½	3—4
# ~ 4	Флаг США (48 звёзд) Самуэль Решевский	0	½	1	0	0	½	½	0	½	½	1	½	0	1	½						1	½	½	1	1	6	5	9	10½	3—4
# ~ 5	Флаг Нидерландов Макс Эйве

# -----------------------------------------------
