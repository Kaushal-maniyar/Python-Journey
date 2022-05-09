from data import *


def check_resources(resources, order):
    """Take resources and order and return the resources if resources are sufficient."""
    if resources['water'] >= MENU[order]['ingredients']['water']:
        if resources['milk'] >= MENU[order]['ingredients']['milk']:
            if resources['coffee'] >= MENU[order]['ingredients']['coffee']:
                return True
            else:
                print("There is no enough coffee.")
                return False
        else:
            print("There is no enough milk.")
            return False
    else:
        print("There is no enough water.")
        return False


def take_payment(cost, order, resources):
    """Take the cost of order and return the refund."""
    print("Insert Coins :")
    qua = int(input("how many quarters?:")) * 0.25
    di = int(input("how many dimes?:")) * 0.1
    nic = int(input("how many nickles?:")) * 0.05
    peni = int(input("how many pennies?:")) * 0.01
    total = qua + di + nic + peni
    if total >= cost:
        resources['water'] -= MENU[order]['ingredients']['water']
        resources['milk'] -= MENU[order]['ingredients']['milk']
        resources['coffee'] -= MENU[order]['ingredients']['coffee']
        print(f"Your refund : $ {round(total-cost, 2)}")
        print(f"Here is your {order}. Enjoy!!")
        resources['money'] += cost
        return resources
    else :
        print(f"Your refund : $ {round(total, 2)}")
        print("Your given money is not sufficient to make your order.")

