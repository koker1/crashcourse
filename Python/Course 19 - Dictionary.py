#dictionary = A changeable, unordered collection of unique key:value pairs. Fast because they use hashing, allow us to access a value quickly
#           = 唯一键值对的可变、无序集合。 快速因为他们使用散列，允许我们快速访问一个值

capitals = {'USA':'Washington DC','India':'New Delhi','China':'Beijing','Russia':'Moscow'}

#update = 加key value,换value
'''capitals.update({'Germany':'Berlin'})'''
'''capitals.update({'USA':'Las Vegas'})'''

#pop = remove一个key value
'''capitals.pop('China')'''

#clear = remove全部key value
'''capitals.clear()'''

#print USA capital
'''print(capitals['USA'])'''

#get = 测试要的element有没有在dictionary
'''print(capitals.get('Germany'))'''

#keys = dictionary的key
'''print(capitals.keys())'''

#values = dictionary的value
'''print(capitals.values())'''

#items = dictionary的内容
'''print(capitals.items())'''

#loop dictionary的key value
for key,value in capitals.items():
    print(key,value)

