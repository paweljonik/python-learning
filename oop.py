#!/usr/bin/env python

import datetime

class Planet:
    def __init__(self,name,locationGlobal,locationLocal):
        self.name = name
        self.locationGlobal = locationGlobal
        self.locationLocal = locationLocal
        #self.color = color
    def getName(self):
        return self.__class__.__name__
    def intro(self):
        print(self.name + " is " + self.locationLocal +  " planet in the " + self.locationGlobal + ".\n")

class Human:
    def __init__(self,name,birthDate,birthPlace):
        self.name = name
        self.birthDate = birthDate
        self.birthPlace = birthPlace
    def getType(self):
        return self.__class__.__name__
    def intro(self):
        print("Hello, my name is " + self.name + ".")
        print("I was born on " + self.birthDate + " in " + self.birthPlace + ".\n")
    def say(self, phrase):
        print(phrase + ".\n")
        
class Work:
    def __init__(self,name,description):
        self.name = name
        self.description = description

earth = Planet("earth", "solar system", "3" + "\n")
earth.intro()

johndoe = Human("John Doe", "13th of October 1982", "Neverwhere")
johndoe.intro()
johndoe.say("One one two... mic check.")

print(johndoe.name)
print(johndoe.birthDate)
print(johndoe.birthPlace)

print(johndoe.getType())

#print(dir(johndoe))

# def __repr__(self):
#     return self.name

