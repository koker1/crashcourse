#**kwargs = parameter that will pack all arguments into a dictionary
#           将所有参数打包到字典中的参数
#           useful so that a function can accept a varying amount of keyword arguments
#           有用以便函数可以接受不同数量的关键字参数

'''def hello(first,last):
    print("Hello "+first+" "+last)

hello(first="Loh",last="Hao")'''

'''def hello(**kwargs):
    ''''''print("Hello "+kwargs['first']+" "+kwargs['last'])''''''
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
        
hello(title="Mr.",first="Loh",middle="Kok",last="Hao")'''