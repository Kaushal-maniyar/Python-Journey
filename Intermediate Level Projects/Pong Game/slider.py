from turtle import Turtle

DIS = 20


class Slider:
    def __init__(self, p1_or_p2):
        self.slider = Turtle('square')
        self.slider.shapesize(stretch_len=1, stretch_wid=5)
        if p1_or_p2 == 1:
            x = -290
        else:
            x = 285
        self.slider.penup()
        self.slider.color('white')
        self.slider.goto(x, 0)

    def up(self):
        if self.slider.ycor() < 250:
            self.slider.goto(self.slider.xcor(), self.slider.ycor() + 20)

    def down(self):
        if self.slider.ycor() > -250:
            self.slider.goto(self.slider.xcor(), self.slider.ycor() - 20)
