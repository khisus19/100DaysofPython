from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(bg="white", padx=50, pady=50)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg="white", width=18)
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", bg="white")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=39)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_input = Entry(width=39)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "khisus19@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
generate_btn = Button(text="Generate Password")
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36)
add_btn.grid(row=4, column=1, columnspan=2)

screen.mainloop()