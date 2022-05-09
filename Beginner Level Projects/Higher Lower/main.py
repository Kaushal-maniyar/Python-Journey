from data import data
from art import logo
from functions import *
import random
import os

count = 0
score = 0
should_continue = True
a = data[random.randint(0, 49)]
b = selection_for_b(a)
while should_continue:
    os.system('cls')
    print(logo)
    print_score(score, count)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print("Vs")
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B':")
    if guess == 'A' or guess == 'a':
        if a['follower_count'] > b['follower_count']:
            a = b
            b = selection_for_b(a)
            score += 1
            count += 1
        else:
            should_continue = False
    else:
        if b['follower_count'] > a['follower_count']:
            a = b
            b = selection_for_b(a)
            score += 1
            count += 1
        else:
            should_continue = False
print(f"You got it wrong,You're final score : {score}")
