#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-27 2025-01-27 1.0
# mousquetaires.py

# ~ Три мушкетёра
# ~ --------------------------

# ~ Кое-что сообщено про мушкетёров и их слуг,
# ~ в соответствии с романами А.Дюма-отца.
# ~ Уточните кое-что из этого всего.

persons = """
мушкетёр;полностью;слуга
Арамис;шевалье Рене д’Эрбле, епископ Ваннский, генерал иезуитского ордена, герцог Аламедский;Базен
д'Артаньян;шевалье д'Артаньян, маршал Франции;Планше
Атос;Оливье, граф де ла Фер;Гримо
Портос;барон дю Валлон де Брасье де Пьерфон;Мушкетон, Мустон, Бонифаций
"""

# ----------------------------------
# программа

from pprint import pp

# ~ Готовим данные...

texts = persons.strip().splitlines()
info = [portion.split(';') for portion in texts]

head = info[0]
info = info[1:]

SHORTNAME = 0
FULLNAME  = 1
SERVANT   = 2

ARAMIS    = 0
DARTAGNAN = 1
ATOS      = 2
PORTOS    = 3

# ----------------------------------

nl = "\n"
print(nl, "Что мы вообще знаем?")

pp(info, width=120)

# ----------------------------------

print(nl, "Как полностью звали мушкетёра, слугу которого звали Гримо?")

for para in info:
    if "Гримо" in para[SERVANT]:
        print(para[FULLNAME])
        break

# ----------------------------------

print(nl, "Как звали мушкетёра, у слуги которого было несколько имён в романе?")

for para in info:
    if para[SERVANT].count(','):
        print(para[SHORTNAME])

# ----------------------------------

print(nl, "Каково прозвище мушкетёра, который (впоследствии) управлял религиозным орденом?")

for para in info:
    if "орден" in para[FULLNAME]:
        print(para[SHORTNAME])

# ----------------------------------

print(nl, "Каково прозвище мушкетёра, который (впоследствии) дослужился до высшей военной должности?")

duties = "лейтенант капитан майор полковник генерал маршал".split()

for para in info:
    if duties[-1] in para[FULLNAME]:
        print(para[SHORTNAME])

# ----------------------------------

print(nl, "Кто знатнее, Атос или Портос?")

titles = "шевалье барон граф маркиз герцог король".split()

posATOS = posPORTOS = -1
nameATOS = namePORTOS = "?"

for ipos, iname in enumerate(titles):
    if iname in info[ATOS][FULLNAME]:
        posATOS = ipos
        nameATOS = iname
    if iname in info[PORTOS][FULLNAME]:
        posPORTOS = ipos
        namePORTOS = iname

print(f"{posATOS=}, {nameATOS}, {posPORTOS=}, {namePORTOS=}")

if posATOS > posPORTOS:
    print(f"Атос знатнее Портоса, Атос - {nameATOS}, а  Портос - {namePORTOS}")
elif posATOS < posPORTOS:
    print(f"Портос знатнее Атоса, Атос - {nameATOS}, а  Портос - {namePORTOS}")
else:
    print("Не знаю, кто знатнее... А кто?..")

print()

# ----------------------------------
# справки

# ~ https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B8_%D0%BC%D1%83%D1%88%D0%BA%D0%B5%D1%82%D1%91%D1%80%D0%B0

# ~ https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BF%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B5%D0%B9_%D1%80%D0%BE%D0%BC%D0%B0%D0%BD%D0%B0_%C2%AB%D0%A2%D1%80%D0%B8_%D0%BC%D1%83%D1%88%D0%BA%D0%B5%D1%82%D1%91%D1%80%D0%B0%C2%BB
