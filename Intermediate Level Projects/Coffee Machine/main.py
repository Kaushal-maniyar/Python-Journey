from functions import *

print("Menu :-")
print("Espresso : $ 1.5")
print("Latte : $ 2.5")
print("Cappuccino : $ 3.0")
should_continue = True
while should_continue:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order == 'espresso' or order == 'latte' or order == 'cappuccino':
        make_it = check_resources(resources, order)
        if make_it:
            take_payment(MENU[order]['cost'], order, resources)
    elif order == 'report':
        print(f"Milk : {resources['milk']} ml")
        print(f"Water : {resources['water']} ml")
        print(f"Coffee : {resources['coffee']} gm")
        print(f"Money : $ {resources['money']} ")
    elif order == 'off':
        should_continue = False
    else:
        print("Enter name properly.")
