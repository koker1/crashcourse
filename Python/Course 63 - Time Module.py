import time

#epoch = a date and time from which a computer measures system time
#        计算机测量系统时间的日期和时间
'''print(time.ctime(1000000))'''    #convert a time expressed in seconds since epoch to a readable string
#                              将自纪元以来以秒表示的时间转换为可读字符串
#                              epoch = when your computer thinks time began (reference point)
#                              当您的计算机认为时间开始时（参考点）

'''print(time.time())''' #return current seconds since epoch
#                   返回自纪元以来的当前秒数

'''print(time.ctime(time.time()))''' #get current date
#                               获取当前日期

'''time_object = time.localtime()        
time_object = time.gmtime()'''  
'''time.strftime(format,time_object)''' #directive find in google                            
#exp
'''local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time)'''

#-------------------------------------------------------------------
'''time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)'''

#-------------------------------------------------------------------
'''time_tuple = (2020,4,20,4,20,0,0,0,0)
time_string = time.asctime(time_tuple)
print(time_string)'''

'''time_tuple = (2020,4,20,4,20,0,0,0,0) #convert to sec
time_string = time.mktime(time_tuple)
print(time_string)'''

