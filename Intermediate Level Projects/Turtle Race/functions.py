from turtle import Turtle

def make_turtles():
    list_turtles = []
    color_list = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
    for i in range(7):
        turtle = Turtle('turtle')
        turtle.color(color_list[i])
        turtle.penup()
        list_turtles.append(turtle)
    return list_turtles


def position(list_of_turtles):
    x = -240
    y = -100
    for i in list_of_turtles:
        i.goto(x, y)
        y += 35
