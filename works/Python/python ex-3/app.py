import os
import shutil
cwd=os.getcwd()

print("current working directory:", cwd)

def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


   
# Changing the CWD
os.chdir('../../../../')

   
# Printing CWD after
current_path()

os.chdir(r"C:\Users\COMPAG\Desktop\A Folder")

current_path()

path = 'C:/Users/COMPAG/Desktop/A Folder'
 
# List files and directories
# in '/home/User/Documents'
print("Before copying file:")
print(os.listdir(path))

source = "C:/Users/COMPAG/Desktop/A Folder/javascript-repeat-string.png"
 
# Destination path
destination = "C:/Users/COMPAG/Desktop/B Folder/javascript-repeat-string.png"

dest = shutil.copyfile(source, destination)
 

print("After copying file:")
print(os.listdir(path))
 

print("Destination path:", dest)

#path="C:\Users\COMPAG\Desktop\A Folder"
path = 'C:/Users/COMPAG/Desktop/A Folder'

fun = lambda x : os.path.isfile(os.path.join(path,x))
files_list = filter(fun, os.listdir(path))

size_of_file = [
    (f,os.stat(os.path.join(path, f)).st_size)
    for f in files_list
]

for f,s in size_of_file:
    print("{} : {}mb".format(f, round(s/(1024*1024),3)))