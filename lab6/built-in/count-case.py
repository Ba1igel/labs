def count_case(s):

    ucount = 0
    lcount = 0

    for char in s:
        if char.isupper():
            ucount += 1

        elif char.islower():
            lcount += 1
    
    return ucount, lcount

word = input()

ucount, lcount = count_case(word)
print(f"There is {ucount} uppercase letters and {lcount} lowercase letters!")
