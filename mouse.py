from tkinter import Tk, Label,Button


bx = 0
by = 0
ox = 0
oy = 0
held = 0

def press(event):
     global held
     held = 1
def release(event):
     global held
     held = 0

def mouse_event(event):
    global bx, by, ox, oy, held
    print(held)
    if held == 1:
        print("Yes")
        if event.x < 6 and ox > 19:
            bx += 1
        elif event.x > 19 and ox < 6:
            bx -= 1
        if event.y < 6 and oy > 19:
            by += 1
        elif event.y > 19 and oy < 6:
            by -= 1
    label.config(text=f"({event.x}, {event.y})({bx},{by})")
    ox = event.x
    oy = event.y

root2 = Tk()
root2.geometry("300x100")
root = Tk()
label = Label(root2, text="Move your mouse!", font=("Arial", 16))

for i in range(20):
        for p in range(20):
            btn = Button(root, text="     ", bg="white", fg="white")
            btn.grid(row = i, column = p+9)

label.pack()
root.bind("<Button-1>", press)
root.bind("<ButtonRelease>", release)
root.bind("<Motion>", mouse_event)
root.mainloop()