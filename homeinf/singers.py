#!/usr/bin/env python
# myke 2026-06-198 2026-06-19 1.0
# singers.py

# ~ сделай список 50 уже умерших популярных артистов эстрады, джаза, рока, фолка, кантри, и сделай таблицу (список python) со столбцами: 
# ~ - name: фамилия и имя, 
# ~ - birth: год рождения,
# ~ - death: год смерти,
# ~ - start: начало карьеры,
# ~ - end: конец карьеры

artists = [
    {"name": "Louis Armstrong", "birth": 1901, "death": 1971, "start": 1919, "end": 1971},
    {"name": "Duke Ellington", "birth": 1899, "death": 1974, "start": 1914, "end": 1974},
    {"name": "Ella Fitzgerald", "birth": 1917, "death": 1996, "start": 1934, "end": 1993},
    {"name": "Miles Davis", "birth": 1926, "death": 1991, "start": 1944, "end": 1991},
    {"name": "Billie Holiday", "birth": 1915, "death": 1959, "start": 1933, "end": 1959},
    {"name": "John Coltrane", "birth": 1926, "death": 1967, "start": 1945, "end": 1967},
    {"name": "Charlie Parker", "birth": 1920, "death": 1955, "start": 1937, "end": 1955},
    {"name": "Thelonious Monk", "birth": 1917, "death": 1982, "start": 1941, "end": 1973},
    {"name": "Nina Simone", "birth": 1933, "death": 2003, "start": 1954, "end": 2002},
    {"name": "Nat King Cole", "birth": 1919, "death": 1965, "start": 1934, "end": 1965},
    {"name": "Elvis Presley", "birth": 1935, "death": 1977, "start": 1953, "end": 1977},
    {"name": "Michael Jackson", "birth": 1958, "death": 2009, "start": 1964, "end": 2009},
    {"name": "Freddie Mercury", "birth": 1946, "death": 1991, "start": 1965, "end": 1991},
    {"name": "John Lennon", "birth": 1940, "death": 1980, "start": 1956, "end": 1980},
    {"name": "George Harrison", "birth": 1943, "death": 2001, "start": 1958, "end": 2001},
    {"name": "David Bowie", "birth": 1947, "death": 2016, "start": 1962, "end": 2016},
    {"name": "Prince", "birth": 1958, "death": 2016, "start": 1975, "end": 2016},
    {"name": "Jimi Hendrix", "birth": 1942, "death": 1970, "start": 1962, "end": 1970},
    {"name": "Janis Joplin", "birth": 1943, "death": 1970, "start": 1962, "end": 1970},
    {"name": "Jim Morrison", "birth": 1943, "death": 1971, "start": 1965, "end": 1971},
    {"name": "Kurt Cobain", "birth": 1967, "death": 1994, "start": 1982, "end": 1994},
    {"name": "Amy Winehouse", "birth": 1983, "death": 2011, "start": 1997, "end": 2011},
    {"name": "Whitney Houston", "birth": 1963, "death": 2012, "start": 1977, "end": 2012},
    {"name": "Aretha Franklin", "birth": 1942, "death": 2018, "start": 1956, "end": 2018},
    {"name": "Ray Charles", "birth": 1930, "death": 2004, "start": 1947, "end": 2004},
    {"name": "James Brown", "birth": 1933, "death": 2006, "start": 1953, "end": 2006},
    {"name": "Marvin Gaye", "birth": 1939, "death": 1984, "start": 1956, "end": 1984},
    {"name": "Bob Marley", "birth": 1945, "death": 1981, "start": 1962, "end": 1981},
    {"name": "Tina Turner", "birth": 1939, "death": 2023, "start": 1957, "end": 2020},
    {"name": "Chuck Berry", "birth": 1926, "death": 2017, "start": 1953, "end": 2017},
    {"name": "Little Richard", "birth": 1932, "death": 2020, "start": 1947, "end": 2020},
    {"name": "Buddy Holly", "birth": 1936, "death": 1959, "start": 1952, "end": 1959},
    {"name": "Frank Sinatra", "birth": 1915, "death": 1998, "start": 1935, "end": 1995},
    {"name": "Edith Piaf", "birth": 1915, "death": 1963, "start": 1935, "end": 1963},
    {"name": "Johnny Cash", "birth": 1932, "death": 2003, "start": 1954, "end": 2003},
    {"name": "Hank Williams", "birth": 1923, "death": 1953, "start": 1937, "end": 1953},
    {"name": "Patsy Cline", "birth": 1932, "death": 1963, "start": 1948, "end": 1963},
    {"name": "Waylon Jennings", "birth": 1937, "death": 2002, "start": 1958, "end": 2002},
    {"name": "George Jones", "birth": 1931, "death": 2013, "start": 1953, "end": 2013},
    {"name": "Kenny Rogers", "birth": 1938, "death": 2020, "start": 1957, "end": 2020},
    {"name": "Glen Campbell", "birth": 1936, "death": 2017, "start": 1958, "end": 2012},
    {"name": "John Denver", "birth": 1943, "death": 1997, "start": 1962, "end": 1997},
    {"name": "Woody Guthrie", "birth": 1912, "death": 1967, "start": 1930, "end": 1956},
    {"name": "Pete Seeger", "birth": 1919, "death": 2014, "start": 1939, "end": 2014},
    {"name": "Leonard Cohen", "birth": 1934, "death": 2016, "start": 1956, "end": 2016},
    {"name": "Vladimir Vysotsky", "birth": 1938, "death": 1980, "start": 1959, "end": 1980},
    {"name": "Viktor Tsoi", "birth": 1962, "death": 1990, "start": 1978, "end": 1990},
    {"name": "Muslim Magomayev", "birth": 1942, "death": 2008, "start": 1959, "end": 2008},
    {"name": "Iosif Kobzon", "birth": 1937, "death": 2018, "start": 1956, "end": 2018},
    {"name": "Eduard Khil", "birth": 1934, "death": 2012, "start": 1960, "end": 2012}
]

# ------------------------ prepare -------------------------

from pprint import pp, pprint

# ----------------------------------------------------------

def part(name):
    print(f"""
----------------------------------------------------------
{name}
----------------------------------------------------------
""")

def cprint(kv, wleft=20):
    for k, v in kv:
        print(f"{k:{wleft}} | {v}")

# -------------------------------------------------
part("1. у кого самая длинная и самая короткая карьера?")
# -------------------------------------------------

got = sorted([ (person['end'] - person['start'], person['name'])
    for person in artists ])

short, long = got[0], got[-1]

print(f"""
самая длинная карьера:  {long[0]} лет: {long[1]}
самая короткая карьера: {short[0]} лет: {short[1]}
""")

# ~ pprint(artists)

# -------------------------------------------------
part("2. у кого карьера занимала наибольшую часть жизни?")
# -------------------------------------------------

for i, p in enumerate(artists):
    artists[i]['part'] = (p['end'] - p['start'] ) / (p['death'] - p['birth'])

artists.sort(key = lambda x: x['part'], reverse=True)

print(artists[0])

long = artists[0]
print(f"""
обладатель самой длинной карьеры: {long['name']}
родился в {long['birth']} году,
умер в {long['death']} году,
начал петь в {long['start']} году,
закончил петь в {long['end']} году,
жил {long['death'] - long['birth']} лет,
пел {long['end'] - long['start']} лет,
творческая часть жизни: {long['part'] * 100:.0f}%.
""")

# -------------------------------------------------
part("конец изучения")

# ~ pprint(artists)

# -------------------------------------------------
