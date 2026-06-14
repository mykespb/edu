#!/usr/bin/env python
# myke 2026-06-08 2026-06-12 1.2
# avia-codes.py

# ~ по сгенерированному списку кодов бортов самолётов определить 3 наиболее активно представленных страны.

from random import choice, randint
import string
from pprint import pp, pprint
import re

# -------------------- MAKING DATA -----------------------

AMOUNT = 30

table = {
    'G':  "Великобритания",
    'HB': "Швейцария",
    'EI': "Ирландия",
    'EJ': "Ирландия",
    'C':  "Канада",
    'B':  "Китай",
    'F':  "Франция",
    '9H': "Мальта",
    'PH': "Нидерланды"
    }


def make_planes(num : int = AMOUNT):
    """сделать случайный список бортов"""

    return [
        choice(tuple(table.keys())) + "-" +
        choice(string.ascii_uppercase) +
        ( choice(string.ascii_uppercase) if choice([False, True]) else choice(string.digits) ) +
        ( choice(string.ascii_uppercase) if choice([False, True]) else choice(string.digits) ) +
        choice(string.digits) 
        for _ in range(num)] 
        

def make_flights(num : int = AMOUNT):
    """сделать случайный список полётов"""

    return [
        choice(string.ascii_uppercase) +
        choice(string.ascii_uppercase) +
        ( choice(string.ascii_uppercase) if choice([False, True]) else choice(string.digits) ) +
        ( choice(string.ascii_uppercase) if choice([False, True]) else choice(string.digits) ) +
        choice(string.digits) +
        choice(string.digits)
        for _ in range(num)]


def make_dates(num : int = AMOUNT):
    """сделать случайный список дат"""

    months = "January February March April May June July August September October November December".split()

    return [ choice(months) + " " + str(randint(1, 28)) + ", " + str(randint(2000, 2026)) for _ in range(num) ]


planes  = make_planes()
flights = make_flights()
dates   = make_dates()

data    = tuple(zip(planes, flights, dates))

pp(data)

def make_story(data):
    """сделать текст на англ. яз. про аэропорт"""

    patterns = (
        "The plane %s for route %s started at %s.",
        "Plane %s for the flight %s began at %s.",
        "Aircraft %s for good flight %s launched at %s.",
        "Aircraft %s for voyage %s launched at %s.",
        )

    text = [
        choice(patterns) % (e1, e2, e3)
        for e1, e2, e3 in data
        ]

    return text


astory = make_story(data)
pp(astory)

cstory = [
 'The plane EJ-UU90 for route JKT706 started at June 17, 2017 .',
 'The plane EJ-RH15 for route KAV466 started at November 19, 2018 .',
 'Aircraft EI-WW76 for good flight FVV287 launched at November 2, 2019 .',
 'The plane EI-LZ40 for route CEB779 started at March 3, 2007 .',
 'The plane G-EM25 for route DBW857 started at September 21, 2008 .',
 'Aircraft F-MM08 for voyage OVY981 launched at July 12, 2023 .',
 'Aircraft C-XQ34 for voyage LON040 launched at July 5, 2017 .',
 'Aircraft G-GT47 for voyage WMD093 launched at April 15, 2000 .',
 'Aircraft EJ-XD39 for voyage BNT458 launched at May 16, 2009 .',
 'Plane B-QM16 for the flight GOB087 began at September 15, 2024 .',
 'Aircraft C-LR57 for good flight GPI738 launched at January 14, 2017 .',
 'Plane 9H-TQ53 for the flight CAU640 began at November 1, 2005 .',
 'Plane 9H-QJ64 for the flight RVX437 began at July 7, 2009 .',
 'Aircraft B-OB47 for good flight UVQ657 launched at June 14, 2021 .',
 'Aircraft EI-AU44 for good flight TJF896 launched at February 2, 2010 .',
 'The plane G-OJ93 for route XJX635 started at January 6, 2001 .',
 'Aircraft G-GI69 for good flight COD050 launched at October 15, 2000 .',
 'Aircraft EJ-ST52 for voyage SAT335 launched at July 27, 2023 .',
 'Aircraft G-AM02 for good flight QRP945 launched at September 11, 2020 .',
 'The plane B-XZ60 for route VMD499 started at January 16, 2003 .'
 ]

pp(cstory)

# -------------------- PROCESSING -----------------------

from collections import Counter

def solve(story):
    """всё порешать"""

    cnt = Counter()

    print("\n================= Here is solving: =================\n")
    
    for line in story:
        print(line)

        for key in table.keys():
            pattern = fr"\b({key})\b-\w+"

            m = re.search(pattern, line)
            if m:
                got = m[1]
                print(f"found '{got}' -> {table[got]}")
                cnt[table[got]] += 1

    print("\nОтвет. 3 самых представленных страны: ", end="")
    print(*list(key[0] for key in cnt.most_common(3)), sep=", ", end=".\n")
    
    print("\n================= Solving is over. =================\n")


solve(cstory)
solve(astory)

# -------------------- THE END -----------------------
