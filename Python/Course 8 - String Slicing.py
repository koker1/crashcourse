#slicing = creating a substring by extracting elements from another string 
#slicing = 通过从另一个字符串中提取元素来创建子字符串
#           indexing[] or slice()
#           [start:stop:step]

name = "Loh Kok Hao"
#字符的位子(从0算起，包括空格)
'''first_name = name[0]
print(first_name)'''
#[从0算起:算字数(从1算起，包括自己)]
#0不要type出来也可以
'''first_name = name[:3]
print(first_name)'''
#如果要后面的字符就不用特地算
'''last_name = name[4:]
print(last_name)'''
#step = 从1算起，你要的号码的倍数字符的位子会被清除，如果是3的话包括2和3的倍数
'''funky_name = name[::3]
print(funky_name)'''
#step是负数就把字符倒转来再清除
'''reversed_name = name[::-1]
print(reversed_name)'''

website = "http://google.com"
#把"google"留下
slice = slice(7,-4)
print(website[slice])