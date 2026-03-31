#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / smart-home.py
# 2026-03-31 2026-03-31 1.0
# Работа с умным загородным домом

class SmartHome: 

    def __init__(self):
        self.starter = []
        self.all_tools = []

    def on(self): 
        for tool in self.starter:
            tool.on()

    def off(self):
        for tool in self.all_tools:
            tool.off()

    def live(self, period): ...

class ELamp:

    def __init__(self):
        self.switch = False

    def on(self):
        self.ensureSmallCurrent()
        self.switch = True

    def off(self): 
        self.switch = False

    def ensureSmallCurrent(self): ...

class Boiler:

    def __init__(self, vol = 10):
        self.volume = vol

    def on(self):
        self.ensureWater()
        self.switch = True

    def off(self): 
        self.switch = False
        self.ensureNoWater()

    def ensureWater(self): ...
    def ensureNoWater(self): ...

class WarmFloor: 

    def __init__(self):
        self.switch = False

    def on(self):
        self.ensureBigCurrent()
        self.switch = True

    def off(self): 
        self.switch = False
        self.ensureNoBigCurrent()

    def ensureBigCurrent(self): ...
    def ensureNoBigCurrent(self): ...

myHome = SmartHome()

lampEnter = ELamp()
lampRoom = ELamp()
lampCabinet = ELamp()
lampCorridor = ELamp()

smallBoiler = Boiler(10)
bigBoiler = Boiler(100)

corridorFloor = WarmFloor()
roomFloor = WarmFloor()
cabinetFloor = WarmFloor()

myHome.starter = [ lampEnter, lampCorridor, smallBoiler, corridorFloor ]

myHome.alltools = ( myHome.starter[:] +
    [ roomFloor, lampRoom, cabinetFloor, bigBoiler, lampCabinet ] )

print("Starting my Smart Home")
myHome.on()
print("Living in my Smart Home")
myHome.live(2)
print("Closing my Smart Home")
myHome.off()
print("Smart Home done. Good-bye!")
