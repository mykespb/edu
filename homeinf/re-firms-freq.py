#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-28 2026-06-11 1.4
# re-firms-freq.py

# гистограмма отчёта о компаниях

text = """
For decades, the tech industry has seen a massive shift in dominance, with IBM and Microsoft laying the foundations of the computing era. In the 1980s and 1990s, IBM ruled corporate hardware, while Microsoft captured the software market with Windows. During this time, Apple struggled to find its footing, and Google did not even exist. As Microsoft grew into a monopoly, IBM slowly began shifting its focus away from personal computers toward enterprise services.
The 2000s completely rewritten the scoreboard. Google burst onto the scene, quickly dominating internet search and challenging Yahoo and Microsoft. Meanwhile, Apple launched the iPhone, kicking off a mobile revolution that caught Microsoft off guard. At the same time, Amazon quietly evolved from an online bookstore into an e-commerce giant, while also laying the groundwork for AWS cloud computing. By 2010, Apple and Google were the new kings of tech, while IBM faded from the consumer spotlight.
The 2010s marked the rise of data and social media, establishing the "GAFAM" era: Google, Apple, Facebook (now Meta), Amazon, and Microsoft. During this decade, Microsoft staged a massive comeback through cloud computing, directly fighting Amazon for enterprise dominance. While Apple raked in massive hardware profits, Google and Meta locked down the global digital advertising market.
By the 2020s, a new technological shift arrived: Artificial Intelligence. This era pushed Nvidia into the spotlight. While Microsoft, Google, and Amazon spent billions buying chips to power AI, Nvidia became the most critical company in the world. Microsoft took an early lead by partnering with OpenAI, forcing Google to rapidly reinvent its search business. Meta open-sourced its own AI models to compete, while Apple carefully integrated AI into its massive device ecosystem.
Looking at the overall timeline, the frequency of success has constantly shifted. Microsoft has shown the most incredible staying power, remaining a top player for over forty years. Apple transformed from a nearly bankrupt underdog into the world's most valuable brand. Google and Amazon reshaped daily human life, while Nvidia quietly built the engine that will power the future.
"""

firms = "Yandex Microsoft Google Apple Amazon IBM Meta Nvidia"

# построить гистограмму часто упоминаний этих компаний в отчёте,
# линии - горизонтально,
# компании - в алфавитном порядке.

firms = sorted(firms.split())
print(f"\ncompanies: {firms}\n")

freqs = { name: text.count(name) for name in firms }
# ~ print(freqs)

kmax = max( [ len(x) for x in freqs.keys() ] )
vmax = max( freqs.values() )

mult = 50

for firm in firms:
    print( f"{firm:{kmax+1}}:", "*" * int(freqs[firm] * mult // vmax) )
print()
