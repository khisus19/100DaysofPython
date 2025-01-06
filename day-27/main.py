import tkinter as tk

window = tk.Tk()
window.title("My first GUI Program")
window.minsize( 500, 300)

# Label
my_label = tk.Label(window, text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()




window.mainloop()