#!/usr/bin/env python3

import datetime

class Being:
    __specie = ""
    __firstName = ""
    __lastName = ""
    __birthDate = ""
    __birthPlace = ""
    __deathDate = None
    __deathPlace = None

    def __init__(self,
            specie,
            firstName,
            lastName,
            birthDate,
            birthPlace,
            deathDate,
            deathPlace,
            notes):
        self.__specie = specie
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthDate = birthDate
        self.__birthPlace = birthPlace
        self.__deathDate = deathDate
        self.__deathPlace = deathPlace
        self.__notes = notes
    def get_type(self):
        return self.__class__.__name__
    def get_specie(self):
        return self.__specie
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_name(self):
        return self.__firstName, self.__lastName
    def get_birthDate(self):
        return self.__birthDate
    def get_birthPlace(self):
        return self.__birthPlace
    def get_deathDate(self):
        return self.__deathDate
    def get_deathPlace(self):
        return self.__deathPlace
    def get_notes(self):
        return self.__notes
    def get_info(self):
        return "{} {} is a {} {}. \nBorn in {} on {}.".format(self.__firstName,
                                                    self.__lastName,
                                                    self.__specie,
                                                    self.__class__.__name__,
                                                    self.__birthDate,
                                                    self.__birthPlace)
        if len(birthDate) != 0:
            return "Died in {} on {}.".format(self.__birthDate,
                                            self.__birthPlace)
        else:
            return "Is still alive."
        if notes != None:
            return "Notes\: \n{}".format(self.__notes)
        else:
            return "Not much more about."
    def set_specie(self,specie):
        self.__specie = specie
    def set_firstName(self,firstName):
        self.__firstName = firstName
    def set_lastName(self,lastName):
        self.__lastName = lastName
    def set_birthDate(self,birthDate):
        self.__birthDate = birthDate
    def set_birthPlace(self,birthPlace):
        self.__birthPlace = birthPlace
    def set_deathDate(self,deathDate):
        self.__deathDate = deathDate
    def set_deathPlace(self,deathPlace):
        self.__deathPlace = deathPlace
    def set_notes(self,notes):
        self.__notes = notes

johndoe = Being(
    "human", 
    "John", 
    "Doe", 
    "Jan 1st 2000", 
    "Nowhere", 
    "", "", "He is a nice guy.")
print(johndoe.get_info())

janedoe = Being(
    "human",
    "Jane",
    "Doe", 
    "Feb 3rd 2001",
    "Neverwhere",
    "Dec 31th 2020",
    "Abys", 
    "She was a nice girl.")

print(janedoe.get_info())

print(johndoe.get_deathDate())



# class Being(Human):
#     def __init__(self,name,birthDate,birthPlace):
#         self.name = name
#         self.birthDate = birthDate
#         self.birthPlace = birthPlace
#     def getType(self):
#         return self.__class__.__name__
#     def intro(self):
#         print("Hello, my name is " + self.name + ".")
#         print("I was born on " + self.birthDate + " in " + self.birthPlace + ".\n")
#     def say(self, phrase):
#         print(phrase + ".\n")
        
# class Work:
#     def __init__(self,name,description):
#         self.name = name
#         self.description = description

# earth = Planet("earth", "solar system", "3" + "\n")
# earth.intro()

# johndoe = Human("John Doe", "13th of October 1982", "Neverwhere")
# johndoe.intro()
# johndoe.say("One one two... mic check.")

# print(johndoe.name)
# print(johndoe.birthDate)
# print(johndoe.birthPlace)

# print(johndoe.getType())

#print(dir(johndoe))

# def __repr__(self):
#     return self.name

