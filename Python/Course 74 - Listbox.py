#listbox = A listing of selectable text items within it's own container
#          它自己的容器中的可选文本项列表

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    print("you have ordered: ")
    #print(listbox.get(listbox.curselection())) #curselection = current selection
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size()) 

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size()) 

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza") #insert 选项
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size()) #根据选项的数量来调整大小

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window,text="submit",command=submit)
submitbutton.pack()

addbutton = Button(window,text="add",command=add)
addbutton.pack()

deletebutton = Button(window,text="delete",command=delete)
deletebutton.pack()

window.mainloop()