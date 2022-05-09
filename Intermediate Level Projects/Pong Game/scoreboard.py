from turtle import Turtle
ALIGN = 'center'
FORMATE = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self, p1_or_p2):
        super().__init__()
        self.score = 0
        self.penup()
        if p1_or_p2 == 1:
            self.goto(-30, 275)
        else:
            self.goto(30, 275)
        self.hideturtle()
        self.color('white')
        self.write(f'{self.score}', move=False, align=ALIGN, font=FORMATE)

    def count(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}', move=False, align=ALIGN, font=FORMATE)
