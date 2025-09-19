# FizzBuzz program
# This program prints the numbers from 1 to 100.
# For multiples of three, it prints "Fizz" instead of the number.
# For multiples of five, it prints "Buzz" instead of the number.
# For numbers which are multiples of both three and five, it prints "FizzBuzz".
# This is a classic programming challenge often used to teach basic control flow.
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)