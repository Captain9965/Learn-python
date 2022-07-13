"""
    The module os provides a set of tools for interacting with the operating system:

"""

#getting the current working directory, which is the directory where the script is running:
import os
print(os.getcwd())

#changing the current working directory:
# os.chdir('../')
# print("---------After changing directory------------")
# print(os.getcwd())

#create a directory using mkdir():
directory_name = "Trial"
parent_dir = os.getcwd()

path = os.path.join(os.getcwd(), "Learn-python/File-handling")
print(path)
os.chdir(path)
print("------------changing the working directory------------------")
print(os.getcwd())
print("--------------Create the directory with a specific mode:------------")
mode = 0o666

#using mkdirs() will create the files if they do not exist in the path
# os.mkdir("file storage", mode)

print("---------Listing all the files and directories in the path:-------------")
print(os.listdir())
print("----------Removing directories using rmdir()-------------------------")
remove_path = os.path.join(os.getcwd(),"file storage")
print(remove_path)

#removes an empty directory. Use remove() method to remove a non-empty directory.
os.rmdir(remove_path)
print("---------Listing directories again-------------------------")
print(os.listdir())

#commonly used functions:
print("------------------os.name()------------\n",os.name)

#os.popen() opens a pipe to or from command and the file descriptor can only be closed by os.close() or close()
#os.rename(fd, "new name") renames the file descriptor
#os.remove("file_name") removes a file from the file system

print("-------------------os.path.exists()-----------------\n", os.path.exists(os.path.join(os.getcwd(), "file storage")))


#os.path.getsize() returns the size in bytes of a file
print("-----------the size of this file is ", os.path.getsize(os.path.join(os.getcwd(), "os-module.py")))


