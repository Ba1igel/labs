#Write a Python program to count the number of lines in a text file.

def count_lines_in_file(file_path):
    answer = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            answer += 1
        return answer
    
print(count_lines_in_file("C:\Users\bajge\OneDrive\PP2\lab6\directories\m.txt"))     