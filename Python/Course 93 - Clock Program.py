from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p") #convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument
                                     #将表示由 gmtime() 或 localtime() 返回的时间的元组或 struct_time 转换为格式参数指定的字符串
                                     #%I = hour (12-hour clock) as a decimal number [01,12]
                                     #%M = minute as a decimal number [00,59]
                                     #%S = second as a decimal number [00,61]
                                     #%p = locale’s equivalent of either AM or PM
    time_label.config(text=time_string)

    day_string = strftime("%A") #%A = locale’s full weekday name
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y") #%B = locale’s full month name
                                        #%d = day of the month as a decimal number [01,31]
                                        #%Y = year with century as a decimal number
    date_label.config(text=date_string)

    time_label.after(1000,update)

window = Tk()

time_label = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",25))
day_label.pack()

date_label = Label(window,font=("Ink Free",30))
date_label.pack()

update()

window.mainloop()

#more information check docs.python.org