from tkinter import *

def calculate():
    km_amount = float(input.get())
    miles_result = km_amount * 1.609
    result_label.config(text=miles_result)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=150)
window.config(padx=20, pady=20)


input = Entry()
input.config(padx=10, pady=10)
input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()