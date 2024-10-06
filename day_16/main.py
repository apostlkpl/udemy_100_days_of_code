from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating the objects based on the classes we are given
menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

while True:
    # Take input from the user
    coff = input(f"What would you like? {menu.get_items()}... :")
    # Hidden "off" input for admin or maintenance
    if coff.lower() == "off":
        quit()
    # Get the report
    elif coff.lower() == "report":
        maker.report()
        money.report()
    # Actually making the coffee
    else:
        order = menu.find_drink(coff)
        if maker.is_resource_sufficient(order) and money.make_payment(order.cost):
            maker.make_coffee(order)
