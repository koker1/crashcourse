from tkinter import *

def display():
    if(x.get()==True):
        print("you agree")
    else:
        print("you don't agree")

window = Tk()

x = BooleanVar()

python_photo = PhotoImage(file='C:\\Users\\crash\\Downloads\\download.png')

check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Times New Roman',20),
                           fg="green",
                           bg="black",
                           activeforeground="green",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=python_photo,
                           compound=LEFT)

check_button.pack()

window.mainloop()