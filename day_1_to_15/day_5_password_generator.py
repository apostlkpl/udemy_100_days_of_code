#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
while True:
    try:
        nr_letters= int(input("How many letters would you like in your password?\n"))
        break
    except ValueError:
        print("Please enter a valid number")
        continue

while True:
    try:
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        break
    except ValueError:
        print("Please enter a valid number")
        continue

while True:
    try:
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        break
    except ValueError:
        print("Please enter a valid number")

combinations = [letters, numbers, symbols]
password = ""
password_length = nr_letters + nr_symbols + nr_numbers

while nr_letters >= 0  and nr_numbers >= 0 and nr_symbols >= 0 and len(password) < password_length:
    idx = random.randint(0, 2)
    if idx  == 0 and nr_letters > 0:
        char = letters[random.randint(0, len(letters) - 1)]
        nr_letters -= 1
        password = password + char
    elif idx == 1 and nr_numbers > 0:
        char = numbers[random.randint(0, len(numbers) - 1)]
        nr_numbers -= 1
        password = password + char
    elif idx == 2 and nr_symbols > 0:
        char = symbols[random.randint(0, len(symbols) - 1)]
        nr_symbols -= 1
        password = password + char

print("Your password is: ", password)
