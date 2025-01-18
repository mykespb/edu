Задачи для реализации в учебных курсах
======================================

Mikhail (myke) Kolodin

2025-01-18

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


Неправильные глаголы
--------------------------

Infinitive	Past Simple (V2)	Participle II (V3)	Перевод
arise	arose	arisen	подниматься
awake	awoke	awoken	пробуждать
be	was (were)	been	быть
bear	bore	born	рожать, переносить
beat	beat	beaten	бить
become	became	become	становиться
begin	began	begun	начинать
bend	bent	bent	наклонять
bet	bet	bet	заключать пари
bind	bound	bound	связывать
bite	bit	bitten	кусать
bleed	bled	bled	кровоточить
blow	blew	blown	дуть
break	broke	broken	ломать
breed	bred	bred	разводить животных
bring	brought	brought	приносить
build	built	built	строить
buy	bought	bought	покупать
catch	caught	caught	ловить
choose	chose	chosen	выбирать
cling	clung	clung	цепляться
come	came	come	приходить
cost	cost	cost	стоить
cut	cut	cut	резать
deal	dealt	dealt	вести дела
dig	dug	dug	копать
do	did	done	делать
draw	drew	drawn	рисовать, тянуть
drink	drank	drunk	пить
drive	drove	driven	водить автомобиль
eat	ate	eaten	кушать
fall	fell	fallen	падать
feed	fed	fed	кормить
feel	felt	felt	чувствовать
fight	fought	fought	бороться
find	found	found	находить
flee	fled	fled	сбегать
fly	flew	flown	летать
forbid	forbade	forbidden	запрещать
forget	forgot	forgotten	забывать
forgive	forgave	forgiven	прощать
freeze	froze	frozen	замораживать
get	got	got (gotten)	получать
give	gave	given	давать
go	went	gone	идти
grow	grew	grown	расти
hang	hung	hung	висеть
have	had	had	иметь
hear	heard	heard	слышать
hide	hid	hidden	прятать
hit	hit	hit	ударять, попадать
hold	held	held	держать
hurt	hurt	hurt	причинять боль
keep	kept	kept	сохранять, соблюдать
know	knew	known	знать
lay	laid	laid	класть
lead	led	led	вести, лидировать
learn	learnt (learned)	learnt (learned)	учиться, узнавать
leave	left	left	покидать, оставлять
lend	lent	lent	давать взаймы
let	let	let	позволять
lie	lay	lain	лежать
light	lit	lit	зажигать, освещать
lose	lost	lost	терять
make	made	made	делать, мастерить
mean	meant	meant	значить
meet	met	met	встречать, знакомиться
pay	paid	paid	платить
put	put	put	класть, ставить
read	read	read	читать
ride	rode	ridden	ездить верхом
ring	rang	rung	звонить
rise	rose	risen	возрастать, подниматься
run	ran	run	бежать
say	said	said	сказать
see	saw	seen	видеть
seek	sought	sought	искать
sell	sold	sold	продавать
send	sent	sent	посылать
set	set	set	устанавливать
shake	shook	shaken	трясти
shine	shone	shone	светить, сиять
shoot	shot	shot	стрелять
show	showed	shown	показывать
shrink	shrank	shrunk	сжиматься
shut	shut	shut	закрывать, затворять
sing	sang	sung	петь
sit	sat	sat	сидеть
sleep	slept	slept	спать
slide	slid	slid	скользить
smell	smelt	smelt	пахнуть, нюхать
speak	spoke	spoken	говорить
spell	spelt (spelled)	spelt (spelled)	произносить или писать по буквам
spend	spent	spent	тратить, проводить время
spill	spilt (spilled)	spilt (spilled)	разлить
spin	spun	spun	крутить
split	split	split	разделять, раскалывать
spoil	spoilt (spoiled)	spoilt (spoiled)	портить
spread	spread	spread	разворачивать, распространять
stand	stood	stood	стоять
steal	stole	stolen	воровать
sting	stung	stung	жалить
stink	stank	stunk	вонять
strike	struck	struck	бастовать, ударять
swear	swore	sworn	клясться, ругаться
sweep	swept	swept	подметать
swell	swelled	swollen (swelled)	опухать
swim	swam	swum	плавать
take	took	taken	брать
teach	taught	taught	обучать
tear	tore	torn	рвать
tell	told	told	рассказывать
think	thought	thought	думать
throw	threw	thrown	бросать
understand	understood	understood	понимать
wake	woke	woken	будить
wear	wore	worn	носить (одежду)
win	won	won	побеждать
wind	wound	wound	обматывать, изгибаться
write	wrote	written	писать

или

be, was/were, been — быть
become, became, become — становиться
begin, began, begun — начинать
break, broke, broken — ломать
bring, brought, brought — приносить
build, built, built — строить
buy, bought, bought — покупать
choose, chose, chosen — выбирать
come, came, come — приходить
do, did, done — делать
drive, drove, driven — водить, вести (машину)
fall, fell, fallen — падать
feel, felt, felt — чувствовать
find, found, found — находить
get, got, got — получать
give, gave, given — давать
go, went, gone — идти, ехать
grow, grew, grown — расти
have, had, had — иметь
hear, heard, heard — слышать
hold, held, held — держать
keep, kept, kept — хранить, держать
know, knew, known — знать
lead, led, led — вести
leave, left, left — покидать, оставлять
let, let, let — позволять
lie, lay, lain — лежать
lose, lost, lost — терять
make, made, made — делать
mean, meant, meant — значить
meet, met, met — встречать, знакомиться
pay, paid, paid — платить
put, put, put — класть, ставить
read, read, read — читать
run, ran, run — бежать
say, said, said — говорить, сказать
see, saw, seen — видеть
send, sent, sent — посылать
set, set, set — устанавливать
show, showed, shown/showed — показывать
sit, sat, sat — сидеть
speak, spoke, spoken — говорить
spend, spent, spent — тратить
stand, stood, stood — стоять
take, took, taken — брать
tell, told, told — говорить, рассказывать
think, thought, thought — думать
understand, understood, understood — понимать
wear, wore, worn — носить
write, wrote, written — писать

Обработать по-всякому
(напр.,
совпадают 1 и 2 формы,
или совпадают все 3 формы)


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


Сложение плюсов и минусов
-----------------------------------

вида
+++ ----- ++++ + + ---
это
+3 -5 -4 +1 +1 -3
а могут быть с или без пробелов
(на самом деле надо просто посчитать плюсы и минусы и вычесть)


Австралия
------------------------------

№	Название	Тип адм. ед.	Столица	Население, чел. (2021)[140]	Площадь, км²[141]
1	Австралийская столичная территория	территория	Канберра	454 499	2358
2	Виктория	штат	Мельбурн	6 503 491	227 444
3	Западная Австралия	штат	Перт	2 660 026	2 527 013
4	Квинсленд	штат	Брисбен	5 156 138	1 729 742
5	Новый Южный Уэльс	штат	Сидней	8 072 163	801 150
6	Северная территория	территория	Дарвин	232 605	1 347 791
7	Тасмания	штат	Хобарт	557 571	68 401
8	Южная Австралия	штат	Аделаида	1 781 516	984 321
Всего	25 422 788	7 688 220

обработать всячески


Прочее
---------------------------- ---- --- --- -

Вычисление выражений, заданных как текст в строке,
вида:
"1   +34  - 67-7 +18"

Решение линейных уравнений

Решение квадратных уравнений

Упрощение выражения и общее приведение подобных
вида
5x- 6 +7 -11x
или со многими переменными
5x- 6 +7 -11x +y -x +78z

Нахождение определителя матрицы 2х2 или 3х3


