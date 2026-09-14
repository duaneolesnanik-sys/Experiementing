from tkinter import Tk, Button, Text, Menu, Label, Entry, Scale
from tkinter.colorchooser import askcolor



def begin(size):
    pixart = Tk()
    pixart.title("Pixel Artist")
    buttons = []
    color = "white"
    colorer = Tk()
    colorer.geometry("150x20")

    def get_color():
        nonlocal color
        color = askcolor()[1]
        pixart.config(bg=color)
        
    def change_color(x, y):
        buttons[y][x].config(bg=color,fg = color)

    rx = 0
    ry = 0
    bx = 0
    by = 0
    ox = 0
    oy = 0
    held = 0
    brush = []

    def press(event):
        nonlocal held, rx, ry , bx, by, brush
        held = 1
        bx = rx
        by = ry

    def release(event):
        nonlocal held, rx, ry, bx ,by, brush
        held = 0
        rx = bx
        ry = by
        brush = []

    def mouse_event(event):
        nonlocal bx, by, ox, oy, held, rx, ry, brush
        if held == 1:
            if event.x%25 < 6 and ox%25 > 19:
                bx += 1
            elif event.x%25 > 19 and ox%25 < 6:
                bx -= 1
            if event.y%25 < 6 and oy%25 > 19:
                by += 1
            elif event.y%25 > 19 and oy%25 < 6:
                by -= 1
        else:
            if event.x < 6 and ox > 19:
                rx += 1
            elif event.x > 19 and ox < 6:
                rx -= 1
            if event.y < 6 and oy > 19:
                ry += 1
            elif event.y > 19 and oy < 6:
                ry -= 1
        ox = event.x
        oy = event.y
        j = True
        for k in brush:
            if k == [bx,by]:
                j = False
        if j:
            brush += [[bx,by]]
            change_color(bx,by)

    Button(colorer, text="Color", command= lambda : get_color()).pack()
   
    for i in range(size):
        buttons.append([])
        for p in range(size):
            btn = Button(pixart, text="     ", bg="white", fg="white", command = lambda x = p, y = i: change_color(x,y) )
            btn.grid(row = i, column = p+9)
            buttons[i].append(btn)

    pixart.bind("<Button-1>", press)
    pixart.bind("<ButtonRelease>", release)
    pixart.bind("<Motion>", mouse_event)
    pixart.mainloop()
    colorer.mainloop()

set_up = Tk()
set_up.title("Size Selecter")
set_up.geometry("500x250")
scale = Scale(set_up, from_=10, to=50, orient="horizontal", length=300, label="Select a Value", font=("Arial", 14), tickinterval=10)
scale.pack(pady=20)
confirm = Button(set_up, text = "Confirm", command = lambda: begin(scale.get()))
confirm.pack(pady=20)

set_up.mainloop()



    
    


