#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-03 2025-01-03 1.1
# find-fairy.py

# ~ Есть повествовательный текст на русском языке.
# ~ Найти и напечатать те предложения,
# ~ в которых упоминаются заданные сказочные перонажи.
# ~ Персонажи - список через запятую, по каждой сказке отдельная строка,
# ~ все в именительном падеже.
# ~ В тесте предложения разделены точками, всё идёт подряд,
# ~ возможно, одним абзацем.

персонажи = """
Дед Мороз, Снегурочка, Баба Яга,
Карлсон,
Буратино, Мальвина, папа Карло, лиса Алиса,
Крот, Дюймовочка
"""

текст = """
Раз - два - три, ёлочка, гори. Не прячьте ваши денежки по банкам и углам. Всё видит лиса Алиса, ничего не спрячешь. По домам ходит Дед Мороз и дарит всем подарки, или не всем, или не подарки. А Крот и говорит: сиди, Дюймовочка, в норе, и не выглядывай. Карлсон летит над городом, кричит: Штирлиц, наших бьют. Теперь о погоде. А зима будет большая, только сумерки да снег.
"""


def find_em():
    """всех отыскать..."""
    
    persons = персонажи.strip().replace("\n", "").split(',')
    persons = list(map(str.strip, persons))
    
    text = текст.strip().split('.')
    text = list(map(str.strip, text))
    text = list(filter(len, text))

    print(persons)       
    print(text)

    for frase in text:
        for pers in persons:
            if pers in frase:
                print(frase.strip() + '.')
                break


find_em()
