#simple program to demonstrate tuples in python
#tuples are immutable, meaning they cannot be changed after creation
#tuples are defined with or without parentheses and their items can be a mix of any data type. They can have one or more items.
#tuples can contain mixed data types


#tuples to represent geographical coordinates (latitude, longitude) of various cities
#each tuple contains two float values representing the latitude and longitude of a city
nashville = (36.16, -86.77,)
new_york = 40.71, -74.00
houston = (29.76, -95.37)
san_francisco = 37.77, -122.42
miami = (25.76, -80.19)
chicago = 41.88, -87.63
seattle = 47.61, -122.33
boston = (42.36, -71.06)
atlanta = 33.75, -84.39
denver = 39.74, -104.99
washington_dc = (38.90, -77.04)
los_angeles = 34.05, -118.24

#list of city tuples
cities = [nashville, new_york, houston, san_francisco, miami, chicago, seattle, boston, atlanta, denver, washington_dc, los_angeles]
city_names = ["Nashville", "New York", "Houston", "San Francisco", "Miami", "Chicago", "Seattle", "Boston", "Atlanta", "Denver", "Washington D.C.", "Los Angeles"]
#printing city names with their indexes
for index, city in enumerate(cities):
    print(f"{index}: {city_names[index]} - Coordinates: {city}")
#accessing tuple elements using indexing
nashville_latitude = nashville[0]
nashville_longitude = nashville[1]
print(f"Nashville Latitude: {nashville_latitude}, Longitude: {nashville_longitude}")

#unpacking tuples into individual variables
lat, lon = new_york
print(f"New York Latitude: {lat}, Longitude: {lon}")

#iterating through the list of city tuples and printing their coordinates
for city, name in zip(cities, city_names):
    print(f"{name} is located at Latitude: {city[0]}, Longitude: {city[1]}")

#Find the distance between two cities using their coordinates from the tuples defined (Haversine formula)
import math
from typing import Tuple, Optional


def haversine(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """Return distance between two (lat, lon) pairs in kilometers using the Haversine formula."""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    # convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, (lat1, lon1, lat2, lon2))
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371.0  # Earth radius in kilometers
    return c * r


def find_city_index(query: str) -> Optional[int]:
    """Find a city index by name (case-insensitive) or numeric index string. Returns None if not found."""
    query_stripped = query.strip()
    # try numeric index
    if query_stripped.isdigit():
        idx = int(query_stripped)
        if 0 <= idx < len(cities):
            return idx
        return None
    # try name match (case-insensitive, allow partial match)
    q = query_stripped.lower()
    # exact match first
    for i, name in enumerate(city_names):
        if q == name.lower():
            return i
    # partial match
    matches = [i for i, name in enumerate(city_names) if q in name.lower()]
    if len(matches) == 1:
        return matches[0]
    return None


def prompt_for_city(prompt: str) -> int:
    """Prompt the user until they supply a valid city index or name. Returns the index."""
    while True:
        user = input(prompt)
        idx = find_city_index(user)
        if idx is not None:
            return idx
        print("City not found. Enter a valid numeric index or city name (e.g. '0' or 'New York').")


def print_city_list():
    print("Available cities:")
    for index, name in enumerate(city_names):
        print(f"{index}: {name}")


def run_interactive():
    print("-- City Distance Finder --")
    print_city_list()
    i1 = prompt_for_city("Enter the first city (index or name): ")
    i2 = prompt_for_city("Enter the second city (index or name): ")
    coord1 = cities[i1]
    coord2 = cities[i2]
    km = haversine(coord1, coord2)
    miles = km * 0.621371
    print(f"\nDistance between {city_names[i1]} and {city_names[i2]}:")
    print(f"{km:.2f} km ({miles:.2f} miles)")


if __name__ == '__main__':
    run_interactive()
