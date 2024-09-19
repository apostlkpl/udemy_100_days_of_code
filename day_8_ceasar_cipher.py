"""
CEASAR CIPHER
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the Ceasar Cipher.\nYou can encrypt or decrypt messages\n")
func = input("Please choose what you\'d like to do, \"encode\" or \"decode\":  ")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted = ""
    for letter in original_text:
        if letter != " ":
            try:
                encrypted += alphabet[alphabet.index(letter) + shift_amount]
            except IndexError:
                encrypted += alphabet[abs(len(alphabet) - alphabet.index(letter) - shift_amount)]
        else:
            encrypted += " "
    print("Here is the encoded result: " + encrypted)

def decrypt(original_text, shift_amount):
    decrypted = ""
    for letter in original_text:
        if letter != " ":
            decrypted += alphabet[alphabet.index(letter) - shift_amount]
        else:
            decrypted += " "
    print("Here is the encoded result: " + decrypted)

if func == "encode":
    encrypt(text, shift)
if func == "decode":
    decrypt(text, shift)
