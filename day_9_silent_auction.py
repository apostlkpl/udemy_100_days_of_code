"""
SILENT AUCTION
"""
import os

print("\nWelcome to the auction!\n\n")
auction = {}
name = input("What is your name? : ")

try:
    bid = int(input("What\'s your bid? : $"))
except TypeError:
    print("\nPlease enter a number, not words\n")

auction[name] = bid

more = input("Are there any other bidders? Type \'yes\' or \'no\'.\n")
os.system("clear")

while more == "yes":
    name = input("What is your name? : ")

    try:
        bid = int(input("What\'s your bid? : $"))
    except TypeError:
        print("\nPlease enter a number, not words\n")

    auction[name] = bid
    more = input("Are there any other bidders? Type \'yes\' or \'no\'.\n")
    os.system("clear")

maximum = ("", 0)
for key, value in auction.items():
    if value > maximum[1]:
        maximum = (key, value)
print(f"\nThe winner is {maximum[0]} with a bid of ${str(maximum[1])}.\n")
