from tkinter import Tk, Button, Text, Menu, Label, Entry, Scale
from tkinter.colorchooser import askcolor



def begin(size):
    #Variables
    if True:
        pixart = Tk()
        pixart.title("Pixel Artist")
        pixart.config(bg = "black")
        buttons = []
        color = "white"
        colorer = Tk()
        colorer.geometry("150x25")
        rx = 0
        ry = 0
        bx = 0
        by = 0
        ox = 0
        oy = 0
        held = 0
        brush = []
        outboundx = 0
        outboundy = 0
    #--------------

    #Events/functions
    if True:
        def get_color():
            nonlocal color
            color = askcolor()[1]
            #pixart.config(bg=color)
            
        def change_color(x, y):
            buttons[y][x].config(bg=color,fg = color)

        def press(event):
            nonlocal held, rx, ry , bx, by, brush
            held = 1
            #bx = rx
            #by = ry

        def release(event):
            nonlocal held, rx, ry, bx ,by, brush
            held = 0
            rx = bx
            ry = by
            brush = []

        def mouse_event(event):
            nonlocal bx, by, ox, oy, held, rx, ry, brush, outboundx, outboundy
            #---Movement---
            if True:
                if held == 1:
                    bx = int((event.x-event.x%20)/20) +rx
                    by = int((event.y-event.y%20)/20) +ry 
                    if bx > size-1:
                        bx = size-1
                    if by > size-1:
                        by = size -1    
                else:
                    if event.x < 6 and ox > 14:
                        rx += 1
                    elif event.x > 14 and ox < 6:
                        rx -= 1
                    if event.y < 6 and oy > 14:
                        ry += 1
                    elif event.y > 14 and oy < 6:
                        ry -= 1
                print(f"{event.x},{event.y}")
            #--------------

            #---Out of bounds---
            if True:
                if event.x > 20*(size+1):
                    outboundx = 1
                elif outboundx == 1:
                    rx = size-1
                    ry = int((oy-(oy%20)-40)/20)
                    outboundx = 0

                if event.y > 20*(size+1):
                    outboundy = 1
                elif outboundy == 1:
                    ry = size-1
                    rx = int((ox-(ox%20)-40)/20)
                    outboundy = 0

                
            #-------------------

            #---Brush---
            if True:
                ox = event.x
                oy = event.y
                if bx < 0:
                    bx = 0
                if by < 0:
                    by = 0
                j = True
                for k in brush:
                    if k == [bx,by] or brush == []:
                        j = False
                if j:
                    brush += [[bx,by]]
                    change_color(bx,by)
            #-----------
    #--------------

    #Set-up
    if True:
        Button(colorer, text="Color", command= lambda : get_color()).pack()
        Label(pixart, text="     ", fg = "green", bg = "green").grid(row = 0, column = 0)
        Label(pixart, text="     ", fg = "green", bg = "green").grid(row = size+1, column = size+1)
        for y in range(size):
            buttons.append([])
            for x in range(size):
                btn = Label(pixart, text = "     ")
                #btn = Button(pixart, text="     ", bg="white", fg="white", command = lambda x = p, y = i: change_color(x,y) )
                btn.grid(row = y+1, column = x+1)
                buttons[y].append(btn)

        pixart.bind("<Button-1>", press)
        pixart.bind("<ButtonRelease>", release)
        pixart.bind("<Motion>", mouse_event)
        pixart.mainloop()
        colorer.mainloop()
    #--------------

set_up = Tk()
set_up.title("Size Selecter")
set_up.geometry("500x250")
scale = Scale(set_up, from_=10, to=50, orient="horizontal", length=300, label="Select a Value", font=("Arial", 14), tickinterval=10)
scale.pack(pady=20)
confirm = Button(set_up, text = "Confirm", command = lambda: begin(scale.get()))
confirm.pack(pady=20)

set_up.mainloop()



    


