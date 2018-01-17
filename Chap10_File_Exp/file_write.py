print("*** Writing to an Empty File ***")

filename = "C:\python\python_work\Chap10_File_Exp\write_file_prog.txt"
 # you can open file in r,w,a -append & r+ read-write mode default is r
 # while opeing file in w mode if file exit before then it will erase old file
with open(filename, 'w') as file_object:
    file_object.write ("I love programming.\n")
    file_object.write ("I love creating data science projects for bank\n")

print("*** Appending to a File ***")
with open(filename, 'a') as file_object:
    file_object.write ("I love database programming.\n")
    file_object.write ("I love creating app for data science graphs\n")