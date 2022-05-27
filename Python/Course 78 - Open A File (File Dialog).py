from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Program Files",
                                          title="Open",
                                          filetypes=(("text files","*.txt"), #only .txt format file
                                          ("all files","*.*"))) #all format file
    file = open(filepath,'r') #r = read
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()