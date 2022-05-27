#sort() method = used with lists
#sort() function = used with iterables 

'''students = ["mar","kok","han","muz","qi"]'''
'''students = ("mar","kok","han","muz","qi")'''

'''students.sort(reverse=True)'''
'''sorted_students = sorted(students,reverse=True)'''

'''for i in students:
    print(i)'''
'''for i in sorted_students:
    print(i)'''

#--------------------------------------

students = [("mar","F",60),
            ("kok","A",33),
            ("han","D",36),
            ("muz","B",20),
            ("qi","C",78)]

'''grade = lambda grades:grades[1]'''
age = lambda ages:ages[2]
'''students.sort(key=grade,reverse=True)'''
students.sort(key=age,reverse=True)

for i in students:
    print(i)