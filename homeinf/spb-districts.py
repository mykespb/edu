#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-10 2024-12-10 0.1
# spb-districts.py
# многокритериальные оценки для Канады -- выбор оптимального места для проживания

data = """номер	буквы	название	воздух	залив	школы	магазины	культура	офисы	промышленность	безопасность	жкх
1	адм	Адмиралтейский	4	5	4	4	7	4	4	5	5
2	вас	Василеостровский	4	8	6	6	5	7	6	5	5
3	выб	Выборгский	4	4	4	4	3	4	6	5	4
4	кал	Калининский	4	2	4	5	4	5	6	5	5
5	кир	Кировский	3	4	4	4	4	4	6	4	4
6	кол	Колпинский	5	1	3	4	3	3	6	4	4
7	крг	Красногвардейский	4	3	4	5	4	5	6	4	4
8	крс	Красносельский	4	8	5	5	4	5	6	5	5
9	кро	Кронштадский	5	9	4	4	4	3	4	5	4
10	кур	Курортный	5	9	4	4	3	4	4	5	4
11	лом	Ломоносовский	5	9	4	4	3	3	4	5	4
12	мос	Московский	3	4	5	6	6	6	6	4	4
13	нев	Невский	4	3	4	5	4	5	6	5	4
14	пав	Павловский	5	1	4	5	5	5	4	5	4
15	пег	Петроградский	3	4	4	5	5	6	6	4	4
16	пед	Петродворцовый	5	9	4	4	5	4	5	5	4
17	при	Приморский	5	9	4	5	4	6	5	5	4
18	пуш	Пушкинский	5	1	5	4	4	5	4	5	4
19	фру	Фрунзенский	3	2	4	5	5	5	4	4	4
20	цен	Центральный	4	3	4	6	6	6	5	5	5"""

quests = """номер	параметр	вопрос
1	воздух	Насколько для вас важно качество воздуха?
2	залив	Насколько для вас важна близость залива (или иных водоёмов)?
3	школы	Насколько для вас важно наличие школ поблизости?
4	магазины	Насколько для вас важно количество и качество магазинов поблизости?
5	культура	Насколько для вас важно богатство и разнообразие культурных объектов и событий?
6	офисы	Насколько для вас важно наличие офисных центров и помещений?
7	промышленность	Насколько для вас важно наличие объектов промышленности и соотв. работы?
8	безопасность	Насколько для вас важна безопасность для себя и семьи?
9	жкх	Насколько для вас важно высокое качество услуг ЖКХ?"""

def prepare_data():
    """подготовить данные для обработки"""
    ...
    
def ask_user():
    """запросить ответы пользователя на вопросы"""
    ...
    
def advice():
    """всё подсчитать и дать рекомендацию: 
    какие районы предпочтительнее для проживания 
    в соответствии с пожеланиями клиента
    """
    ...
    
def main():
    ...
    