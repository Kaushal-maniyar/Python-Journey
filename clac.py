import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2) :
    return n1 + n2
def sub(n1,n2) :
    return n1 - n2
def mul(n1,n2) :
    return n1 * n2
def div(n1,n2) :
    return n1 / n2

functions = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div,
}
def calculator() : 
    print(logo)
    os.system('cls')
    n1 = float(input("What's the first number : "))
    print("Operators : ")
    for i in functions :
        print(i)
    operator = input("Pick one Operator :")
    n2 = float(input("What's the second number : "))
    result = functions[operator](n1,n2)
    print(f"{n1} {operator} {n2} = {result}")
    keep_doing = 'y'
    while keep_doing == 'y' :
        keep_doing = input(f"Type 'y' to continue with {result} and type 'n' to exit :").lower()
        if keep_doing == 'y' :
            operator = input("Pick another operator :")
            n2 = float(input("What's next number :"))
            n1 = result
            result = functions[operator](n1,n2)
            print(f"{n1} {operator} {n2} = {result}")
        else :
            calculator()
             

calculator()