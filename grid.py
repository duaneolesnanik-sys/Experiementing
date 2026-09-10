from tkinter import Tk, Label, Entry, Button

root = Tk()
Label(root, text="First Name:").grid(row=0, column=0)
Entry(root).grid(row=0, column=1)
Label(root, text="Last Name:").grid(row=1, column=0)
Entry(root).grid(row=1, column=1)
Button(root, text="Submit").grid(row=2, column=0, columnspan=2)
Label(root, text="Clarence").grid(row=3, column = 2)
Label(root, text="Clarence").grid(row=4, column = 3)
Label(root, text="Clarence").grid(row=5, column = 4)


root.mainloop()
