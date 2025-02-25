

import re
def spliter(s):
    return re.findall(r'[A-Z][A-Z]*', s)
text = "jJakfjjaJKJkjkjafkjksjKJKJfefFNJEWJ"
print(spliter(text))