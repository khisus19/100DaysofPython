from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 15, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_label = Label(
            text="Some Question text", 
            font=("Arial", 18, "italic"), 
            fg=THEME_COLOR, 
            bg="white",
            wraplength=280
        )
        self.question_label.grid(row=1, column=0, columnspan=2)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.user_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.user_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question_label.config(text=q_text)

    def user_true(self):
        self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        time.sleep(1)
        self.get_next_question()

    def user_false(self):
        self.quiz.check_answer("False")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        time.sleep(1)
        self.get_next_question()