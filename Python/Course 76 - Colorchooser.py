from tkinter import *
from tkinter import colorchooser #submodule 子模块

def click():
    '''color = colorchooser.askcolor() #assign color to a variable 将颜色分配给变量
    #print(color) 
    colorHex = color[1] #assign element at index 1 to a variable 将索引 1 处的元素分配给变量
    #print(colorHex)
    window.config(bg=colorHex) #change background color'''

    #or
    '''color = colorchooser.askcolor()
    window.config(bg=color[1])'''

    #or
    '''window.config(bg=colorchooser.askcolor()[1])'''

window = Tk()
window.geometry("420x420")
button = Button(text="click me",command=click)
button.pack()
window.mainloop()