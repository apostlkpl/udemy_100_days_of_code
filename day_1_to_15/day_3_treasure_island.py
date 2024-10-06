print("Welcome tot Treasure Island\nYour mission is to find the treasure")
print("You\'re at a cross road. Where do you want to go?")
move1 = input("\tType \"left\" or \"right\" ")
if move1.lower() != "left":
    print("You fell into a hole.\nGame over.")
    quit()
else:
    print("You\'ve come to a lake. There is an island in the middle of the lake.")
    move2 = input("\tType \"wait\" to wait for a boat. Type \"swim\" to swim across ")
    if move2.lower() != "wait":
        print("Attacked by trout.\nGame over.")
        quit()
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue")
        move3 = input("\tWhich door do you choose? ")
        if move3.lower() == "red":
            print("Burned by fire.\nGame Over.")
            quit()
        elif move3.lower() == "blue":
            print("Eaten by beasts.\nGame Over.")
            quit()
        elif move3.lower() == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
            quit()
