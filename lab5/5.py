#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
pattern = r"[A-Z][a-z]"
def find_pattern(s):
    return bool(re.search(pattern,s))
texts = ['a', 'ab', 'AAA_b','aab_acbc', 'va', 'ca', 'ababU', 'abbbbbb', 'baaaaaJ', 'baGbanbsbaban']
for text in texts:
    print(f"{text}: {find_pattern(text)}")