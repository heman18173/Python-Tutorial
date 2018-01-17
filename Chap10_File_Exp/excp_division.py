try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by Zero")
print("*** Using Exceptions to Prevent Crashes ***")    
print("Give 2 numbers, I will divide and give results")
print("Enter q to quit")

while True:
    first_num = input("\nEnter first number:")
    if first_num == 'q':
        break
    second_number = input("Enter second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_num)/int(second_number)    
    except ZeroDivisionError:
        print("Can not divide by zero")
    else:
        print(answer)    

print("***Handling the FileNotFoundError Exception ***")        
file_path = "p1.txt"
try:
    with open(file_path) as file_object:
        content = file_path.read()
except FileNotFoundError:
    print("Sorry file " + file_path + " does not exist ")    

print("*** Analyzing Text ***")
file_path = "Hemant.txt"
title = "Hemant is programmer"
print(title.split())

file_path = "Hemant.txt"
try:
    with open(file_path) as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("Sorry file " + file_path + " does not exist ")    
else:
    # Count words
    words = content.split()
    num_words =  len(words)
    print("Then File" + file_path + " has total "+  str(num_words) + " Words")




