# simple fortune cookie app
#import the random module to select a fortune at random
import random

def read_fortune():
  # This function simulates cracking open a fortune cookie and reading the fortune inside.
  # It randomly selects a fortune from a predefined list of fortunes and prints it out.
  fortunes = ["Don't pursue happiness – create it", 
  "All things are difficult before they are easy.", 
  "The early bird gets the worm, but the second mouse gets the cheese.", 
  "Someone in your life needs a letter from you.", 
  "Don't just think. Act!", 
  "Your heart will skip a beat.", 
  "The fortune you search for is in another cookie.", 
  "Help! I'm being held prisoner in a Chinese bakery!"
  ]
  # Select a random fortune from the list
  random_fortune = random.choice(fortunes)
    # Print the fortune
  print("You crack open the fortune cookie and the fortune inside reads...")
    # Print the selected fortune
  print(random_fortune)

read_fortune()