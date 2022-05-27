#nested loop = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"
#            = “内循环”将在完成“外循环”的一次迭代之前完成所有的迭代

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
print()