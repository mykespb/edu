#!/usr/bin/env python
# macros.py 2023-08-27 2023-08-27 1.0
# (C) Mikhail Kolodin, 2023

# There are macro definitions in text like:
# VAR1="Hello"
# VAR2="World"
# and places for their substitutions like:
# Var1 = $VAR1
# Var2 = $VAR2
# etc
# Make all substitutions.

text = """
The text

Remember it all:
VAR1="Hello"
VAR2="World"
and make subs
Var1 is $VAR1
Var2 is $VAR2

All done.
"""

from collections import defaultdict

def macro(text: str) -> None:

    macros = defaultdict(str)

    for line in text.split("\n"):
        line = line.strip()
        if not line: 
            print()
            continue

        if "=" in line:
            var, val = line.split("=")
            var = var.strip()
            val = val.strip().strip("'").strip('"')

            macros[var] = val

        else:
            for var in macros:
                sub = "$" + var
                if (pos := line.find(sub)) >= 0:
                    line = line[:pos] + macros[var] + line[pos+len(sub):]

        print(line)


macro(text)

#The text
#
#Remember it all:
#VAR1="Hello"
#VAR2="World"
#and make subs
#Var1 is Hello
#Var2 is World
#
#All done.

