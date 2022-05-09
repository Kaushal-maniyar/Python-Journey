from art import logo
from caesar_cipher_brain import *

print(logo)
should_continue = "y"
while should_continue == 'y':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    should_continue = input("Do you want to continue? Yes or No?").lower()[0]
    if should_continue == 'n':
        print("See you soon!")

   