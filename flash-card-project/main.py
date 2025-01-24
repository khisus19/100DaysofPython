import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
pt_word = ""
sp_word = ""
current_word_pair = []

#####--------------------- Data -------------------------#####
df = pd.read_csv("./data/portuguese_words.csv")
pt_words_dict = df.to_dict("records")


def next_card():
    global pt_word, sp_word, flip_timer, current_word_pair

    # Fetching new word pair
    current_word_pair = random.choice(pt_words_dict)
    pt_word = current_word_pair["Portuguese"]
    sp_word = current_word_pair["Spanish"]

    window.after_cancel(flip_timer)

    # Update the card pt_word_canvas
    canvas.create_image(400, 270, image=front_card)
    canvas.create_text(400, 150, text="Portuguese", font=("Arial", 35, "italic"), fill="black")
    canvas.create_text(400, 280, text=pt_word, font=("Arial", 60, "bold"), fill="black")


    flip_timer = window.after(3000, flip_card)
    

#####--------------------- Flip Card -------------------------#####

def flip_card():
    canvas.create_image(400, 270, image=back_card)
    canvas.create_text(400, 150, text="Spanish", font=("Arial", 35, "italic"), fill="white")
    canvas.create_text(400, 280, text=sp_word, font=("Arial", 60, "bold"), fill="white")



#####--------------------- Remove learned word -------------------------#####
def remove_word():
    global current_word_pair
    pt_words_dict.remove(current_word_pair)
    print(current_word_pair)
    print(len(pt_words_dict))
    next_card()


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

flip_timer = window.after(3000, flip_card)


# Card title
card_title_canvas = canvas.create_text(400, 150, text="", font=("Arial", 35, "italic"))

# Card pt_word_canvas
pt_word_canvas = canvas.create_text(400, 280, text="", font=("Arial", 60, "bold"))


# Correct button
right_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=remove_word)
right_btn.grid(row=1, column=0)



# Incorrect button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)


next_card()


window.mainloop()