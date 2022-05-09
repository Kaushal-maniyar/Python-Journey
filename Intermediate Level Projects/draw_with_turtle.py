from turtle import Turtle, Screen

tim = Turtle()
current_head = tim.heading()


def move():
    tim.forward(10)


def back():
    tim.back(10)


def counter_clockwise():
    global current_head, tim
    current_head += 5
    tim.setheading(current_head)


def clockwise():
    global current_head, tim
    current_head += -5
    tim.setheading(current_head)


def clear():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.setheading(0)
    tim.pendown()


tim.shape('turtle')
screen = Screen()
screen.listen()
screen.onkey(fun=move, key='w')
screen.onkey(fun=back, key='s')
screen.onkey(fun=counter_clockwise, key='a')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=clear, key='c')
screen.exitonclick()
