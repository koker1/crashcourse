from tkinter import *

#widgets = GUI elements: buttons, textboxes, labels, images
#          GUI 元素：按钮、文本框、标签、图像
#windows = serves as a container to hold or contain these widgets
#          用作容纳或包含这些小部件的容器

window = Tk() #instantiate an instance of a window
#              实例化一个窗口实例
window.geometry("420x420") #size of the window
window.title("Koker first GUI program") #set the title of the window 

icon = PhotoImage(file='C:\\Users\\crash\\Downloads\\0-7229_coca-cola-logo-coca-cola.png') #setup icon of the window
window.iconphoto(True,icon)
window.config(background="#abbdff") #change the background colour
#hex color picker find in google

window.mainloop() #place window on computer screen, listen for events   
#                  在电脑屏幕上放置窗口，监听事件