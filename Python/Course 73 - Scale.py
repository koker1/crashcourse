from tkinter import *

def submit():
    print("the temperature is "+str(scale.get())+" degrees C")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, #orientation for scale 规模方向
              font=('Consolas',20),
              tickinterval=10, #adds numeric indicators for value 添加数值指标
              #showvalue=0, #hide current value
              resolution=5, #increment of slider 滑块增量
              troughcolor='blue',
              fg='red',
              bg='black'
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window,
                text='submit',
                command=submit)
button.pack()

window.mainloop()