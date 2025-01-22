from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Drawing the card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 273, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

# Card title
card_title = canvas.create_text(400, 150, text="Portuguese", font=("Arial", 35, "italic"))

# Card pt_word
pt_word = canvas.create_text(400, 280, text="Palavra", font=("Arial", 60, "bold"))


# Correct button
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0)
right_btn.grid(row=1, column=0)


# Incorrect button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0)
wrong_btn.grid(row=1, column=1)





window.mainloop()