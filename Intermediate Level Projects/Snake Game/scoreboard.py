from turtle import Turtle
ALIGN = 'center'
FORMATE = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.color('red')
        self.write(f'Score : {self.score} , High Score : {self.high_score}', move=False, align=ALIGN, font=FORMATE)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f'Score : {self.score} , High Score : {self.high_score}', move=False, align=ALIGN, font=FORMATE)

    def game_over(self):
        self.home()
        self.write('GAME OVER!!', move=False, align=ALIGN, font=FORMATE)

    def count(self):
        self.clear()
        self.score += 1
        self.write(f'Score : {self.score} , High Score : {self.high_score}', move=False, align=ALIGN, font=FORMATE)
