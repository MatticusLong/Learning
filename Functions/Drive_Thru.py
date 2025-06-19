#Drive-thru
#define a funtion that takes a parameter for a menu item and returns the item
def get_item(number):
  if number == 1:
    print('🍔 Cheeseburger')
  elif number == 2:
    print('🍟 Fries')
  elif number == 3:
    print('🥤 Soda')
  elif number == 4:
    print('🍦 Ice Cream')
  elif number == 5:
    print('🍪 Cookie')
  else:
    print("Sorry, We dont have that on the menu")
# Define a function that welcomes the user and displays the menu
def welcome():
  print(f'Welcome to the Burger Shack!\nOur menu is as follows:\n #1 is a Cheeseburger\n#2 is an order of fries\n#3 Is a soda\n#4 Is an Ice Cream\n#5 Is a cookie')
  print('What would you like?')
  number = int(input())
  return(get_item(number))

welcome()
