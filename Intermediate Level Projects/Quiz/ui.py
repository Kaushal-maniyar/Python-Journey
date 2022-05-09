from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.score = 0
        self.quizz = quiz
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Label
        self.score_label = Label(text=f"Score : {self.score}", fg="white", bg=THEME_COLOR, font=("Arial", 18, "normal"))
        self.score_label.grid(row=0, column=1, pady=5, padx=5)

        # Button
        self.right_img = PhotoImage(file="./images/true.png")
        self.right = Button(image=self.right_img,
                            highlightthickness=0,
                            command=lambda: self.check("true"))
        self.right.grid(row=2, column=0, padx=5, pady=5)

        self.wrong_img = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=self.wrong_img,
                            highlightthickness=0,
                            command=lambda: self.check("false"))
        self.wrong.grid(row=2, column=1, padx=5, pady=5)

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=5, padx=5)
        self.text = self.canvas.create_text(150,
                                            125,
                                            width=290,
                                            text="Hello",
                                            fill="black",
                                            font=("Arial", 15, "normal"))

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quizz.still_has_question():
            self.right.config(state="active")
            self.wrong.config(state="active")
            q_text = self.quizz.next_question()
            self.canvas.config(bg="white")
            self.canvas.itemconfigure(self.text, fill="black", text=q_text)
        else:
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
            self.canvas.config(bg="white")
            self.canvas.itemconfigure(self.text, fill="black", text="You've done it. Quiz is completed.")

    def check(self, given_ans: str):
        self.right.config(state="disabled")
        self.wrong.config(state="disabled")
        actual_ans = self.quizz.check_answer()
        if given_ans == actual_ans.lower():
            self.score += 1
            self.canvas.config(bg="green")
            self.canvas.itemconfigure(self.text, fill="white")
            self.score_label.config(text=f"Score : {self.score}")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfigure(self.text, fill="white")
        self.window.after(1000, self.next_question)
