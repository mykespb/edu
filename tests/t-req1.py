#! /usr/bin/env python
# testing requests library
# python3, requests (virtualenv)
# myke 2019-01-24

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
