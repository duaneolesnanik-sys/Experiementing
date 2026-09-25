from tkinter import Tk, Canvas, PhotoImage

def move_up(event):
    canvas.move(image, 0, -10)
def move_down(event):
    canvas.move(image, 0, 10)
def move_left(event):
    canvas.move(image, -10, 0)
def move_right(event):
    canvas.move(image, 10, 0)

root = Tk()
canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack()

photo = PhotoImage(file="car.png")  # Use an image in your directory
image = canvas.create_image(200, 200, image=photo)

root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.mainloop()