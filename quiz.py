print("Welcome to my computer quiz.")

playing = input("Do yu want to play? Yes or No: ")

if playing.lower() != "yes":
  
  quit()

print("Okay Let's play:) ")

score = 0
  
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")

  
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")


answer = input("What does ROM stand for? ")
if answer == "read only memory":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")


answer = input("What does AI stand for? ")
if answer.lower() == "artificial intelligence":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")


answer = input("What does ML stand for? ")
if answer.lower() == "machine learning":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")


answer = input("What does VR stand for? ")
if answer == "virtual reality":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")


answer = input("What does AR stand for? ")
if answer.lower() == "augmented reality":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")


answer = input("What does DP stand for? ")
if answer.lower() == "desktop":
  print("Correct!")
  score += 1

else :
  print("Incorrect!")

print("You got " + str(score) + " Questions correct!")

print("You got " + str((score/4)*100) + " Questions correct!")
