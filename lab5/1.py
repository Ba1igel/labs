#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

import re
pattern = "ab*"
def find_pattern(s):
    return bool(re.findall(pattern,s))
texts = ['a', 'ab', 'AAAb','aabacbc', 'va', 'ca', 'abab']
for text in texts:
    print(f"{text}: {find_pattern(text)}")
