# number guessing game 

import random 

correct = random.randint(1, 100)
guesses = 0

while True:
  guess = int(input("Guess a number between 1 and 100: "))
  guesses += 1

  if guess < correct:
    print(f"{guess} too low!")
  elif guess > correct: 
    print(f"{guess} too high!")
  elif not guess.isdigit():
    print("invalid guess, please enter numbers only")
  else:
    print("Correct!")
    break 
  
     
print(f"You guesses it in {guesses} guesses!")