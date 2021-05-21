#!/usr/bin/env python
# coding: utf-8

# # Примеры и упражнения по Python3  - средний уровень - часть 1

# Автор-составитель - Михаил Колодин

# Версия 2021-04-16 от 2021-04-18 - 1.3

# Разделы:
# * [Циклы](#loops)
# * [Строки](#strings)
# * [Кортежи и списки, словари и множества](#structs1)
# * [Функции](#functions)
# * [Исключения](#except)
# * [Математика](#math)

# ---
# **Циклы** <a name=loops></a>

# ---
# ***Факториал $n! = 1 \cdot 2 \cdot 3 \cdot \dots \cdot n$***

# In[2]:


UP = 30
f = 1


# In[3]:


for i in range(1, UP):
    f *= i             #  то же, что f = f * i
    print("%10i!  =" % i, "%40i" % f)


# ---
# ***Сколько нулей?***

# __Вопрос.__ Как видно, n! быстро растёт, и на конце этого большого числа появляется много нулей. 
# А сколько именно?
# Само число n! вычислять не надо.
# 
# __Решение.__ Разложим n! на простые множители. 
# Нуль в конце появляется тогда и только тогда, когда перемножаются 2 и 5. 
# Посчитаем пары двоек и пятёрок. 
# Пятёрок меньше, так что посчитаем их. 
# Сумма и даст число нулей на конце n!.

# In[14]:


N = 100    # это исходное число, N!

nuls = 0
for x in range(2, N+1):
    n = x
    while n % 5 == 0:
        n //= 5
        nuls += 1
        
print(f"на конце числа {N}! будет нулей: {nuls}.")


# ---
# ***Константа е - аппроксимация***

# См. [статью в википедии](https://ru.wikipedia.org/wiki/E_(%D1%87%D0%B8%D1%81%D0%BB%D0%BE))

# $$e = \sum\limits_{n=0}^\infty \frac1{n!} = \frac1{1!} + \frac1{2!} + \frac1{3!} + \frac1{4!} + \frac1{5!} + ... = \frac11 + \frac12 + \frac16 + \frac1{24} + \frac1{120} + ... \approx 2,7182818284590452353602874713527…$$

# In[34]:


UP = 30
add = 1
sum = 1


# In[35]:


for i in range(1, UP):
    add /= i
    sum += add
    print("%30.25g -> %30.25g" % (add, sum))


# ---
# **Строки** <a name=strings></a>

# ---
# ***Шифр Цезаря***

# In[65]:


# setup shift
shift = 1
# setup method
import string
alfa = string.digits + string.ascii_letters
alfa_len = len(alfa)
print(alfa_len, alfa)


# In[66]:


sopen = "Hello commander! Start at noon! Ceasar"

#sopen = "Здравствуй, Цезарь! Идущие на смерть тебя приветствуют!"
#sopen = "Ave, Caesar, morituri te salutant"
#sopen = "Николай неохотно поплёлся к директору: «Ave, Caesar, morituri te salutant!» — воскликнул он в дверях."

shift = 1
print(sopen)


# In[67]:


scoded = "".join(alfa[alfa.index(c) + shift] if c in alfa else c for c in sopen)
print(scoded)


# In[68]:


sback = "".join(alfa[alfa.index(c) - shift] if c in alfa else c for c in scoded)
print(sback)


# ---
# ***Подсчёт символов***
# 
# (найти 10 самых частых букв)

# In[38]:


stroka1 = "Twas brillig, and the slithy toves Did gyre and gimble in the wabe: All mimsy were the borogoves, And the mome raths outgrabe."

stroka2 = "Варкалось. Хливкие шорьки Пырялись по наве, И хрюкотали зелюки, Как мюмзики в мове."

# "Гло́кая ку́здра ште́ко будлану́ла бо́кра и курдя́чит бокрёнка"
stroka3 = "Глокая куздра штеко будланула бокра и курдячит бокрёнка"

# панграмма
stroka4 = "Съешь еще этих мягких французских булок да выпей же чаю"

stroka5 = "A Counter is a container that keeps track of how many times equivalent values are added. It can be used to implement the same algorithms for which bag or multiset data structures are commonly used in other languages."    "Counter supports three forms of initialization. Its constructor can be called with a sequence of items, a dictionary containing keys and counts, or using keyword arguments mapping string names to counts."    "This example counts the letters appearing in all of the words in the system dictionary to produce a frequency distribution, then prints the three most common letters. Leaving out the argument to most_common() produces a list of all the items, in order of frequency."

