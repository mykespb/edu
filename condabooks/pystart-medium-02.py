#!/usr/bin/env python
# coding: utf-8

# # Примеры и упражнения по Python3  - средний уровень - часть 2

# Автор-составитель - Михаил Колодин

# Версия 2021-04-16 от 2021-04-19 - 1.4

# Разделы:
# * [Кортежи и списки, словари и множества](#structs1)
# * [Прочие сложные структуры данных](#structs2)
# * [Математика](#math)

# ---
# **Кортежи и списки, словари и множества** <a name=structs1></a>

# ---
# ***Ребята-спортсмены***

# In[43]:


# исходные данные

sport = {
    'Лена': ['шахматы', 'плавание'],
    'Саша': ['плавание'],
    'Коля': [],
    'Андрей': ['шашки', 'бокс'],
}

print(sport, "\n")

from pprint import pprint as pp
pp(sport)


# In[44]:


# получаем полезную информацию из этого

# список имён по алфавиту
people = sorted([key for key in sport.keys()])
print(people)


# In[45]:


# все виды спорта по алфавиту
sl = [value for value in sport.values()]
sps = set()
for sg in sl:
    sps |= set(sg)
sps = sorted(list(sps))
print(sps)


# In[72]:


# самый активный спортсмен - у кого больше всего видов спорта (один, любой, если их несколько)
spmen = [(k, len(v)) for k, v in sport.items()]
spmen.sort(key = lambda x: x[1], reverse = True)
print(spmen[0])
print()
# самый активный спортсмен - у кого больше всего видов спорта (все, если их несколько)
maxsport = spmen[0][1]
print([x for x in spmen if x[1] == maxsport])


# ---
# ***Спецструктуры: OrderedDict***

# In[15]:


# TODO
pass


# ---
# ***Спецструктуры: NamedTuple***

# In[9]:


# TODO
pass


# ---
# ***Спецструктуры: FrozenSet***

# In[10]:


# TODO
pass


# ---
# ***Спецструктуры: Counter***

# In[11]:


# TODO
pass


# ---
# ***Спецструктуры: Deque***

# In[12]:


# TODO
pass


# ---
# ***Спецструктуры: Deque, имитация стека***

# In[13]:


# TODO
pass


# ---
# ***Спецструктуры: Deque, имитация очереди***

# In[14]:


# TODO
pass


# ---
# **Прочие сложные структуры данных** <a name=structs2></a>

# In[2]:


# TODO
# 
pass


# ---
# **Функции** <a name=functions></a>

# In[142]:


# TODO
pass


# ---
# ***Рекурсивные функции***

# In[3]:


# TODO
pass


# ---
# ***Динамическое программирование***

# In[4]:


# TODO
pass


# ---
# **Менеджеры контекстов** <a name=context></a>

# In[19]:


# TODO
pass


# ---
# **Итераторы, генераторы, лямбда** <a name=lambda></a>

# In[ ]:


# TODO
pass


# ---
# **Исключения** <a name=except></a>

# ---
# ***Работа с файлами***

# In[7]:


# TODO
pass


# ---
# ***Собственные исключения, основное***

# In[5]:


# TODO
pass


# ---
# ***Собственные исключения, имитации переходов и прочее нетипичное***

# In[6]:


# TODO
pass


# ---
# **Математика** <a name=math></a>

# ---
# ***Простые числа***

# In[74]:


# простые числа (primes)
def primes (lim=100):
    """ show primes up to lim """
    found = []
    for tested in range (2, lim+1):
        for tester in found:
            if tested % tester == 0:
                break
        else:
            found.append (tested)
            print (tested, end=" ")
    print()

primes()
primes(1000)

