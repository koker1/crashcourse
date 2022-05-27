#thread = a flow of execution. Like a seperate order of instructions.
#         执行流程。 就像一个单独的指令顺序。
#               However each thread takes a turn running to achieve concurrency
#               然而每个线程轮流运行以实现并发
#               GIL = (global interpreter lock),
#                     (全局解释器锁),
#               allows only one thread to hold the control of the Python Interpreter at any one time
#               任何时候只允许一个线程控制 Python 解释器

#cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#            程序/任务大部分时间都在等待内部事件（CPU 密集型）
#            use multiprocessing
#            使用多处理

#io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#           程序/任务大部分时间都在等待外部事件（用户输入、网页抓取）
#           use multithreading
#           使用多线程

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("you ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("you drank coffee")

def study():
    time.sleep(5)
    print("you finish studying")

x = threading.Thread(target=eat_breakfast,args=())
x.start()

y = threading.Thread(target=drink_coffee,args=())
y.start()

z = threading.Thread(target=study,args=())
z.start()

x.join() #join = thread再到check thread command
y.join()
z.join()

'''eat_breakfast()
drink_coffee()
study()'''

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())