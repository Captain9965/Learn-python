"""
    we use open(filename, access_mode) to open a file
    where the filename is the name of the file and the access mode is any of:
        1. 'r' - read only
        2. 'r+' - open file for reading and writing. The file handle is placed at the beginning of the file.
        3. 'w' - The file is opened for writing. If an existing file, it is overwritten and truncated
        4. 'w+' - The file is opened for reading and writing. If existing, it is overwritten and truncated.
        5. 'a' - The file is opened for writing. The data is appended if existing. the file handle is placed at the end of the file.
        6. 'a+' - The file is opened for reading and writing. The handle is placed at the end of the file.

""" 
#use with to automatically close the file:

with open("notes",'r+') as file:
    if file.readable():
        print("The file is readable")
        file.write("I am Lenny Orengo")
        file.write("\n")

        #return the file handle to the beginning of the file:
        file.seek(0)
        print("---------------The output of readlines:---------------------")
        print(file.readlines())
        print("---------------The output of read()--------------------------")
        file.seek(0)
        print(file.read())
        print("-----------------The output of readline()----------------")
        file.seek(0)
        print(file.readline())

        #use write() to write a line at a time and writelines to write a list of strings/elements:
        [file.write(x) for x in ["Nope nope\n", "nope\n"]]

        #get the position of the file handler:
        print(file.tell())

    else:
        print("Nothing to see here")

