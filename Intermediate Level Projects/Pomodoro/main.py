from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
rows = 3
ticks = []
reset = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global rows
    global ticks
    global reset
    reset = True
    if ticks:
        for tick in ticks:
            tick.config(text='')
        ticks.clear()
    canvas.itemconfigure(timer_text, text="00:00")
    start.config(command=start_count_down)
    title.config(text="Timer", fg=GREEN)
    reps = 0
    rows = 3


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count_down():
    global reps
    global rows
    global ticks
    global reset
    reset = False
    start.config(command=do_nothing)
    if reps <= 8:
        if reps == 7:
            title.config(text="Long Break", fg=PINK)
            count_down(LONG_BREAK_MIN * 60)
        elif reps % 2 == 1:
            tick = Label(text="✔", fg=GREEN, font=(FONT_NAME, 15, 'normal'), bg=YELLOW)
            tick.grid(row=rows, column=1)
            ticks.append(tick)
            title.config(text="Short Break", fg=RED)
            rows += 1
            count_down(SHORT_BREAK_MIN * 60)
        elif reps == 8:
            title.config(text="Well Done!!", fg=GREEN)
        elif reps % 2 == 0:
            title.config(text="Work", fg=GREEN)
            count_down(WORK_MIN * 60)


def do_nothing():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    if not reset:
        canvas.itemconfigure(timer_text, text=f'{"{:02d}".format(int(count / 60))}:{"{:02d}".format(count % 60)}')
        if count > 0:
            window.after(1000, count_down, count - 1)
        else:
            reps += 1
            window.after(1000, start_count_down)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 124, text="00:00", font=(FONT_NAME, 30, 'bold'), fill='white')
canvas.grid(row=1, column=1)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=YELLOW)
title.grid(row=0, column=1)

start = Button(text="Start", command=start_count_down)
start.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
