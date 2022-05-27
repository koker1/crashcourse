#str.format() = optional method that gives users more control when displaying output
#               可选方法，让用户在显示输出时有更多控制权

'''animal = "cow"'''
'''item = "moon"'''

#answer = The cow jumped over the moon
'''print("The "+animal+" jumped over the "+item)'''
'''print("The {} jumped over the {}".format("cow","moon"))'''
'''print("The {} jumped over the {}".format(animal,item))''' 
'''print("The {0} jumped over the {1}".format(animal,item))''' #positional argument 
'''print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))''' #keyword argument

'''text = "The {} jumped over the {}"'''

'''print(text.format(animal,item))'''

#

'''name = "Kok"'''

'''print("Hello, my name is {}".format(name))'''
'''print("Hello, my name is {:10}. Nice to meet you".format(name))'''
'''print("Hello, my name is {:<10}. Nice to meet you".format(name))'''
'''print("Hello, my name is {:>10}. Nice to meet you".format(name))'''
'''print("Hello, my name is {:^10}. Nice to meet you".format(name))'''

#

'''number = 3.14159'''
#f = float
'''print("The number pi is {:.2f}".format(number))'''

#

number = 1000
#, = add comma
'''print("The number is {:,}".format(number))'''
#b = binary
'''print("The number is {:b}".format(number))'''
#o = octal 八进制
'''print("The number is {:o}".format(number))'''
#x = hexadecimal 十六进制
'''print("The number is {:x}".format(number))'''
#e = scientific notation
'''print("The number is {:e}".format(number))'''