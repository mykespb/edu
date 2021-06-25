# Примеры и упражнения по Python3  - средний уровень - часть 2

Автор-составитель - Михаил Колодин

Версия 2021-04-16 от 2021-04-19 - 1.4

Разделы:
* [Кортежи и списки, словари и множества](#structs1)
* [Прочие сложные структуры данных](#structs2)
* [Математика](#math)

---
**Кортежи и списки, словари и множества** <a name=structs1></a>

---
***Ребята-спортсмены***


```python
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
```

    {'Лена': ['шахматы', 'плавание'], 'Саша': ['плавание'], 'Коля': [], 'Андрей': ['шашки', 'бокс']} 
    
    {'Андрей': ['шашки', 'бокс'],
     'Коля': [],
     'Лена': ['шахматы', 'плавание'],
     'Саша': ['плавание']}



```python
# получаем полезную информацию из этого

# список имён по алфавиту
people = sorted([key for key in sport.keys()])
print(people)
```

    ['Андрей', 'Коля', 'Лена', 'Саша']



```python
# все виды спорта по алфавиту
sl = [value for value in sport.values()]
sps = set()
for sg in sl:
    sps |= set(sg)
sps = sorted(list(sps))
print(sps)
```

    ['бокс', 'плавание', 'шахматы', 'шашки']



```python
# самый активный спортсмен - у кого больше всего видов спорта (один, любой, если их несколько)
spmen = [(k, len(v)) for k, v in sport.items()]
spmen.sort(key = lambda x: x[1], reverse = True)
print(spmen[0])
print()
# самый активный спортсмен - у кого больше всего видов спорта (все, если их несколько)
maxsport = spmen[0][1]
print([x for x in spmen if x[1] == maxsport])
```

    ('Лена', 2)
    
    [('Лена', 2), ('Андрей', 2)]


---
***Спецструктуры: OrderedDict***


```python
# TODO
pass
```

---
***Спецструктуры: NamedTuple***


```python
# TODO
pass
```

---
***Спецструктуры: FrozenSet***


```python
# TODO
pass
```

---
***Спецструктуры: Counter***


```python
# TODO
pass
```

---
***Спецструктуры: Deque***


```python
# TODO
pass
```

---
***Спецструктуры: Deque, имитация стека***


```python
# TODO
pass
```

---
***Спецструктуры: Deque, имитация очереди***


```python
# TODO
pass
```

---
**Прочие сложные структуры данных** <a name=structs2></a>


```python
# TODO
# 
pass
```

---
**Функции** <a name=functions></a>


```python
# TODO
pass
```

---
***Рекурсивные функции***


```python
# TODO
pass
```

---
***Динамическое программирование***


```python
# TODO
pass
```

---
**Менеджеры контекстов** <a name=context></a>


```python
# TODO
pass
```

---
**Итераторы, генераторы, лямбда** <a name=lambda></a>


```python
# TODO
pass
```

---
**Исключения** <a name=except></a>

---
***Работа с файлами***


```python
# TODO
pass
```

---
***Собственные исключения, основное***


```python
# TODO
pass
```

---
***Собственные исключения, имитации переходов и прочее нетипичное***


```python
# TODO
pass
```

---
**Математика** <a name=math></a>

---
***Простые числа***


```python
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
```

    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
    2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461 463 467 479 487 491 499 503 509 521 523 541 547 557 563 569 571 577 587 593 599 601 607 613 617 619 631 641 643 647 653 659 661 673 677 683 691 701 709 719 727 733 739 743 751 757 761 769 773 787 797 809 811 821 823 827 829 839 853 857 859 863 877 881 883 887 907 911 919 929 937 941 947 953 967 971 977 983 991 997 
