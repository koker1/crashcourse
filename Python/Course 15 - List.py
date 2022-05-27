#list = used to store multiple items in a single variable
#     = 用于在单个变量中存储多个项目

food = ["pizza","burger","hotdog","spaghetti","pudding"]
'''print(food)'''

#第一个element是0,第二个是1，以此类推
'''print(food[0])'''

#element换成别的element
'''food[0] = "sushi"
print(food[0])'''

#loop list
'''for x in food:
    print(x)'''

#append = 加element在最后
'''food.append("ice cream")
print(food)'''

#remove = remove其中一个element
'''food.remove("hotdog")
print(food)'''

#pop = remove最后的element
'''food.pop()
print(food)'''

#insert = (加element在哪一个element的前面, 要加的element)
'''food.insert(0, "cake")
print(food)'''

#sort = a to z
'''food.sort()
print(food)'''

#clear = remove全部element
'''food.clear()
print(food)'''