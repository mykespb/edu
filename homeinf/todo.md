Задачи для реализации в учебных курсах
======================================

Mikhail (myke) Kolodin

2025-01-19

textgraf-trig
--------------------------------------

Графики синуса и косинуса в тексте

В массиве строк.


Однофамильцы в школе.
---------------------------------------

Есть списки классов, вида "имя фамилия".
Найти однофамильцев и выписать, в каких они классах.

а. просто
б. однофамильцы могут отличаться окончаниями вида "Петров - Петрова" или "Зелёный - Зелёная".

пример:
(пустые строки пропускаем,
описание класса начинается строкой вида 
    "класс имя"
)

класс 1а
Иван Сергеев
Шила Мылова
Клава Кардинале

класс 2б
Толик Хозяинов
Проста Гипербола
Мыла Шилова
Иннокентий Сергиевский

класс 3а
Соня Дурова
Иван Дуров
Иван Павлов

(можно воспользоваться конструкцией match-case для кортежей)


Послание от инопланетян
-----------------------------------

Есть наборы текстов.
Среди них, возможно, есть ПоИ.
Оно соответствует некоторым закономерностям.
Найти его или сказать, что нет такого.

Возможные закономерности:

- каждое слово начинается с нескольких букв от предыдущего,
напр.,
soloto osenik iksonet networkas astoplat latassonika sonikatipika

- все слова начинаются с согласных букв, а заканчиваются гласными.

- согласных букв в каждом слове больше, чем гласных.

- длины слов есть ряд (3, 4, 5...) и т.п. по кругу.

- каждое чётное (считаем с 1, по-человечески :) ) слово
соответствует шаблону СГ, т.е. согласная+гласная,
напр.,
"parama ta mubaba mu sigana ne".

- то же, но и короткое слово должно начинаться с той же буквы,
что  и предыдущее длинное,
а длинное должно быть не короче 3 букв.

+ м.б. может применяться сразу несколько правил,
и подходит применение любого к каждой строке.


Правильная дата
-----------------------------------------

Даётся запись даты.
Проверить, правильная ли она,
т.е. 
а) правильно ли записана,
б) возможна ли такая дата.


Первым делом - самолёты
------------------------------------

Даны наборы параметров самолётов по классам.
Даны параметры некоторого самолёта.
Определить, к какому классу он относится.
(М.б. придётся дополнить или округлить).


Fuzzy fitting
--------------------------

Есть "набор" слов и одно слово-"подбор".
Определить, к каким словам из "набора" подходит "подбор",
если "подходит" значит:
подходящее слово содержит все буквы из подбора,
но, возможно, с пропусками (не подряд),
напр.,
"подбору"  "виза"
подходят такие:
подвизаться, виртуализация, вертикализация, вискоза.


Снова об Америке
----------------------------------

Отсортировать штаты по 2ой букве, по последней буквен, по имени в обратном порядке и т.п.

Айдахо
Айова
Алабама
Аляска
Аризона
Арканзас
Вайоминг
Вашингтон
Вермонт
Виргиния
Висконсин
Гавайи
Делавэр
Джорджия
Западная Виргиния
Иллинойс
Индиана
Калифорния
Канзас
Кентукки
Колорадо
Коннектикут
Луизиана
Массачусетс
Миннесота
Миссисипи
Миссури
Мичиган
Монтана
Мэн
Мэриленд
Небраска
Невада
Нью-Гэмпшир
Нью-Джерси
Нью-Йорк
Нью-Мексико
Огайо
Оклахома
Орегон
Пенсильвания
Род-Айленд
Северная Дакота
Северная Каролина
Теннесси
Техас
Флорида
Южная Дакота
Южная Каролина
Юта


Прочее
---------------------------- ---- --- --- -

Вычисление выражений, заданных как текст в строке,
вида:
"1   +34  - 67-7 +18"
а. операции + -
б. операции + - * .
в. то же, и скобки.


Решение линейных уравнений.


Решение квадратных уравнений.


Упрощение выражения и общее приведение подобных
вида
5x- 6 +7 -11x
или со многими переменными
5x- 6 +7 -11x +y -x +78z


Нахождение определителя матрицы 2х2 или 3х3.


Известно что данные 2+ слова можно пересечь в кросворде. Сделать это. 


Известно что данные 5 слов можно пересечь в кросворде,
причём как стороны и диагонали квадрата.
(Стороны нечётной длины (5, 7, 9,...))
Сделать это. 


Девизы штатов США
------------------------------

