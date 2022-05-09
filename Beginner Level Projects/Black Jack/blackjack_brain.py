import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def black_jack(my_hand, com_hand):
    my_total = sum(my_hand)
    com_total = sum(com_hand)
    if my_total == 21:
        print("You have black jack!")
    if com_total == 21:
        print("Computer has black jack!")


def give_cards():
    hand = [random.choice(deck), random.choice(deck)]
    return hand


def add_card(hand):
    hand.append(random.choice(deck))
    return hand


def print_hands(my_hand, com_hand, com_print):
    print(f"My hand : {my_hand}   Total : {sum(my_hand)}")
    if com_print == 'y':
        print(f"Computer's hand : {com_hand}   Total : {sum(com_hand)}")
    else:
        print(f"Computer's hand :[{com_hand[0]},_]")


def remove_11(hand):
    total = sum(hand)
    while 11 in hand and total > 21:
        hand.remove(11)
        hand.append(1)
        total = sum(hand)
    return hand


def win_or_lose(my_hand, com_hand):
    com_total = sum(com_hand)
    my_total = sum(my_hand)
    if my_total > 21:
        print_hands(my_hand, com_hand, 'y')
        black_jack(my_hand, com_hand)
        print("You lose!")
    elif com_total < 17:
        while com_total < 17:
            com_hand = add_card(com_hand)
            com_hand = remove_11(com_hand)
            com_total = sum(com_hand)
        logic_17(my_hand, com_hand)
    else:
        logic_17(my_hand, com_hand)


def logic_17(my_hand, com_hand):
    com_total = sum(com_hand)
    my_total = sum(my_hand)
    if my_total > com_total:
        print_hands(my_hand, com_hand, 'y')
        black_jack(my_hand, com_hand)
        print("You won!")
    elif my_total < com_total:
        if com_total > 21:
            print_hands(my_hand, com_hand, 'y')
            black_jack(my_hand, com_hand)
            print("You won!")
        else:
            print_hands(my_hand, com_hand, 'y')
            black_jack(my_hand, com_hand)
            print("You lose!")
    else:
        print_hands(my_hand, com_hand, 'y')
        black_jack(my_hand, com_hand)
        print("Draw!!")
