import math
import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


sleep_time = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initiate Scoreboard
score = Scoreboard()

# Initiate Player
player = Player()
screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

# Car List
car_list = []
for _ in range(15):
    car = CarManager()
    x = random.randint(-240, 265)
    y = random.randint(-250, 265)
    car.goto(x, y)
    car_list.append(car)

screen.update()
count = 1
game_is_on = True
while game_is_on:
    if count % 6 == 0:
        car = CarManager()
        y = random.randint(-250, 265)
        car.goto(300, y)
        car_list.append(car)
    for car in car_list:
        car.move()
        if car.xcor() < -400:
            car_list.remove(car)
        if car.distance(player) < 30 and math.fabs(car.ycor() - player.ycor()) < 20:
            game_is_on = False
            score.game_over()
    count += 1
    if player.ycor() >= 280:
        player.goto(0, -280)
        score.count()
        sleep_time *= .95

    time.sleep(sleep_time)
    screen.update()


screen.exitonclick()
