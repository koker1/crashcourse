#if statements = a block of code that will execute if it's condition is true
#              = 条件为真时执行的代码块

age = int(input("How old are you?: "))

#>= = 大于或等于
if age >= 18:
    print("You are an adult!")
#如果答案是错的电脑不会回答你
#elif = else if
#< = 小于
elif age < 0:
    print("You have not been born yet!")
#只可以==, 不能=
elif age == 100:
    print("You are a century old!")
#else = 除了以上指令的答案
else:
    print("You are a child!")
#第一个statement不能elif