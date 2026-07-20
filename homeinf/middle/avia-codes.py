#!/usr/bin/env python
# myke 2026-06-08 2026-06-19 1.4
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
        "Airplane %s registered as %s flew away at %s.",
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
 'The plane C-QJ17 for route GE2S98 started at January 20, 2009.',
 'Aircraft 9H-Z185 for voyage QF7B04 launched at February 18, 2022.',
 'Aircraft EI-QB94 for voyage FFG857 launched at January 13, 2017.',
 'Aircraft EJ-SS26 for voyage TTQG66 launched at August 25, 2016.',
 'Aircraft EI-F342 for good flight WEX755 launched at November 9, 2009.',
 'Plane 9H-J249 for the flight QEOZ89 began at November 10, 2026.',
 'The plane PH-I8I0 for route OP2C13 started at January 5, 2025.',
 'Aircraft B-Q273 for good flight VGWZ54 launched at January 2, 2024.',
 'Plane G-J5A2 for the flight FD1V66 began at June 10, 2018.',
 'The plane EI-O9B9 for route BR5E17 started at December 21, 2010.',
 'The plane EI-U956 for route KUFB07 started at February 1, 2014.',
 'Plane HB-S5A6 for the flight IUI814 began at June 19, 2014.',
 'Aircraft G-COU5 for voyage SDZE22 launched at June 9, 2006.',
 'Aircraft PH-E4A4 for good flight MD4376 launched at December 9, 2020.',
 'Plane PH-O9E3 for the flight CCBZ45 began at February 27, 2017.',
 'Plane B-SX90 for the flight JD4481 began at March 11, 2002.',
 'The plane EI-C482 for route CZ7263 started at August 4, 2016.',
 'The plane F-XT89 for route XH2605 started at October 12, 2003.',
 'Aircraft B-ORW8 for voyage HT2301 launched at November 28, 2021.',
 'Plane HB-TA09 for the flight PX5A34 began at November 8, 2017.',
 'Plane EJ-PCT0 for the flight OZSE59 began at August 28, 2026.',
 'Aircraft EJ-OZ64 for voyage DO1971 launched at February 14, 2017.',
 'Plane F-IX03 for the flight CW8V14 began at August 6, 2020.',
 'Aircraft G-Q682 for good flight ON2L92 launched at June 5, 2008.',
 'Aircraft G-D6P9 for voyage AI8427 launched at June 7, 2016.',
 'Aircraft G-FHI2 for good flight TQ3863 launched at January 3, 2007.',
 'Aircraft G-DA92 for voyage CB9C55 launched at September 27, 2021.',
 'Aircraft G-M373 for good flight CNE404 launched at September 21, 2006.',
 'Plane EI-NUX1 for the flight SG3011 began at February 25, 2021.',
 'The plane G-B233 for route GT5352 started at January 25, 2015.']

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
# ~ solve(astory)

# -------------------- THE END -----------------------
