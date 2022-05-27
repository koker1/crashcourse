import os

'''os.remove('D:\\Private\\Script\\Python\\text.txt')'''
#or
'''path = "D:\\Private\\Script\\Python\\text.txt"
os.remove(path)'''

path = "D:\\Private\\Script\\Python\\Course 37 - Module.txt"

try:
    '''os.remove(path)''' #delete a file
    '''os.rmdir(path)''' #delete an empty directory
    '''shutil.rmtree(path)''' #delete a directory containing files
except FileNotFoundError:
    print("That file wasn't found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path +" was deleted")