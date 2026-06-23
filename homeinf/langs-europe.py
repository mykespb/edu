#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# langs-europe.py
# 2026-06-24 2026-06-24 1.0

# ~ перечисли 50 основных европейских разговорных языков в формате list[dict], указав:
# ~ - name; название,
# ~ - people: сколько человек говорит,
# ~ - worsd: сколько слов  в языке,
# ~ - diff: относительную сложность для русскоговорящего.

# --------------- данные --------------------

langs = [
    {
        "number": 1,
        "name": "Albanian",
        "people": 7500000,
        "words": 85000,
        "diff": 4
    },
    {
        "number": 2,
        "name": "Armenian",
        "people": 7000000,
        "words": 150000,
        "diff": 4
    },
    {
        "number": 3,
        "name": "Azerbaijani",
        "people": 31000000,
        "words": 80000,
        "diff": 3
    },
    {
        "number": 4,
        "name": "Basque",
        "people": 750000,
        "words": 50000,
        "diff": 5
    },
    {
        "number": 5,
        "name": "Belarusian",
        "people": 5000000,
        "words": 180000,
        "diff": 1
    },
    {
        "number": 6,
        "name": "Bosnian",
        "people": 3000000,
        "words": 120000,
        "diff": 2
    },
    {
        "number": 7,
        "name": "Bulgarian",
        "people": 9000000,
        "words": 120000,
        "diff": 2
    },
    {
        "number": 8,
        "name": "Catalan",
        "people": 10000000,
        "words": 90000,
        "diff": 2
    },
    {
        "number": 9,
        "name": "Croatian",
        "people": 6000000,
        "words": 120000,
        "diff": 2
    },
    {
        "number": 10,
        "name": "Czech",
        "people": 13000000,
        "words": 250000,
        "diff": 3
    },
    {
        "number": 11,
        "name": "Danish",
        "people": 6000000,
        "words": 100000,
        "diff": 3
    },
    {
        "number": 12,
        "name": "Dutch",
        "people": 30000000,
        "words": 400000,
        "diff": 2
    },
    {
        "number": 13,
        "name": "English",
        "people": 1500000000,
        "words": 470000,
        "diff": 2
    },
    {
        "number": 14,
        "name": "Estonian",
        "people": 1100000,
        "words": 150000,
        "diff": 5
    },
    {
        "number": 15,
        "name": "Finnish",
        "people": 6000000,
        "words": 210000,
        "diff": 5
    },
    {
        "number": 16,
        "name": "French",
        "people": 310000000,
        "words": 135000,
        "diff": 3
    },
    {
        "number": 17,
        "name": "Galician",
        "people": 2500000,
        "words": 60000,
        "diff": 2
    },
    {
        "number": 18,
        "name": "Georgian",
        "people": 4000000,
        "words": 120000,
        "diff": 5
    },
    {
        "number": 19,
        "name": "German",
        "people": 135000000,
        "words": 330000,
        "diff": 3
    },
    {
        "number": 20,
        "name": "Greek",
        "people": 13000000,
        "words": 300000,
        "diff": 4
    },
    {
        "number": 21,
        "name": "Hungarian",
        "people": 13000000,
        "words": 1000000,
        "diff": 5
    },
    {
        "number": 22,
        "name": "Icelandic",
        "people": 350000,
        "words": 250000,
        "diff": 4
    },
    {
        "number": 23,
        "name": "Irish",
        "people": 2000000,
        "words": 140000,
        "diff": 4
    },
    {
        "number": 24,
        "name": "Italian",
        "people": 67000000,
        "words": 260000,
        "diff": 2
    },
    {
        "number": 25,
        "name": "Latvian",
        "people": 2000000,
        "words": 120000,
        "diff": 3
    },
    {
        "number": 26,
        "name": "Lithuanian",
        "people": 3000000,
        "words": 150000,
        "diff": 3
    },
    {
        "number": 27,
        "name": "Macedonian",
        "people": 2000000,
        "words": 80000,
        "diff": 2
    },
    {
        "number": 28,
        "name": "Maltese",
        "people": 500000,
        "words": 40000,
        "diff": 4
    },
    {
        "number": 29,
        "name": "Norwegian",
        "people": 5500000,
        "words": 300000,
        "diff": 3
    },
    {
        "number": 30,
        "name": "Polish",
        "people": 45000000,
        "words": 140000,
        "diff": 2
    },
    {
        "number": 31,
        "name": "Portuguese",
        "people": 265000000,
        "words": 110000,
        "diff": 2
    },
    {
        "number": 32,
        "name": "Romanian",
        "people": 25000000,
        "words": 150000,
        "diff": 2
    },
    {
        "number": 33,
        "name": "Russian",
        "people": 255000000,
        "words": 200000,
        "diff": 1
    },
    {
        "number": 34,
        "name": "Serbian",
        "people": 11000000,
        "words": 120000,
        "diff": 2
    },
    {
        "number": 35,
        "name": "Slovak",
        "people": 5500000,
        "words": 250000,
        "diff": 2
    },
    {
        "number": 36,
        "name": "Slovenian",
        "people": 2500000,
        "words": 130000,
        "diff": 3
    },
    {
        "number": 37,
        "name": "Spanish",
        "people": 560000000,
        "words": 100000,
        "diff": 2
    },
    {
        "number": 38,
        "name": "Swedish",
        "people": 10500000,
        "words": 125000,
        "diff": 3
    },
    {
        "number": 39,
        "name": "Turkish",
        "people": 90000000,
        "words": 115000,
        "diff": 3
    },
    {
        "number": 40,
        "name": "Ukrainian",
        "people": 45000000,
        "words": 250000,
        "diff": 1
    },
    {
        "number": 41,
        "name": "Welsh",
        "people": 900000,
        "words": 100000,
        "diff": 4
    }
]


