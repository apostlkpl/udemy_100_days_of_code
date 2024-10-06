print("#########################################")
print("##### Welcome to the coffee machine #####")
print("#########################################\n\n")


# What you can order:
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

# What the machine has available:
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Starting with some money, for example 50$ :
money = 50

# Take input from the user
while True:
    coff = input("What would you like? (espresso - 1.50$/latte - 2.50$/cappuccino - 3.00$): ")
    if coff.lower() == "off":
        quit()
    if coff.lower() == "report":
        print("Coffee machine report:\n###################")
        print("Coffee:", resources["coffee"])
        print("Milk:", resources["milk"])
        print("Water:", resources["water"])
        print("Money:", money)
        coff = input("What would you like? (espresso - 1.50$/latte - 2.50$/cappuccino - 3.00$): ")


    print("Please insert coins.")
    while True:
        try:
            quarters = int(input("How many quarters? : "))
            dimes = int(input("How many dimes? : "))
            nickels = int(input("How many nickels? : "))
            pennies = int(input("How many pennies? : "))
            break
        except ValueError:
            print("Please add the values of the coins as integers (starting from the beggining)")

# Calculate the money total the customer gave us:
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    try:
        if total <  menu[coff.lower()]["cost"]:
            print("Sorry, that\'s not enough money. Money refunded.")
        else:
            if resources["water"] >=  menu[coff.lower()]["ingredients"]["water"] and resources["milk"] >= menu[coff.lower()]["ingredients"]["milk"] and resources["coffee"] >=  menu[coff.lower()]["ingredients"]["coffee"]:
                money += total
                if money < total - menu[coff.lower()]["cost"]:
                    print("Sorry, out of change.")
                else:
                    print(f"Here is {total - menu[coff.lower()]["cost"]} in change.")
                    print(f"Here is your {coff} ☕ Enjoy!")
                    money -= total - menu[coff.lower()]["cost"]
                    resources["water"] -= menu[coff.lower()]["ingredients"]["water"]
                    resources["milk"] -= menu[coff.lower()]["ingredients"]["milk"]
                    resources["coffee"] -= menu[coff.lower()]["ingredients"]["coffee"]
            else:
                if resources["water"] < menu[coff.lower()]["ingredients"]["water"]:
                    print("Sorry, there is not enough water.")
                elif resources["milk"] < menu[coff.lower()]["ingredients"]["milk"]:
                    print("Sorry, there is not enough milk.")
                elif resources["coffee"] <  menu[coff.lower()]["ingredients"]["coffee"]:
                    print("Sorry, there is not enough coffee.")
    except KeyError:
        print("You entered an invalid type of coffee. Please try again.")
