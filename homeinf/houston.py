#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-19 2025-01-24 1.1
# ~ houston.py

# ~ Во время полёта космического корабля "Аполлон 13" (США) экипаж сообщил
# ~ в ЦУП (Центр Управления Полётами NASA) о неисправности фразой,
# ~ которая стала знаменитой (хотя и была потом в фильме произнесена неточно).
# ~ Как была указана неисправность и когда о ней сообщили впервые?"

# --------------------------------
# initial data

chat = """
055:55:19 Swigert: Okay, Houston ...
055:55:19 Lovell: ... Houston...
055:55:20 Swigert: ... we've had a problem here. [Pause.]
055:55:28 Lousma: This is Houston. Say again, please.
055:55:35 Lovell: [Garble.] Ah, Houston, we've had a problem. We've had a Main B Bus Undervolt.
"""

badwords = """
bad trouble problem crisis break shit devil badass gosh damage crash error
mistake malfunction explosion fire death terrible smash broken
"""

# --------------------------------
# start

class ex(Exception): pass


def main():
    """запуск"""

    events = []

    for line in chat.strip().splitlines():
        events.append( line.strip().split(" ", maxsplit = 1) )

    bwords = badwords.strip().split()

    try:
        for moment, message in events:
            lc_message = message.lower()
            for bw in bwords:
                if bw in lc_message:
                    print(f"в момент '{moment}' термин '{bw}' был в сообщении '{message}'")
                    raise ex
    except:
        pass
                

main()

# --------------------------------
# results

# ~ в момент '055:55:20' термин 'problem' был в сообщении 'Swigert: ... we've had a problem here. [Pause.]'

# --------------------------------

# ~ рус.: "Хьюстон, у нас проблемы..."
# ~ https://en.wikipedia.org/wiki/Houston,_we_have_a_problem
# ~ «Хьюстон, у нас проблема» часто ошибочно цитируют как фразу, произнесенную во время миссии «Аполлон-13», миссии НАСА в рамках космической программы «Аполлон» и третьей миссии, предназначенной для высадки на Луну
# ~ 55:54:20 (03:07 UTC on April 14, 1970)

# --------------------------------
