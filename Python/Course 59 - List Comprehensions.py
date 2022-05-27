#list comprehension = a way to create a new list with less syntax
#                     一种使用较少语法创建新列表的方法
#                     can mimic certain lambda functions, easier to read
#                     可以模仿某些 lambda 函数，更容易阅读
#                     list = [expression for item in iterable]
#                            [可迭代项的表达式]
#                            [expression for item in iterable if conditional]
#                            [如果有条件，则可迭代项的表达式]
#                            [expression if/else for item in iterable]

squares = []                #create an empty list
for i in range(1,11):       #create a for loop
    squares.append(i*i)     #define what each loop iteration should do 定义每个循环迭代应该做什么
print(squares)

squares = [i*i for i in range(1,11)]
print(squares)

#------------------------------------------

students = [100,90,80,70,60,50,40,30,0]

'''passed_students = list(filter(lambda x:x>=60,students))'''

'''passed_students = [i for i in students if i >= 60]'''

passed_students = [i if i >= 60 else "Failed" for i in students]    

print(passed_students)