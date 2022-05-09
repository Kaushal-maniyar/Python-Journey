from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__('square')
        color = COLORS[random.randint(0, 5)]
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE, self.ycor())

    def move_increment(self):
        self.move_distance += MOVE_INCREMENT

