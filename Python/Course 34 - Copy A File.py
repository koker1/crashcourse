#copyfile() = copies contents of a file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

'''shutil.copyfile('D:\\Private\\Script\\Python\\text.txt','D:\\Private\\Script\\Python\\copy.txt')''' #src = source, dst = destination
'''shutil.copy('D:\\Private\\Script\\Python\\text.txt','D:\\Private\\Script\\Python\\copy.txt')'''
'''shutil.copy2('D:\\Private\\Script\\Python\\text.txt','D:\\Private\\Script\\Python\\copy.txt')'''