#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
pattern = r"[a-z]+_"
def find_pattern(s):
    return bool(re.search(pattern,s))
texts = ['a', 'ab', 'AAA_b','aab_acbc', 'va', 'ca', 'ababU', 'abbbbbb', 'baaaaaJ', 'baGbanbsbaban']
for text in texts:
    print(f"{text}: {find_pattern(text)}")