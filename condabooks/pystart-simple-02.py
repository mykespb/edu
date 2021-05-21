#!/usr/bin/env python
# coding: utf-8

# # Примеры и упражнения по Python3 - простой уровень - часть 2

# Автор-составитель - Михаил Колодин

# Версия 2021-04-17 от 2021-04-19 - 1.5

# Разделы:
# * [Кортежи и списки](#lists)
# * [Словари и множества](#dicts)
# * [Функции](#funcs)
# * [Форматированный вывод](#output)
# * [Текстовые файлы](#textfiles)

# ---
# **Кортежи и списки** <a name=lists></a>

# ---
# ***Перестановка слов***

# In[93]:


stroka = "привет всем питонистам"
print(stroka)


# In[104]:


# подробно по шагам
t1 = stroka.split()
print(t1)
t2 = reversed(t1)
print(t2)
t3 = list(reversed(t1))
print(t3)
t4 = " ".join(t2)
print(t4)
print()

# по-быстрому
revstroka1 = " ".join(reversed(stroka.split()))
print(revstroka1)


# In[96]:


revstroka2 = " ".join((stroka.split())[::-1])
print(revstroka2)


# ---
# ***Сортировка***
# 
# Дан список (мы его сами сделаем, для удобства, но случайным образом.
# 
# Задача. Надо отсортировать = упорядочить элементы списка по возрастанию (точнее, по неубыванию).
# 
# Есть несколько способов. Это суперклассика программирования.

# In[1]:


from random import randint as ri


# In[2]:


LEN = 10
MIN = -10 
MAX = +10
l = [ri(MIN, MAX) for _ in range(LEN)]
print(l)


# In[4]:


l.sort()
print(l)


# In[5]:


l.sort(reverse = True)
print(l)


# In[6]:


l.sort(key = lambda x: abs(x))
print(l)


# In[7]:


ls = sorted(l)
print(l)
print(ls)


# ---
# ***Поиск***
# 
# Поиск информации в последовательности - классика.
# Проверяем наличие.

# In[17]:


LEN = 10
MIN = -10 
MAX = +10
l = [ri(MIN, MAX) for _ in range(LEN)]
print(l)


# In[18]:


# Ищем число 5 в списке
# 1. Тупо

WHAT = 5

found = False
for i in range(len(l)):
    if l[i] == WHAT:
        print("Нашли!")
        break
else:
    print("Не нашли!")


# In[19]:


# Пролутупо

WHAT = 5

for e in l:
    if l[i] == WHAT:
        print("Нашли!")
        break
else:
    print("Не нашли!")


# In[21]:


# Умно, по-питоновски:  :)

print("Нашли!" if WHAT in l else "Не нашли!")


# Есть много разных классических способов сортировки и поиска. 
# 
# См. Д.Кнут. "Искусство программирования для ЭВМ", том 3.
# 
# И полезно писать свои.
# 
# И уметь оценивать затраты времени и памяти на такие операции с помощью О большого, напр., 
# $$O(1), O(n), O(n^2), O(n \log n)$$

# ---
# ***Минимум и максимум***

# Найти минимальное и максимальное значение элементов целочисленного списка.
# 
# Список создаётся случайным образом (в программе мы не можем использовать знания о том, какие элементы входят в этот список и даже какой он длины (короткий или длинный); мы только знаем, что это целые числа).
# 
# В программе задаются константы LEN, MIN, MAX, характеризующие этот список.
# 
# Нужно найти оба значения не более, чем за 1 проход по списку.

# In[1]:


import random


# In[2]:


# создаём список случайных целых чисел
LEN = 10      # длина списка
MIN = -100    # минимальное возможное число
MAX = 100     # максимальное возможное число
import random
rl = [random.randint(MIN, MAX) for _ in range(LEN)]
print("случайный список:", rl)


# In[13]:


# не по-питоновски:
amin = rl[0]
amax = rl[0]

for i in range(1, LEN):
    if rl[i] < amin:
        amin = rl[i]
    if rl[i] > amax:
        amax = rl[i]

# вывод результата по-чужому :)
print("минимум равен", amin, ", максимум равен", amax)


# In[14]:


# полу-по-питоновски
amin = rl[0]
amax = rl[0]

for e in rl[1:]:
    if e < amin:
        amin = e
    if e > amax:
        amax = e
        
# вывод результата по-старому
print("минимум равен %d, максимум равен %d" % (amin, amax))
# или по-новому
print("минимум равен {}, максимум равен {}".format(amin, amax))


# In[15]:


# по-питоновски

print(f"минимум равен {min(rl)}, максимум равен {max(rl)}")


# ---
# ***Удалить из списка повторяющиеся  значения***

# In[8]:


# создаём случайный список
LEN = 10      # длина списка
MIN = 0    # минимальное возможное число
MAX = 10     # максимальное возможное число
import random
rl = [random.randint(MIN, MAX) for _ in range(LEN)]
print("случайный список:", rl)


# In[9]:


# решение полупитоновское
pl = []
for e in rl:
    if e not in pl:
        pl += [e]
        
