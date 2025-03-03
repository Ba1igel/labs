#Write a Python program to write a list to a file.


def listToFile(path, data_list):
    with open(path, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(item + '\n')
        
lst = ["example", "storage"]
listToFile(r"C:\Users\bajge\OneDrive\PP2\lab6\directories.txt", lst)