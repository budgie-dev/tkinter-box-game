import tkinter as tk
from random import randint
from threading import Thread
from time import sleep

root = tk.Tk()
root.geometry('700x750')

gridlist = []
litupold = []
posold = []

for i in range(49):
    gridlist.append(tk.Canvas(bg='white', height=100, width=100))
    litupold.append(False)
    posold.append(-69)

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
gameovercheck = False
pointlabel = tk.Label(text=f'Points: {points}', font='Terminus 30')
pointlabel.place(y=700)

def gameover():
    global pointlabel, gridlist, gameovercheck
    if gameovercheck == True:
        pass
    else:
        for i in range(49):
            gridlist[i].place_forget()
        pointlabel.place_forget()
        root.unbind_all('siur')
        for i in range(5):
            tk.Label().pack()
        tk.Label(text='No i ciul, przegrałeś.', font='Terminus 30').pack()
        gameovercheck = True

def poscheck(posvar, list):
    global applepos, applestatus, points, pointlabel, posold, litupold
    for i in range(49):
        if posvar == i:
            list[i].config(bg='green')
        else:
            if i == posold:
                pass
            else:
                list[i].config(bg='white')
                litupold[i] = False

        
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
        
        if posold[0] != -69:
            list[posold[0]].config(bg='green')
            litupold[posold[0]] = True
        
        #game over christopher
        if litupold[i] == True:
            if posvar == i:
                gameover()
                exit()
        
lastup = False
lastdown = False
lastright = False
lastleft = False

def up():
    global pos, gridlist, posold
    if pos in (0,1,2,3,4,5,6):
        exit()
    else:
        posold[0] = pos
        pos -= 7
        poscheck(pos, gridlist)

def left():
    global pos, gridlist, posold
    if pos in (0,7,14,21,28,35,42):
        exit()
    else:
        posold[0] = pos
        pos -= 1
        poscheck(pos, gridlist)

def right():
    global pos, gridlist, posold
    if pos in (6,13,20,27,34,41,48):
        exit()
    else:
        posold[0] = pos
        pos += 1
        poscheck(pos, gridlist)

def down():
    global pos, gridlist, posold
    if pos in (42,43,44,45,46,47,48):
        exit()
    else:
        posold[0] = pos
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
        sleep(0.1)
        if lastup == False:
            exit()
        up()

def downloop():
    global lastup, lastdown, lastright, lastleft
    lastupdate('down')
    while True:
        sleep(0.1)
        if lastdown == False:
            exit()
        down()

def rightloop():
    global lastup, lastdown, lastright, lastleft
    lastupdate('right')
    while True:
        sleep(0.1)
        if lastright == False:
            exit()
        right()

def leftloop():
    global lastup, lastdown, lastright, lastleft
    lastupdate('left')
    while True:
        sleep(0.1)
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

root.bind('<Up>', upstart)
root.bind('<Down>', downstart)
root.bind('<Left>', leftstart)
root.bind('<Right>', rightstart)

poscheck(pos, gridlist)

root.mainloop()
