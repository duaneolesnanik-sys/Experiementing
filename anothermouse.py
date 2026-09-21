from tkinter import *
import random

window = Tk()
window.geometry("2500x500")

#22-40 = -1, 41-58 = -2, 59-77 = -3, 78-96 = -4
#209-402 = +1, 403-597 = +2, 598-791 = +3, 792-986 = +4
lw =22 #random.randint(20,4000)
lh = 5
w = lw *(97/13+117/16)/2 + (16-lw)/3 
if lw > 21:
    w -= (lw-21)/17
if lw > 28 and w < 208:
    w +=1 
if lw > 208:
    w += (lw-208)/194
print(lw)
h = lh *16.2

move_over = w - 500

# Function to initialize the drag by capturing the initial mouse position
def drag_start(event):
    widget = event.widget  # Get the widget (label) that is being interacted with
    widget.startX = event.x  # Store the starting X position of the mouse within the widget
    widget.startY = event.y  # Store the starting Y position of the mouse within the widget

# Function to handle the motion of the mouse while dragging
def drag_motion(event):
    widget = event.widget  # Get the widget (label) that is being dragged
    # Calculate the new position by considering the current widget position and the mouse movement
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    # Move the widget to the new position using the `place` method
    widget.place(x=x, y=y)

# Create a red label with a specified size (width=10, height=5) and set its position to (0, 0)
label = Label(window, bg="red", width=lw, height=lh)
label.place(x=0-move_over, y=0)  # Position the label at coordinates (0, 0)

# Create a blue label with a specified size (width=10, height=5) and set its position to (100, 100)
label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=w-move_over, y=10)  # Position the label at coordinates (100, 100)

label3 = Label(window, bg="green", width=10, height=5)
label3.place(x=10, y=h)

# Bind the left mouse button click event to start dragging (drag_start function) for the first label
label.bind("<Button-1>", drag_start)
# Bind the left mouse button motion event to move the label (drag_motion function) while dragging
label.bind("<B1-Motion>", drag_motion)

# Bind the left mouse button click event to start dragging (drag_start function) for the second label
label2.bind("<Button-1>", drag_start)
# Bind the left mouse button motion event to move the label (drag_motion function) while dragging
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()