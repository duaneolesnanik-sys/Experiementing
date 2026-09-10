from tkinter import Tk, Button, Text, Menu, Frame, Label, Entry
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def open_file(): print("Open file clicked")
def save_file(): print("Save file clicked")
def exit_app(): root.quit()


def save_file():
    file_path = asksaveasfilename(defaultextension=".txt",
                                   filetypes=[("Text Files", "*.txt"), ("HTML Files", "*.html"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get("1.0", "end-1c"))

def open_file():
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            print(file.read())


def change_bg():
    color = askcolor()[1]  # Selects color and retrieves hex value
    if color:
        root.config(bg=color)

root = Tk()
root.geometry("1300x1300")

Button(root, text="Choose Color", command=change_bg).pack()

def print_text():
    content = text_area.get("1.0", "end-1c")  # Retrieves text from the widget
    print(content)

text_area = Text(root, height=10, width=40, font=("Ink Free", 16))
text_area.pack()
Button(root, text="Submit", command=print_text).pack()
Button(root, text="Open File", command=open_file).pack()
text_area = Text(root)
text_area.pack()
Button(root, text="Save File", command=save_file).pack()
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
frame = Frame(root, bg="pink", relief="sunken", borderwidth=5)
frame.pack(fill="both", expand=True)

Button(frame, text="Button 1").pack(side="left")
Button(frame, text="Button 2").pack(side="left")
Label(root, text="First Name:").grid(row=0, column=0)
Entry(root).grid(row=0, column=1)
Label(root, text="Last Name:").grid(row=1, column=0)
Entry(root).grid(row=1, column=1)
Button(root, text="Submit").grid(row=2, column=0, columnspan=2)


root.mainloop()