import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
  top_of_range = int(top_of_range)

  if top_of_range <=0:
    print("Please type number more than 0")
    quit()
else:
  print("Enter a digit")
  quit()

random_number = random.randrange(top_of_range)
guesses = 0

while True:
  guesses += 1
  user_guess = input("make a guess: ")
  if user_guess.isdigit():
    user_guess = int(user_guess)

  else:
      print("Please enter a number")
      continue

  if user_guess == random_number:
      print("Right")
      break
  elif user_guess > random_number:
        print("Above number")
  else:
        print("Below number")

print("You got", guesses, "Guesses")

print(random_number)
