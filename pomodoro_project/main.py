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
CHECKMARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(103, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


timer_label = Label(window, text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

check_marks_label = Label(window, text=f"{CHECKMARK}", font=(FONT_NAME, 14), fg=GREEN, bg=YELLOW)
check_marks_label.grid(row=3, column=1)

start_button = Button(text="Start", command=None, font=("Helvetica", 14, "normal"), highlightthickness=0, bg=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=None, font=("Helvetica", 14, "normal"), highlightthickness=0, bg=YELLOW)
reset_button.grid(row=2, column=2)

window.mainloop()