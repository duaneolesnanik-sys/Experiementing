from tkinter import Tk, Label,Button, Canvas

rx = 0
ry = 0
bx = 0
by = 0
ox = 0
oy = 0
held = 0

def press(event):
    global held, rx, ry , bx, by
    held = 1
    bx = rx
    by = ry

def release(event):
    global held, rx, ry, bx ,by
    held = 0
    rx = bx
    ry = by

def mouse_event(event):
    global bx, by, ox, oy, held, rx, ry
    print(event.x,",",event.y)
    
    if held == 1:
        bx = rx+(event.x-event.x%25)/25
        by = ry+(event.y-event.y%25)/25
        """
        if event.x%25 < 6 and ox%25 > 19:
            bx += 1
        elif event.x%25 > 19 and ox%25 < 6:
            bx -= 1
        if event.y%25 < 6 and oy%25 > 19:
            by += 1
        elif event.y%25 > 19 and oy%25 < 6:
            by -= 1
            """
    else:
        if event.x < 6 and ox > 14:
            rx += 1
        elif event.x > 14 and ox < 6:
            rx -= 1
        if event.y < 6 and oy > 14:
            ry += 1
        elif event.y > 14 and oy < 6:
            ry -= 1
    label.config(text= f"({rx}, {ry})({bx},{by})({event.x},{event.y})")
    ox = event.x
    oy = event.y

root2 = Tk()
root2.geometry("300x100")
root = Tk()
label = Label(root2, text="Move your mouse!", font=("Arial", 16))

canvas = Canvas(root, width=400, height=400, bg="white")
canvas.grid(row = 0,column = 0)#pack()
canvas2 = Canvas(root, width=200, height = 400, bg = "blue")
canvas2.grid(row=0,column = 1)#pack()

j = canvas.create_rectangle(50, 50, 150, 150, fill="purple")
print(j)
#j.config(fill = "green")

#Label(root, text = "     ", fg = "green", bg = "green").grid(row = 0, column = 0)
#Label(root, text = "     ", fg = "green", bg = "green").grid(row = 0, column = 22)
#Label(root, text = "     ", fg = "green", bg = "green").grid(row = 22, column = 0)
#Label(root, text = "     ", fg = "green", bg = "green").grid(row = 22, column = 22)

for i in range(20):
        for p in range(20):
            btn = Label(root, text = "     ")
            #btn = Button(root, text="     ", bg="white", fg="white")
            #btn.grid(row = i+1, column = p+1)

label.pack()
root.bind("<Button-1>", press)
root.bind("<ButtonRelease>", release)
root.bind("<Motion>", mouse_event)
root.mainloop()