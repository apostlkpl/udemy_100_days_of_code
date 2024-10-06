print(" _____________________")
print("|  _________________  |")
print("| | PYcal        0. | |")
print("| |_________________| |")
print("|  ___ ___ ___   ___  |")
print("| | 7 | 8 | 9 | | + | |")
print("| |___|___|___| |___| |")
print("| | 4 | 5 | 6 | | - | |")
print("| |___|___|___| |___| |")
print("| | 1 | 2 | 3 | | x | |")
print("| |___|___|___| |___| |")
print("| | . | 0 | = | | / | |")
print("| |___|___|___| |___| |")
print("|_____________________|")
print(" \nWELCOME TO THE PYTHON CALCULATOR\n\n")

first = float(input("What\'s the first number? : "))
oper = input("\n+\n-\n*\n/\nPick an operation: ")
second = float(input("\nWhat\'s the second number? : "))

def add(a, b):
    print(f"\nResult:\n{a} + {b} = {a+b}\n")
def subtr(a, b):
    print(f"\nResult:\n{a} - {b} = {a-b}\n")
def mult(a, b):
    print(f"\nResult:\n{a} * {b} = {a*b}\n")
def div(a, b):
    if b == 0:
        print("\nCan\'t devide by zero.\n")
        return
    print(f"\nResult:\n{a} ÷ {b} = {a/b}\n")

if oper == "+":
    add(first, second)
if oper == "-":
    subtr(first, second)
if oper == "*":
    mult(first, second)
if oper == "/":
    div(first, second)
