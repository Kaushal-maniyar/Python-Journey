import random
from turtle import Screen
from functions import *

should_continue = True
turtles = make_turtles()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="There are 7 Turtles :Violet,Indigo,Blue,Green,Yellow,Orange,"
                                                          "Red: Which turtle will win the race? Enter a color:").lower()
position(turtles)
if user_bet:
    while should_continue:
        for turtle in turtles:
            if should_continue:
                dis = random.randint(0, 10)
                turtle.forward(dis)
                if turtle.xcor() >= 227:
                    should_continue = False
                    if turtle.pencolor() == user_bet:
                        screen.textinput(title="", prompt='You won!!  ')
                    else:
                        screen.textinput(title="", prompt=f'Oops!!! You lose, Winner is {turtle.pencolor()} turtle  ')
screen.exitonclick()
