#reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#           将函数应用于可迭代对象并将其减少为单个累积值。
#           performs function on first two elements and repeats process until 1 value remains
#           对前两个元素执行函数并重复处理直到剩下 1 个值
#reduce(function,iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y,letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y,factorial)
print(result)