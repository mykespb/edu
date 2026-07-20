#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-28 2026-06-18 2.2
# re-firms-freq.py

# гистограмма отчёта о компаниях

text = """
For decades, the tech industry has seen a massive shift in dominance, with IBM and Microsoft laying the foundations of the computing era. In the 1980s and 1990s, IBM ruled corporate hardware, while Microsoft captured the software market with Windows. During this time, Apple struggled to find its footing, and Google did not even exist. As Microsoft grew into a monopoly, IBM slowly began shifting its focus away from personal computers toward enterprise services.
The 2000s completely rewritten the scoreboard. Google burst onto the scene, quickly dominating internet search and challenging Yahoo and Microsoft. Meanwhile, Apple launched the iPhone, kicking off a mobile revolution that caught Microsoft off guard. At the same time, Amazon quietly evolved from an online bookstore into an e-commerce giant, while also laying the groundwork for AWS cloud computing. By 2010, Apple and Google were the new kings of tech, while IBM faded from the consumer spotlight.
The 2010s marked the rise of data and social media, establishing the "GAFAM" era: Google, Apple, Facebook (now Meta), Amazon, and Microsoft. During this decade, Microsoft staged a massive comeback through cloud computing, directly fighting Amazon for enterprise dominance. While Apple raked in massive hardware profits, Google and Meta locked down the global digital advertising market.
By the 2020s, a new technological shift arrived: Artificial Intelligence. This era pushed Nvidia into the spotlight. While Microsoft, Google, and Amazon spent billions buying chips to power AI, Nvidia became the most critical company in the world. Microsoft took an early lead by partnering with OpenAI, forcing Google to rapidly reinvent its search business. Meta open-sourced its own AI models to compete, while Apple carefully integrated AI into its massive device ecosystem.
Looking at the overall timeline, the frequency of success has constantly shifted. Microsoft has shown the most incredible staying power, remaining a top player for over forty years. Apple transformed from a nearly bankrupt underdog into the world's most valuable brand. Google and Amazon reshaped daily human life, while Nvidia quietly built the engine that will power the future.
"""

firms = "Yandex Microsoft Google Apple Amazon IBM Meta Nvidia"

# построить гистограмму часто упоминаний этих компаний в отчёте,
# линии - горизонтально,
# компании - в алфавитном порядке.

firms = sorted(firms.split())
print(f"\ncompanies: {firms}\n")

freqs = { name: text.count(name) for name in firms }
# ~ print(freqs)

kmax = max( [ len(x) for x in freqs.keys() ] )
vmax = max( freqs.values() )

mult = 50

