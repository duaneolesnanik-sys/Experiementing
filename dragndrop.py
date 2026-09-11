from tkinter import Tk, Label

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

root = Tk()
label = Label(root, text="Drag Me!", bg="lightblue", width=10, height=2)
label.place(x=100, y=100)
label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)
root.mainloop()