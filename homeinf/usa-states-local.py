#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2024-11-06 2024-11-22 2.0
# usa-states-local.py

# ~ Даны данные о штатах США.
# в каких штатах различаются крупнейший город и столица?

data = """№	Штат	Официальное название	Почтовый код	Дата основания	Население, человек (перепись 2020)	Территория, км²	ВВП на душу населения (2005), дол. США	Административный центр	Крупнейший город 
1	Айдахо	State of Idaho	ID	3 июля 1890	1 839 106	216 632	33 012	Бойсе	Бойсе
2	Айова	State of Iowa	IA	28 декабря 1846	3 190 369	145 743	38 529	Де-Мойн	Де-Мойн
3	Алабама	State of Alabama	AL	14 декабря 1819	5 024 279	135 765	32 866	Монтгомери	Бирмингем
4	Аляска	State of Alaska	AK	3 января 1959	733 391	1 717 854	60 079	Джуно	Анкоридж
5	Аризона	State of Arizona	AZ	14 февраля 1912	7 151 502	295 254	36 327	Финикс	Финикс
6	Арканзас	State of Arkansas	AR	15 июня 1836	3 011 524	137 732	31 233	Литл-Рок	Литл-Рок
7	Вайоминг	State of Wyoming	WY	10 июля 1890	576 851	253 348	53 843	Шайенн	Шайенн
8	Вашингтон	State of Washington	WA	11 ноября 1889	7 705 281	184 827	42 702	Олимпия	Сиэтл
9	Вермонт	State of Vermont	VT	4 марта 1791	643 077	24 923	37 130	Монтпилиер	Берлингтон
10	Виргиния	Commonwealth of Virginia	VA	25 июня 1788	8 631 393	110 785	46 613	Ричмонд	Верджиния-Бич
11	Висконсин	State of Wisconsin	WI	29 мая 1848	5 893 718	169 639	39 294	Мадисон	Милуоки
12	Гавайи	State of Hawai`i Moku`a-ina o Hawai`i	HI	21 августа 1959	1 455 271	28 311	42 119	Гонолулу	Гонолулу
13	Делавэр	State of Delaware	DE	7 декабря 1787	989 948	6452	64 437	Довер	Уилмингтон
14	Джорджия	State of Georgia	GA	2 января 1788	10 711 908	153 909	40 155	Атланта	Атланта
15	Западная Виргиния	State of West Virginia	WV	20 июня 1863	1 793 716	62 755	29 602	Чарлстон	Чарлстон
16	Иллинойс	State of Illinois	IL	3 декабря 1818	12 812 508	149 998	43 886	Спрингфилд	Чикаго
17	Индиана	State of Indiana	IN	11 декабря 1816	6 785 528	94 321	38 048	Индианаполис	Индианаполис
18	Калифорния	State of California	CA	9 сентября 1850	39 538 223	423 970	44 846	Сакраменто	Лос-Анджелес
19	Канзас	State of Kansas	KS	29 января 1861	2 937 880	213 096	38 419	Топика	Уичито
20	Кентукки	Commonwealth of Kentucky	KY	1 июня 1792	4 505 836	104 659	33 632	Франкфорт	Луисвилл
21	Колорадо	State of Colorado	CO	1 августа 1876	5 773 714	269 837	46 314	Денвер	Денвер
22	Коннектикут	State of Connecticut	CT	9 января 1788	3 605 944	14 357	55 400	Хартфорд	Бриджпорт
23	Луизиана	State of Louisiana État de Louisiane	LA	30 апреля 1812	4 657 757	135 382	36 765	Батон-Руж	Новый Орлеан
24	Массачусетс	Commonwealth of Massachusetts	MA	6 февраля 1788	7 029 917	27 336	51 344	Бостон	Бостон
25	Миннесота	State of Minnesota	MN	11 мая 1858	5 706 494	225 181	45 451	Сент-Пол	Миннеаполис
26	Миссисипи	State of Mississippi	MS	10 декабря 1817	2 961 279	125 443	27 545	Джэксон	Джэксон
27	Миссури	State of Missouri	MO	10 августа 1821	6 154 913	180 533	37 251	Джефферсон-Сити	Канзас-Сити
28	Мичиган	State of Michigan	MI	26 января 1837	10 077 331	250 493	37 338	Лансинг	Детройт
29	Монтана	State of Montana	MT	8 ноября 1889	1 084 225	381 156	31 903	Хелена	Биллингс
30	Мэн	State of Maine	ME	15 марта 1820	1 362 359	91 646	34 105	Огаста	Портленд
31	Мэриленд	State of Maryland	MD	28 апреля 1788	6 177 224	32 133	43 729	Аннаполис	Балтимор
32	Небраска	State of Nebraska	NE	1 марта 1867	1 961 504	200 520	39 950	Линкольн	Омаха
33	Невада	State of Nevada	NV	31 октября 1864	3 104 614	286 367	45 778	Карсон-Сити	Лас-Вегас
34	Нью-Гэмпшир	State of New Hampshire	NH	21 июня 1788	1 377 529	24 217	42 513	Конкорд	Манчестер
35	Нью-Джерси	State of New Jersey	NJ	18 декабря 1787	9 288 994	22 608	49 414	Трентон	Ньюарк
36	Нью-Йорк	State of New York	NY	26 июля 1788	20 201 249	141 300	50 038	Олбани	Нью-Йорк
37	Нью-Мексико	State of New Mexico Estado de Nuevo México	NM	6 января 1912	2 117 522	315 194	35 949	Санта-Фе	Альбукерке
38	Огайо	State of Ohio	OH	1 марта 1803	11 799 448	116 096	38 594	Колумбус	Кливленд
39	Оклахома	State of Oklahoma	OK	16 ноября 1907	3 959 353	181 196	33 978	Оклахома-Сити	Оклахома-Сити
40	Орегон	State of Oregon	OR	14 февраля 1859	4 237 256	255 026	39 920	Сейлем	Портленд
41	Пенсильвания	Commonwealth of Pennsylvania	PA	12 декабря 1787	13 002 700	119 283	39 194	Гаррисберг	Филадельфия
42	Род-Айленд	State of Rhode Island and Providence Plantations	RI	29 мая 1790	1 097 379	4002	40 691	Провиденс	Провиденс
43	Северная Дакота	State of North Dakota	ND	2 ноября 1889	779 094	183 272	37 975	Бисмарк	Фарго
44	Северная Каролина	State of North Carolina	NC	21 ноября 1789	10 439 388	139 509	39 690	Роли	Шарлотт
45	Теннесси	State of Tennessee	TN	1 июня 1796	6 910 840	109 247	37 985	Нашвилл	Мемфис
46	Техас	State of Texas	TX	29 декабря 1845	29 145 505	696 241	42 975	Остин	Хьюстон
47	Флорида	State of Florida	FL	3 марта 1845	21 538 187	170 304	37 889	Таллахасси	Джэксонвилл
48	Южная Дакота	State of South Dakota	SD	2 ноября 1889	886 667	199 905	40 037	Пирр	Су-Фолс
49	Южная Каролина	State of South Carolina	SC	23 мая 1788	5 118 425	82 931	32 848	Колумбия	Колумбия
50	Юта	State of Utah	UT	4 января 1896	3 271 616	219 887	36 377	Солт-Лейк-Сити	Солт-Лейк-Сити"""

