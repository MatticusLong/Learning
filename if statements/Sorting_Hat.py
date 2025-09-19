# The Sorting hat
# Fun little game with some questions to determine which Hogwarts house you will join
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
#Variable for each question stores the questions answers from user input
#Q1 has only 2 questions.
Q1 = int(input("Do you like Dawn or Dusk?\n1) Dawn \n2) Dusk\n")) #When printing to go to a new line use \n
if Q1 >= 2:
  Hufflepuff += 1           #When adding to a variable += is the same as Var = value + value
  Slytherin += 1
else:
  Gryffindor += 1
  Ravenclaw += 1

Q2 = int(input("When I'm dead, I want people to remember me as:\n1) The Good \n2) The Great\n3) The Wise\n4) The Bold\n"))
if Q2 == 1:
  Hufflepuff += 2
elif Q2 == 2:
  Slytherin += 2
elif Q2 == 3:
  Ravenclaw += 2
else:
  Gryffindor += 2

Q3 = int(input("Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The Piano\n4) The drum\n"))
if Q3 == 1:
  Slytherin += 4
elif Q3 == 2:
  Hufflepuff += 4
elif Q3 == 3:
  Ravenclaw += 4
else:
  Gryffindor +=4

print(f"Gryffindor: {Gryffindor} \nRavenclaw: {Ravenclaw} \nHufflepuff: {Hufflepuff} \nSlytherin: {Slytherin}")