from tkinter import Tk, Label

def key_pressed(event):
    label.config(text=f"You pressed: {event.keysym}")

root = Tk()
label = Label(root, font=("Arial", 24))
label.pack()
root.bind("<Key>", key_pressed)
root.mainloop()