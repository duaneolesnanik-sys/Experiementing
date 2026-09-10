import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.btn_text = "Click Me"
        self.my_button = tk.Button(self, text=self.btn_text, command=self.on_click)
        self.my_button.pack()

    def on_click(self):
        print("Button clicked!")

root = tk.Tk()
app = MyFrame(root)
app.pack()
root.mainloop()