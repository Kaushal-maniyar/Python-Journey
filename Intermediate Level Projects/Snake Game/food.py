from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.hideturtle()
        self.color('red')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 270)
        self.goto(x, y)
        self.showturtle()