Штат	Девиз	Перевод	Язык	Принят	*
Айдахо	Esto Perpetua	Будет всегда	латинский	1890	[6][7]
Айова	Our Liberties We Prize and Our Rights We Will Maintain	Мы ценим наши свободы и сохраним наши права	английский	1847	[7][8]
Алабама	Audemus Jura Nostra Defendere[англ.]	Мы защищаем наши права	латинский	1923	[7][9]
Аляска	North to the Future	На север в будущее	английский	1967	[7][10]
Американское Самоа	Samoa, Muamua Le Atua	Самоа, пусть первым будет Бог	самоанский	1973	[11][12]
Аризона	Ditat Deus[англ.]	Господь обогащает	латинский	1863	[7][13][14]
Арканзас	Regnat Populus[англ.]	Народ правит	латинский	1907	[К 2][7][15]
Вайоминг	Equal Rights	Равные права	английский	1893	[16]
Вашингтон	Al-ki	Мало-помалу	чинукский жаргон	—	[К 3][17]
Вермонт	Freedom and Unity[англ.]	Свобода и единство	английский	20 февраля 1779	[7][18]
Виргиния	Sic semper tyrannis	Такова участь тиранов	латинский	1776	[7][19]
Виргинские Острова (США)	United in Pride and Hope	Едины в гордости и надежде	английский	1 января 1991	[11][20]
Висконсин	Forward	Вперёд	английский	1851	[21]
Гавайи	Ua Mau ke Ea o ka ʻĀina i ka Pono	Жизнь страны увековечивается в справедливости	гавайский	31 июля 1843	[К 4][7][22][23]
Гуам	Guahan I Tanó ManChamorro	Гуам — земля народа чаморро	чаморро	1945	[24][11]
Делавэр	Liberty and Independence[англ.]	Свобода и независимость	английский	1847	[7][25]
Джорджия	Wisdom, Justice, and Moderation	Мудрость, справедливость и сдержанность	английский	1798	[7][26][27]
Западная Виргиния	Montani Semper Liberi	Горцы всегда свободны	латинский	26 сентября 1863	[28][29]
Иллинойс	State Sovereignty, National Union	Суверенитет штата, единство нации	английский	1819	[7][30]
Индиана	The Crossroads of America	Перекрёсток Америки	английский	1937	[7][31]
Калифорния	Eureka (Εὕρηκα, Ηὕρηκα)	Эврика (Я нашёл)	греческий	1849	[К 5][7][32]
Канзас	Ad Astra per Aspera	К звёздам через тернии	латинский	1861	[7][33]
Кентукки	United We Stand, Divided We Fall[англ.] Deo Gratiam Habeamus	 В единении — сила (Вместе мы выстоим, порознь — падём) Возблагодарим Господа	английский латинский	1942 2002	[3][7]
Колорадо	Nil Sine Numine	Ничто без Провидения	латинский	5 ноября 1861	[7][34]
округ Колумбия	Justitia Omnibus	Правосудие для всех	латинский	3 августа 1871	[11][35]
Коннектикут	Qui Transtulit Sustinet	Кто пересадил, тот оберегает	латинский	9 октября 1662	[7][36]
Луизиана	Union, Justice, Confidence	Союз, справедливость, уверенность	английский	1902	[7][37]
Массачусетс	Ense petit placidam sub libertate quietem[англ.]	Мечом мы устанавливаем мир, но мир под знаменем свободы	латинский	1775	[7][38]
Миннесота	L’Étoile du Nord	Северная звезда	французский	1861	[К 6][7][39]
Миссисипи	Virtute et Armis	Доблестью и оружием	латинский	7 февраля 1894	[7][40]
Миссури	Salus Populi Suprema Lex Esto	Да будет высшим законом благосостояние народа	латинский	11 января 1822	[7][41]
Мичиган	Si quaeris peninsulam amoenam circumspice	Если ищешь приятный глазу полуостров, посмотри вокруг себя	латинский	2 июня 1835	[К 7][7][42][43]
Монтана	Oro y plata	Золото и серебро	испанский	9 февраля 1865	[7][44]
Мэн	Dirigo[англ.]	Я направляю	латинский	1820	[7][45]
Мэриленд	Fatti Maschii, Parole Femine[англ.]	Твёрдость в делах, мягкость в словах	итальянский	1874	[К 8][7][46][47]
Небраска	Equality Before the Law	Равенство перед законом	английский	1867	[7][48]
Невада	All for Our Country	Всё для нашей страны	английский	24 февраля 1866	[К 9][7][49]
Нью-Гэмпшир	Live Free or Die	Живи свободным или умри (Свобода или смерть)	английский	1945	[7][50]
Нью-Джерси	Liberty and Prosperity	Свобода и процветание	английский	26 марта 1928	[7][51]
Нью-Йорк	Excelsior	Всё выше	латинский	1778	[7][52]
Нью-Мексико	Crescit Eundo	Растёт на ходу	латинский	1887	[К 10][7][53]
Огайо	With God, All Things Are Possible[англ.]	С божьей помощью всё возможно	английский	1 октября 1959	[7][54]
Оклахома	Labor omnia vincit[англ.]	Труд побеждает всё	латинский	10 марта 1893	[К 11][7][57]
Орегон	Alis volat propriis	Она летит на собственных крыльях	латинский	1854	[К 12][К 13][58]
Пенсильвания	Virtue, Liberty, and Independence	Добродетель, свобода и независимость	английский	1875	[7][60]
Пуэрто-Рико	Joannes Est Nomen Eius	Иоанн — имя его	латинский	1511	[К 14][К 15][5][61]
Род-Айленд	Hope	Надежда	английский	1644; утверждён Генеральной ассамблеей 4 мая 1664	[62][63]
Северная Дакота	Liberty and Union, Now and Forever, One and Inseparable[англ.]	Свобода и союз, отныне и навсегда, единый и неделимый	английский	1889	[64]
Северная Каролина	Esse quam videri[англ.]	Быть, а не казаться	латинский	1893	[65]
Теннесси	Agriculture and Commerce	Сельское хозяйство и коммерция	английский	24 мая 1802	[К 16][67]
Техас	Friendship	Дружба	английский	1930	[68]
Флорида	In God We Trust	На Бога уповаем	английский	1868	[К 17][69][7]
Южная Дакота	Under God the People Rule	Власть народа по воле Божьей	английский	1885	[7][71]
Южная Каролина	Dum Spiro Spero , Animis Opibusque Parati	Пока дышу, надеюсь , Готовы душою и действием	латинский	22 мая 1777	[2][7][72]
Юта	Industry	Усердие	английский	3 мая 1896	[К 18][К 19][75]


