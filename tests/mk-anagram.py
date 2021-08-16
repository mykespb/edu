#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# M.Kolodin mk-anagram.py 2016-02-12 2021 2.1
# find all anagrams in given text
# return tuple of tuples with anagramix words

from pprint import pprint
from collections import defaultdict

text = """
123 345 231
ethic thetic tethic
удача учада чаадаев овин вино нави винна
tuli tulli tuuli tuulli util little litu
"""

def base (t):
    """ find basic form of word """
    return str("".join(sorted(t)))

def trovu (t):
    """ find all anagrams in given list of words """
    res = {}
    for w in t.split():
        ind = base(w)
        if ind in res:
            res [ind] += [w]
        else:
            res [ind] = [w]
    res = [res[x] for x in res if len(res[x])>1]
    res = [tuple(sorted(x)) for x in res]
    return tuple(sorted(res))

def defdict(t):
    """ one liner for it all """
    d = defaultdict(list)
    for a in [ ("".join(sorted(w)), w) for w in t.split()]:
        d[a[0]].append(a[1])
    return d.values()

def main(args):
    pprint (trovu (text))
    pprint (defdict (text))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


# ~ (('123', '231'),
 # ~ ('litu', 'tuli', 'util'),
 # ~ ('tethic', 'thetic'),
 # ~ ('вино', 'овин'),
 # ~ ('удача', 'учада'))

