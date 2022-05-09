import os

from art import logo
from blackjack_brain import *
import replit


replit.clear()
yes_no = 'y'
while yes_no == 'y':
    yes_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()[0]
    if yes_no == 'y':
        os.system('cls')
        print(logo)
        my_hand = give_cards()
        my_hand = remove_11(my_hand)
        my_total = sum(my_hand)
        com_hand = give_cards()
        com_hand = remove_11(com_hand)
        add_one_card = 'y'
        while my_total < 21 and add_one_card == 'y':
            print_hands(my_hand, com_hand, "n")
            add_one_card = input("Do you want one more card? Type 'y' for Yes and 'n' for NO :")
            if add_one_card == 'y':
                my_hand = add_card(my_hand)
                remove_11(my_hand)   
            else:
                add_one_card = 'n'
            my_total = sum(my_hand)
        win_or_lose(my_hand, com_hand)
    else:
        yes_no = 'n' 
