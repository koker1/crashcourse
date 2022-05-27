#exception = events detected during execution that interrupt the flow of a program
#            在执行期间检测到的中断程序流程的事件

'''numerator = int(input("Enter a number to divide: "))
#numerator 分子
denominator = int(input("Enter a number to divide by: "))
#denominator 分母
result = numerator / denominator
print(result)'''

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divde by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")
except ValueError as e:
    print(e)
    print("Enter only number")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")
