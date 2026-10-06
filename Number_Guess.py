# Number guessing game :-


import random

print("Easy")
print("Medium")
print("Hard")

difficulty_valid = True
while difficulty_valid == True:
    difficulty = input("Enter the diffculty :-").lower()
    if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
        difficulty_valid = False
    else:
        print("Please enter from the above !")
        continue


def my_function(difficulty):

    if difficulty == "easy":
        max_num = 50

    elif difficulty == "medium":
        max_num = 100

    elif difficulty == "hard":
        max_num = 500

    storednum = random.randint(1, max_num)
    print(storednum)
    print("Number guessing game --:--\n")

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
                    continue
                elif askguess < 1:
                    print("sorry number lesser than 1")
                    continue
                valid = True
            elif difficulty == "medium":
                if askguess > 100:
                    print(f"Sorry number above {max_num}")
                    continue
                elif askguess < 1:
                    print("sorry number lesser than 1")
                    continue
                valid = True
            elif difficulty == "hard":
                if askguess > 500:
                    print(f"Sorry number above {max_num}")
                    continue
                elif askguess < 1:
                    print("sorry number lesser than 1")
                    continue
                valid = True
        except ValueError:
            print("Please enter a valid number!")
            valid = False
    while askguess != storednum:

        if askguess > storednum:
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
                        continue
                    elif askguess < 1:
                        print("sorry num lesser than 1")
                        continue
                    insidevalid = True
                elif difficulty == "medium":
                    if askguess > 100:
                        print(f"Sorry number above {max_num}")
                        continue
                    elif askguess < 1:
                        print("sorry num lesser than 1")
                        continue
                    insidevalid = True
                elif difficulty == "hard":
                    if askguess > 500:
                        print(f"Sorry number above {max_num}")
                        continue
                    elif askguess < 1:
                        print("sorry num lesser than 1")
                        continue
                    insidevalid = True
            except ValueError:
                print("Please enter a valid number!")
                insidevalid = False
                print("remaining attempts are: ", attempts)

        if attempts == 1:
            print("Game Over! Attempts Finished")
            print("The secret number is:", storednum)
            break
        elif attempts < 6:
            if difficulty == "easy":
                if storednum > 0 and storednum < 10:
                    print("The number is between 0 and 10 !!")
                elif storednum > 10 and storednum < 20:
                    print("The number is between 10 and 20 !!")
                elif storednum > 20 and storednum < 30:
                    print("The number is between 20 and 30 !!")
                elif storednum > 30 and storednum < 40:
                    print("The number is between 30 and 40 !!")
                elif storednum > 40 and storednum < 50:
                    print("The number is between 40 and 50 !!")

                if askguess < 0 or askguess > 10:
                    print("You are going out of the range !!")
                elif askguess < 10 or askguess > 20:
                        print("You are going out of the range !!")
                elif askguess < 20 or askguess > 30:
                    print("You are going out of the range !!")
                elif askguess < 30 or askguess > 40:
                    print("You are going out of the range !!")
                elif askguess < 40 or askguess > 50:    
                    print("You are going out of the range !!")

    else:
        print("You won the game !!")
        print("Number of guesses are :", guesses)


my_function(difficulty=difficulty)
