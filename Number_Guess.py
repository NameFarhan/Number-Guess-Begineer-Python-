
# Number guessing game :-


import random

storednum = random.randint(1,100)

guesses = 1
attempts = guesses
print("Number guessing game --:--\n")

askguess = int(input("Enter Your guess :"))

while askguess != storednum:
   
    if askguess > storednum:
        print("Guess high!")

    elif askguess < storednum:
        print("Guess low!")

    askguess = int(input("Enter guess again: "))
    guesses += 1
    attempts -= 1
    if guesses == 10:
        print("Game Over! Attempts Finished")
        break
    elif guesses == 7:
        print("3 attempts remaining!")



else:
  print("You won the game !!") 
  print("Number of guesses are :", guesses) 

