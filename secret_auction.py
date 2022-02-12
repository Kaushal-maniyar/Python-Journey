import os
os.system('cls')  
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Secrect Auction!")
max = 0
members = {}
response = "y"
winner_name =""
while response == "y" :
    name = input("Enter your Name :")
    bid = int(input("Enter your Bid :$"))
    members[name] = bid
    if members[name] > max :
        max = members[name]
        winner_name = name
    response = input("Is there other biders?Yes or No?").lower()[0]
    os.system('cls')  
print(f"Winner is {winner_name} with bid of {members[winner_name]}$!")    
