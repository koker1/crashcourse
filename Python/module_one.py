#if __name__ == '__main__'

#why?
#1. module can be run as a standalone program
#   模块可以作为独立程序运行
#2. module can be imported and used by other modules
#   模块可以被其他模块导入和使用

#Python interpreter sets "special variables", one of which is __name__
#Python解释器设置“特殊变量”，其中之一是__name__
#then Python will execute the code found within __main__
#然后 Python 将执行在 __main__ 中找到的代码

#behind the scenes
#Python interpreter... (refer in front)
#Python will assign the __name__ variable a value of '__main__'  if it's
#Python 会为 __name__ 变量赋值 '__main__' 如果它是
#the initial module being run
#正在运行的初始模块

'''if __name__=='__main__':
    print("running this module directly")
else:
    print("running other module indirectly")'''

def main():
    print("hello")

if __name__=='__main__':
    main()