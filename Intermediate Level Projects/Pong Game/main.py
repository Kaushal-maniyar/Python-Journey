from turtle import Screen, Turtle
from slider import Slider
from ball import Ball
from scoreboard import ScoreBoard
import time
refresh_rate = 0.05

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# Dotted line
t = Turtle()
t.hideturtle()
t.penup()
t.goto(0, 300)
t.pendown()
t.setheading(270)
t.pencolor('white')
while t.ycor() != -300:
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()

# Slider Creation
p1 = Slider(1)
p2 = Slider(2)


screen.listen()
screen.onkeypress(p1.up, 'w')
screen.onkeypress(p1.down, 's')
screen.onkeypress(p2.up, 'Up')
screen.onkeypress(p2.down, 'Down')

# Pong Creation
ball = Ball()

# Score Display
scr1 = ScoreBoard(1)
scr2 = ScoreBoard(2)
screen.update()

# Game on Action
should_continue = True
while should_continue:
    ball.move()
    if ball.xcor() < -285:
        scr2.count()
        ball.goto_home()
        refresh_rate = 0.05
    if ball.xcor() > 280:
        scr1.count()
        ball.goto_home()
        refresh_rate = 0.05
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.collision_with_wall()
    if (ball.xcor() > 270 and ball.distance(p2.slider) < 55) or (ball.xcor() < -275 and ball.distance(p1.slider) < 55):
        ball.collision_with_slider()
        refresh_rate *= 0.95

    screen.update()
    time.sleep(refresh_rate)
screen.exitonclick()
