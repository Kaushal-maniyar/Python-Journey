from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-230, 265)
        self.write(f'Score :{self.score}', align=ALIGN, font=FONT)

    def count(self):
        self.clear()
        self.score += 1
        self.write(f'Score :{self.score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!!', align=ALIGN, font=FONT)