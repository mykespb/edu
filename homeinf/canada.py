#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-10 2024-12-14 1.0
# canada.py
# многокритериальные оценки для Канады -- выбор оптимального места для проживания

from pprint import pp

srcdata = """номер	буквы	название	английский	французский	политика	тепло	влажность	школы	промышленность	население	культура
1	DC	Британская Колумбия	да	нет	левый	5	7	7	5	8	7
2	AB	Альберта	да	нет	правый	4	3	7	6	6	6
3	SK	Саскачеван	да	нет	правый	3	3	6	5	4	5
4	MB	Манитоба	да	нет	правый	3	3	6	5	4	4
5	ON	Онтарио	да	нет	правый	4	5	7	8	9	9
6	QC	Квебек	нет	да	левый	4	5	7	7	8	9
7	NB	Нью-Брансуик	да	да	левый	4	5	6	4	4	3
8	PE	Остров Принца Эдуарда	да	да	левый	4	5	6	2	2	3
9	NS	Новая Шотландия	да	нет	левый	4	5	4	3	3	3
10	NL	Ньюфаундленд и Лабрадор	да	нет	левый	3	5	4	2	1	2
11	YT	Юкон	да	нет	левый	1	4	2	1	1	1
12	NT	Северо-Западные территории	да	нет	левый	1	3	1	1	1	1
13	NU	Нунавут	да	нет	левый	1	3	1	1	1	1"""

srcquests = """номер	показатель	вопрос
1	английский	Важно ли, чтобы говорили по-английски?
2	французский	Важно ли, чтобы говорили по-французски?
3	политика	Предпочитаете левые (от 1) или правые (к 9) взгляды?
4	тепло	Любите ли тепло?
5	влажность	Любите ли влажность?
6	школы	Важно ли наличие хороших школ?
7	промышленность	Важно ли наличие рабочих мест в промышленности?
8	население	Хотите ли много народа вокруг?
9	культура	Важно ли наличие объектов и событий культуры?"""

def prepare_data():
    """подготовить данные для обработки"""
    
    global data, titles, quests
    
    # обработка исходных численных данных
    
    titles = srcdata.strip().split("\n", 1)[0].split("\t")
    print(titles)
    
    data = []
    
    for elem in srcdata.strip().split("\n")[1:]:
        points = elem.split("\t")
        
        points[0] = int(points[0])
        points[3] = 9 if points[3] == 'да' else 0
        points[4] = 9 if points[4] == 'да' else 0
        points[5] = 9 if points[5] == 'правый' else 0
        
        for pnum in range(6, len(points)):
            points[pnum] = int(points[pnum])
    
        print(elem)
        
        data.append(points)
    
    pp(data)
    
    # обработка вопросов 
    
    quests = []
    
    for elem in srcquests.strip().split("\n")[1:]:
        points = elem.split("\t")
        quests.append(points)
    
    
def ask_user():
    """запросить ответы пользователя на вопросы"""
    # если нет ответов, вернуть False

    global data, titles, quests
    
    print("""
Ответьте, пожалуйства, на несколько вопросов.
Укажите по шкале 1..9, насколько для вас важен каждый из предложенных параметров.
Если не важен, укажите 1. Если очень важен, то укажите 9.
Если не хотите отвечать на вопросы, нажмите просто ВВОД.
""")
    
    result = []
    
    for quest in quests:
        resp = input(f"Вопрос {int(quest[0])}. {quest[2]} => ")
        if resp:
            resp = int(resp)
            if 0 < resp <= 9:
                result.append(resp)
                # print(f"{resp=}")
            else:
                return False
        else:
            return False
        
    return result


def advice(request):
    """всё подсчитать и дать рекомендацию: 
    какие провинции предпочтительнее для проживания 
    в соответствии с пожеланиями клиента
    """

    global data, titles, quests
    
    print(f"{request=}")
    
    marks = [ 
            [ sum ( [ request[qnum] * data[prov][qnum+3]   for qnum in range(len(quests)) ] ),
            prov
            ]
            for prov in range(len(data))
        ]
        
    marks.sort(reverse=True)
    
    print("\nЛучше всего вам подходят:")
    for prio in range(3):
        print(f"{prio+1}. {data[prio][2]} c {marks[prio][0]} баллами.")

    
def main():
    prepare_data()
    
    print("\nДоброго времени суток! Давайте выберем оптимальную провинцию.")
    
    while (request := ask_user()):
        advice(request)
        
    print("\n\nСпасибо за работу!\n")
    

main()
