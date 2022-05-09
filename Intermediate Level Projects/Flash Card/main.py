from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 25, "normal")
WORD_FONT = ("Arial", 45, "bold")
FRENCH = 0
ENGLISH = 1
CARD = {}
try:
    dataframe = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    dataframe = pandas.read_csv("./data/french_words.csv")
words_list = dataframe.to_dict(orient="records")


def flip_card():
    canvas.itemconfigure(card_img, image=back_img)
    canvas.itemconfigure(title_text, text="English", fill='white')
    canvas.itemconfigure(word_text, text=CARD['English'], fill='white')


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, flip_card)


def known():
    words_list.remove(CARD)
    words_to_learn = pandas.DataFrame(words_list)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    display_card()


def display_card():
    global CARD
    global timer
    CARD = choice(words_list)
    window.after_cancel(id=timer)
    canvas.itemconfigure(card_img, image=front_img)
    canvas.itemconfigure(title_text, text="French", fill='black')
    canvas.itemconfigure(word_text, text=CARD['French'], fill='black')
    timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 267, image=front_img)
title_text = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word_text = canvas.create_text(400, 267, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=known)
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=display_card)
wrong_button.grid(row=1, column=1)

display_card()

window.mainloop()