stroka6 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Гомер. Одиссея
stroka7 = """
Муза, скажи мне о том многоопытном муже, который,
Странствуя долго со дня, как святой Илион им разрушен,
Многих людей города посетил и обычаи видел,
Много и сердцем скорбел на морях, о спасенье заботясь
Жизни своей и возврате в отчизну сопутников; тщетны
Были, однако, заботы, не спас он сопутников: сами
Гибель они на себя навлекли святотатством, безумцы,
Съевши быков Гелиоса, над нами ходящего бога, —
День возврата у них он похитил. Скажи же об этом
Что-нибудь нам, о Зевесова дочь, благосклонная Муза.
Все уж другие, погибели верной избегшие, были
Дома, избегнув и брани и моря; его лишь, разлукой
С милой женой и отчизной крушимого, в гроте глубоком
Светлая нимфа Калипсо, богиня богинь, произвольной
Силой держала, напрасно желая, чтоб был ей супругом.
Но когда, наконец, обращеньем времен приведен был
Год, в который ему возвратиться назначили боги
В дом свой, в Итаку (но где и в объятиях верных друзей он
Всё не избег от тревог), преисполнились жалостью боги
Все; Посейдон лишь единый упорствовал гнать Одиссея,
Богоподобного мужа, пока не достиг он отчизны."""

stroka = stroka2

print(stroka)


# In[41]:


# не по-питоновски (ну, частично)
HOWMANY = 10    # сколько букв искать?
cnt = {}

# counting all characters
for c in stroka:
    cc = c.lower()
    if cc not in cnt:
        cnt[cc] = 0
    cnt[cc] += 1
        
# finding max by sorting
arr = [(k, v) for k, v in cnt.items()]
print("unsorted:", arr)

arr.sort(key = lambda x: x[1], reverse = True)
print("sorted:", arr)

loc = [x[0] for x in arr[:HOWMANY]]

print("\n* most often characters are:", loc)


# In[40]:


# по-питоновски
import collections as coll

cnt = coll.Counter(stroka.lower())
print("* most often characters are:", [x[0] for x in cnt.most_common(HOWMANY)])


# ---
# ***Анаграммы***
# 
# Анаграммы - слова (или предложения), состоящите из одних и  тех же букв, но в разном порядке.
# 
# Дан набор строк. Определить, какие из них явлеются анаграммами каких.

# In[4]:


# список слов
words = "астероид кукла трос кулак каприз алкаш сорт приказ шнурок мышка осока кабан камыш поза директор коршун диаретса лунь банка ром срам шкала нуль мор марс рост остр ".split()
print(words)


# In[10]:


# ищем анаграммы
from pprint import pprint as pp

dow = {}
for w in words:
    ws = "".join(sorted(w))
    if ws not in dow:
        dow[ws] = [w]
    else:
        dow[ws] += [w]
#pp(dow)
res = [v for v in dow.values() if len(v) > 1]
pp(res)


# ---
# **Кортежи и списки, словари и множества** <a name=structs1></a>

# ---
# ***Работа с изменяемыми значениями (mutables)***

# In[20]:


m1 = [1, 2, 3]
m2 = m1
print(m1)
print(m2)


# In[21]:


m1[1] = 55
print(m1)
print(m2)


# Python отличается от многих других ЯП. 
# 
# В нём нет присваивания.
# 
# При "присваивании" не происходит копирования информации.
# 
# Знаком "=" обозначается операция установления (копирования) ссылки на объект в памяти.
# 
# Причём переменные живут в своих пространствах, а значения - в своей глобальной памяти (куче).

# ---
# ***Поиск самой длинной положительной последовательности***
# 
# Найти в последовательности целых чисел подпоследовательность максимальной длины, состоящую только из положительных чисел.

# In[1]:


# программа
from random import randint as ri

def posseq1(seq):
    """поиск последовательности"""
    longseq = 0
    longstart = -1
    for i in range(LEN):
        if seq[i] <= 0:
            continue
        thisseq = 1
        thisstart = i
        for j in range(i+1, LEN):
            if seq[j] <= 0:
                break
            else:
                thisseq = j - i + 1
        if thisseq > longseq:
            longseq = thisseq
            longstart = thisstart
            #print(longseq, longstart, seq[longstart : longstart + longseq])
    return longseq, longstart


# In[15]:


# данные
LEN = 20
MIN = -10
MAX = +10

# проверка
seq = [ri(MIN, MAX) for _ in range(LEN)]
print(seq)


# In[16]:


