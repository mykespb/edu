#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-09-24 2025-09-24 1.1
# re-test.py

import re

# ~ https://docs.python.org/3/library/re.html
# ~ https://docs.python.org/3/howto/regex.html
# ~ https://www.w3schools.com/python/python_regex.asp
# ~ https://www.geeksforgeeks.org/python/python-regex-re-search-vs-re-findall/


print("""------------------------------------------
example 1
------------------------------------------""")

# ~ fid simple text

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

print(re.search(r'how', txt))

print(re.findall(r'how', txt))

for i, ex in enumerate(re.findall(r'how', txt)):
    print(i, ex)

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
announce2 = re.sub(r'шило', 'мыло', announce1)
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
# ~ <re.Match object; span=(73, 76), match='how'>
# ~ ['how', 'how']
# ~ 0 how
# ~ 1 how
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

