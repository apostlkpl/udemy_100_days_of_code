"""
HANGMAN GAME
"""

import random

# Making a list of words:
words = ["book", "stylus", "mouse", "coffee", "sound", "theater", "speaker", "college", "drawer", "cowboy", "wizard", "plant", "priest", "candle", "pillow", "bicycle", "balcony", "action", "thriller", "zebra", "orange", "apple", "crab", "dolphin", "sticker", "kitchen"]
target = random.choice(words)
blanks = ""
for _ in range(len(target)):
    blanks = blanks + "_"
length = len(target)

# Take input from the user:
tries = 10
print("\nWelcome to the HANGMAN game.\nYou have 10 tries to guess the word, letter by letter.\n")
print(f"This is the word you have to guess.\nIt has {length} letters:\n{blanks}")
history = []
wrong_letters = []
while length > 0 and tries > 0:
    print("\nLives left: ", tries)
    letter = input("Guess a letter from a to z:  ")
    if letter not in history:
        found = False
        for i in range(len(target)):
            if target[i] == letter.lower():
                blanks_str = list(blanks)
                blanks_str[i] = letter.lower()
                blanks = "".join(blanks_str)
                length -= 1
                found = True
                if length == 0:
                    break
        print(blanks)
        if found == False and letter not in wrong_letters:
            tries -= 1
            wrong_letters.append(letter)
    else:
        print("You have already entered this letter. Try another one.")
    print("Letters you have tried but are not in the word:")
    for letter in wrong_letters:
        print(letter + ", ", end = "")
    print()

# Final verdict:
if length == 0 and tries > 0:
    print("\n\nCongrats! You found the word: ", blanks)
if tries == 0:
    print("\n\nRIP bro. Better luck next time.")
    print("The word was: ", target)
