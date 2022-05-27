from tkinter import *

def doSomething(event):
    print("You pressed: "+ event.keysym)
    label.config(text=event.keysym)

window = Tk()

#format = window.bind(event,function)
window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()