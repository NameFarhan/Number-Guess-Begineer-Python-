# Number guessing game :-


import random

print("Easy")
print("Medium")
print("Hard")

difficulty = str(input("Enter the diffculty :-")).lower()


def my_function(difficulty):

    if difficulty == "easy":
        max_num = 50

    elif difficulty == "medium":
        max_num = 100

    elif difficulty == "hard":
        max_num = 500

    storednum = random.randint(1, max_num)
    print("Number guessing game --:--\n")

    print(storednum)
    guesses = 1
    if difficulty == "easy":
        selective_attempts = 10

    elif difficulty == "medium":
        selective_attempts = 7

    elif difficulty == "hard":
        selective_attempts = 8
    attempts = selective_attempts
    valid = False

    while valid == False:
        try:
            askguess = int(input(f"Enter your guess between 1 to {max_num}: "))
            if difficulty == "easy":
                if askguess > 50:
                    print(f"Sorry number above {max_num}")
                elif askguess < 1:
                    print("sorry num lesser than 1")
            continue
            valid = True
        except ValueError:
            print("Please enter a valid number!")
            valid = False
    while askguess != storednum:

        if askguess > 100 or askguess < 0:
            print("Please enter the number between 0 and 100!")
            attempts += 1
            guesses -= 1

        elif askguess > storednum:
            print("Guess high!")

        elif askguess < storednum:
            print("Guess low!")

        attempts -= 1
        guesses += 1
        print("remaining attempts are: ", attempts)
        insidevalid = False

        while insidevalid == False:
            try:
                askguess = int(input(f"Enter your guess between 1 to {max_num}: "))
                if difficulty == "easy":
                    if askguess > 50:
                     print(f"Sorry number above {max_num}")
                    elif askguess < 1:
                     print("sorry num lesser than 1")
                continue
                insidevalid = True
            except ValueError:
                print("Please enter a valid number!")
                insidevalid = False
                print("remaining attempts are: ", attempts)

        if guesses == 10:
            print("Game Over! Attempts Finished")
            print("The secret number is:", storednum)
            break

    else:
        print("You won the game !!")
        print("Number of guesses are :", guesses)


my_function(difficulty=difficulty)
