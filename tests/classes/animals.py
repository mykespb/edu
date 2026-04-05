#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / smart-home.py
# 2026-04-06 2026-04-06 1.4
# Как разговаривают животные

class Animal:
    def say(self):
        print("Вау!")

am = Animal()
am.say()

class Dog():
    def say(self):
        print("Гав!")

fido = Dog()
fido.say()

class Cat:
    def say(self):
        print("Мяу!")
    
pussy = Cat()
pussy.say()

class Human:
    def say(self):
        print("Привет!")

човек = Human()
човек.say()

class President(Human):
    def __init__(self, name="просто президент"):
        self.name = name
        
    def say(self):
        print(f"Здравствуйте! Я {self.name}!")

somepres = President()
somepres.say()

trump = President("Наивеликий Супертрампище")
trump.say()

beast = fido
beast.say()

beast = pussy
beast.say()

from random import choice

beast = choice((am, fido, pussy, човек, somepres, trump))
beast.say()
