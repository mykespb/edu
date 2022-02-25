#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-25 2022-02-25 1.0
# alfabravo.py

# ~ вот фонетический алфавит
# ~ напечатать слова, в которых есть буква А

abc = '''
A Alfa
B Bravo
C Charlie
D Delta
E Echo
F Foxtrot
G Golf
H Hotel
I India
J Juliett
K Kilo
L Lima
M Mike
N November
O Oscar
P Papa
Q Quebec
R Romeo
S Sierra
T Tango
U Uniform
V Victor
W Whiskey
X X-ray
Y Yankee
Z Zulu
'''

for word in abc.split():
    if len(word) > 1 and 'a' in word.lower():
        print(word, end=', ')
        

# ~ Alfa, Bravo, Charlie, Delta, India, Lima,
# ~ Oscar, Papa, Sierra, Tango, X-ray, Yankee, 
