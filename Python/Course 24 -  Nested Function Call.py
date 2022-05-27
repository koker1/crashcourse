#nested function calls = function calls inside other function calls
#                        其他函数调用中的函数调用
#                        innermost function calls are resolved first
#                        首先解析最内层的函数调用
#                        returned value is used as argument for the next outer function
#                        返回值用作下一个外部函数的参数

'''num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)'''

print(round(abs(float(input("Enter a whole positive number: ")))))