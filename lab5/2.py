#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

import re
pattern = r"ab{2,3}"
def find_pattern(s):
    return bool(re.search(pattern,s))
texts = ['a', 'ab', 'AAAb','aabacbc', 'va', 'ca', 'abab', 'abbbbbb', 'baaaaa', 'babanbsbaban']
for text in texts:
    print(f"{text}: {find_pattern(text)}")