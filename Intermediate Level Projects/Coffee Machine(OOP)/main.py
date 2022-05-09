from coffee_machine import *

menu = Menu()
make_coffee = CoffeeMaker()
counter = MoneyMachine()
print("Menu :-")
print("Espresso : $ 1.5")
print("Latte : $ 2.5")
print("Cappuccino : $ 3.0")
should_continue = True
while should_continue:
    choice = input(f"What would you like? (n{menu.get_items()}):").lower()
    if choice == 'report':
        make_coffee.report()
        counter.report()
    elif choice == 'off':
        should_continue = False
    else:
        order = menu.find_drink(choice)
        if make_coffee.is_resource_sufficient(order) and counter.make_payment(order.cost):
            make_coffee.make_coffee(order)