print("получился список", pl)


# In[10]:


# решение питоновское
pl = list(set(rl))
print("получился список", pl)


# ---
# ***Подсчёт букв***
# 
# Подсчитать, сколько в тексте гласных и согласных букв, и каково их отношение. Говорят. что можно по частоте букв и слов определить авторство произведения.

# In[27]:


# начальные данные - несколько текстов
text_rus = """
Позванивает тишь в июльский колокольчик,
Расправляя пальцами рассвета лепестки.
Заря малиновый плащ около околицы
Навстречу солнцу выбросить спешит.

Пьют утренний туман стреноженные кони,
Звук рвущейся травы на замшевых губах.
И первая пчела пускается в погоню
За солнечным лучом на клеверных лугах.

Лежу, заворожён рассветной дрёмой,
Вдали от нервных городов.
И не понять: ну где ж я дома - 
В асфальтовых краях иль здесь, среди лугов?

Позванивает тишь в июльский колокольчик...
(Валентин Вихорев)
"""

text_eng = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'
So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.
There was nothing so VERY remarkable in that; nor did Alice think it so VERY much out of the way to hear the Rabbit say to itself, 'Oh dear! Oh dear! I shall be late!' (When she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural.)
But when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-POCKET, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge.
"""


# In[35]:


# перечисляем буквы алфавитов
alfa_rus_vowels = 'уеаоэяию'
alfa_rus_consonants = 'йцкнгшщзхъфвпрлджчсмтьб'
alfa_eng_vowels = 'eyuioaj'
alfa_eng_consonants = 'qwrtpsdfghjklzxcvbnm'


# In[36]:


# выбираем текст для анализа

alfa_vowels = alfa_rus_vowels
alfa_consonants = alfa_rus_consonants
#alfa_vowels = alfa_eng_vowels
#alfa_consonants = alfa_eng_consonants

text = text_rus
#text = text_rus


# In[37]:


# вариант 1
count_vowels = count_consonants = 0
for c in text:
    cc = c.lower()
    count_vowels += cc in alfa_vowels
    count_consonants += cc in alfa_consonants
    
count_rel = 0 if count_consonants == 0 else count_vowels / count_consonants

print(f"""всего насчитали гласных букв {count_vowels}, 
согласных букв {count_consonants},
отношение гласных к согласным равно {round(count_rel, 3)}.
""")


# In[38]:


# вариант 2
count_vowels = count_consonants = 0
for c in text:
    cc = c.lower()
    if cc in alfa_vowels:
        count_vowels += 1
    if cc in alfa_consonants:
        count_consonants += 1
    
count_rel = 0 if count_consonants == 0 else count_vowels / count_consonants

print(f"""всего насчитали гласных букв {count_vowels}, 
согласных букв {count_consonants},
отношение гласных к согласным равно {round(count_rel, 3)}.
""")


# In[39]:


# выбираем текст для анализа

#alfa_vowels = alfa_rus_vowels
#alfa_consonants = alfa_rus_consonants
alfa_vowels = alfa_eng_vowels
alfa_consonants = alfa_eng_consonants

#text = text_rus
text = text_eng


# In[40]:


# вариант 1
count_vowels = count_consonants = 0
for c in text:
    cc = c.lower()
    count_vowels += cc in alfa_vowels
    count_consonants += cc in alfa_consonants
    
count_rel = 0 if count_consonants == 0 else count_vowels / count_consonants

print(f"""всего насчитали гласных букв {count_vowels}, 
согласных букв {count_consonants},
отношение гласных к согласным равно {round(count_rel, 3)}.
""")


# In[41]:


# вариант 2
count_vowels = count_consonants = 0
for c in text:
    cc = c.lower()
    if cc in alfa_vowels:
        count_vowels += 1
    if cc in alfa_consonants:
        count_consonants += 1
    
count_rel = 0 if count_consonants == 0 else count_vowels / count_consonants

print(f"""всего насчитали гласных букв {count_vowels}, 
согласных букв {count_consonants},
отношение гласных к согласным равно {round(count_rel, 3)}.
""")


# ---
# **Словари и множества** <a name=dicts></a>

# ---
# ***Ребята-спортсмены***

# In[26]:


# исходные данные

sport = {
    'Лена': ['шахматы', 'плавание'],
    'Саша': ['плавание'],
    'Коля': [],
    'Андрей': ['шашки', 'бокс'],
}

print(sport, "\n")

# prettyprint
from pprint import pprint as pp
pp(sport)

sos = {s for s in sport.keys()}
print("\nспортсмены", sos)


# ---
# **Функции** <a name=funcs></a>

# ---
# ***Функция sign: знак (-1, 0, +1)***

# In[84]:


# описание функции, подробно
def sign1(x):
    """ знак числа (-1, 0, 1)"""
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# простая проверка
print("просто проверка:", sign1(5), sign1(0), sign1(-1))

# описание функции, кратко
def sign2(x):
    """ знак числа (-1, 0, 1)"""
    return 1 if x > 0 else -1 if x < 0 else 0

# выбор нужной функции
sign = sign2

# вызов функции
tests = [0, 1, 100, -1, -3, 10000000, 1.4, -0.5, 1e16, 3.14e-5]
print("большой тест:", [sign(x) for x in tests])


# ---
# ***Високосность года***
# 
#     год високосный (имеет 29 дней в феврале) тогда и только тогда, когда его номер:
#     делится нацело на 4,
#       кроме тех, которые делятся на 100,
#         кроме тех, которые делятся на 400

# In[176]:


# исходные данные - проверить для этих лет
gody = 1968, 2000, 1900, 2021, 1983, 2010, 2020


# In[23]:


# собственно наша функция для проверки

# по-скучному
def is_leap_dull(y):
    """ проверка года на високосность"""
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False


# In[22]:


# а теперь - по-правильному
def is_leap(y):
    """ проверка года на високосность"""
    return y % 400 == 0 or y % 4 == 0 and y %100 != 0


# In[24]:


# NB: 
# y % 400 == 0 or y % 4 == 0 and y %100 != 0
# считается как 
# (y % 400 == 0) or ((y % 4 == 0) and (y %100 != 0))


# In[180]:


# проверяем
for y in sorted(gody):
    print(y, "високосный" if is_leap(y) else "не високосный")


# ---
# **Отладка** <a name=debug></a>

# ---
# ***Ручная прокрутка***

# In[186]:


first = 100
print(first)
second = -100
print(second)
third = first / second
print(third)
first, second, third


# ---
# ***Утверждения assert***

# In[140]:


var1 = 12
assert var1 != 0
var2 = 0
assert var2 != 0
var3 = var1 / var2


# ---
# ***Проверки типов***
# 
# Новая возможность, по-разному реализована в разных версиях, постепенно становится удобнее

# In[184]:


# собственно наша функция для проверки
def is_leap1(y : int) -> bool:
    """ проверка года на високосность"""
    return y % 400 == 0 or y % 4 == 0 and y %100 != 0


# In[185]:


# проверяем снова
# исходные данные - проверить для этих лет
gody = 1968, 2000, 1900, 2021, 1983, 2010, 2020
# запуск
for y in sorted(gody):
    print(y, "високосный" if is_leap1(y) else "не високосный")


# ---
# **Форматированный вывод** <a name=output></a>

# In[72]:


# данные
i = 5
f = 1.5
s = "string"


# In[73]:


print(i, f, s)


# In[74]:


# устаревший способ, не рекомендуется использовать
print("%5i %10.5f %-10s" % (i, f, s))


# In[75]:


# современный способ
print("{0} {1} {2}".format(i, f, s))
print("{0:5} {1:10} {2:20} {0}".format(i, f, s))


# In[76]:


# новый способ, есть не во всех версиях python, только в очень свежих
print(f"{i} {f} {s}")
print(f"{i=} {f=} {s=}")


# ---
# **Работа с файлами, ввод-вывод** <a name=textfiles></a>

# ---
# ***Ручной ввод данных***

# In[18]:


# ввод строки
s = input()
print("вы ввели:", s)
# input вводит именно строку, но можно с пробелами
# для остальных типов нужно явно преобразовывать


# In[190]:


# ввод строки с приглашением
s = input("введите строку: ")
print("вы ввели:", s)


# In[191]:


# ввод целого числа с приглашением
n = int(input("введите целое число: "))
print("вы ввели:", n)


# ---
# ***Чтение и запись простых текстовых файлов***

# In[192]:


# файл input-1.txt
infile  = 'input-1.txt'
outfile = 'output-1.txt'


# *входной файл:*
# 
#     Широка страна моя родная.
#     Много в ней лесов, полей и рек.
#     Я другой такой страны не знаю,
#     где так вольно дышит человек.
#     
# ("Песня о Родине". Авторы: музыка - Исаак Дунаевский, слова - Василий Лебедев-Кумач, 1936)
# 
# [Источник в Википедии](https://ru.wikipedia.org/wiki/%D0%A8%D0%B8%D1%80%D0%BE%D0%BA%D0%B0_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B0_%D0%BC%D0%BE%D1%8F_%D1%80%D0%BE%D0%B4%D0%BD%D0%B0%D1%8F)
#     
# *выходной файл (последний)*
# 
#     родная. моя страна широка
#     рек. и полей лесов, ней в много
#     знаю, не страны такой другой я
#     человек. дышит вольно так где

# In[195]:


f = open(infile, 'r')
t = f.read()
print(t)
f.close()


# In[194]:


with open(infile) as inf:
    for inline in inf:
        print(inline.strip())


# In[204]:


with open(infile, 'r') as inf, open(outfile, 'w') as outf:
    for inline in inf:
        print(inline.strip())
        outf.write(" ".join(reversed(inline.lower().split())) + "\n")


# In[207]:


with open(infile, 'r', encoding='utf8') as inf:
    strs = inf.readlines()
    print(strs)
    pp(strs)

