#Write a Python program to split a string at uppercase letters.

import re
def spliter(s):
    return re.findall(r'[A-Z][A-Z]*', s)
text = "jJakfjjaJKJkjkjafkjksjKJKJfefFNJEWJ"
print(spliter(text))