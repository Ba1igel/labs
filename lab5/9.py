#Write a Python program to insert spaces between words starting with capital letters.


import re

text = "ZeWarudoTokioTomaru"

result = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
print(result)