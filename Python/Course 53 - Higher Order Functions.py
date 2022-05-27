#higher order function = a function that either:
#                        1. accepts a function as an argument
#                           接受一个函数作为参数
#                        2. returns a function 
#                           返回一个函数
#                           (In python, functions are also treated as objects)
#                          （在python中，函数也被视为对象）

'''def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("hello")
    print(text)

hello(loud)
hello(quiet)'''

# --------------------------------------
#divisor = 除数
#dividend = 除法
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))