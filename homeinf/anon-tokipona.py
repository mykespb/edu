#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-03-28 2025-05-21 1.2
# anon-tokipona.py

# ~ Выполнить анонимизацию текста на языке токипона.

text = """
tawa anpa nasa.
lon o, sina tawa wawa weka. tenpo ali la mi lon tenpo suno ali
sama ni: jan Kata tawa lon sitelen lape suli. wile mi li lawa e mi.
jan Sonja kama jo ala e tawa jan Misa.
jan Misa pilin e ni: ali li lon lawa mi.
jan Kola alasa kama lukin e lon nasin jan Misa.
taso sitelen nasin li kama ike. sitelen sona li ike kin.
tan ni la jan Kola kama e ni: mi kepeken lawa pi sama taso
monsuta lape li lawa e jan Sonja tawa insa pi pimeja ali.
"""

# ~ “Going down to craziness.”
# ~ Existence, you run away. Always, I live every day
# ~ as if I move in a big dream. My desires lead me.
# ~ I don’t get my goals.
# ~ I think that it is all in my head.
# ~ I try to find my regular place.
# ~ But the road map is bad and the signs are bad too.
# ~ So I bring it about that I use my own rules.
# ~ A nightmare leads me into total darkness.


def prepare(txt):
    """приготовить текст"""

    for sep in ".,!@&%$()-_+={}[]|;:":
        txt = txt.replace(sep, ' ' + sep)

    ltxt = txt.strip().split()

    # ~ print(ltxt)
    return ltxt


def anon(txt):
    """анонимизировать!"""

    anol = {}
    state = 0
    num = 0
    atxt = []

    for w in txt:
        if state:
            if w in anol:
                atxt.append(str(anol[w]))
            else:
                num += 1
                anol[w] = num
                atxt.append(str(num))
            state = 0
        else:
            atxt.append(w)
            if w == "jan":
                state = 1

    # ~ print(anol)
    # ~ print(atxt)
    return atxt


def postproc(txt):
    """приготовить к печати"""

    otxt = " ".join(txt)

    for sep in ".,!@&%$()-_+={}[]|;:":
        otxt = otxt.replace(' ' + sep, sep)

    otxt = otxt.replace('. ', '.\n')

    return otxt


def main():
    """запуск"""
    print(text)
    ltxt = prepare(text)
    # ~ print(ltxt)
    etxt = anon(ltxt)
    # ~ print(etxt)
    otxt = postproc(etxt)
    print(otxt)


main()

