import random
game_slang = ["Rock","Paper","Scissors"]
print("0 for Rock, 1 for Paper, 2 for Scissors")
your_choice= int(input("Enter your choise :"))
if your_choice < 0  or your_choice > 2 :
    print("Invalid.")
else :
    print("Your choice is : "+game_slang[your_choice])
    computer_choice = random.randint(0,2)
    print(f"Compter's choise :{game_slang[computer_choice]}")
    difference = your_choice - computer_choice
    if difference == -2 or  difference == 1 :
        print("You won.")
    elif difference == -1 or difference == 2 :
        print("You lose.")
    else :
        print("Match draw.")
