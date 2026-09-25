from tkinter import Tk, Canvas

root = Tk()
canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Draw shapes
canvas.create_line(0, 0, 400, 400, fill="blue", width=5)
canvas.create_rectangle(50, 50, 150, 150, fill="purple")
canvas.create_polygon(200, 0, 300, 100, 100, 100, fill="yellow")
canvas.create_arc(50, 200, 150, 300, start=0, extent=180, fill="red")

canvas.create_image(0,0)
root.mainloop()