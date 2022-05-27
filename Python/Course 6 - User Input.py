name = input("What is your name?: ")
#做数学计算input前面前面要加float或者int, str不能做计算
age = int(input("How old are you?: "))
age = age + 1
#如果答案有小数input前面要放float
height = float(input("How tall are you?: "))

print("Hello, "+name)
print("You are "+str(age) +" years old")
print("You are "+str(height)+"cm tall")
