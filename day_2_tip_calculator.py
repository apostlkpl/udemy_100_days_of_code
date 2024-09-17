print("Welcome to the tip calculator!")

total = 0
while True:
    try:
        total = float(input("What was the total bill? "))
        break
    except ValueError:
        print("Please insert the amount as a number")
        continue
        

tip = 0
while True:
    try:
        tip = input("How much tip would you like to give? 10%, 12%, or 15% ? ")
        if int(tip) == 10 or int(tip) == 12 or int(tip) == 15:
            break
        else:
            print("Please enter one of the pre-defined amounts")
            continue
    except ValueError:
        print("Please insert the amount as a number")
        continue

people = 0
while True:
    try:
        people = int(input("How many people to split the bill? "))
        break
    except ValueError:
        print("Please insert the amount of people as a number")
        continue

print("Each person should pay: $", round((total + (total * 0.01 *  int(tip))) / people, 2), sep = "")
