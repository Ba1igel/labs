#WWrite a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt



import string

for name in string.ascii_uppercase:
    fileName = f"{name}.txt"
    with open(fileName, 'w') as file:
        file.write(f"name")