# --------------- обработка --------------------

from collections import Counter, defaultdict
from pprint import pprint

print("1. сгруппировать языки по сложности, вывести по группам по алфавиту")

gl = defaultdict(list)

for lang in langs:
    gl[lang['diff']] .append( lang['name'] )

for g in gl.values():
    g.sort()

pprint(gl)

# --------------- результат --------------------

# ~ 1. сгруппировать языки по сложности, вывести по группам по алфавиту
# ~ defaultdict(<class 'list'>,
            # ~ {1: ['Belarusian', 'Russian', 'Ukrainian'],
             # ~ 2: ['Bosnian',
                 # ~ 'Bulgarian',
                 # ~ 'Catalan',
                 # ~ 'Croatian',
                 # ~ 'Dutch',
                 # ~ 'English',
                 # ~ 'Galician',
                 # ~ 'Italian',
                 # ~ 'Macedonian',
                 # ~ 'Polish',
                 # ~ 'Portuguese',
                 # ~ 'Romanian',
                 # ~ 'Serbian',
                 # ~ 'Slovak',
                 # ~ 'Spanish'],
             # ~ 3: ['Azerbaijani',
                 # ~ 'Czech',
                 # ~ 'Danish',
                 # ~ 'French',
                 # ~ 'German',
                 # ~ 'Latvian',
                 # ~ 'Lithuanian',
                 # ~ 'Norwegian',
                 # ~ 'Slovenian',
                 # ~ 'Swedish',
                 # ~ 'Turkish'],
             # ~ 4: ['Albanian',
                 # ~ 'Armenian',
                 # ~ 'Greek',
                 # ~ 'Icelandic',
                 # ~ 'Irish',
                 # ~ 'Maltese',
                 # ~ 'Welsh'],
             # ~ 5: ['Basque', 'Estonian', 'Finnish', 'Georgian', 'Hungarian']})

# --------------- конец --------------------
