#!/usr/bin/env python
# myke 2022-05-17 2022-05-19 2.0
# datastr-try.py 

# ~ опыты над структурами данных

# ~ словари и их сортировка

d = {1: 11, 2: 22, 4: 44, 3: 33, 0: 33}
print(d)

d = dict( sorted( (k, v) for k, v in d.items() ) )
print(d)

d = dict( sorted( (v, k) for k, v in d.items() ) )
print(d)

# ~ {1: 11, 2: 22, 4: 44, 3: 33, 0: 33}
# ~ {0: 33, 1: 11, 2: 22, 3: 33, 4: 44}
# ~ {11: 1, 22: 2, 33: 3, 44: 4}

# работа со строками

stroka = "строка"
strol = list(stroka)
print(stroka, "\n", strol)
for c in stroka:
    print(c, end=", ")

# ~ строка 
 # ~ ['с', 'т', 'р', 'о', 'к', 'а']
# ~ с, т, р, о, к, а, 

