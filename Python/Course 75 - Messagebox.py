from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    '''messagebox.showinfo(title='this is an info messagebox',message='you are a person')'''
    
    '''messagebox.showwarning(title='WARNING!',message='you HAVE a VIRUS!')'''
    
    '''messagebox.showerror(title='ERROR!',message='something went wrong')'''

    '''if messagebox.askokcancel(title='ask ok cancel',message='do you want to do the thing?'):
        print("you did a thing!")
    else:
        print("you canceled a thing!")'''

    '''if messagebox.askretrycancel(title='ask retry cancel',message='do you want to retry the thing?'):
        print("you retried a thing!")
    else:
        print("you canceled a thing!")'''

    '''if messagebox.askyesno(title='ask yes no',message='do you like cake?'):
        print("you like cake!")
    else:
        print("you dont like cake")'''

    '''answer = messagebox.askquestion(title='ask question',message='do you like pie?')
    if answer == 'yes':
        print("you like pie")
    else:
        print("you dont like pie")'''

    '''answer = messagebox.askyesnocancel(title='yes no cancel',message='do you like to code?',icon='info')
    if answer == True:
        print("you like to code")
    elif answer == False:
        print("you dont like to code")
    else:
        print("you have dodged a question")'''
    
window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()