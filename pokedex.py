# pokedex.py
# This file defines the Pokedex class and its methods for managing Pokemon data.

class Pokedex:
    def __init__(self, entry, name, types, description, height, weight):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.height = height
        self.weight = weight

        def speak(self):
            print(f"{self.name} says: Hello, I am {self.name}!")
