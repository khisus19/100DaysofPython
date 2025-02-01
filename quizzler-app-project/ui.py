from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        label_score = Label(text="Score: 0", font=("Arial", 15, "normal"))
        label_score.grid(row=0, column=1)
        label_question = Label(bg="white", text="This is the question", font=("Arial", 20, "italic"))
        label_question.grid(row=1, column=0, columnspan=2)

        self.window.mainloop()