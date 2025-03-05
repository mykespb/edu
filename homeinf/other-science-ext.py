#!/usr/bin/env python
# Mikhail (myke) Kolodin
# other-science-ext.py
# 2025-02-17 2025-02-19 2.1

# ~ Лишнее слово в науке
# ~ ------------------------------------

# ~ Есть неколько наборов слов,
# ~ соответствующих научным дисциплинам.
# ~ Есть фраза, включающая эти слова из одной области
# ~ и ещё одно лишнее слово.
# ~ Определить научную область и лишнее слово.
# ~ Расширяем фразы мусором.

# ~ Пример:
# ~ """
# ~ физика тяжесть давление сила масса вес сопротивление напряжение скорость ускорение
# ~ геометрия точка линия прямая плоскость пространство биссектриса касательная объём площадь гипербола парабола сечение пересечение проекция
# ~ алгебра число интеграл производная функция высота угол первообразная частное делитель делимое произведение синус косинус тангенс котангенс отображение период слагаемое сумма разность
# ~ химия раствор щёлочь кислота основание пробирка лакмус фенолфтолеин спирт осадок огонь
# ~ """

# ~ варианты
# ~ а) в тексте есть только указанные слова, 
# ~ б) текст произвольный, и в нём есть вкрапления этих слов.
# ~ здесь единое решение.


sciwords = """
физика тяжесть давление сила масса вес сопротивление напряжение скорость ускорение
геометрия точка линия прямая плоскость пространство биссектриса касательная объём площадь гипербола парабола сечение пересечение проекция
алгебра число интеграл производная функция высота угол первообразная частное делитель делимое произведение синус косинус тангенс котангенс отображение период слагаемое сумма разность
химия раствор щёлочь кислота основание пробирка лакмус фенолфтолеин спирт осадок огонь
"""

texts = """
тяжесть величина процесс современность неясно предположительно давление сила масса вес тангенс сопротивление
пробирка лакмус Василиса трудно легко весело зелёный функция фенолфтолеин спирт осадок огонь
ускорение касательная трам пам пам объём площадь тут и сказке конец гипербола парабола ученье свет сечение пересечение а неучёных тьма проекция
"""

from collections import Counter
from pprint import pprint

def prepare():
    """подготовить данные к обработке"""

    global bytopic, tostudy

    bytopic = {}
    for note in sciwords.strip().splitlines():
        topic, *words = note.strip().split()
        bytopic[topic] = words

    tostudy = []
    for text in texts.strip().splitlines():
        tostudy.append(text.strip().split())

    # ~ print(f"{bytopic=}")
    # ~ print(f"{tostudy=}")
    

from collections import defaultdict

def gather():
    """собрать нужное вместе"""
    
    global bytopic, tostudy

    for task in tostudy:
        print("\nизучаем задачу про:", *task)

        temy = defaultdict(int)
        
        for what in task:
            for tema, words in bytopic.items():
                if what in words:
                    temy[tema] += 1

        most = Counter(temy)
        # ~ print("ответ:", most)
        most = most.most_common(2)
        # ~ print("счётчик:", most)

        print(f"основная тема: {most[0][0]}, а лишнее слова из темы: {most[1][0]}")

prepare()

pprint(bytopic, compact=True)
pprint(tostudy, compact=True)

gather()


# результат:

# ~ {'алгебра': ['число', 'интеграл', 'производная', 'функция', 'высота', 'угол',
             # ~ 'первообразная', 'частное', 'делитель', 'делимое', 'произведение',
             # ~ 'синус', 'косинус', 'тангенс', 'котангенс', 'отображение',
             # ~ 'период', 'слагаемое', 'сумма', 'разность'],
 # ~ 'геометрия': ['точка', 'линия', 'прямая', 'плоскость', 'пространство',
               # ~ 'биссектриса', 'касательная', 'объём', 'площадь', 'гипербола',
               # ~ 'парабола', 'сечение', 'пересечение', 'проекция'],
 # ~ 'физика': ['тяжесть', 'давление', 'сила', 'масса', 'вес', 'сопротивление',
            # ~ 'напряжение', 'скорость', 'ускорение'],
 # ~ 'химия': ['раствор', 'щёлочь', 'кислота', 'основание', 'пробирка', 'лакмус',
           # ~ 'фенолфтолеин', 'спирт', 'осадок', 'огонь']}
# ~ [['тяжесть', 'давление', 'сила', 'масса', 'вес', 'тангенс', 'сопротивление'],
 # ~ ['пробирка', 'лакмус', 'функция', 'фенолфтолеин', 'спирт', 'осадок', 'огонь'],
 # ~ ['ускорение', 'касательная', 'объём', 'площадь', 'гипербола', 'парабола',
  # ~ 'сечение', 'пересечение', 'проекция']]

# ~ изучаем задачу про: тяжесть давление сила масса вес тангенс сопротивление
# ~ ответ: Counter({'физика': 6, 'алгебра': 1})
# ~ основная тема: физика, а лишнее слова из темы: алгебра

# ~ изучаем задачу про: пробирка лакмус функция фенолфтолеин спирт осадок огонь
# ~ ответ: Counter({'химия': 6, 'алгебра': 1})
# ~ основная тема: химия, а лишнее слова из темы: алгебра

# ~ изучаем задачу про: ускорение касательная объём площадь гипербола парабола сечение пересечение проекция
# ~ ответ: Counter({'геометрия': 8, 'физика': 1})
# ~ основная тема: геометрия, а лишнее слова из темы: физика

# ~ или

# ~ изучаем задачу про: тяжесть давление сила масса вес тангенс сопротивление
# ~ основная тема: физика, а лишнее слова из темы: алгебра

# ~ изучаем задачу про: пробирка лакмус функция фенолфтолеин спирт осадок огонь
# ~ основная тема: химия, а лишнее слова из темы: алгебра

# ~ изучаем задачу про: ускорение касательная объём площадь гипербола парабола сечение пересечение проекция
# ~ основная тема: геометрия, а лишнее слова из темы: физика

# ~ изучаем задачу про: тяжесть величина процесс современность неясно предположительно давление сила масса вес тангенс сопротивление
# ~ основная тема: физика, а лишнее слова из темы: алгебра

# ~ изучаем задачу про: пробирка лакмус Васлиса трудно легко весело зелёный функция фенолфтолеин спирт осадок огонь
# ~ основная тема: химия, а лишнее слова из темы: алгебра

# ~ изучаем задачу про: ускорение касательная трам пам пам объём площадь тут и сказке конец гипербола парабола ученье свет сечение пересечение а неучёных тьма проекция
# ~ основная тема: геометрия, а лишнее слова из темы: физика
