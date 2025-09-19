#solar system program to pull a random planet from a list of planets and find the area of the planet
from random import choice as ch
from math import pi
#list of planets
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

def random_planet():
    """Returns a random planet from the list."""
    return ch(planets)

def get_radius(planet):
    """Returns the radius of the given planet in km."""
    if planet == 'Mercury':
        r = 2440  # radius in km
    elif planet == 'Venus':
        r = 6052
    elif planet == 'Earth':
        r = 6371
    elif planet == 'Mars':
        r = 3390
    elif planet == 'Saturn':
        r = 58232
    else:
        print("An error occurred. Please try again.")
        r = 0
    return r

def calculate_surface_area(radius):
    """Calculates the surface area of a sphere given its radius."""
    return 4 * pi * (radius ** 2)

print("Welcome to the Solar System Program!")
planet = random_planet()
print(f"Randomly selected planet: {planet}")
r = get_radius(planet)

if r > 0:
    area = calculate_surface_area(r)  # Calculate the surface area using a = 4 * π * r²
    print(f"The surface area of {planet} is approximately {area:.2f} km².")
else:
    print("Could not calculate area due to invalid radius.")