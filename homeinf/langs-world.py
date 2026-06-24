#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# langs.py
# 2026-06-24 2026-06-24 1.0

# ~ перечисли 50 основных разговорных языков в формате list[dict], указав:
# ~ - name; название,
# ~ - people: сколько человек говорит,
# ~ - words: сколько слов  в языке,
# ~ - diff: относительную сложность для русскоговорящего.

# --------------- данные --------------------

langs = [
    {
        "number": 1,
        "name": "Amharic",
        "people": 26000000,
        "words": 50000,
        "diff": 4
    },
    {
        "number": 2,
        "name": "Arabic",
        "people": 275000000,
        "words": 12000000,
        "diff": 5
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
        "name": "Bengali",
        "people": 273000000,
        "words": 100000,
        "diff": 3
    },
    {
        "number": 5,
        "name": "Burmese",
        "people": 33000000,
        "words": 50000,
        "diff": 4
    },
    {
        "number": 6,
        "name": "Dutch",
        "people": 30000000,
        "words": 400000,
        "diff": 2
    },
    {
        "number": 7,
        "name": "Egyptian Arabic",
        "people": 75000000,
        "words": 250000,
        "diff": 4
    },
    {
        "number": 8,
        "name": "English",
        "people": 1500000000,
        "words": 470000,
        "diff": 2
    },
    {
        "number": 9,
        "name": "French",
        "people": 310000000,
        "words": 135000,
        "diff": 3
    },
    {
        "number": 10,
        "name": "German",
        "people": 135000000,
        "words": 330000,
        "diff": 3
    },
    {
        "number": 11,
        "name": "Gujarati",
        "people": 62000000,
        "words": 140000,
        "diff": 3
    },
    {
        "number": 12,
        "name": "Hausa",
        "people": 75000000,
        "words": 45000,
        "diff": 3
    },
    {
        "number": 13,
        "name": "Hindi",
        "people": 610000000,
        "words": 150000,
        "diff": 3
    },
    {
        "number": 14,
        "name": "Indonesian",
        "people": 200000000,
        "words": 125000,
        "diff": 2
    },
    {
        "number": 15,
        "name": "Iranian Persian (Farsi)",
        "people": 77000000,
        "words": 150000,
        "diff": 3
    },
    {
        "number": 16,
        "name": "Italian",
        "people": 67000000,
        "words": 260000,
        "diff": 2
    },
    {
        "number": 17,
        "name": "Japanese",
        "people": 125000000,
        "words": 250000,
        "diff": 5
    },
    {
        "number": 18,
        "name": "Javanese",
        "people": 68000000,
        "words": 85000,
        "diff": 4
    },
    {
        "number": 19,
        "name": "Kannada",
        "people": 64000000,
        "words": 100000,
        "diff": 4
    },
    {
        "number": 20,
        "name": "Kazakh",
        "people": 24000000,
        "words": 130000,
        "diff": 2
    },
    {
        "number": 21,
        "name": "Khmer",
        "people": 18000000,
        "words": 45000,
        "diff": 4
    },
    {
        "number": 22,
        "name": "Korean",
        "people": 82000000,
        "words": 500000,
        "diff": 5
    },
    {
        "number": 23,
        "name": "Kurdish",
        "people": 30000000,
        "words": 120000,
        "diff": 3
    },
    {
        "number": 24,
        "name": "Malagasy",
        "people": 25000000,
        "words": 60000,
        "diff": 3
    },
    {
        "number": 25,
        "name": "Malayalam",
        "people": 39000000,
        "words": 200000,
        "diff": 5
    },
    {
        "number": 26,
        "name": "Mandarin Chinese",
        "people": 1100000000,
        "words": 370000,
        "diff": 5
    },
    {
        "number": 27,
        "name": "Marathi",
        "people": 100000000,
        "words": 120000,
        "diff": 4
    },
    {
        "number": 28,
        "name": "Moroccan Arabic",
        "people": 33000000,
        "words": 100000,
        "diff": 4
    },
    {
        "number": 29,
        "name": "Nepali",
        "people": 25000000,
        "words": 110000,
        "diff": 3
    },
    {
        "number": 30,
        "name": "Nigerian Pidgin",
        "people": 120000000,
        "words": 30000,
        "diff": 2
    },
    {
        "number": 31,
        "name": "Oromo",
        "people": 32000000,
        "words": 35000,
        "diff": 3
    },
    {
        "number": 32,
        "name": "Polish",
        "people": 45000000,
        "words": 140000,
        "diff": 2
    },
    {
        "number": 33,
        "name": "Portuguese",
        "people": 265000000,
        "words": 110000,
        "diff": 2
    },
    {
        "number": 34,
        "name": "Romanian",
        "people": 25000000,
        "words": 150000,
        "diff": 2
    },
    {
        "number": 35,
        "name": "Russian",
        "people": 255000000,
        "words": 200000,
        "diff": 1
    },
    {
        "number": 36,
        "name": "Somali",
        "people": 17000000,
        "words": 40000,
        "diff": 4
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
        "name": "Swahili",
        "people": 72000000,
        "words": 70000,
        "diff": 3
    },
    {
        "number": 39,
        "name": "Tagalog (Filipino)",
        "people": 83000000,
        "words": 60000,
        "diff": 3
    },
    {
        "number": 40,
        "name": "Tamil",
        "people": 87000000,
        "words": 160000,
        "diff": 4
    },
    {
        "number": 41,
        "name": "Telugu",
        "people": 96000000,
        "words": 110000,
        "diff": 4
    },
    {
        "number": 42,
        "name": "Thai",
        "people": 61000000,
        "words": 65000,
        "diff": 4
    },
    {
        "number": 43,
        "name": "Turkish",
        "people": 90000000,
        "words": 115000,
        "diff": 3
    },
    {
        "number": 44,
        "name": "Ukrainian",
        "people": 45000000,
        "words": 250000,
        "diff": 1
    },
    {
        "number": 45,
        "name": "Urdu",
        "people": 230000000,
        "words": 150000,
        "diff": 4
    },
    {
        "number": 46,
        "name": "Uzbek",
        "people": 35000000,
        "words": 85000,
        "diff": 3
    },
    {
        "number": 47,
        "name": "Vietnamese",
        "people": 85000000,
        "words": 80000,
        "diff": 4
    },
    {
        "number": 48,
        "name": "Western Punjabi",
        "people": 66000000,
        "words": 90000,
        "diff": 3
    },
    {
        "number": 49,
        "name": "Yoruba",
        "people": 30000000,
        "words": 40000,
        "diff": 4
    },
    {
        "number": 50,
        "name": "Yue Chinese (Cantonese)",
        "people": 86000000,
        "words": 150000,
        "diff": 5
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
            # ~ {1: ['Russian', 'Ukrainian'],
             # ~ 2: ['Dutch',
                 # ~ 'English',
                 # ~ 'Indonesian',
                 # ~ 'Italian',
                 # ~ 'Kazakh',
                 # ~ 'Nigerian Pidgin',
                 # ~ 'Polish',
                 # ~ 'Portuguese',
                 # ~ 'Romanian',
                 # ~ 'Spanish'],
             # ~ 3: ['Azerbaijani',
                 # ~ 'Bengali',
                 # ~ 'French',
                 # ~ 'German',
                 # ~ 'Gujarati',
                 # ~ 'Hausa',
                 # ~ 'Hindi',
                 # ~ 'Iranian Persian (Farsi)',
                 # ~ 'Kurdish',
                 # ~ 'Malagasy',
                 # ~ 'Nepali',
                 # ~ 'Oromo',
                 # ~ 'Swahili',
                 # ~ 'Tagalog (Filipino)',
                 # ~ 'Turkish',
                 # ~ 'Uzbek',
                 # ~ 'Western Punjabi'],
             # ~ 4: ['Amharic',
                 # ~ 'Burmese',
                 # ~ 'Egyptian Arabic',
                 # ~ 'Javanese',
                 # ~ 'Kannada',
                 # ~ 'Khmer',
                 # ~ 'Marathi',
                 # ~ 'Moroccan Arabic',
                 # ~ 'Somali',
                 # ~ 'Tamil',
                 # ~ 'Telugu',
                 # ~ 'Thai',
                 # ~ 'Urdu',
                 # ~ 'Vietnamese',
                 # ~ 'Yoruba'],
             # ~ 5: ['Arabic',
                 # ~ 'Japanese',
                 # ~ 'Korean',
                 # ~ 'Malayalam',
                 # ~ 'Mandarin Chinese',
                 # ~ 'Yue Chinese (Cantonese)']})

# --------------- конец --------------------
