#lambda function = function written in 1 line using lambda keyword
#                  使用 lambda 关键字在 1 行中编写的函数
#                  accept any number of arguments, but only has one expression
#                  接受任意数量的参数，但只有一个表达式
#                  (think of it as a shortcut)
#                 （把它想象成一个快捷方式）
#                  (useful if needed for a short period of time, throw-away)
#                 （在短时间内需要时很有用，扔掉）

#lambda parameters:expression

'''def double(x):
    return x*2

print(double(5))'''

double = lambda x:x*2
multiply = lambda x,y:x*y
add = lambda x,y,z:x+y+z
full_name = lambda first_name,last_name:first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False
print(double(5))
print(multiply(5,6))
print(add(5,6,7))
print(full_name("Loh","Kok Hao"))
print(age_check(18))
