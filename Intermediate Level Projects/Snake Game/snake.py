from turtle import Turtle

DIS = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.tail = self.snake_list[-1]

    def create_snake(self):
        x = 0
        y = 0
        for _ in range(3):
            t = Turtle('square')
            t.penup()
            t.color('white')
            t.goto(x, y)
            x -= 20
            self.snake_list.append(t)

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            x = self.snake_list[i - 1].xcor()
            y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(x, y)
        self.head.forward(DIS)

    def reset(self):
        for i in self.snake_list:
            i.goto(800, 800)
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.tail = self.snake_list[-1]

    def extend_tail(self):
        t = Turtle('square')
        t.penup()
        t.color('white')
        x = self.tail.xcor()
        y = self.tail.ycor()
        t.goto(x, y)
        self.snake_list.append(t)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
