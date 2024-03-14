'''
Homework Assignment #8: Input and Output (I/O)
'''
import os

#take the input from the user
path = input("Enter the file path and file name to create: (example:'C:\\temp\\text.txt') \n") #C:\temp\text.txt

#check whether the file is exists
isFile = os.path.isfile(path)

#if not exists, then create
if isFile == False:
    text_file = open(path, "w")
    text_to_write = input("enter the text to write to a file: \n")
    text = text_file.write(text_to_write)
    print("text is enter to the file and saved in : " + path)
    text_file.close()
else: #if its exists, then ask for overwrite
    file_present = input("The specified file is already exist, you want to overwrite it of append the text? (enter overwrite or append) \n")
    if file_present.lower() == "overwrite":
       # append_txt = input("You want to append the text?")
        #if append_txt.lower() == "yes":
            text_file = open(path, "w")
            text_to_write = input("enter the text to overwrite: \n")
            text = text_file.write(text_to_write)
            print("Entered the text and file is saved in : " + path)
            text_file.close()
    elif file_present.lower() == "append": #append the text
            text_file = open(path, "a")
            text_to_write = input("enter the text to append: \n")
            text = text_file.write("\n")
            text = text_file.write(text_to_write)
            print("Entered text is appended saved in : " + path)
            text_file.close()
    else:
        print("wrong selection") #if user enter the wrong text








