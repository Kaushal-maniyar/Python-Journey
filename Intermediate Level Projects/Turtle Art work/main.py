import random
import turtle
from turtle import Turtle, Screen
from function import make_color_list


turtle.colormode(255)
timmy = Turtle()
timmy.speed(0)
timmy.penup()
timmy.hideturtle()
screen = Screen()
screen.screensize(650, 650)
color_list = make_color_list(100)
for i in range(-315, 326, 70):
    for j in range(-315, 326, 70):
        timmy.goto(j, i)
        timmy.color(random.choice(color_list))
        timmy.dot(20)
screen.exitonclick()
