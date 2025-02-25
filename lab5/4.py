#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'


import re
pattern = r"[a-b]+b$"
def find_pattern(s):
    return(bool(re.search(pattern,s)))
texts = ['a', 'ab', 'AAA_b','aab_acbc', 'va', 'ca', 'ababU', 'abbbbbb', 'baaaaaJ', 'baGbanbsbaban']
for text in texts:
    print(f"{text}: {find_pattern(text)}")
