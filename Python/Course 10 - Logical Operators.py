#logical operators (and, or, not) = used to check if two or more conditional statements are true
#                                 = 用于检查两个或多个条件语句是否为真

temp = int(input("What's the temperature outside?: "))

#and = 拥有全部条件的答案
'''if temp >= 10 and temp <= 30:
    print("The temperature is good today!")
    print("You can go outside!")'''
#or = 拥有其中一个条件的答案
'''elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("You should stay inside!")'''

#not = 没有以上条件的答案
'''if not (temp >= 10 and temp <= 30):
    print("The temperature is bad today!")
    print("You should stay inside!")'''
'''if not (temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("You can go outside!")'''