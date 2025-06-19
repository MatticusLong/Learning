#Learning Python: Classes and Objects
# This code demonstrates how to create a class in Python and instantiate objects from that class.
# Define a class named Restaurant
class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

# Create an object of the Restaurant class for bob's burgers
bob_burgers = Restaurant()
bob_burgers.name = "Bob\'s Burgers"
bob_burgers.category = 'American Diner'
bob_burgers.rating = 4.7
bob_burgers.delivery = False
# Print the details of bob's burgers
print(vars(bob_burgers))

#create an object of the Restaurant class for a different restaurant
Taco_Town = Restaurant()
Taco_Town.name = "Taco Town"
Taco_Town.category = 'Mexican'
Taco_Town.rating = 4.5
Taco_Town.delivery = True
# Print the details of Taco Town
print(vars(Taco_Town))

# Create an object of the Restaurant class for another restaurant
Pizza_Palace = Restaurant()
Pizza_Palace.name = "Pizza Palace"
Pizza_Palace.category = 'Italian'
Pizza_Palace.rating = 4.8
Pizza_Palace.delivery = True
# Print the details of Pizza Palace
print(vars(Pizza_Palace))