from tkinter import Tk, Button, Text, Menu, Label, Entry, Scale
from tkinter.colorchooser import askcolor

def begin(size):
    pixart = Tk()
    pixart.title("Pixel Artist")
    buttons = []
    color = "white"

    def get_color():
        nonlocal color
        color = askcolor()[1]
        pixart.config(bg=color)
        
    def change_color(x, y):
        buttons[y][x].config(bg=color,fg = color)

    Button(pixart, text="Color", command= lambda : get_color()).grid(row = 11, column = 4)
   
    for i in range(size):
        buttons.append([])
        for p in range(size):
            btn = Button(pixart, text="     ", bg="white", fg="white", command = lambda x = p, y = i: change_color(x,y) )
            btn.grid(row = i, column = p+9)
            buttons[i].append(btn)

    pixart.mainloop()

set_up = Tk()
set_up.title("Size Selecter")
set_up.geometry("500x250")
scale = Scale(set_up, from_=10, to=50, orient="horizontal", length=300, label="Select a Value", font=("Arial", 14), tickinterval=10)
scale.pack(pady=20)
confirm = Button(set_up, text = "Confirm", command = lambda: begin(scale.get()))
confirm.pack(pady=20)

set_up.mainloop()



    
    


