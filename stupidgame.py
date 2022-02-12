print("Welcometo Treasure Island.")
print("Your mission is to find the treasure.")
first = input("Right or Left?").lower()
if first == "right" :
    print("Game Over.")
else :
    second = input("Swim or wait?").lower()
    if second == "swim" :
        print("Game Over.")
    else :
        third = input("Red or Blue or Yellow ?").lower()
        if third == "red" or third == "blue" :
            print("Game Over")
        else :
            print("You Won")
