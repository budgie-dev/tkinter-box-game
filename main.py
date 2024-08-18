import tkinter as tk
from random import randint

root = tk.Tk()
root.geometry('700x750')

gridlist = []
for i in range(49):
    gridlist.append(tk.Canvas(bg='white', height=100, width=100))

defx = -100
defy = -100
gridlistitem = 0
for i in range(7):
    defy += 100
    defx = -100
    for j in range(7):
        defx+= 100
        gridlist[gridlistitem].place(x=defx, y=defy)
        gridlistitem += 1
    
pos = 4
applestatus = False
applepos = -1
points = 0
pointlabel = tk.Label(text=f'Points: {points}', font='Terminus 30')
pointlabel.place(y=700)

def poscheck(posvar, list):
    global applepos, applestatus, points, pointlabel
    for i in range(49):
        if posvar == i:
            list[i].config(bg='green')
        if posvar == i:
            pass
        else:
            list[i].config(bg='white')
        
        #collision
        if posvar == applepos:
             applestatus = False
             points +=1
             pointlabel.config(text=f'Points: {points}')
             
        #applepos calculate
        if applestatus == False:
            applepos = randint(0, 48)
        while applepos == posvar:
            applepos = randint(0,48)
        
        #add da apple
        list[applepos].config(bg='red')
        applestatus = True
        

def up(event):
    global pos, gridlist
    if pos in (0,1,2,3,4,5,6):
        pass
    else:
        pos -= 7
        poscheck(pos, gridlist)

def left(event):
    global pos, gridlist
    if pos in (0,7,14,21,28,35,42):
        pass
    else:
        pos -= 1
        poscheck(pos, gridlist)

def right(event):
    global pos, gridlist
    if pos in (6,13,20,27,34,41,48):
        pass
    else:
        pos += 1
        poscheck(pos, gridlist)

def down(event):
    global pos, gridlist
    if pos in (42,43,44,45,46,47,48):
        pass
    else:
        pos += 7
        poscheck(pos, gridlist)
                
root.bind('w', up)
root.bind('d', right)
root.bind('a', left)
root.bind('s', down)
poscheck(pos, gridlist)

root.mainloop()