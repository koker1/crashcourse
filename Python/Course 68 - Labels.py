from tkinter import *

#labels = an area widget that holds text and/or an image within a window
#         在窗口中保存文本和/或图像的区域小部件

window = Tk()

photo = PhotoImage(file='C:\\Users\\crash\\Downloads\\download.png')

label = Label(window,
              text="hello world",
              font=('Arial',40,'bold'),
              foreground='blue',
              background='black',
              relief=RAISED,
              border=10,
              padx=20, #pad = add space between word and border
              pady=20,
              image=photo,
              compound='bottom')
label.pack()
'''label.place(x=0,y=0)'''

window.mainloop()