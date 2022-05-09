import os
from art import logo

os.system('cls')
print(logo)
print("Welcome to the Secret Auction!")
max_amount = 0
members = {}
response = "y"
winner_name = ""
while response == "y":
    name = input("Enter your Name :")
    bid = int(input("Enter your Bid :$"))
    members[name] = bid
    if members[name] > max_amount:
        max_amount = members[name]
        winner_name = name
    response = input("Is there other bidders ?Yes or No?").lower()[0]
    os.system('cls')
print(f"Winner is {winner_name} with bid of {members[winner_name]}$!")
