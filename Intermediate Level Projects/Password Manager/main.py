from tkinter import *
from tkinter import messagebox
import pyperclip
from random import randint, choice, shuffle
import json


# ---------------------------- SEARCH PASSWORD  ------------------------------- #
def search_password():
    website = website_text.get()
    if website:
        try:
            with open("password.json", mode="r") as data_file:
                data = json.load(data_file)
                try:
                    messagebox.showinfo(title=website, message=f"Email : {data[website.lower()]['email']}\nPassword : "
                                                               f"{data[website.lower()]['password']}")
                except KeyError:
                    messagebox.showwarning(title="Oops!!", message=f"{website} doesn't exist.")
        except FileNotFoundError:
            messagebox.showwarning(title="Oops!!", message="File doesn't exist.")
    else:
        messagebox.showwarning(title="Oops!!", message="Website field shouldn't be empty.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_list = [choice(letters) for _ in range(randint(8, 14))] + [choice(numbers) for _ in
                                                                        range(randint(3, 5))] + [choice(symbols) for _
                                                                                                 in
                                                                                                 range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_text.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = website_text.get()
    email = username_text.get()
    password = password_text.get()
    new_data = {
        website.lower(): {
            "email": email,
            "password": password,
        }
    }
    if website and email and password:
        is_ok = messagebox.askyesno(title='Conformation', message=f"You have Entered Following details :\n"
                                                                  f"Website : {website}\n"
                                                                  f"Username : {email}\n"
                                                                  f"Password : {password} \n"
                                                                  f"Is it okay to save?")
        if is_ok:
            try:
                with open("password.json", mode="r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("password.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("password.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

            website_text.delete(0, END)
            password_text.delete(0, END)
    else:
        messagebox.showwarning(title="Warning", message="All fields are required.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website :")
website_label.grid(row=1, column=0, pady=1, padx=1)

username_label = Label(text="Email/Username :")
username_label.grid(row=2, column=0, pady=1, padx=1)

password_label = Label(text="Password :")
password_label.grid(row=3, column=0, pady=1, padx=1)

# Entries
website_text = Entry()
website_text.grid(row=1, column=1, pady=1, padx=1, sticky='EW')
website_text.focus()

username_text = Entry()
username_text.grid(row=2, column=1, columnspan=2, pady=1, padx=1, sticky="EW")
username_text.insert(0, "codingismagic@gmail.com")

password_text = Entry()
password_text.grid(row=3, column=1, pady=1, padx=1, sticky='EW')

# Buttons
get_password = Button(text='Get Password', command=generate_password)
get_password.grid(row=3, column=2, sticky='EW')

search = Button(text='Search', command=search_password)
search.grid(row=1, column=2, sticky="EW")

add = Button(text="Add", command=add_to_file)
add.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
