#daemon threads = a thread that runs in the background, not important for program to run
#                 在后台运行的线程，对程序运行不重要
#                 your program will not wait for daemon threads to complete before exiting
#                 你的程序在退出前不会等待守护线程完成
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#                 非守护线程通常不能被杀死，保持活动直到任务完成
#                 ex. background tasks, garbage collection, waiting for input, long running process 
#                 例如。 后台任务、垃圾回收、等待输入、长时间运行的进程

import threading 
import time 

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(" logging in for: ",count,"seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

'''x.setDaemon(True)'''
'''print(x.isDaemon())'''

answer = input("do you wish to exit?: ")