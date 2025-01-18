#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-18 2025-01-19 1.2
# irr-verbs.py

# ~ Неправильные глаголы
# ~ Обработать по-всякому
# ~ (напр., совпадают 2 любые формы, или совпадают все 3 формы)

# ----------------------------------
# данные:

verbs = """
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
"""

# ----------------------------------
# обработка:

verbs = verbs.strip().splitlines()
headers = verbs[0]
verbs = verbs[1:]

# ~ print(headers)
# ~ print(verbs)

two = []
three = []

for one in verbs:
    f1, f2, f3, trans = one.strip().split('\t')

    if f1 == f2 == f3:
        three.append(f1)
    elif f1 == f2 or f1 == f3 or f2 == f3:
        two.append(f1)

sepa = '\n' + 80 * '=' + '\n'

print(sepa, f"\nwe have {len(verbs)} irregular verbs")

print(sepa, f"\nverbs with 3 similar forms ({len(three)}):\n", sep="")
print(*three, sep=", ")

print(sepa, f"\nverbs with 2 similar forms ({len(two)}):\n", sep="")
print(*two, sep=", ")

print(sepa)

# ----------------------------------
# результаты:

# ~ ================================================================================

# ~ we have 120 irregular verbs

# ~ ================================================================================

# ~ verbs with 3 similar forms (12):

# ~ bet, cost, cut, hit, hurt, let, put, read, set, shut, split, spread

# ~ ================================================================================

# ~ verbs with 2 similar forms (61):

# ~ beat, become, bend, bind, bleed, breed, bring, build, buy, catch, cling, come, deal, dig, feed, feel, fight, find, flee, hang, have, hear, hold, keep, lay, lead, learn, leave, lend, light, lose, make, mean, meet, pay, run, say, seek, sell, send, shine, shoot, sit, sleep, slide, smell, spell, spend, spill, spin, spoil, stand, sting, strike, sweep, teach, tell, think, understand, win, wind

# ~ ================================================================================

# ----------------------------------
