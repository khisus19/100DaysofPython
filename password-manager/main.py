from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]    
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    random_password = "".join(password_list)
    
    pyperclip.copy(random_password)
            
    password_input.delete(0, "end")
    password_input.insert(0, random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("./data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("./data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
        
            with open("./data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")
            website_input.focus()

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    web_name = website_input.get()

    try:
        with open("./data.json", "r") as file:
            # Reading old data
            data = json.load(file)
            searched_email = data[web_name]["email"]
            searched_pwd = data[web_name]["password"]
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found")
    except KeyError:
        messagebox.showinfo("Error", "No details for the website exists")
    else:
        messagebox.showinfo(web_name, f"Email: {searched_email} \nPassword: {searched_pwd} ")

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
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

username_input = Entry(width=39)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "khisus19@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
search_btn = Button(text="Search", width=14, bg="blue", command=search_password)
search_btn.grid(row=1, column=2)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)



screen.mainloop()