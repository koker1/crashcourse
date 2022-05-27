#radio button = similar to checkbox, but you can only select one from a group
#               类似于复选框，但您只能从一组中选择一个

from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("you ordered pizza")
    elif(x.get()==1):
        print("you ordered hamburger")
    elif(x.get()==2):
        print("you ordered hotdog")
    else:
        print("jm9?")

window = Tk()

pizzaImage = PhotoImage(file='C:\\Users\\crash\\Downloads\\pizza.png')
hamburgerImage = PhotoImage(file='C:\\Users\\crash\\Downloads\\hamburger.png')
hotdogImage = PhotoImage(file='C:\\Users\\crash\\Downloads\\hotdog.png')
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #add text to radio button
                              variable=x, #group radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx=25, #adds padding on x-axis
                              font=('Impact',50),
                              image= foodImages[index], #adds image to radiobutton
                              compound=LEFT, #add image & text (left side)
                              indicatoron=0, #eliminate circle indicators 消除圆圈指标
                              width=375, #sets width of radiobuttons
                              command=order #set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)

window.mainloop()