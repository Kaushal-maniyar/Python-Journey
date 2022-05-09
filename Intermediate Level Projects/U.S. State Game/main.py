import turtle
import pandas

state_info = pandas.read_csv('50_states.csv')


def get_coordinate(state_name):
    state = state_info[state_info.state == state_name ]
    x = int(state['x'])
    y = int(state['y'])
    tuple_xy = (x, y)
    return tuple_xy


t = turtle.Turtle()
t.penup()
t.hideturtle()
t.speed(0)
image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

states = state_info['state'].tolist()
total = len(states)
count = 0
while states:
    name = screen.textinput(title=f" {count}/{total} State Correct", prompt="What's another state's name ?").title()
    if name == 'Exit':
        break
    if name in states:
        xy = get_coordinate(name)
        t.goto(xy)
        t.write(name, align='center', font=("Courier", 10, "normal"))
        states.remove(name)
        count += 1

missing_state = {
    'Missing State': states
}

df = pandas.DataFrame(missing_state)
df.to_csv('Missing_State.csv')
