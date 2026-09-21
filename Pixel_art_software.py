from tkinter import Tk, Button, Text, Menu, Label, Entry, Scale
from tkinter.colorchooser import askcolor

def begin(size):
    pixart = Tk()
    pixart.title("Pixel Artist")
    pixart.config(bg = "green")
    locations = []
    color = "white"

    def color_select():
        nonlocal color
        color = askcolor()[1]
        pixart.config(bg=color)

    def begin_stroke():
        print()

    for rows in range(size):
        for columns in range(size):
            square = Label(pixart, text = "      ")
            square.grid(row = rows, column = columns)
            locations += [square]
    color_choser = Button(pixart,text = "Color", command = color_select).grid(row = size+1, column = size+1)
    pixart.bind("<Button-1>",)
    pixart.bind("<ButtonRelease>",)
    pixart.bind("<Motion>",)
    pixart.mainloop()


set_up = Tk()
set_up.title("Size Selecter")
set_up.geometry("500x250")
scale = Scale(set_up, from_=10, to=50, orient="horizontal", length=300, label="Select a Value", font=("Arial", 14), tickinterval=10)
scale.pack(pady=20)
confirm = Button(set_up, text = "Confirm", command = lambda: begin(scale.get()))
confirm.pack(pady=20)
set_up.mainloop()