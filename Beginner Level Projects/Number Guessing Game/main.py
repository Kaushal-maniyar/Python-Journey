import random
import os
from art import logo

os.system('cls')
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Difficulty level :")
print("Easy : 10 Attempts")
print("Hard : 5 Attempts")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' :")
if difficulty == 'easy':
    attempt = 10
else:
    attempt = 5
guessed = False
num = random.randint(1, 100)
print(num)
while not guessed and attempt > 0:
    guessed_num = int(input("Make a guess :"))
    if guessed_num == num:
        guessed = True
        print(f"You got it! The Number is {num}.")
    elif guessed_num >= num:
        print("It's high.")
        attempt -= 1
        print(f"Attempt left : {attempt}")
    elif guessed_num <= num:
        print("It's low.")
        attempt -= 1
        print(f"Attempt left : {attempt}")    
if not guessed:
    print("You Lose!!")
