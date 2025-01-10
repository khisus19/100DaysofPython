import tkinter as tk

window = tk.Tk()
window.title("My first GUI Program")
window.minsize( 500, 300)


def button_clicked():
    input_text = input.get()
    my_label.config(text=input_text)

# Label
my_label = tk.Label(window, text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Button 2
new_button = tk.Button(text="Click me too")
new_button.grid(column=2, row=0)

# Entry

input = tk.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()