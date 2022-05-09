from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

snake = Snake()
food = Food()
food.refresh()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

should_continue = True
while should_continue:
    if snake.head.distance(food) < 15:
        food.refresh()
        score.count()
        snake.extend_tail()
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    for i in snake.snake_list[1:]:
        if snake.head.distance(i) < 15:
            score.reset()
            snake.reset()
    for i in snake.snake_list:
        if i.distance(food) < 10:
            food.refresh()
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()