print(seq)
plen, pstart = posseq1(seq)
print(f"sequence of length {plen}, starting from {pstart}, is {seq[pstart : pstart+plen]}")


# Замечание: решение не оптимально, можно его заметно ускорить.
# Найти место и ускорить... :)
# 
# Подсказка: алгоритм многократно проходит по длинным последовательностям. Это не влияет на результат, но замедляет работу.

# In[5]:


# программа - попытка исправления неэффективности
from random import randint as ri

def posseq2(seq):
    """поиск последовательности"""
    longseq = 0
    longstart = -1
    skipto = -1
    for i in range(LEN):
        if seq[i] <= 0:
            continue
        if i < skipto:
            continue
        skipto = -1
        thisseq = 1
        thisstart = i
        for j in range(i+1, LEN):
            if seq[j] <= 0:
                break
            else:
                thisseq = j - i + 1
                skipto = j
        if thisseq > longseq:
            longseq = thisseq
            longstart = thisstart
            #print(longseq, longstart, seq[longstart : longstart + longseq])
    return longseq, longstart


# In[9]:


# данные
LEN = 20
MIN = -10
MAX = +10

# проверка
seq = [ri(MIN, MAX) for _ in range(LEN)]
print(seq)


# In[17]:


print(seq)
plen, pstart = posseq2(seq)
print(f"sequence of length {plen}, starting from {pstart}, is {seq[pstart : pstart+plen]}")


# ---
# ***Любовь и шарики***
# 
# У каждого мальчика и у каждой девочки может быть по шарику. У кого одинакового цвета -- те, наверное, влюблены. Найти все пары.

# In[11]:


# Что мы знаем:
chibo = {
    "Маша": "Белый", 
    "Миша": "Зелёный",
    "Вася": "",
    "Катя": "Зелёный",
    "Ванечка": "Синий",
    "Коля": "Голубой",
    "Малика": "Фиолетовый",
    "Зоя": "Синий"
}
from pprint import pprint as pp
pp(chibo)


# In[12]:


# Найдём же все пары:
pairs = set()
for k1, v1 in chibo.items():
    for k2, v2 in chibo.items():
        if not v1 or not v2:                  # кто без шариков -- не влюблены
            continue
        if k1 != k2 and v1 == v2:             # а кто с одинаковыми - те да
            para = tuple(sorted([k1, k2]))
            pairs |= {para}
pp(pairs)


# ---
# ***Матрицы***
# 
# Здесь это -- двумерные массивы. В питоне размерность может быть и больше 2.

# In[12]:


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m)
from pprint import pprint as pp
pp(m)

q = [[11, 12, 13, 14, 15], 
     [21, 22, 23, 24, 25], 
     [31, 32, 33, 34, 35], 
     [41, 42, 43, 44, 45], 
     [51, 52, 53, 54, 55]]
print(q)
pp(q)


# ---
# ***Транспонирование матрицы***
# 
# Это красивое название для симметричного отражения её относительно главной диагонали.

# In[13]:


from copy import deepcopy as dc
tm = dc(m)
tq = dc(q)


# In[14]:


# непосредственно
for i in range(len(tm)):
    for j in range(i):
        tm[i][j], tm[j][i] = tm[j][i], tm[i][j]

pp(tm)

for i in range(len(tq)):
    for j in range(i):
        tq[i][j], tq[j][i] = tq[j][i], tq[i][j]

pp(tq)


# In[15]:


# по-взрослому, спецпакетом
import numpy as np

nm = np.asmatrix(m)
pp(nm)

tnm = nm.transpose()
pp(tnm)

nq = np.asmatrix(q)
pp(nq)

tnq = nq.transpose()
pp(tnq)


# ---
# ***Генератор речей***

# In[50]:


# mk-genspeech.py 2014-05-25 1.1
# Генератор речей
# Mikhail (myke) Kolodin, mykespb@gmail.com 

import random

