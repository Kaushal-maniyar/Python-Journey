#import replit
import  os
from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


functions = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}


def calculator():
    os.system('cls')
    print(logo)
    n1 = float(input("What's the first number : "))
    print("Operators : ")
    for i in functions:
        print(i)
    operator = input("Pick one Operator :")
    n2 = float(input("What's the second number : "))
    result = functions[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {result}")
    keep_doing = 'y'
    while keep_doing == 'y':
        keep_doing = input(f"Type 'y' to continue with {result} and type 'n' to exit :").lower()
        if keep_doing == 'y':
            operator = input("Pick another operator :")
            n2 = float(input("What's next number :"))
            n1 = result
            result = functions[operator](n1, n2)
            print(f"{n1} {operator} {n2} = {result}")
        else:
            calculator()
