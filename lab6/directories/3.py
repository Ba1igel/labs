import os
def checkPathDetails(path):
    if os.path.exists(path):
        print(f"Dir name:  {os.path.dirname(path)}")
        print(f"File name: {os.path.basename(path)}")
        
    else:
        print("Path is not exist.")
checkPathDetails(r"C:\Users\bajge\OneDrive\PP2\lab6\built-in")