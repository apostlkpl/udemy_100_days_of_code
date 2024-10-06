"""
BLACKJACK GAME
"""

import random
import numpy as np

print(r"""
         ______
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|""")

print("\n\t\tWELCOME TO BLACKJACK\n\n")

# Create a deck
one_set = ['Ace', 'Jack', 'Queen', 'King', '2', '3', '4', '5', '6', '7', '8', '9', '10']
deck = one_set * 4
# Blackjack usually uses six decks
jack = deck * 6
random.shuffle(jack)
#print(len(jack))

def card_to_points(card):
    if (card == 'Jack') | (card == 'Queen') | (card == 'King'):
        return 10;
    elif card == 'Ace':
        return
    else:
        return int(card)

# Initial two cards for player
r1, r2 = random.randint(0, len(jack)-1), random.randint(0, len(jack)-1)
player_cards = [jack[r1], jack[r2]]
# Those two cards removed from the decks
jack.pop(r1)
jack.pop(r2)

# Initial cards for computer/dealer
r3, r4 = random.randint(0, len(jack)-1), random.randint(0, len(jack)-1)
dealer_cards = [jack[r3], jack[r4]]
# Remove those cards from the deck
jack.pop(r3)
jack.pop(r4)
#print(len(jack))

player_win = 0
for cc in player_cards:
    if cc == 'Ace':
        player_win += 11
    else:
        player_win += card_to_points(cc)
if player_win == 21:
    print(f"Your cards are: {player_cards}, and your points are: {player_win}\nYou won!\n")
    quit()


dealer_win = 0
for cc in dealer_cards:
    if cc == 'Ace':
        dealer_win += 11
    else:
        dealer_win += card_to_points(cc)
if dealer_win == 21:
    print(f"The dealer\'s cards are: {dealer_cards}, and their points are: {dealer_win}\nYou lost!\n")
    quit()

print(f"\nYour cards: {player_cards[0]}, {player_cards[1]}")
print(f"\nDealer\'s first card: {dealer_cards[0]}\n")

while True:
    next_round = input("Type \'y\' to get another card, type \'n\' to pass: ")
    if next_round == 'y':
        r = random.randint(0, len(jack)-1)
        player_cards.append(jack[r])
        jack.pop(r)
        print(f"Your cards are now: {player_cards}.\n")
        if 'Ace' not in dealer_cards:
            if np.sum(list(map(card_to_points, dealer_cards))) < 17:
                rr = random.randint(0, len(jack)-1)
                dealer_cards.append(jack[rr])
                jack.pop(rr)
        else:
            dealer_sum = 0
            for cc in dealer_cards:
                if cc == 'Ace':
                    dealer_sum += 1
                else:
                    dealer_sum += card_to_points(cc)
            if dealer_sum < 17:
                rr2 = random.randint(0, len(jack)-1)
                dealer_cards.append(jack[rr2])
                jack.pop(rr2)
        continue
    elif (next_round != 'y') & (next_round != 'n'):
        print("\nPlease enter \'y\' or \'n\'")
        continue
    elif next_round == 'n':
        break

dealer_sum = 0
if 'Ace' not in dealer_cards:
    dealer_sum = np.sum(list(map(card_to_points, dealer_cards)))
else:
    for cc in dealer_cards:
        if cc == 'Ace':
            dealer_sum += 1
        else:
            dealer_sum += card_to_points(cc)

while dealer_sum < 17:
    if 'Ace' not in dealer_cards:
        if np.sum(list(map(card_to_points, dealer_cards))) < 17:
            rr3 = random.randint(0, len(jack)-1)
            dealer_cards.append(jack[rr3])
            jack.pop(rr3)
            if jack[rr3] != 'Ace':
                dealer_sum += card_to_points(jack[rr3])
            else:
                dealer_sum += 1
    else:
        dealer_sum_ace = 0
        for cc in dealer_cards:
            if cc == 'Ace':
                dealer_sum_ace += 1
            else:
                dealer_sum_ace += card_to_points(cc)
        rr4 = random.randint(0, len(jack)-1)
        dealer_cards.append(jack[rr4])
        jack.pop(rr4)
        if jack[rr4] != 'Ace':
            dealer_sum_ace += card_to_points(jack[rr3])
        else:
            dealer_sum_ace += 1
        dealer_sum = dealer_sum_ace

player_points = 0
if 'Ace' not in player_cards:
    player_points = np.sum(list(map(card_to_points, player_cards)))
else:
    for cc in player_cards:
        if cc == 'Ace':
            player_points += 11
        else:
            player_points += card_to_points(cc)
    if player_points > 21:
        player_points = 0
        for cc in player_cards:
            if cc == 'Ace':
                player_points += 1
            else:
                player_points += card_to_points(cc)

dealer_points = 0
if 'Ace' not in dealer_cards:
    dealer_points = np.sum(list(map(card_to_points, dealer_cards)))
else:
    for cc in dealer_cards:
        if cc == 'Ace':
            dealer_points += 1
        else:
            dealer_points += card_to_points(cc)

print(f"\nYour final hand: {player_cards}, and your final score: {player_points}\n")
print(f"The dealer\'s final hand: {dealer_cards}, and their final score: {dealer_points}\n")

if (player_points <= 21) & (dealer_points <= 21):
    if player_points > dealer_points:
        print("You Win!\n")
    elif player_points < dealer_points:
        print("You loose!\n")
    else:
        print("It\'s a tie!\n")

if (player_points <= 21) & (dealer_points > 21):
    print("You win!\n")
if player_points > 21:
    print("You loose!\n")

