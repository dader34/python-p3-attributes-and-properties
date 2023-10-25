#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name="Guido",breed="Mastiff"):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
        if(type(name) == str and len(name) > 0 and len(name) < 26):
            self.name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
        if breed in approved_breeds:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

