#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-26 2022-02-26 1.1
# word-fl.py

# ~ найти в тексте все слова, которые начинаются и заканчиваются
# ~ на одинаковые буквы (напр., alfa)

s = """Olivia Ava Amelia Emily Jessica Isla Isabella Poppy Mia Sophie Lily Ruby Evie Grace Ella Sophia Chloe Scarlett Freya Isabelle Phoebe Alice Ellie Bethany Maryam Heidi Paige Faith Rose Ivy Florence Hurriet Maddison Zoe Samuel Jack Joseph Harry Alfie Jacob Thomas Charlie Oscar James William Joshua George Ethan Noah Archie Henry Leo John Oliver David Ryan Dexter Connor Albert Austin Stanley Theodore Owen Caleb"""

for word in s.split():
    if word[0].lower() == word[-1]:
        print(word, end=', ')

# ~ Ava, Amelia, Evie, Ellie, Maryam, David, 
