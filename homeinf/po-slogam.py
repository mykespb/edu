#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# po-slogam.py
# 2025-02-16 2025-02-16 1.0

# ~ По слогам
# ~ ------------------------------------

# ~ Есть набор слов.
# ~ Разделить его на группы по количеству слогов и распечатать эти группы
# ~ по возрастанию количества слогов, а внутри - в алфавитном порядке.


slova = """
О сколько нам открытий чудных
готовит просвещенья дух
и опыт сын ошибок трудных
и гений парадоксов друг
и случай бог изобретатель
"""

vowels = "уеёыаоэяию"

from collections import defaultdict

def slogov(slovo):
    """найти количество слогов"""

    return sum( [ c in vowels for c in slovo] )


vse = slova.strip().lower().split()

gruppy = defaultdict(list)

max_slogov = 0
for slovo in vse:
    gruppy[ sm := slogov(slovo) ] .append(slovo)
    max_slogov = max(max_slogov, sm)

for ns in range(max_slogov):
    if ns in gruppy:
        print(f"слогов: {ns}", end=", слова: ")
        print(* sorted(set(gruppy[ns])), sep=", " )


# ~ слогов: 1, слова: бог, друг, дух, и, нам, о, сын
# ~ слогов: 2, слова: гений, опыт, сколько, случай, трудных, чудных
# ~ слогов: 3, слова: готовит, открытий, ошибок
# ~ слогов: 4, слова: парадоксов, просвещенья
