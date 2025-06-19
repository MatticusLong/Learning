# pokedex.py
# This file defines the Pokedex class and its methods for managing Pokemon data.
#class Pokedex:
# This class represents a Pokedex that contains information about various Pokemon.
class Pokedex:
    def __init__(self, entry, name, types, description, is_caught, height, weight):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        self.height = height
        self.weight = weight
       # # Initialize the Pokedex with the given attributes
    def display_details(self):
        print(f"Entry: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Types: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        print(f"Height: {self.height} m")
        print(f"Weight: {self.weight} kg")
    # Display the details of the Pokemon in the Pokedex
    #define a method to speak the name of the Pokemon
    # This method prints the name of the Pokemon twice, simulating a Pokemon sound
    def speak(self):
        print(f"{self.name}!, {self.name}!")
#create instances of Pokedex for different Pokemon
# Example Pokemon entries
Blastoise = Pokedex(9, "Blastoise", ["Water"], "The Shellfish Pokémon.", True, 1.6, 85.5)

Pikachu = Pokedex(25, "Pikachu", ["Electric"], "The Mouse Pokémon.", False, 0.4, 6.0)
# Example usage of the Pokedex class

Blastoise.speak()
Blastoise.display_details()

Pikachu.speak()
Pikachu.display_details()