#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-09-24 2025-09-24 0.1
# re-test.py

import re

# ~ https://docs.python.org/3/library/re.html
# ~ https://docs.python.org/3/howto/regex.html
# ~ https://www.w3schools.com/python/python_regex.asp
# ~ https://www.geeksforgeeks.org/python/python-regex-re-search-vs-re-findall/


print("""------------------------------------------
example 1
------------------------------------------""")

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(f"{x=}, [{x}]")
if x:
  print("YES! We have a match!")
else:
  print("No match")

print("""------------------------------------------
example 2
------------------------------------------""")

txt = """
How many roads must a man walk down
Before you call him a man?
Yes, ’n’ how many seas must a white dove sail
Before she sleeps in the sand?
Yes, ’n’ how many times must the cannonballs fly
Before they’re forever banned?
The answer, my friend, is blowin’ in the wind
The answer is blowin’ in the wind
"""

print(re.search(r'how', txt))

print(re.findall(r'how', txt))

for i, ex in enumerate(re.findall(r'how', txt)):
    print(i, ex)

print("""------------------------------------------
example 3
------------------------------------------""")

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 

print("""------------------------------------------
example 4
------------------------------------------""")

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
