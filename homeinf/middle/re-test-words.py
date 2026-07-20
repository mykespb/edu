#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2025-09-24 2026-06-06 1.5
# re-test-words.py

# ~ Regular expressions: words

# ~ https://docs.python.org/3/library/re.html
# ~ https://www.w3schools.com/python/python_regex.asp
# ~ https://www.geeksforgeeks.org/python/re-search-in-python/
# ~ https://www.geeksforgeeks.org/python/re-match-in-python/

# https://www.w3schools.com/python/ref_string_maketrans.asp
# https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_find
# https://mimo.org/glossary/python/string-find

# ~ https://docs.python.org/3/howto/regex.html
# ~ https://www.geeksforgeeks.org/python/python-regex-re-search-vs-re-findall/
# ~ https://www.w3schools.com/python/ref_string_count.asp

import re

print("""------------------------------------------
example 1
------------------------------------------""")

# ~ find simple text

txt = """
How many roads must a man walk down
Before you call him a man?
Yes, ’n’ how many seas must a white dove sail
Before she sleeps in the sand?
Yes, ’n’ how many times must the cannonballs fly
Before they’re forever banned?
The answer, my friend, is blowin’ in the wind
The answer is blowin’ in the wind
(Bob Dylan, 1962)
"""

print("search 1:", re.search(r'how', txt), "=>", re.search(r'how', txt)[0])
print("search 2:", re.search(r'how', txt, flags = re.IGNORECASE), "=>",
    re.search(r'how', txt, flags = re.IGNORECASE)[0])

print("findall 1:", re.findall(r'how', txt))
print("findall 2:", re.findall(r'how', txt, flags = re.IGNORECASE))

print("for:")
for i, ex in enumerate(re.findall(r'how', txt)):
    print(i, ex)

print("""------------------------------------------
example 1.1 Schedule
------------------------------------------""")

# ~ print("\n--------------- Schedule -------------------\n")

txtx = """
date 2026-06-04T14:00 flight ABC123 status OK
date 2026-06-05T10:30 flight RENO987 status OK
date 2026-06-06T02:00 flight BARA14 status PLANNED
date 2026-06-07T15:00 flight SOHO1 status POSTPONED
date 2026-06-08T20:20 flight TBD00 status DELETED
"""

print('test 1')

for line in txtx.strip().splitlines():
    if "OK" in line:
        print(line)

print('test 2')

for line in txtx.strip().splitlines():
    if "OK" in line:
        ls = line.split()
        print(ls[1], ls[3])

print('test 3')

for line in txtx.strip().splitlines():
    m = re.match(r"date ([\w\d.:-]+) flight (\w+) status (\w+)", line)
    if m:
        print(m.groups())

print('test 4')

for line in txtx.strip().splitlines():
    # ~ print(line)
    # ~ m = re.match(r"date (\w+)", line)
    m = re.match(r"date ([\w\d.:-]+) flight (\w+) status (\w+)", line)
    # ~ m = re.match(r"date (\w+) flight (\w+) status (\w+)", line)
    if m:
        print(m[1], m[2], m[3])
    else:
        print("re.match failed")

print('test 5')

for line in txtx.strip().splitlines():
    m = re.match(r"date (?P<DATE>[\w\d.:-]+) flight (?P<FLIGHT>\w+) status (?P<STATUS>\w+)", line)
    if m:
        print(m['DATE'], m['FLIGHT'], m['STATUS'])

print('test 6')

txtx = """
date 2026-06-04T14:00 flight ABC123 status OK
date 2026-06-05T10:30 pvt flight RENO987 status OK
date 2026-06-06T02:00 flight PVT14 status PLANNED
date 2026-06-07T15:00 flight SOHO1 status POSTPONED
date 2026-06-08T20:20 PVT flight TBD00 status DELETED
"""

for line in txtx.strip().splitlines():
    m = re.match(r"date (?P<DATE>[\w\d.:-]+) (?i:pvt )?flight (?P<FLIGHT>\w+) status (?P<STATUS>\w+)", line)
    if m:
        print(m['DATE'], m['FLIGHT'], m['STATUS'])

print('test 0 for Newton')

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))

print("""------------------------------------------
example 2
------------------------------------------""")

# ~ find or split by simple pattern

txt = "The rain in Spain"
x = re.search(r"\s", txt)

print("The first white-space character is located in position:", x.start()) 

print("""------------------------------------------
example 3
------------------------------------------""")

# split the string at every white-space character:

txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)

print("""------------------------------------------
example 4
------------------------------------------""")

# ~ find by more complex pattern

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(f"{x=}, [{x}]")
if x:
  print("YES! We have a match!")
else:
  print("No match")

print("""------------------------------------------
example 5
------------------------------------------""")

# ~ match all group

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(1,2))

print("""------------------------------------------
example 6
------------------------------------------""")

# ~ match groups and vars

m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())

m = re.match(r"(\d+)\.(\d+)\.(\d+)", "20.03.1968")
print(m.groups())
day, month, year = map(int, m.groups())
print(f"{year=}, {month=}, {day=}")

