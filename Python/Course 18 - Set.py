#set = collection which is ordered, unindexed. No duplicate values
#    = 有序、未索引的集合。 没有重复值

utensils = {"fork","spoon","knife"}
'''utensils = {"fork","spoon","knife","knife","knife"}'''
dishes = {"bowl","plate","cup","knife"}

#add = 加element
'''utensils.add("napkin")'''

#remove = remove element
'''utensils.remove("fork")'''

#clear = remove全部element
'''utensils.clear()'''

#update = 把一个set加进另外一个set
'''utensils.update(dishes)'''

#union = 把两个set加在一起再create新的set
'''dinner_table = utensils.union(dishes)'''

#difference = 两个set的不同点
#比较前的set是后面的set没有的
'''print(dishes.difference(utensils))'''

#intersection = 两个set的共同点
'''print(utensils.intersection(dishes))'''

'''for x in utensils:
    print(x)'''
'''for x in dinner_table:
    print(x)'''
#set会掉乱次序，与list不同
#如果set里有重复的element,在loop时不会重复
