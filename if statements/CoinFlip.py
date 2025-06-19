# Coin Flip Simulation 
# This program simulates a coin flip by generating a random number
# that is either 0 or 1. If the number is 0, it prints "Tails"; if it's 1, it prints "Heads".
import random
num = random.randint(0, 1) # generates a number thats either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')
