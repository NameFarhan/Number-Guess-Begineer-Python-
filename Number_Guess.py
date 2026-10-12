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
        if difficulty == "easy":
          cold_message = storednum - 20
          warm_message = storednum - 10
          hot_message = storednum - 5

          if askguess > cold_message or askguess < cold_message:
              print("you are cold !")
          elif askguess > warm_message or askguess < warm_message:
              print("you are warm !")
          elif askguess > hot_message or askguess < hot_message:
              print("you are hot !")    

        if askguess > storednum:
            print("Go Lower !")

        elif askguess < storednum:
            print("Go higher !")

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

    else:
        print("You won the game !!")
        print("Number of guesses are :", guesses)


my_function(difficulty=difficulty)
