#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
no_letters= int(input("How many letters would you like in your password?\n")) 
no_symbols = int(input("How many symbols would you like?\n"))
no_numbers = int(input("How many numbers would you like?\n"))

password = ""
for letter in range(no_letters) :
    password += random.choice(letters)
for symbol in range(no_symbols) :
    password += random.choice(symbols)
for number in range(no_numbers) :
    password += random.choice(numbers)

list_pass = list(password)
random.shuffle(list_pass)
password = ''.join(list_pass)
 
print(f"Here is your Password :{password}")