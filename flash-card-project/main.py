import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

#####--------------------- Data -------------------------#####
df = pd.read_csv("./data/portuguese_words.csv")
pt_words_dict = df.to_dict("split")


def fetch_word():
    new_word_pair = random.choice(pt_words_dict["data"])
    new_pt_word, new_sp_word = new_word_pair
    # Update the card pt_word
    canvas.itemconfig(card_title, text="Portuguese")
    canvas.itemconfig(pt_word, text=new_pt_word)
    
    print(new_pt_word)
    print(new_sp_word)


#####--------------------- UI -------------------------#####

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Drawing the card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 270, image=front_card)
canvas.grid(row=0, column=0, columnspan=2)

# Card title
card_title = canvas.create_text(400, 150, text="", font=("Arial", 35, "italic"))

# Card pt_word
pt_word = canvas.create_text(400, 280, text="", font=("Arial", 60, "bold"))


# Correct button
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=fetch_word)
right_btn.grid(row=1, column=0)


# Incorrect button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=fetch_word)
wrong_btn.grid(row=1, column=1)


fetch_word()


window.mainloop()