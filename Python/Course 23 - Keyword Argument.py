#keyword arguments = arguments preceded by an identifier when we pass them to a function. 
#                    The order of the arguments doesn't matter, unlike positional arguments. 
#                    Python knows the names of the arguments that our function receives.
#                  = 当我们将参数传递给函数时，参数前面有一个标识符。
#                    与位置参数不同，参数的顺序无关紧要。
#                    Python 知道我们的函数接收的参数的名称。

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

'''hello("Loh","Kok","Hao")'''
hello(last="Hao",middle="Kok",first="Loh")