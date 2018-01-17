print("*******Reading entire file in one go*************")
file_path = "C:\Python\python_work\my_files\pi.txt"
with open(file_path) as file_object:
    data = file_object.read()
    print(data.strip())

print("*** Read file line by line ***")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
         
print("*** Making a List of Lines from a File ***")
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())    

print("*** Working with a File's Contents use int() or float() for number ***")    
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)    
print(len(pi_string))

print("*** Large Files: One Million Digits ***")
file_path = "C:\Python\python_work\my_files\pi_large.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string[:52])    
print(len(pi_string))

print("*** Is Your Birthday Contained in Pi? ***")
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")