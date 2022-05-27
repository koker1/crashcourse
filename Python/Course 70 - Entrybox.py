from tkinter import *

#entry widget = textbox that accepts a single line of user input
#               接受单行用户输入的文本框

def submit():
    username = entry.get()
    print("hello " + username)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)


window = Tk()

entry = Entry(window,
              font=('Arial',50),
              fg="blue",
              bg="black")

'''entry.insert(0,'Spongebob')'''
'''entry.config(state=DISABLED)'''
'''entry.config(show="*")'''

entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()