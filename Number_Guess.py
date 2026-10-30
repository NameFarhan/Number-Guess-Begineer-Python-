# Number guessing game :-


import random


game_loss = 0
game_wins = 0
games_played = 0

def my_function(game_loss,game_wins,games_played):

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
        if difficulty == "easy":
            max_num = 50

        elif difficulty == "medium":
            max_num = 100

        elif difficulty == "hard":
            max_num = 500

        storednum = random.randint(1, max_num)
        print(storednum)
        print("Number guessing game --:--\n")

        score = 1
        num1 = 1
        num2 = max_num
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
                selective_hot = 5
                selective_warm = 10
                selective_cold = 15
            elif difficulty == "medium":
                selective_hot = 10
                selective_warm = 15
                selective_cold = 25
            else:
                selective_hot = 15
                selective_warm = 25
                selective_cold = 50
            difference = abs(storednum - askguess)
            if difference <= selective_hot:
                print("you are hot !")
            elif difference <= selective_warm:
                print("you are warm !")
            elif difference <= selective_cold:
                print("you are cold !")

            if askguess > storednum:
                print("Go Lower !")
                num2 = askguess - 1
            else:
                print("Go higher !")
                num1 = askguess + 1

            print(f"Range is {num1} and {num2}")
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
                print("Your score is: ", score)
                print("The secret number is:", storednum)
                game_loss += 1
                games_played += 1
                def new_game():
                    new_game_valid = True
                    while new_game_valid == True:
                        ask_game = input("Want to play another game Y/N  ").lower()
                        if ask_game == "yes" or ask_game == "y":
                            my_function(game_loss,game_wins,games_played)
                            break
                        elif ask_game == "no" or ask_game == "n":
                            print("")
                            print("Thanks for playing the game !")
                            print("Your number of games win are:-- ", game_wins)
                            print("Your number of games lost are:-- ", game_loss)
                            print("Number of games played are:--  ", games_played)
                            new_game_valid == False
                            break
                        else:
                            print("Please select yes or no !")
                new_game()
                break
        else:
            if guesses >= 1 and guesses <= 2 and askguess == storednum:
                score += 99
            elif guesses >= 3 and guesses <= 4 and askguess == storednum:
                score += 79
            elif guesses >= 5 and guesses <= 6 and askguess == storednum:
                score += 59
            elif guesses >= 7 and guesses <= 8 and askguess == storednum:
                score += 29
            print("You won the game !!")
            print("Your score is: ", score)
            print("Number of guesses are :", guesses)
            game_wins += 1
            games_played += 1

            def new_game():
                new_game_valid = True
                while new_game_valid == True:
                    ask_game = input("Want to play another game Y/N  ").lower()
                    if ask_game == "yes" or ask_game == "y":
                        my_function(game_loss,game_wins,games_played)
                        break
                    elif ask_game == "no" or ask_game == "n":
                        print("")
                        print("Thanks for playing the game !")
                        print("Your number of games win are:-- ", game_wins)
                        print("Your number of games lost are:-- ", game_loss)
                        print("Number of games played are :--  ", games_played)
                        new_game_valid == False
                        break
                    else:
                        print("Please select yes or no !")

            new_game()


my_function(game_loss = game_loss,game_wins =game_wins,games_played = games_played)
