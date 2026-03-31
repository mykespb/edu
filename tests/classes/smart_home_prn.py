#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / smart_home_prn.py
# 2026-03-31 2026-03-31 2.0
# Работа с умным загородным домом

class SmartHome: 

    counter = 0

    def __init__(self):
        SmartHome.counter += 1
        self.number = SmartHome.counter
        self.name = f"Smart Home #{self.number}"
        self.starter = []
        self.all_apls = []
        self.state = False

    def on(self):
        self.state = True
        for tool in self.starter:
            tool.on()

    def off(self):
        self.state = False
        for tool in self.all_apls:
            tool.off()

    def live(self, period=1):
        for day in range(period):
            print(f"living day {day+1}")

    def __str__(self):
        return f"{self.name} is {self.state}"

class ELamp:

    counter = 0

    def __init__(self):
        ELamp.counter += 1
        self.number = ELamp.counter
        self.name = f"ELamp #{self.number}"
        self.state = False

    def on(self):
        if self.ensureSmallCurrent():
            self.state = True

    def off(self): 
        self.state = False

    def __str__(self):
        return f"{self.name} is {self.state}"

    def ensureSmallCurrent(self):
        return True

class Boiler:

    counter = 0

    def __init__(self, volume = 10):
        Boiler.counter += 1
        self.number = Boiler.counter
        self.volume = volume if volume >= 10 else 10
        self.name = f"Boiler #{self.number} of {volume}L"
        self.state = False

    def on(self):
        if self.ensureWater():
            self.state = True

    def off(self): 
        self.state = False
        self.ensureNoWater()

    def __str__(self):
        return f"{self.name} is {self.state}"

    def ensureWater(self):
        return True

    def ensureNoWater(self):
        return True

class WarmFloor: 

    counter = 0

    def __init__(self, name = "A Warm Floor"):
        WarmFloor.counter += 1
        self.number = WarmFloor.counter
        self.name = f"Warm Floor #{self.number}"
        self.state = False

    def on(self):
        if self.ensureBigCurrent():
            self.state = True

    def off(self): 
        self.state = False
        self.ensureNoBigCurrent()

    def __str__(self):
        return f"{self.name} is {self.state}"

    def ensureBigCurrent(self):
        return True

    def ensureNoBigCurrent(self):
        return True

# my home setup

myHome = SmartHome()
print(myHome)

lampEnter = ELamp()
lampRoom = ELamp()
lampCabinet = ELamp()
lampCorridor = ELamp()

lamps = lampEnter, lampCabinet, lampRoom, lampCorridor
for lamp in lamps:
    print(lamp)

smallBoiler = Boiler(10)
bigBoiler = Boiler(100)

boilers = smallBoiler, bigBoiler
for boiler in boilers:
    print(boiler)

corridorFloor = WarmFloor()
roomFloor = WarmFloor()
cabinetFloor = WarmFloor()

floors = corridorFloor, roomFloor, cabinetFloor
for floor in floors:
    print(floor)

myHome.starter = [ lampEnter, lampCorridor, smallBoiler, corridorFloor ]

print(myHome)
for lamp in lamps:
    print(lamp)
for boiler in boilers:
    print(boiler)
for floor in floors:
    print(floor)

myHome.all_apls = ( myHome.starter[:] +
    [ roomFloor, lampRoom, cabinetFloor, bigBoiler, lampCabinet ] )

# my home usage

print("\n********** Starting my Smart Home **********\n")

myHome.on()

print(myHome)
for lamp in lamps:
    print(lamp)
for boiler in boilers:
    print(boiler)
for floor in floors:
    print(floor)

print("\n********** Living in my Smart Home **********\n")

myHome.live(3)

print("\n********** Closing my Smart Home **********\n")

myHome.off()

print(myHome)
for lamp in lamps:
    print(lamp)
for boiler in boilers:
    print(boiler)
for floor in floors:
    print(floor)

print("\n********** Smart Home done. Good-bye! **********\n")


# all done.
