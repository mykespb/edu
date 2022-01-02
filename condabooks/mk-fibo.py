#!/usr/bin/env python
# coding: utf-8

# # Числа Фибоначчи
# 
# ## Основное 
# 
# ### Определение
# 
# _**Числа Фибоначчи (ряд Фибоначчи, последовательность Фибоначчи)**_ - последовательность натуральных чисел $f_n$ такая, что
# $f_1 = f_2 = 1$, 
# а для всех $n>2 : f_n = f_{n-2} + f_{n-1}$.
# 
# Т.о. ряд имеет вид: 1, 1, 2, 3, 5, 8, 13, 21, 34,...
# 
# Это пример рекуррентной последовательности 2 порядка, 
# при которой первые два элемента равны единице, а каждый последующий равен сумме двух предыдущих.

# ---
# Ссылки: 
# 
# 1. [Числа Фибоначчи](https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8)
# 2. [Сам Фибоначчи](https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8)

# ---
# __1. Расчёт с массивами:__
# 
# заводим массив (в питоне: список) на весь запрошенный диапазон, 
# заполняем его числами по возрастанию.

# In[1]:


def fib1(n=10):
    """ 1st version: pre-allocate list """
    if n < 1:
        return []

    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    f = [0 for x in range(n)]
    f[0] = f[1] = 1

    for i in range(2, n):
        f[i] = f[i-2] + f[i-1]

    return f


# In[6]:


# тесты: 

fib = fib1

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(10))

print(fib())

print(fib(100))


# ---
# __2. Расчёт с массивами:__ 
# 
# поэлементно наращивая список на весь запрошенный диапазон, заполняем его числами по возрастанию.

# In[5]:


def fib2(n=10):
    """ 1st version: dynamic list """
    if n < 1:
        return []

    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    f = [1, 1]

    for i in range(n-2):
        f.append(0)
        f[-1] = f[-3] + f[-2]

    return f


# In[7]:


# тесты: 

fib = fib2

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(10))

print(fib())

print(fib(100))


# ---
# __3. Фибоначчи не по-питоновски,__ 
# 
# зато экономно по памяти: используем только 3 переменные, как того и требует классическая теория работы с рекуррентными последовательностями

# In[10]:


UP = 50    # вычисляем и печатаем 50 первых чисел Фибоначчи, рекуррентные последовательности
f1 = 1
f2 = 1
print(f1, f2, sep=", ", end=", ")
for n in range(2, UP):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=", ")


# ---
# __4. Фибоначчи более по-питоновски,__ 
# 
# да  и экономно по памяти: используем только 2 переменные

# In[14]:


UP = 50        # вычисляем и печатаем 50 первых чисел Фибоначчи
f1 = f2 = 1
print(f1, f2, sep=", ", end=", ")
for _ in range(2, UP):
    f1, f2 = f2, f1+f2
    print(f2, end=", ")


# ---
# __5. Расчёт с учётом времени__
# 
# __Классическая рекурсивная версия__

# In[4]:


import timeit
MAX = 39     # сколько чисел выводим?


# In[2]:


def fibclassic (n):
    """ classic version of fibonacci """

    return 1 if n < 3 else fibclassic (n-2) + fibclassic (n-1)


# In[5]:


# только считаем время
print ("classics:\n")
for n in range (1, MAX+1):
    print ("number=", n, end=", time=")
    print (timeit.timeit("fibclassic (%d)" % (n,), number=1, globals=globals()))


# __6. Динамическое программмирование__

# In[6]:


def fibdynamic (n):
    """ dynamic version of fibonacci """

    res = {}

    def fib (n):
        nonlocal res
        if n < 3:
            return 1
        if n in res:
            return res [n]
        sum = fib (n-2) + fib (n-1)
        res [n] = sum
        return sum

    return fib (n)


# In[7]:


print ("\ndynamic:\n")
for n in range (1, MAX):
    print ("number=", n, end=", time=")
    print (timeit.timeit("fibdynamic (%d)" % (n,), number=1, globals=globals()))


# __7. Время для классики__

# In[8]:


def fibnormal (n):
    """ fibonacci as it should be"""

    if n < 3:
        return 1
    f1 = f2 = 1
    for i in range (n-1):
        f3 = f1 + f2
        f1, f2 = f2, f3

    return f3


# In[9]:


print ("\nnormal:\n")
for n in range (1, MAX):
    print ("number=", n, end=", time=")
    print (timeit.timeit("fibnormal (%d)" % (n,), number=1, globals=globals()))


# __8. Используем кэш__
# 
# Иногда есть декоратор `cache`, иногда `lru_cache`.

# In[14]:


from functools import lru_cache

@lru_cache
def fibcache(n):
    if n <= 1:
        return 1
    return fibcache(n-2) + fibcache(n-1)        


# In[17]:


for i in range(100):
    print("fib(", i, ") = ", fibcache(i))


# ---
# # Дополнительное
# 
# ## Фибоначчиподобное

# In[18]:


pass


# ---
# ## Фибоначчинеподобное

# __1. Трибоначчи__
# 
# Рекуррентная последовательность 3-го порядка: 
# 
# $f_1 = f_2 = f_3 = 1,$
# 
# $f_n = f_{n-3} + f_{n-2} + f_{n-1}$, при $n \geq 4$

# In[25]:


f1 = f2 = f3 = 1
MAX = 50


# In[26]:


print(f1, f2, f3, sep=", ", end=", ")
for i in range(MAX-4):
    f1, f2, f3 = f2, f3, f1 + f2 + f3
    print(f3, end=", ")


# In[ ]:




