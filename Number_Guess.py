
# Number guessing game :-


import random

storednum = random.randint(1,100)

print("Number guessing game --:--\n")

askguess = int(input("Enter Your guess :"))

while storednum != askguess:
   
    if askguess > storednum:
        print("Guess high!")

    elif askguess < storednum:
        print("Guess low!")

    askguess = int(input("Enter guess again: "))

else:
  print("You guessed correct and won the game !") 