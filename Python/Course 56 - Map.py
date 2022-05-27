#map() = applies a function to each item in an iterable (list, tuple, etc.)
#        将函数应用于可迭代对象（列表、元组等）中的每个项目
#map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

'''to_euros = lambda data:(data[0],data[1]*0.82)'''
'''to_dollars = lambda data:(data[0],data[1]/0.82)'''

'''store_euros = list(map(to_euros,store))'''
'''store_dollars = list(map(to_dollars,store))'''

'''for i in store_euros:
    print(i)'''
'''for i in store_dollars:
    print(i)'''