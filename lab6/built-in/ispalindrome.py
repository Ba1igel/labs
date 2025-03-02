def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
word = input()

if is_palindrome(word):
    print(f"The {word} is palindrome")
else:
    print(f"The {word} is not palindrome")