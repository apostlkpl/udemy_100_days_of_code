"""
ROCK PAPER SCISSORS GAME
"""
import random

print("Welcome to the \"Rock, Paper, Scissors\" game")
while True:
    try:
        player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
        if player not in [0, 1, 2]:
            print("Please enter 0, 1, or 2. No other numbers permitted")
            continue
        else:
            break
    except ValueError:
        print("Please write one of the numbers. No words permitted")
        continue
choices = ["Rock", "Paper", "Scissors"]
computer = choices[random.randint(0, 2)]

if choices[player] == computer:
    result = "It\'s a tie!"
if choices[player] == "Rock":
    if computer == "Paper":
        result = "You lose"
    elif computer == "Scissors":
        result = "You Win!"
if choices[player] == "Paper":
    if computer == "Rock":
        result = "You Win!"
    elif computer == "Scissors":
        result = "You lose"
if choices[player] == "Scissors":
    if computer == "Rock":
        result = "You lose"
    elif computer == "Paper":
        result == "You Win!"


print(f"You chose {choices[player]}\nThe computer chose {computer}\n{result}")
