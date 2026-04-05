#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / smart-home.py
# 2026-04-06 2026-04-06 1.1
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
    def say(self):
        print("Здравствуйте! Я наивеликий СуперТрампище!")

trump = President()
trump.say()
