
# Number guessing game :-


import random

storednum = random.randint(1,100)

guesses = 1

print("Number guessing game --:--\n")

askguess = int(input("Enter Your guess :"))

while storednum != askguess:
   
    if askguess > storednum:
        print("Guess high!")

    elif askguess < storednum:
        print("Guess low!")

    askguess = int(input("Enter guess again: "))
    guesses += 1

else:
  print("You won the game !!") 
  print("Number fo guesses are :", guesses) 

