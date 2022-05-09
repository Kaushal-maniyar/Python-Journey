from tkinter import *


def on_click():
    text = float(my_input.get())
    answer['text'] = round(text * 1.6, 2)


# Window
window = Tk()
window.title("Miles to Kms Converter!")
window.minsize(width=200, height=100)
window.config(padx=12, pady=12)


# Label
# Miles
miles = Label(text="Miles")
miles.grid(row=0, column=3)

# Equal
equal = Label(text="is equal to")
equal.grid(row=1, column=0)

# Answer
answer = Label(text="0")
answer.grid(row=1, column=1)

# kilo Meter
km = Label(text="Km")
km.grid(row=1, column=2)


# Button
calculate = Button(text="Calculate", command=on_click)
calculate.grid(row=2, column=1)

# Entry
my_input = Entry(width=10)
my_input.grid(row=0, column=1)


window.mainloop()