def read_states():
    """read data from tabbed multistring"""

    caps = []

    for num, line in enumerate(data.split('\n')):
        if num == 0: continue
        info = line.strip().split('\t')
        if info[-2] != info[-1]:
            caps.append((info[1], info[-2], info[-1]))

    return caps


def capitals():
    """select and print needed states"""
    
    states = read_states()

    for num, state in enumerate(states, 1):
        print(f"{num}. штат: {state[0]}, столица: {state[1]}, крупнейший город: {state[2]}")


capitals()

# ~ https://ru.wikipedia.org/wiki/%D0%90%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%A1%D0%A8%D0%90

# ~ 1. штат: Алабама, столица: Монтгомери, крупнейший город: Бирмингем
# ~ 2. штат: Аляска, столица: Джуно, крупнейший город: Анкоридж
# ~ 3. штат: Вашингтон, столица: Олимпия, крупнейший город: Сиэтл
# ~ 4. штат: Вермонт, столица: Монтпилиер, крупнейший город: Берлингтон
# ~ 5. штат: Виргиния, столица: Ричмонд, крупнейший город: Верджиния-Бич
# ~ 6. штат: Висконсин, столица: Мадисон, крупнейший город: Милуоки
# ~ 7. штат: Делавэр, столица: Довер, крупнейший город: Уилмингтон
# ~ 8. штат: Иллинойс, столица: Спрингфилд, крупнейший город: Чикаго
# ~ 9. штат: Калифорния, столица: Сакраменто, крупнейший город: Лос-Анджелес
# ~ 10. штат: Канзас, столица: Топика, крупнейший город: Уичито
# ~ 11. штат: Кентукки, столица: Франкфорт, крупнейший город: Луисвилл
# ~ 12. штат: Коннектикут, столица: Хартфорд, крупнейший город: Бриджпорт
# ~ 13. штат: Луизиана, столица: Батон-Руж, крупнейший город: Новый Орлеан
# ~ 14. штат: Миннесота, столица: Сент-Пол, крупнейший город: Миннеаполис
# ~ 15. штат: Миссури, столица: Джефферсон-Сити, крупнейший город: Канзас-Сити
# ~ 16. штат: Мичиган, столица: Лансинг, крупнейший город: Детройт
# ~ 17. штат: Монтана, столица: Хелена, крупнейший город: Биллингс
# ~ 18. штат: Мэн, столица: Огаста, крупнейший город: Портленд
# ~ 19. штат: Мэриленд, столица: Аннаполис, крупнейший город: Балтимор
# ~ 20. штат: Небраска, столица: Линкольн, крупнейший город: Омаха
# ~ 21. штат: Невада, столица: Карсон-Сити, крупнейший город: Лас-Вегас
# ~ 22. штат: Нью-Гэмпшир, столица: Конкорд, крупнейший город: Манчестер
# ~ 23. штат: Нью-Джерси, столица: Трентон, крупнейший город: Ньюарк
# ~ 24. штат: Нью-Йорк, столица: Олбани, крупнейший город: Нью-Йорк
# ~ 25. штат: Нью-Мексико, столица: Санта-Фе, крупнейший город: Альбукерке
# ~ 26. штат: Огайо, столица: Колумбус, крупнейший город: Кливленд
# ~ 27. штат: Орегон, столица: Сейлем, крупнейший город: Портленд
# ~ 28. штат: Пенсильвания, столица: Гаррисберг, крупнейший город: Филадельфия
# ~ 29. штат: Северная Дакота, столица: Бисмарк, крупнейший город: Фарго
# ~ 30. штат: Северная Каролина, столица: Роли, крупнейший город: Шарлотт
# ~ 31. штат: Теннесси, столица: Нашвилл, крупнейший город: Мемфис
# ~ 32. штат: Техас, столица: Остин, крупнейший город: Хьюстон
# ~ 33. штат: Флорида, столица: Таллахасси, крупнейший город: Джэксонвилл
# ~ 34. штат: Южная Дакота, столица: Пирр, крупнейший город: Су-Фолс

