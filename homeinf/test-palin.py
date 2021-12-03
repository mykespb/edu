#!/python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-12-04 2021-12-04 1.2
# para-palin.py

# ~ найти в строке все пары слов-палиндромов
# ~ и распечатать (каждую пару - не более 1 раза)
# ~ хорошо бы сразу прокрутить несколько примеров
# ~ регистр слов игнорировать

stroki = """кони Инок ваня иван новая
Голод пара палиндром долог
Меня никто не слышит
зов болото ВОЗ иноков колесо важен лишь оселок
кто тут лог мал лама дол гол
"""

for frase in stroki.split("\n"):
    frase = frase.strip().lower()
    if not frase:
        continue

    print ("фраза:", frase)

    for one in frase.split():
        for two in frase.split():
            if one != two and one == two[::-1] and one < two:
                print (f"пара:  {one}, {two}")
