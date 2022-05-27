#scope = The region that a variable is recognized
#        识别变量的区域
#        A variable is only available from inside the region it is created.
#        变量只能从它创建的区域内部使用。
#        A global and locally scoped versions of a variable can be created
#        可以创建变量的全局和局部范围版本

name = "Loh" #global scope (available inside & outside functions)

def display_name():
    name = "Kok Hao"   #local scope (available only inside this function)
    print(name)

display_name()
print(name)

#L = local
#E = enclosing
#G = global
#B = built-in
