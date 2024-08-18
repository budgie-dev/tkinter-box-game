import tkinter as tk
from random import randint
from threading import Thread
from time import sleep

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
    
pos = 24
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
        
lastup = False
lastdown = False
lastright = False
lastleft = False

def up():
    global pos, gridlist
    if pos in (0,1,2,3,4,5,6):
        pass
    else:
        pos -= 7
        poscheck(pos, gridlist)

def left():
    global pos, gridlist
    if pos in (0,7,14,21,28,35,42):
        pass
    else:
        pos -= 1
        poscheck(pos, gridlist)

def right():
    global pos, gridlist
    if pos in (6,13,20,27,34,41,48):
        pass
    else:
        pos += 1
        poscheck(pos, gridlist)

def down():
    global pos, gridlist
    if pos in (42,43,44,45,46,47,48):
        pass
    else:
        pos += 7
        poscheck(pos, gridlist)
                
def lastupdate(lastdirection):
    global lastup, lastdown, lastright, lastleft
    lastup = False
    lastdown = False
    lastright = False
    lastleft = False
    match lastdirection:
        case 'up':
            lastup = True
        case 'down':
            lastdown = True
        case 'right':
            lastright = True
        case 'left':
            lastleft = True

    
def uploop():
    global lastup, lastdown, lastright, lastleft
    lastupdate('up')
    while True:
        sleep(0.3)
        if lastup == False:
            exit()
        up()

def downloop():
    global lastup, lastdown, lastright, lastleft
    lastupdate('down')
    while True:
        sleep(0.3)
        if lastdown == False:
            exit()
        down()

def rightloop():
    global lastup, lastdown, lastright, lastleft
    lastupdate('right')
    while True:
        sleep(0.3)
        if lastright == False:
            exit()
        right()

def leftloop():
    global lastup, lastdown, lastright, lastleft
    lastupdate('left')
    while True:
        sleep(0.3)
        if lastleft == False:
            exit()
        left()
def leftstart(event):
    global lastleft
    if lastleft == False:
        Thread(target=leftloop).start()
def upstart(event):
    global lastup
    if lastup == False:
        Thread(target=uploop).start()
def downstart(event):
    global lastdown
    if lastdown == False:
        Thread(target=downloop).start()
def rightstart(event):
    global lastright
    if lastright == False:
        Thread(target=rightloop).start()

root.bind('w', upstart)
root.bind('s', downstart)
root.bind('a', leftstart)
root.bind('d', rightstart)

poscheck(pos, gridlist)

root.mainloop()
