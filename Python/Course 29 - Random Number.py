import random 

x = random.randint(1,6)
#random.random() = between 0 and 1
y = random.random()

mylist = ['rock','paper','scissors']
z = random.choice(mylist)

card = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(card)

print(card)