print("""------------------------------------------
example 7
------------------------------------------""")

# ~ substitute texts by simple templates

announce1 = 'Имеется прекрасное шило!'
print(f"{announce1=}")
announce2 = re.sub('шило', 'мыло', announce1)
print(f"{announce2=}")

print("""------------------------------------------
example 8
------------------------------------------""")

# ~ substitute texts by more complex templates

announce1 = 'Имеется прекрасное шило! Если бы пило, то не выло б. На два кило ещё! Два Ужасных Киловатта!'
print(f"{announce1=}")
announce2 = re.sub(r'([кпш]ило)', r'мыло', announce1)
print(f"{announce2=}")
announce3 = re.sub(r'([кпш]ило)', r'мыло (а было слово: \1)', announce1, flags=re.IGNORECASE)
print(f"{announce3=}")

print("""------------------------------------------
the end.
------------------------------------------""")

# ~ ------------------------------------------
# ~ example 1
# ~ ------------------------------------------
# ~ search 1: <re.Match object; span=(73, 76), match='how'> => how
# ~ search 2: <re.Match object; span=(1, 4), match='How'> => How
# ~ findall 1: ['how', 'how']
# ~ findall 2: ['How', 'how', 'how']
# ~ for:
# ~ 0 how
# ~ 1 how
# ~ ------------------------------------------
# ~ example 1.1 Schedule
# ~ ------------------------------------------
# ~ test 1
# ~ date 2026-06-04T14:00 flight ABC123 status OK
# ~ date 2026-06-05T10:30 flight RENO987 status OK
# ~ test 2
# ~ 2026-06-04T14:00 ABC123
# ~ 2026-06-05T10:30 RENO987
# ~ test 3
# ~ ('2026-06-04T14:00', 'ABC123', 'OK')
# ~ ('2026-06-05T10:30', 'RENO987', 'OK')
# ~ ('2026-06-06T02:00', 'BARA14', 'PLANNED')
# ~ ('2026-06-07T15:00', 'SOHO1', 'POSTPONED')
# ~ ('2026-06-08T20:20', 'TBD00', 'DELETED')
# ~ test 4
# ~ 2026-06-04T14:00 ABC123 OK
# ~ 2026-06-05T10:30 RENO987 OK
# ~ 2026-06-06T02:00 BARA14 PLANNED
# ~ 2026-06-07T15:00 SOHO1 POSTPONED
# ~ 2026-06-08T20:20 TBD00 DELETED
# ~ test 5
# ~ 2026-06-04T14:00 ABC123 OK
# ~ 2026-06-05T10:30 RENO987 OK
# ~ 2026-06-06T02:00 BARA14 PLANNED
# ~ 2026-06-07T15:00 SOHO1 POSTPONED
# ~ 2026-06-08T20:20 TBD00 DELETED
# ~ test 6
# ~ 2026-06-04T14:00 ABC123 OK
# ~ 2026-06-05T10:30 RENO987 OK
# ~ 2026-06-06T02:00 PVT14 PLANNED
# ~ 2026-06-07T15:00 SOHO1 POSTPONED
# ~ 2026-06-08T20:20 TBD00 DELETED
# ~ test 0 for Newton
# ~ Isaac Newton
# ~ ------------------------------------------
# ~ example 2
# ~ ------------------------------------------
# ~ The first white-space character is located in position: 3
# ~ ------------------------------------------
# ~ example 3
# ~ ------------------------------------------
# ~ ['The', 'rain', 'in', 'Spain']
# ~ ------------------------------------------
# ~ example 4
# ~ ------------------------------------------
# ~ x=<re.Match object; span=(0, 17), match='The rain in Spain'>, [<re.Match object; span=(0, 17), match='The rain in Spain'>]
# ~ YES! We have a match!
# ~ ------------------------------------------
# ~ example 5
# ~ ------------------------------------------
# ~ Isaac Newton
# ~ Isaac
# ~ Newton
# ~ ('Isaac', 'Newton')
# ~ ------------------------------------------
# ~ example 6
# ~ ------------------------------------------
# ~ ('24', '1632')
# ~ ('20', '03', '1968')
# ~ year=1968, month=3, day=20
# ~ ------------------------------------------
# ~ example 7
# ~ ------------------------------------------
# ~ announce1='Имеется прекрасное шило!'
# ~ announce2='Имеется прекрасное мыло!'
# ~ ------------------------------------------
# ~ example 8
# ~ ------------------------------------------
# ~ announce1='Имеется прекрасное шило! Если бы пило, то не выло б. На два кило ещё! Два Ужасных Киловатта!'
# ~ announce2='Имеется прекрасное мыло! Если бы мыло, то не выло б. На два мыло ещё! Два Ужасных Киловатта!'
# ~ announce3='Имеется прекрасное мыло (а было слово: шило)! Если бы мыло (а было слово: пило), то не выло б. На два мыло (а было слово: кило) ещё! Два Ужасных мыло (а было слово: Кило)ватта!'
# ~ ------------------------------------------
# ~ the end.
# ~ ------------------------------------------

