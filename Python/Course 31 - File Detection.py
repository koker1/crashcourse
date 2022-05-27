import os

path = "D:\\Private\\Script\\Python\\text.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
    #directory 目录
else:
    print("That location doesn't exist")