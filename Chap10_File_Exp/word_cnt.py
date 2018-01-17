def count_words(filename):
    """ This function counts words in a file """
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        #print("Sorry file " + filename + " does not exist ")    
        pass # fail sliently
    else:
        # Count words
        words = content.split()
        num_words =  len(words)
        print("The File " + filename + " has total "+  str(num_words) + " Words")

filename = "C:\Python\python_work\Chap10_File_Exp\Hemant.txt"
count_words(filename)

file_lists = ["C:/Python/test_files/Hemant.txt", "C:/Python/test_files/book1.txt", 
            "C:/Python/test_files/book2.txt", "harry.txt"]
             
for file_nm in file_lists:
    count_words(file_nm)