Метро СПб
----------------------------------

1 Первая линия (Кировско-Выборгская)	2 Вторая линия (Московско-Петроградская)	3 Третья линия (Невско-Василеостровская)	4 Четвёртая линия (Лахтинско-Правобережная)	5 Пятая линия (Фрунзенско-Приморская)	6 Шестая линия (Красносельско-Калининская)

(1)
Девяткино
Гражданский проспект
Академическая
Политехническая
Площадь Мужества
Лесная
Выборгская
Площадь Ленина
Чернышевская
Площадь Восстания
Владимирская
Пушкинская
Технологический институт
Балтийская
Нарвская
Кировский завод
Автово
Ленинский проспект
Проспект Ветеранов

(2)
Парнас
Проспект Просвещения
Озерки
Удельная
Пионерская
Чёрная речка
Петроградская
Горьковская
Невский проспект
Сенная площадь
Технологический институт
Фрунзенская
Московские ворота
Электросила
Парк Победы
Московская
Звёздная
Купчино

(3)
Беговая
Зенит
Приморская
Василеостровская
Гостиный двор
Маяковская
Площадь Александра Невского
Елизаровская
Ломоносовская
Пролетарская
Обухово
Рыбацкое

(4)
Горный институт
Театральная
Спасская
Достоевская
Лиговский проспект
Площадь Александра Невского
Новочеркасская
Ладожская
Проспект Большевиков
Улица Дыбенко

(5)
Комендантский проспект
Старая Деревня
Крестовский остров
Чкаловская
Спортивная
Адмиралтейская
Садовая
Звенигородская
Обводный канал
Волковская
Бухарестская
Международная
Проспект Славы
Дунайская
Шушары

(6)
Путиловская
Юго-Западная

(переходы)
Площадь Восстания→Переход на Маяковскую
Владимирская→Переход на Достоевскую
Пушкинская→Переход на Обводный канал
Технологический институт→Переход к поездам второй линии
Невский проспект→Переход на Гостиный двор
Сенная площадь→Переход на Спасскую Переход на Садовую
Технологический институт→Переход к поездам первой линии
Гостиный двор→Переход на Невский проспект
Маяковская→Переход на Площадь Восстания
Площадь Александра Невского→Переход на Площадь Александра Невского-2
Спасская→Переход на Сенную площадь Переход на Садовую
Достоевская→Переход на Владимирскую
Площадь Александра Невского→Переход на Площадь Александра Невского-1
Садовая→Переход на Сенную площадь Переход на Спасскую
Звенигородская→Переход на Пушкинскую

