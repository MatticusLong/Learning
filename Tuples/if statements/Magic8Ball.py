
import random


question = input('Question:     ')
random_number = random.randint(1, 9)


if random_number == 9:
  print(question)
  print('Yes - definitely')
elif random_number == 8:
  print(question)
  print('It is decidedly so.')
elif random_number == 7:
  print(question)
  print('Without a doubt')
elif random_number == 6:
  print(question)
  print('Reply hazy, try again.')
elif random_number == 5:
  print(question)
  print('Ask again later')
elif random_number == 4:
  print(question)
  print('Better not tell you now')
elif random_number == 3:
  print(question)
  print('My sources say no.')
elif random_number == 2:
  print(question)
  print('Outlook not so good.')
else:
  print(question)
  print('Very doubtful')