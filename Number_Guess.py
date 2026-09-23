
# Number guessing game :-


import random

storednum = random.randint(1,100)

guesses = 1
attempts = 10
print("Number guessing game --:--\n")
print(storednum)

askguess = int(input("Enter Your guess :"))

while askguess != storednum:
   
    if askguess > storednum:
        print("Guess high!")

    elif askguess < storednum:
        print("Guess low!")

    attempts -= 1
    print("remaining attempts are: ", attempts)
    askguess = int(input("Enter guess again: "))
    guesses += 1
    if guesses == 10:
        print("Game Over! Attempts Finished")
        print("The secret number is:" ,storednum)
        break



else:
  print("You won the game !!") 
  print("Number of guesses are :", guesses) 

