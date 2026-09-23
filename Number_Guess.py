
# Number guessing game :-


import random

storednum = random.randint(1,100)

guesses = 1
attempts = 10
print("Number guessing game --:--\n")
print(storednum)

askguess = int(input("Enter Your guess :"))

while askguess != storednum:

    if askguess > 100 or askguess < 0:
        print("Please enter the number between 0 and 100")
        attempts += 1
        guesses -= 1

    elif askguess > storednum:
        print("Guess high!")

    elif askguess < storednum:
        print("Guess low!")

    attempts -= 1
    guesses += 1
    print("remaining attempts are: ", attempts)
    askguess = int(input("Enter guess again: "))
    if guesses == 10:
        print("Game Over! Attempts Finished")
        print("The secret number is:" ,storednum)
        break



else:
  print("You won the game !!") 
  print("Number of guesses are :", guesses) 

