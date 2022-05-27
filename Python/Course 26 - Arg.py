#*args = parameter that will pack all arguments into a tuple
#       将所有参数打包成一个元组的参数
#       useful so that a function can accept a varying amount of arguments
#       有用以便函数可以接受不同数量的参数

'''def add(num1,num2):
    return num1+num2

x = add(1,2)
print(x)'''

'''def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

x = add(1,2,3,4,5,6)
print(x)'''

'''def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum = sum + i
    return sum

x = add(1,2,3,4,5,6)
print(x)'''