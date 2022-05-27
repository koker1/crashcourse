from tkinter import *

def create_window():
    '''new_window = Toplevel()'''
    new_window = Tk()       #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
                            #             其他窗口的“顶部”新窗口，链接到“底部”窗口
                            #Tk() = new independent window
    old_window.destroy()    #close out of old window

old_window = Tk()

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()