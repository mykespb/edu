#!/usr/bin/env python3.10
# makula.py
# (C) Mikhail Kolodin, 2021
# ver. 2021-08-26 2021-08-27 1.8
# updated 2021-10-05 to py3.10

# ----------------------------------------------

# ~ сбор макулатуры
# ~ дан список имён учеников класса.
# ~ известно, что каждый сдал столько кг макулатуры, сколько букв в его имени.
# ~ подсчитать результат класса.

# ~ дано:
names = "Вася Коля Иванушка Тимур Иннокентий Веста Мальвина".split()

# ~ решение:
kg = sum([len(x) for x in names])
print("\nученики", end=" ")
print(*names, sep=", ", end=" ")
print("всего сдали", kg, "кг")

# ----------------------------------------------

# ~ то же, есть списки, но на этот раз в них указаны и имена, и фамилии
# ~ задание то же

# ~ дано:
names = "Вася Васильков,Коля Колокольчиков,Иванушка Интернешнл,Тимур Батькович,Иннокентий Невинный,Веста Нордова,Мальвина Карлова".split(",")

# ~ решение:
pnames = [x.split()[0] for x in names ]
kg = sum([len(x) for x in pnames])
print("\nученики", end=" ")
print(*names, sep=", ", end=" ")
print("всего сдали", kg, "кг")

# ----------------------------------------------

# ~ классы соревнуются по сбору.
# ~ найти, какие классы собрали больше всего
# ~ (может быть несколько победителей)

# ~ дано:
got = 34, 15, 11, 10, 11, 17, 42, 42, 33, 23, 10
# ~ got = 34, 15, 11, 10, 11, 17, 42, 42, 33, 23, 90
# начиная с 0 элемента = 1 класс

# ~ решение:
print()
for klass, kg in enumerate(got):
    print("класс", klass+1, "сдал", round(kg), "кг")

# всего сдали
kgall = sum(got)

maks = max(got)
avg  = kgall / len(got)
print("всего сдали:", kgall, ", максимум равен", maks, ", в среднем по", round(avg), "кг на класс")

best = [i+1 for i, j in enumerate(got) if j == maks]
print("победили классы:" if len(best)>1 else "победил класс", end=" ")
print(*best, sep=", ")
print()

# ----------------------------------------------

# ~ награды
# ~ за сбор всем выдали 1000 рублей
# ~ и распределили пропорционально сданным кг
# ~ сколько кому досталось?

# всего денег
money = 1000

# ~ решение
prop = [money * x / kgall for x in got]

print("всего денег:", round(sum(prop)))
for klass, gotmoney in enumerate(prop):
    print("класс", klass+1, "получил", round(gotmoney), "руб.")

# ----------------------------------------------

# ~ ученики Вася, Коля, Иванушка, Тимур, Иннокентий, Веста, Мальвина всего сдали 44 кг

# ~ ученики Вася Васильков, Коля Колокольчиков, Иванушка Интернешнл, Тимур Батькович, Иннокентий Невинный, Веста Нордова, Мальвина Карлова всего сдали 44 кг

# ~ класс 1 сдал 34 кг
# ~ класс 2 сдал 15 кг
# ~ класс 3 сдал 11 кг
# ~ класс 4 сдал 10 кг
# ~ класс 5 сдал 11 кг
# ~ класс 6 сдал 17 кг
# ~ класс 7 сдал 42 кг
# ~ класс 8 сдал 42 кг
# ~ класс 9 сдал 33 кг
# ~ класс 10 сдал 23 кг
# ~ класс 11 сдал 10 кг
# ~ всего сдали: 248 , максимум равен 42 , в среднем по 23 кг на класс
# ~ победили классы: 7, 8

# ~ всего денег: 1000
# ~ класс 1 получил 137 руб.
# ~ класс 2 получил 60 руб.
# ~ класс 3 получил 44 руб.
# ~ класс 4 получил 40 руб.
# ~ класс 5 получил 44 руб.
# ~ класс 6 получил 69 руб.
# ~ класс 7 получил 169 руб.
# ~ класс 8 получил 169 руб.
# ~ класс 9 получил 133 руб.
# ~ класс 10 получил 93 руб.
# ~ класс 11 получил 40 руб.
