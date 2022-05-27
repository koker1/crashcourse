#zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                  聚合来自两个或多个可迭代对象（列表、元组、集合等）的元素
#                  create a zip object with paired elements stored in tuples for each element
#                  创建一个 zip 对象，其中成对的元素存储在每个元素的元组中

usernames = ["Loh","Kok Hao","Mister"]
passwords = ("password","123456","guest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]

users = zip(usernames,passwords,login_date)
print(users)
for i in users:
    print(i)

'''users = list(zip(usernames, passwords))
print(type(users))
for i in users:
    print(i)'''

'''users = dict(zip(usernames, passwords))
print(type(users))
for key,value in users.items():
    print(key+": "+value)'''
