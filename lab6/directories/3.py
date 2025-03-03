#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

import os
def checkPathDetails(path):
    if os.path.exists(path):
        print(f"Dir name:  {os.path.dirname(path)}")
        print(f"File name: {os.path.basename(path)}")
        
    else:
        print("Path is not exist.")
checkPathDetails(r"C:\Users\bajge\OneDrive\PP2\lab6\built-in")