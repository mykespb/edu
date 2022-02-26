#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-25 2022-02-25 1.1
# str1.py

# ~ найти в тексте все слова-палиндромы (регистром пренебречь)

s = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras erat dui, finibus vel lectus ac, pharetra dictum odio. Etiam risus sapien, auctor eu volutpat sit amet, porta in nunc. Quisque vitae varius ex, eu volutpat orci. Cras vel elit sed mi placerat pharetra eget vel odio. Cras vel elit sed mi ege placerat pharetra eget vel odio. Proin ipsum purus, laoreet quis dictum a, laoreet sed ligula. Cras erat dui, finibus vel lectus ac, pharetra dictum odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque vitae varius ex, eu volutpat orci. Quisque vitae varius ex, eu volutpat orci. Duis ac nulla varius diam ultrices rutrum. Nullam tempus scelerisque purus, sed mattis elit condimentum nec. Cras erat dui, finibus vel sumus lectus ac, pharetra dictum odio. Etiam risus sapien, auctor eu volutpat sit amet, porta in nunc. Quisque vitae varius ex, eu volutpat orci. Integer ultricies malesuada quam. Etiam risus sapien, auctor eu volutpat sit amet, porta in nunc.
Nullam tempus scelerisque purus, sed mattis elit condimentum nec. Cras vel elit sed mi placerat pharetra eget vel odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ultricies malesuada quam. Cras vel elit sed mi placerat pharetra eget vel odio. Duis ac nulla varius diam ultrices rutrum. Cras erat dui, finibus vel lectus ac, pharetra dictum odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam tempus scelerisque purus, sed mattis elit condimentum nec. Duis ac nulla varius diam ultrices rutrum. Etiam risus trekert sapien, auctor eu volutpat sit amet, porta in nunc. Quisque vitae varius ex, eu volutpat orci. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae varius ex, eu volutpat orci. Proin ipsum purus, laoreet quis dictum a, laoreet sed oko ligula. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque vitae varius ex, eu volutpat orci.
"""

# ~ фишки:
# ~ - здесь есть заглавные и строчные буквы
# ~ - здесь есть знаки препинания, в состав слов они не входят
# ~ - буквы только латинские

import string

letters = string.ascii_lowercase
chars = letters + " "

s = s.lower()

so = ""
for c in s:
    if c in chars:
        so += c

s = so

for word in s.split():
    if word == word[::-1]:
        print(word, end=', ')


# ~ ege, a, sumus, trekert, a, oko,
