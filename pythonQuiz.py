#Python Quiz Game

questions = ("How many elements are in the periodic table? ",
             "Which animal lays the largest eggs? ",
             "What is the most abundnt gas in the Earth's atmosphere? ",
             "How many bones are in the human body? ",
             "Which planet in the solar system is the hottest? ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. CO2", "D. Hydrogen"), 
           ("A. 206", "B. 205", "C. 208", "D. 204"), 
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

score = 0
question_num = 0
guesses = []

for question in questions:
  print('-----------------------------------------------------')
  print(question)
  for option in options[question_num]:
    print(option)
    
  guess = input("Enter your answer (A, B, C, D): ").upper()    
  guesses.append(guess)
  
  if guess == answers[question_num]:
    print("Correct")
    score += 1
  else:
    print("Incorrect")
  
  question_num += 1
  
print('''-----------------------------
        Your Results: 
-----------------------------''')

print("Answers: ")

for a in answers: 
  print(a, end = " ")
print()

print("Your Guesses: ")

for g in guesses:
  print(g, end = " ") 
print()

print()
score = int(score /(len(questions)) * 100)
print(f"Your score is {score}%")