text = """
  Товарищи! / Господа! / Коллеги! / Дорогие товарищи! / Уважаемые коллеги! / Дамы и господа! /  Уважаемые участники! / Друзья! / Граждане соучастники! / Граждане и гражданки! / / / / / / /
  С другой стороны / Равным образом / Не следует, однако, забывать о том, что /  Таким образом / Повседневная практика показывает. что / Значимость этих проблем настолько очевидна, что / Из выступление товарища начальника ясно следует, что / В решениях съезда нашей партии указано, что/ Разнообразный и богатый опыт / Задача организации, в особенности же / Идейные соображения  высшего порядка, а также / Принимая во внимание, что / Вы, конечно, знаете, что / Вам, должно быть, известен тот факт, что
  реализация намеченных плановых заданий / рамки и место обучения кадров / постоянный количественный рост и сфера нашей активности / сложившаяся структура организации / новая модель организационной деятельности / дальнейшее развитие различных форм деятельности / постоянное информационно-пропагандистское обеспечение нашей деятельности / управление и развитие структуры / консультация с широким активом / начало повседневной работы по формированию позиции
  играет важную роль в формировании / требуют от нас анализа / требуют определения и уточнения /  способствуют подготовке и реализации / обеспечивают широкому кругу специалистов участие в формировании
  , что позволяет выполнить важные задания по разработке / , что в значительной степени обуславливает создание / , что позволяет оценить значение / , что представляет собой интересный эксперимент / , что влечёт за собой интересный процесс внедрения и модернизации
  существенных финансовых и административных условий / дальнейших направлений развития /  системы массового участия / позиций, занимаемых участниками в отношении поставленных задач /  новых предложений / направлений прогрессивного развития / форм воздействия /  модели развития / соответствующих условий активизации / системы обучения кадров, соответствующей  насущным потребностям
  """

def make_speech (rows=1):
    parts = [part.split('/') for part in text.split('\n')]
    for num in range(1, rows+1):
        print ("Пункт %d.\n" % num + "".join([random.choice(part) for part in parts]) + '.')

make_speech(4)


# ---
# **Исключения** <a name=except></a>

# ---
# ***Деление на нуль***

# In[49]:


q = 5 / 0
print(q)


# In[48]:


try:
    q = 5 / 0
except:
    print("тут поделили на нуль!")
    q = 0
print(q)


# In[52]:


a = 5
b = 0
# ... многобукв...

try:
    q = a / b
except:
    print("тут поделили на нуль!")
    q = 0
print(q)


# In[49]:


# практический пример полутривиальный
# пусть есть данные -- несколько списков
# надо найти для каждого некую величину, равную частному от произведения всех чисел на из сумму

data = [
    (1, 2, 3, 4, 5),
    (1, 3, 0, -2),
    (1, -1, 5, -4, -1, 0)
]


# In[50]:


# неправильно
print("начинаем расчеты")
for gruppa in data:
    print(gruppa, end=" -> ")
    prod = 1
    for el in gruppa:
        prod *= el
    summa = 0
    for el in gruppa:
        summa += el
    quot = prod / summa
    print(quot)
print("продолжаем расчеты")


# In[51]:


# правильно
print("начинаем расчеты")
for gruppa in data:
    try:
        print(gruppa, end=" --> ")
        prod = 1
        for el in gruppa:
            prod *= el
        summa = 0
        for el in gruppa:
            summa += el
        quot = prod / summa
        print(quot)
    except ZeroDivisionError as error:
        print(error)
        quot = 0
    except e:
        print(e)
        print("something happened!")
print("продолжаем расчеты")


# ---
# **Математика** <a name=math></a>

# ---
# ***Линейное уравнение***
# 
# Дано: $ax + b = 0$, 
# причём $a \ne 0$. 
# Требуется найти $x$ для конкретных $a, b$.
# 
# Решение: $x = \frac{-b}a$.

# In[16]:


# дано: ax + b = 0
a = -3
b = 6
print(f"линейное уравнение {a}x{b:+n} = 0")


# In[17]:


# решение: x = -b / a
# если a!= 0
if a:
    x = -b / a
    print(f"решение: x = {x}")
else:
    print("а=0, это не линейное уравнение!")


# ---
# ***Квадратное уравнение***

# Дано: $ax^2 + bx + c = 0$,
# причём $a \ne 0$.
# Требуется найти $x$ для конкретных $a, b, c$.

# Решение: $x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$, либо $x = \frac{-b}{2a}$

# In[1]:


import math


# In[2]:


# дано: a, b, c
a = 1
b = 6
c = -8
print(f"Решаем квадратное уравнение с коэффициентами {a=}, {b=}, {c=}")


# In[4]:


if a:
    
    d = b**2 - 4*a*c      # это дискриминант
    print(f"дискриминант равен {d=},", 
     "положительный (2 решения)" if d>0 else
     "отрицательный (нет решений)" if d<0 else
     "нулевой (1 решение)" )

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"вот 2 решения:\n{x1=}\n{x2=}")
    elif d == 0:
        x = -b / (2*a)
        print(f"вот 1 решение:\n{x=}")
    else:
        print("решений в R нет")

else:
    print("a=0, это не квадратное уравнение")

