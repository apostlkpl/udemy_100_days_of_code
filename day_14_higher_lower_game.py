logo =r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from day_14_game_data import data
import random
from os import system

# Choosing a random integer between 0 and list.length - 1
def rand(n):
    return random.randint(0, n - 1)

lost = False
score = 0
while not lost:
    aa = data[rand(len(data))]
    bb = data[rand(len(data))]
    print(logo, "\n")
    if score > 0:
        print("You\'re right! Current score:", score, "\n")
    print(f"Compare A: {aa['name']}, a(n) {aa['description']}, from {aa['country']}.")
    print(vs, "\n")
    print(f"Compare B: {bb['name']}, a(n) {bb['description']}, from {bb['country']}.")
    inp = ""
    while inp != 'A' and inp != 'a' and inp != 'B' and inp != 'b':
        inp = input("\nWho has more followers? Type A or B : ")
    if inp == 'A' or inp == 'a':
        if aa['follower_count'] >= bb['follower_count']:
            score += 1
        else:
            lost = True
    elif inp == 'B' or inp == 'b':
        if aa['follower_count'] < bb['follower_count']:
            score += 1
        else:
            lost =  True
    system("clear")

print(logo, "\n\n")
print("Sorry, that\'s wrong. Final score:", score, "\n\n")
