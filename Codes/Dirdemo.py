name = "John"
age = 23
fptr=open("demo.txt",mode="a+")
fptr.write("%s is %d years old.\n" % (name, age))
fptr.write(str(age))
fptr.seek(0)
print(fptr.read())
import os
print("The directory in which file is created is:",os.getcwd())
print("The directory in which file is created is:",os.path.abspath('demo.txt'))
print("The directory in which file is created is:",os.path.exists('memo.txt‘))                                                         
print("The directory in which file is created is:",os.path.isdir('memo.txt'))
print("The directory in which file is created is:",os.path.exists('lib'))


