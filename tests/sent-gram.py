#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-08 2025-01-08 1.0
# sent-gram.py

# ~ а. По заданной грамматике построить случайные предложения.
# ~ б. То же, проверить правильность предложения.

# grammar and vocabulary

grammar_rules = """
phrase subject-group predicate-group
subject-group adjective* noun
predicate-group adverb+ verb object?
object noun
"""

noun = """
boy girl thing bus house string computer man woman desk port stone brush boo pen pencil
"""

adverb = """
well loudly slowly quickly pretty
"""

adjective = """
quiet funny long short bright green red yellow black white silver rosy nice tiny great big small
"""

verb = """
does gives wants sings takes thinks says checks
"""


# imports

from pprint import pp, pprint
from random import randint, choice


# preparations

def prepare_all() -> None:
    """
    подготовить грамматику и словарь к реальному использованию
    """

    global grammar, words

    grammar = {}
    words = {}

    print("PREPARE:")

    for rule_line in grammar_rules.strip().split("\n"):

        name, *ruler = rule_line.split()

        rule = []

        for item in ruler:
            if item.endswith(("?", "*", "+")):
                rule.append( [ item[:-1], "", item[-1] ] )
            else:
                rule.append( [ item, "", "" ] )

        grammar[name] = rule

    for name, rule in grammar.items():
        for item in rule:
            item[1] = 'rule' if item[0] in grammar else 'word'

    pprint(grammar, compact=True)

    add_words(noun, 'noun')
    add_words(adverb, 'adverb')
    add_words(verb, 'verb')
    add_words(adjective, 'adjective')

    pprint(words, compact=True)

    print("Preparation done.")


def add_words(var : str, item : str) -> None:
    """
    добавить словарь слов
    """

    words[item] = []
    
    for what in var.strip().replace("\n", " ").split():
        words[item].append(what)


# rules

def make(what : str) -> str:
    """
    создать набор данных, соответствующий заданному элементу грамматики
    """

    assert what in grammar

    out = []

    for item in grammar[what]:
        name, mode, times = item

        if times == '':
            range_from = 1
            range_to = 2
        elif times == '?':
            range_from = 0
            range_to = 1
        elif times == '+':
            range_from = 0
            range_to = 2
        if times == '*':
            range_from = 0
            range_to = 3
        
        for rep_word in range( range_from, randint(range_from+1, range_to)):

            if mode == 'word':
                out.append( choice(words[name]) )
            else:
                out.extend( make(name) ) 

    return out


def pretty(frase : str) -> str:
    """
    привести к приятному виду фразу
    """

    for iword in range(1, len(frase)):
        if frase[iword-1] == frase[iword]:
            frase[iword-1] = ""

    frase = list( filter( None, frase) )

    out = " " .join(frase) + '.'

    out = out.capitalize()

    return out
    

def main(howmany : int = 1) -> None:
    """
    главный пуск
    """

    print("\n---------------------- ФРАЗЕР по грамматике ----------------------\n")
    prepare_all()

    for rept in range(1, howmany+1):
        print(f"\n---------------------- ФРАЗЕР {rept} ----------------------\n")
        frase = pretty(make("phrase"))
        print(frase)

    print("\n---------------------- Конец работы ----------------------\n")

main(10)

# TODO: будет ещё часть для проверки...
#...


# ~ ---------------------- ФРАЗЕР по грамматике ----------------------

# ~ PREPARE:
# ~ {'object': [['noun', 'word', '']],
 # ~ 'phrase': [['subject-group', 'rule', ''], ['predicate-group', 'rule', '']],
 # ~ 'predicate-group': [['adverb', 'word', '+'], ['verb', 'word', ''],
                     # ~ ['object', 'rule', '?']],
 # ~ 'subject-group': [['adjective', 'word', '*'], ['noun', 'word', '']]}
# ~ {'adjective': ['quiet', 'funny', 'long', 'short', 'bright', 'green', 'red',
               # ~ 'yellow', 'black', 'white', 'silver', 'rosy', 'nice', 'tiny',
               # ~ 'great', 'big', 'small'],
 # ~ 'adverb': ['well', 'loudly', 'slowly', 'quickly', 'pretty'],
 # ~ 'noun': ['boy', 'girl', 'thing', 'bus', 'house', 'string', 'computer', 'man',
          # ~ 'woman', 'desk', 'port', 'stone', 'brush', 'boo', 'pen', 'pencil'],
 # ~ 'verb': ['does', 'gives', 'wants', 'sings', 'takes', 'thinks', 'says',
          # ~ 'checks']}
# ~ Preparation done.

# ~ ---------------------- ФРАЗЕР 1 ----------------------

# ~ Quiet short boo loudly well wants girl.

# ~ ---------------------- ФРАЗЕР 2 ----------------------

# ~ Nice tiny string pretty gives house.

# ~ ---------------------- ФРАЗЕР 3 ----------------------

# ~ Great long thing slowly says boy.

# ~ ---------------------- ФРАЗЕР 4 ----------------------

# ~ White funny red pencil pretty checks desk.

# ~ ---------------------- ФРАЗЕР 5 ----------------------

# ~ Funny bus well slowly gives port.

# ~ ---------------------- ФРАЗЕР 6 ----------------------

# ~ Green short man quickly does stone.

# ~ ---------------------- ФРАЗЕР 7 ----------------------

# ~ Tiny quiet red brush loudly well says house.

# ~ ---------------------- ФРАЗЕР 8 ----------------------

# ~ Tiny boy well checks stone.

# ~ ---------------------- ФРАЗЕР 9 ----------------------

# ~ Bright woman pretty gives woman.

# ~ ---------------------- ФРАЗЕР 10 ----------------------

# ~ Great pen quickly says brush.

# ~ ---------------------- Конец работы ----------------------