for firm in firms:
    print( f"{firm:{kmax+1}}:", "*" * int(freqs[firm] * mult // vmax) )
print()

# ~ --- version with std modules:

import re
from collections import Counter
cnt = Counter()

for name in re.finditer(r"\b(\w+)\b", text):
    if (good := name.group()) in firms:
        cnt[good] += 1
        print(good, end=", ")
print("\n\n", cnt, "\n")

# ~ companies: ['Amazon', 'Apple', 'Google', 'IBM', 'Meta', 'Microsoft', 'Nvidia', 'Yandex']

# ~ Amazon    : *************************
# ~ Apple     : ***********************************
# ~ Google    : ****************************************
# ~ IBM       : ********************
# ~ Meta      : ***************
# ~ Microsoft : **************************************************
# ~ Nvidia    : ***************
# ~ Yandex    : 


# ~ For decades, the tech industry has seen a massive shift in dominance, with IBM and Microsoft laying the foundations of the computing era. In the 1980s and 1990s, IBM ruled corporate hardware, while Microsoft captured the software market with Windows. During this time, Apple struggled to find its footing, and Google did not even exist. As Microsoft grew into a monopoly, IBM slowly began shifting its focus away from personal computers toward enterprise services.
# ~ The 2000s completely rewritten the scoreboard. Google burst onto the scene, quickly dominating internet search and challenging Yahoo and Microsoft. Meanwhile, Apple launched the iPhone, kicking off a mobile revolution that caught Microsoft off guard. At the same time, Amazon quietly evolved from an online bookstore into an e-commerce giant, while also laying the groundwork for AWS cloud computing. By 2010, Apple and Google were the new kings of tech, while IBM faded from the consumer spotlight.
# ~ The 2010s marked the rise of data and social media, establishing the "GAFAM" era: Google, Apple, Facebook (now Meta), Amazon, and Microsoft. During this decade, Microsoft staged a massive comeback through cloud computing, directly fighting Amazon for enterprise dominance. While Apple raked in massive hardware profits, Google and Meta locked down the global digital advertising market.
# ~ By the 2020s, a new technological shift arrived: Artificial Intelligence. This era pushed Nvidia into the spotlight. While Microsoft, Google, and Amazon spent billions buying chips to power AI, Nvidia became the most critical company in the world. Microsoft took an early lead by partnering with OpenAI, forcing Google to rapidly reinvent its search business. Meta open-sourced its own AI models to compete, while Apple carefully integrated AI into its massive device ecosystem.
# ~ Looking at the overall timeline, the frequency of success has constantly shifted. Microsoft has shown the most incredible staying power, remaining a top player for over forty years. Apple transformed from a nearly bankrupt underdog into the world's most valuable brand. Google and Amazon reshaped daily human life, while Nvidia quietly built the engine that will power the future.
# ~ ## Company Mention Counts

# ~ * Microsoft: 7 times (The ultimate survivor)
# ~ * Google: 6 times (The internet gatekeeper)
# ~ * Apple: 5 times (The consumer ecosystem king)
# ~ * Amazon: 4 times (The retail and cloud backbone)
# ~ * IBM: 3 times (The early pioneer)
# ~ * Meta: 2 times (The social media giant)
# ~ * Nvidia: 2 times (The new AI superpower)

# ~ If you'd like, I can:

# ~ * Add exact years to create a specific chronological timeline
# ~ * Include hardware rivalries like Intel vs. AMD vs. Nvidia
# ~ * Turn this into a script for a video essay or presentation

# ~ Let me know how you would like to proceed.


# ~ ---

# ~ "Построй горизонтальную гистограмму, показывающую численность населения в 10 крупнейших городах России. Города покажи в алфавитном порядке. Линии выполняются текстом, знаками "*"."

# ~ Вот текстовая горизонтальная гистограмма для 10 крупнейших городов России по численности населения (на основе актуальных данных Росстата). [1, 2, 3] 
# ~ Города отсортированы в алфавитном порядке, а масштаб линий округлен для удобства восприятия (один знак * равен примерно 250 000 человек).

# ~ Город           | Население     | Гистограмма (масштаб: 1 звезда = 250 тыс. чел.)
# ~ ----------------+---------------+-------------------------------------------------
# ~ Екатеринбург    | ~1,55 млн чел.| ******
# ~ Казань          | ~1,33 млн чел.| *****
# ~ Красноярск      | ~1,21 млн чел.| *****
# ~ Москва          | ~13,27 млн чел| *****************************************************
# ~ Нижний Новгород | ~1,20 млн чел.| *****
# ~ Новосибирск     | ~1,64 млн чел.| ******
# ~ Самара          | ~1,16 млн чел.| *****
# ~ Санкт-Петербург | ~5,65 млн чел.| ***********************
# ~ Уфа             | ~1,16 млн чел.| *****
# ~ Челябинск       | ~1,18 млн чел.| *****

# ~ ## Краткие факты по графику

# ~ * Москва и Санкт-Петербург предсказуемо лидируют с гигантским отрывом, занимая первые две строчки по стране.
# ~ * Новосибирск прочно удерживает статус третьего по величине города России и крупнейшего в ее азиатской части.
# ~ * Разница между городами, занимающими места с 5-го по 10-е (Казань, Красноярск, Нижний Новгород, Челябинск, Самара, Уфа), минимальна, поэтому в данном масштабе длина их текстовых линий практически одинакова.

# ~ Если хотите, мы можем:

# ~ * Изменить масштаб (например, сделать 1 звезду равной 100 000 человек, чтобы точнее показать разницу между Поволжьем, Сибирью и Уралом).
# ~ * Включить в список все 16 городов-миллионников России.
# ~ * Построить аналогичный текстовый график для крупнейших по площади территорий городов.

# ~ Напишите, какой вариант вам подходит больше!

# ~ [1] [https://xn--h1alcedd.xn--d1aqf.xn--p1ai](https://xn--h1alcedd.xn--d1aqf.xn--p1ai/questions/spisok-rossiyskikh-gorodov-millionnikov/)
# ~ [2] [https://novomoscow.ru](https://novomoscow.ru/info/goroda-millionniki/)
# ~ [3] [https://vfokuse.mail.ru](https://vfokuse.mail.ru/articles/67741856-skolko-gorodov-v-rossii/)

# ~ ---

# ~ "Изменить масштаб (например, сделать 1 звезду равной 100 000 человек, чтобы точнее показать разницу между Поволжьем, Сибирью и Уралом).Включить в список все 16 городов-миллионников России."

# ~ Вот обновленная горизонтальная гистограмма, включающая все 16 официальных городов-миллионников России в алфавитном порядке. Масштаб изменен: теперь один знак * равен ровно 100 000 человек. [1, 2, 3] 
# ~ Для точности отображения количество звезд рассчитано путем математического округления официальных данных Росстата. [3] 

# ~ Город           | Население*    | Гистограмма (масштаб: 1 звезда = 100 тыс. человек)
# ~ ----------------+---------------+---------------------------------------------------------------------------------------------------------------------------------
# ~ Волгоград       | ~1,03 млн чел.| **********
# ~ Воронеж         | ~1,05 млн чел.| ***********
# ~ Екатеринбург    | ~1,54 млн чел.| ***************
# ~ Казань          | ~1,31 млн чел.| *************
# ~ Краснодар       | ~1,12 млн чел.| ***********
# ~ Красноярск      | ~1,20 млн чел.| ************
# ~ Москва          | ~13,10 млн чел| *********************************************************************************************************************************
# ~ Нижний Новгород | ~1,21 млн чел.| ************
# ~ Новосибирск     | ~1,64 млн чел.| ****************
# ~ Омск            | ~1,11 млн чел.| ***********
# ~ Пермь           | ~1,03 млн чел.| **********
# ~ Ростов-на-Дону  | ~1,14 млн чел.| ***********
# ~ Самара          | ~1,16 млн чел.| ************
# ~ Санкт-Петербург | ~5,60 млн чел.| ********************************************************
# ~ Уфа             | ~1,16 млн чел.| ************
# ~ Челябинск       | ~1,18 млн чел.| ************

# ~ * Примечание: Для построения использованы официальные муниципальные данные Росстата без учета расширенных городских агломераций. Количество звезд округлено до ближайшего целого числа. [4] 
# ~ ## Что изменилось при новом масштабе?

# ~ * Разница регионов: Теперь наглядно виден разрыв между Поволжьем, Сибирью и Уралом. Например, Новосибирск (Сибирь) заметно длиннее Омска. Екатеринбург за счет своего масштаба четко выделяется на фоне других уральских миллионников — Перми и Челябинска. [4, 5] 
# ~ * Поволжский кластер: Города Поволжья теперь не сливаются. Казань (13 звезд) визуально обходит Нижний Новгород, Самару и Уфу (по 12 звезд). [4] 
# ~ * Новые миллионники: Города, относительно недавно перешагнувшие этот рубеж (Краснодар, Воронеж, Красноярск), аккуратно замыкают основную группу с длинами линий от 11 до 12 звезд. [4, 6] 
# ~ * Лидеры: Из-за высокой детализации линия Москвы теперь растянулась на рекордную 131 звезду, а Санкт-Петербург занял твердые 56 звезд. [4] 

# ~ Если вы хотите продолжить работу с географическими данными, я могу:

# ~ * Отсортировать этот список по географическому положению (с запада на восток), чтобы оценить плотность населения.
# ~ * Составить таблицу, показывающую, в каком году каждый из этих городов официально стал миллионником.
# ~ * Добавить в сравнение города-кандидаты, которые ближе всего подобрались к отметке в 1 миллион (например, Тюмень или Саратов). [4, 7] 

# ~ Какое направление вам интересно?

# ~ [1] [https://xn--h1alcedd.xn--d1aqf.xn--p1ai](https://xn--h1alcedd.xn--d1aqf.xn--p1ai/questions/spisok-rossiyskikh-gorodov-millionnikov/)
# ~ [2] [https://vfokuse.mail.ru](https://vfokuse.mail.ru/articles/67741856-skolko-gorodov-v-rossii/)
# ~ [3] [https://www.mojgorod.ru](http://www.mojgorod.ru/cities/pop2025_1.html)
# ~ [4] [https://novomoscow.ru](https://novomoscow.ru/info/goroda-millionniki/)
# ~ [5] [https://znanierussia.ru](https://znanierussia.ru/articles/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B8%D0%BB%D0%BB%D0%B8%D0%BE%D0%BD%D0%B5%D1%80%D1%8B_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8)
# ~ [6] [https://travel.yandex.ru](https://travel.yandex.ru/journal/krupneyshie-gorodamillionniki-rossii/)
# ~ [7] [https://ru.wikipedia.org](https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%B0-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83)

# ~ "Измени масштаб: самая длинная полоса должна быть 40 знаков."

# ~ Город           | Население     | Гистограмма (масштаб: максимум = 40 знаков)
# ~ ----------------+---------------+-----------------------------------------
# ~ Волгоград       | ~1,01 млн чел.| ***
# ~ Воронеж         | ~1,04 млн чел.| ***
# ~ Екатеринбург    | ~1,55 млн чел.| *****
# ~ Казань          | ~1,33 млн чел.| ****
# ~ Краснодар       | ~1,15 млн чел.| ***
# ~ Красноярск      | ~1,21 млн чел.| ****
# ~ Москва          | ~13,27 млн чел| ****************************************
# ~ Нижний Новгород | ~1,20 млн чел.| ****
# ~ Новосибирск     | ~1,64 млн чел.| *****
# ~ Омск            | ~1,10 млн чел.| ***
# ~ Пермь           | ~1,03 млн чел.| ***
# ~ Ростов-на-Дону  | ~1,14 млн чел.| ***
# ~ Самара          | ~1,15 млн чел.| ***
# ~ Санкт-Петербург | ~5,65 млн чел.| *****************
# ~ Уфа             | ~1,17 млн чел.| ****
# ~ Челябинск       | ~1,18 млн чел.| ****

# ~ Вот обновленная горизонтальная гистограмма для всех 16 городов-миллионников России, в которой масштаб изменен так, что самая длинная полоса (Москва) составляет ровно 40 знаков. [1] 
# ~ Города расположены строго в алфавитном порядке, а количество звезд рассчитано пропорционально численности населения. [1] 

# ~ Город           | Население     | Гистограмма (масштаб: максимум = 40 знаков)
# ~ ----------------+---------------+-----------------------------------------
# ~ Волгоград       | ~1,01 млн чел.| ***
# ~ Воронеж         | ~1,04 млн чел.| ***
# ~ Екатеринбург    | ~1,55 млн чел.| *****
# ~ Казань          | ~1,33 млн чел.| ****
# ~ Краснодар       | ~1,15 млн чел.| ***
# ~ Красноярск      | ~1,21 млн чел.| ****
# ~ Москва          | ~13,27 млн чел| ****************************************
# ~ Нижний Новгород | ~1,20 млн чел.| ****
# ~ Новосибирск     | ~1,64 млн чел.| *****
# ~ Омск            | ~1,10 млн чел.| ***
# ~ Пермь           | ~1,03 млн чел.| ***
# ~ Ростов-на-Дону  | ~1,14 млн чел.| ***
# ~ Самара          | ~1,15 млн чел.| ***
# ~ Санкт-Петербург | ~5,65 млн чел.| *****************
# ~ Уфа             | ~1,17 млн чел.| ****
# ~ Челябинск       | ~1,18 млн чел.| ****

# ~ ## Заметные особенности при новом масштабе:

# ~ * Сжатие данных: Из-за уменьшения разрешения до 40 символов для Москвы многие города с населением около 1–1,15 млн человек (Волгоград, Воронеж, Краснодар, Омск, Пермь, Ростов-на-Дону, Самара) теперь имеют одинаковую длину полосы в 3 звезды.
# ~ * Группа лидеров: Четко выделяются три уровня: Москва (40), Санкт-Петербург (17) и крупные региональные центры Сибири и Урала — Новосибирск и Екатеринбург (по 5 звезд).

# ~ Если вы хотите продолжить анализ демографии, я могу:

# ~ * Вывести этот же график, но отсортированный по убыванию населения, чтобы сразу видеть реальный рейтинг.
# ~ * Рассчитать, какой процент от общего населения страны живет в каждом из этих городов.
# ~ * Показать динамику: какие города быстрее всего растут, а какие теряют население.

# ~ Какой вариант вам интересен?

# ~ data = {
    # ~ "Волгоград": 1012219,
    # ~ "Воронеж": 1041722,
    # ~ "Екатеринбург": 1548187,
    # ~ "Казань": 1329825,
    # ~ "Краснодар": 1154885,
    # ~ "Красноярск": 1211756,
    # ~ "Москва": 13274285,
    # ~ "Нижний Новгород": 1200187,
    # ~ "Новосибирск": 1637266,
    # ~ "Омск": 1101367,
    # ~ "Пермь": 1027518,
    # ~ "Ростов-на-Дону": 1143123,
    # ~ "Самара": 1154223,
    # ~ "Санкт-Петербург": 5652922,
    # ~ "Уфа": 1166098,
    # ~ "Челябинск": 1176770
# ~ }
# ~ moscow_pop = data["Москва"]
# ~ max_stars = 40
# ~ # scale factor: stars per personscale = max_stars / moscow_pop
# ~ for city in sorted(data.keys()):
    # ~ pop = data[city]
    # ~ stars = round(pop * scale)
    # ~ # Ensure moscow is exactly 40
    # ~ if city == "Москва":
        # ~ stars = 40
    # ~ print(f"{city:<16} | {pop/1e6:.2f} млн | {'*' * stars} ({stars})")


# ~ [1] [https://xn--h1alcedd.xn--d1aqf.xn--p1ai](https://xn--h1alcedd.xn--d1aqf.xn--p1ai/questions/spisok-rossiyskikh-gorodov-millionnikov/)

