#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-28 2026-04-28 1.1
# re-test-dates.py

# ~ Regular expressions: dates

import re

# ~ https://docs.python.org/3/library/re.html
# ~ https://docs.python.org/3/howto/regex.html
# ~ https://www.w3schools.com/python/python_regex.asp
# ~ https://www.geeksforgeeks.org/python/python-regex-re-search-vs-re-findall/


print("""------------------------------------------
example 1. find dates.
------------------------------------------""")

txt = """
Charles III (Charles Philip Arthur George; born 14 November 1948) is King of the United Kingdom and 14 other Commonwealth realms.
Charles was created Prince of Wales and Earl of Chester on 26 July 1958.
Diana died following a car crash in Paris on 31 August 1997.
Charles acceded to the British throne on his mother's death on 8 September 2022.
28.04.2026 is the date of creation of this text.
It is also known as 2026-04-28, as you may know.
"""

months = "January February March April May June July August September October November December" . split()
# ~ print(months)

def finder(txt):
    fs = re.findall(r"\d{1,2}\s+\w+\s+[12]\d{3}", txt)
    print(fs)

finder(txt)

print("""------------------------------------------
example 2. find dates and change all of them to standard format.
------------------------------------------""")

def sub_months(m):
    for mp in months:
        m = re.sub(mp, "%02d" % (months.index(mp)+1), m)
    return m

def stander(txt):
    fs = re.sub(r"(\d{2})\s+(\w+)\s+([12]\d{3})",
        r"\3-\2-\1",
        txt)
    fs = re.sub(r"(\d{1})\s+(\w+)\s+([12]\d{3})",
        r"\3-\2-0\1",
        fs)
    fs = re.sub(r"(\d{2})\.(\d{2}).(\d{4})",
        r"\3-\2-\1",
        fs)
    fs = sub_months(fs)
    print(fs)

stander(txt)

# ~ ------------------------------------------
# ~ ['14 November 1948', '26 July 1958', '31 August 1997', '8 September 2022']
# ~ ------------------------------------------
# ~ example 2. find dates and change all of them to standard format.
# ~ ------------------------------------------

# ~ Charles III (Charles Philip Arthur George; born 1948-11-14) is King of the United Kingdom and 14 other Commonwealth realms.
# ~ Charles was created Prince of Wales and Earl of Chester on 1958-07-26.
# ~ Diana died following a car crash in Paris on 1997-08-31.
# ~ Charles acceded to the British throne on his mother's death on 2022-09-08.
# ~ 2026-04-28 is the date of creation of this text.
# ~ It is also known as 2026-04-28, as you may know.

# ~ ------------------------------------------
# ~ the end.
# ~ ------------------------------------------
