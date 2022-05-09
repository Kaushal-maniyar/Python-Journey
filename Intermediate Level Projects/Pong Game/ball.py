from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.speed(2)
        self.color('white')
        self.random_head()

    def move(self):
        self.forward(10)

    def collision_with_wall(self):
        self.setheading(((180-self.heading())*2)+self.heading())

    def collision_with_slider(self):
        self.setheading(180-self.heading())

    def random_head(self):
        right_left = random.randint(0, 1)
        if right_left == 1:
            self.setheading(random.randint(-45, 45))
            while self.heading() == 0:
                self.setheading(random.randint(-45, 45))
        else:
            self.setheading(random.randint(135, 225))
            while self.heading() == 180:
                self.setheading(random.randint(135, 225))


    def goto_home(self):
        self.goto(0, 0)
        self.random_head()