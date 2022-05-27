#Variable: a container for a value. Behaves as the value that it contains.
#变数    : 一个值的容器。表现为它包含的值。
#Variable也可以比喻成algebra(代数)
#变数在print的时候不用放("")

'''name = ("Loh Kok Hao")
print(name)'''

#有字母的值放(""), 数字的不用放("")

#Welcome message
'''name = ("Loh Kok Hao")
print("Hello, Welcome! " + name)'''

#把两个变数加在一起
'''first_name = ("Loh")
last_name = ("Kok Hao")
#在first_name和last_name之间放" " = spacebar
full_name = first_name + " " + last_name
print("Hello, Welcome! " + full_name)'''

#Varible为数值(integer)
'''number = 1
print(number)'''

#integer加法有两种写法
#第一种
'''age = 21
age = age + 1
print(age)'''
#第二种
'''age = 21
age += 1
print(age)'''

#Variable有分两种
#第一种是string(字符)，第二种是integer(整数)
#证明法: print(type(variable))
#integer = 21 (没有"")
#string = "21" (有"")

#print的时候有string,那原本是integer的variable要换成string
#str to str correct, str to int wrong
'''age = 21
age += 1
print("Your age is: " + str(age))'''

#float = floating point number 浮点数 (a decimal number 十进制数)
'''height = 250.5
print(height)'''
'''height = 250.5
print("Your height is: " + str(height) + "cm")'''

#boolean = true or false
#boolean的shortform = bool
'''human = False
print(human)'''
'''human = False
print("Are you a human: " + str(human))'''

#总结variable有四种 = string, integer, float, boolean
