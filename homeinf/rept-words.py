#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-03 2025-01-13 1.1
# rept-words.py

# ~ Пересечения слов

# ~ Дан набор слов.
# ~ Найти пары слов, имеющих наибольшее количество одинаковых букв, идущих подряд.

# ~ пример:
# ~ вертушка полушка шкаф шкатулка втулка полуостров
# ~ имеет максимум
# ~ "тулка" для шкатулка и втулка


stroki = """
вертушка полушка шкаф шкатулка втулка полуостров
дело задело делопроизводитель поделом
стратег стратосфера растрата таран растопырка тарабарщина
листинг вокалист стиляга растительность глист
"""

class ex(Exception): pass
    

def frep(stroka):

    print(f"ищем длинные слова в строке: {stroka}")
    
    words = stroka.strip().split()
    mlen = max( [ len(x) for x in words ])

    # ~ print(f"для {words} -> макс. длина {mlen}")

    try:

        for dlina in range(mlen, 0, -1):
            # ~ print(f"проверка для длины {dlina}:", end=" ")

            for iword in range(len(words)):
                
                word = words[iword]
                
                if len(word) < dlina:
                    continue

                # ~ print(f"слово {word}", end=": ")

                for start in range(len(word) - dlina + 1):
                    # ~ print(start, end=",")

                    sub = word[start:start+dlina]
                    # ~ print(f"тест на подслово {sub}", end=", ")

                    for other in range(iword+1, len(words)):

                        if sub in words[other]:

                            print(f"найдена пара: '{word}' и '{words[other]}' с общей частью '{sub}'")
                            raise ex

    except ex:
        ...

        print()



def main():
    for stroka in stroki.strip().splitlines():
        frep(stroka)


main()
