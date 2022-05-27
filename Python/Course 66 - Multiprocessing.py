#multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threads 
#                  在不同的 CPU 内核上并行运行任务，绕过用于线程的 GIL
#                  multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                                    更适合 cpu 绑定任务（大量 cpu 使用）
#                  multithreading = better for io bound tasks (waiting around)
#                                   更适合 io 绑定任务（等待）

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while counter < num:
        count += 1

def main():
    
    print(cpu_count())

    a = Process(target=counter,args=(1000000,))
    b = Process(target=counter,args=(1000000,))
    c = Process(target=counter,args=(1000000,))
    d = Process(target=counter,args=(1000000,))
    e = Process(target=counter,args=(1000000,))
    f = Process(target=counter,args=(1000000,))
    g = Process(target=counter,args=(1000000,))
    h = Process(target=counter,args=(1000000,))
    

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    print("finished in",time.perf_counter(),"seconds")

if __name__=='__main__':
    main()