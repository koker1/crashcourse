from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x) + "," + str(event.y))


window = Tk()

#window.bind(event,function)
#window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #mouse scroll
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething) #leave the window
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<Motion>",doSomething) #where the mouse moved

window.mainloop()