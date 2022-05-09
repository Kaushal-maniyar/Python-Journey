from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__(shape='turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.color('black')

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
