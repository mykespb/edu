#! /usr/bin/env python3
# testing requests library
# python3, requests (virtualenv)
# myke 2019-01-24 1.1

import requests
import re

urls = """
http://www.myke.spb.ru
https://www.youtube.com
https://www.youtube.com/watch?v=O4zlCn-rwJM
https://www.youtube.com/watch?v=Fne7Quz3oGs
""".split()

def main():

    for url in urls:
        if not url: continue

        print (f"URL   = {url}")

        try:
            r = requests.get(url)
            m = re.search('<title>([^<]+)</title>', r.text)
            print (f"Title = {m.group(1)}")
        except:
            print("no good answer")
        finally:
            print ("step done.\n")

    print ("all done.\n")

main()

# ~ URL   = http://www.myke.spb.ru
# ~ Title = Main webpage of Myke
# ~ step done.

# ~ URL   = https://www.youtube.com
# ~ Title = YouTube
# ~ step done.

# ~ URL   = https://www.youtube.com/watch?v=O4zlCn-rwJM
# ~ Title = Cirrus Owner: Ken Griffey, Jr. - YouTube
# ~ step done.

# ~ URL   = https://www.youtube.com/watch?v=Fne7Quz3oGs
# ~ Title = Как стать программистом? Настройка тестирования Pytest Стрим за 9 минут - YouTube
# ~ step done.

# ~ all done.
