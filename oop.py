#!/usr/bin/env python3

import datetime

class Being:
    __specie = ""
    __gender = ""
    __firstName = ""
    __lastName = ""
    __birthDate = ""
    __birthPlace = ""

    def __init__(self,
            specie,
            gender,
            firstName,
            lastName,
            birthDate,
            birthPlace,
            deathDate,
            deathPlace,
            notes):
        self.__specie = specie
        self.__gender = gender
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
    def get_gender(self):
        return self.__gender
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
        return "{} {} is a {} {}. \n{} was born in {} in {}.".format(
            self.__firstName, 
            self.__lastName, 
            self.__specie, 
            self.__class__.__name__, 
            "He" if self.__gender == "male" else "She", 
            self.__birthDate, 
            self.__birthPlace), " Died on {} in {}.".format(
                self.__deathDate, 
                self.__deathPlace) if self.__deathDate != "" else "", "\n{}".format(self.__notes) if self.__notes != "" else ""

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
    "male", 
    "John", 
    "Doe", 
    "Jan 1st 2000", 
    "Nowhere", 
    "", 
    "", 
    "He is a nice guy.")

print(''.join(johndoe.get_info()))

janedoe = Being(
    "human",
    "female",
    "Jane",
    "Doe", 
    "Feb 3rd 2001",
    "Neverwhere",
    "Dec 31th 2020",
    "Abys", 
    "She was a nice girl.")

print(''.join(janedoe.get_info()))
