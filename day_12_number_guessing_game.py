print(r"""  _   _                 _                  ____                     _                ____                      
 | \ | |_   _ _ __ ___ | |__   ___ _ __   / ___|_   _  ___  ___ ___(_)_ __   __ _   / ___| __ _ _ __ ___   ___ 
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | |  _ / _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|\___||___/___/_|_| |_|\__, |  \____|\__,_|_| |_| |_|\___|
                                                                            |___/                              """)

import random

print("\nWelcome to the Number Guessing Game!")
print("I\'m thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type \'easy\' or \'hard\': ")
actual_number = random.randint(1, 100)

def guesses():
    attempts = 0
    if diff == "easy":
        attempts = 10
    elif diff == "hard":
        attempts = 5
    while attempts > 0:
        try:
            number = int(input(f"You have {attempts} remaining to guess the number.\nMake a guess: "))
            if attempts == 1:
                if number == actual_number:
                    print(f"You\'ve got it. The answer was {actual_number}.\n")
                    break
                elif number > actual_number:
                    print("Too high.\nYou\'re out of guesses. You lose.\n")
                    break
                else:
                    print("Too low.\nYou\'re out of guesses. You lose.\n")
                    break
            if number > actual_number:
                print("Too high.\nGuess again.")
                attempts -= 1
            elif number < actual_number:
                print("Too low.\nGuess again.")
                attempts -= 1
            else:
                print(f"You got it. The answer was {actual_number}.\n")
                break
        except TypeError:
            print("Please write an integer between 1 and 100\n")
            continue
    if attempts == 0:
        print("You\'re out of guesses. You lose.\n")

guesses()

