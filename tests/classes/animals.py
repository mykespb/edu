#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / smart-home.py
# 2026-04-06 2026-04-06 1.5
# Как разговаривают животные

class Animal:
    def say(self):
        print("Вау!")

am = Animal()
am.say()

class Dog(Animal):
    def say(self):
        print("Гав!")

fido = Dog()
fido.say()

class Cat(Animal):
    def say(self):
        print("Мяу!")
    
pussy = Cat()
pussy.say()

class Human(Animal):
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

we = am, fido, pussy, човек, somepres, trump

print("choice:")
beast = choice(we)
beast.say()

print("all:")
for ani in we:
    ani.say()
