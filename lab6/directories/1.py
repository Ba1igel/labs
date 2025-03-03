#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list_items(path):

    all_items = os.listdir(path)
    full_paths = [os.path.join(path, item) for item in all_items]

    directories = [item for item in full_paths if os.path.isdir(item)]
    files = [item for item in full_paths if os.path.isfile(item)]

    print("Directories:")
    for directory in directories:
        print(directory)


    print("Files:")
    for file in files:
        print(file)



list_items(r"C:\Users\bajge\OneDrive\PP2\lab6\built-in")