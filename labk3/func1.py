from math import sqrt 
from itertools import permutations 
 
 
def gramsToOunces(grams): 
    ounces = 28.3495231 * grams 
    return ounces 
 
 
def fahrenheitToCentigrate(F): 
    C = (5 / 9) * (F - 32) 
    return C   
 
def solve(num_heads, num_legs): 
    rabbits = (num_legs - 2 * num_heads) // 2 
    chickens = num_heads - rabbits 
 
    print(f"Number of rabbits: {rabbits}, Number of chickens: {chickens}") 
 
 
def is_prime(x): 
    if x < 2: 
        return False 
    for i in range(2, int(sqrt(x)) + 1): 
        if x % i == 0: 
            return False 
    return True 
 
 
def filter_prime(arr): 
    return [num for num in arr if is_prime(num)] 
 
 
 
def perm(): 
    string = input("Enter a string: ") 
    string_permutations = ["".join(p) for p in permutations(string)] 
 
    for perm in string_permutations: 
        print(perm) 
 
 
def reverse_string(): 
    words = input("Enter a sentence: ").split() 
    print(" ".join(reversed(words))) 
 
 
def threes(arr): 
    return any(arr[i] == 3 and arr[i + 1] == 3 for i in range(len(arr) - 1)) 
 
 
def spy_game(lst): 
    sequence = [0, 0, 7] 
    index = 0 
     
    for num in lst: 
        if num == sequence[index]: 
            index += 1 
            if index == len(sequence): 
                return True 
    return False 
 
 
def volumeOfSphere(radius): 
    return (4 / 3) * 3.14 * (radius ** 3) 
 
 
def uniq(lst): 
    return list(dict.fromkeys(lst)) 
 
def is_palindrome(x): 
    return x == x[::-1] 
 
def histogram(lst): 
    for i in lst: 
        print('*' * i) 
 
import random 
 
def game(): 
    print("Hello! What is your name?") 
 
    number = random.randint(1, 20) 
    user_name = input() 
    number_gusses = 0 
 
    print(f"Well, {user_name}, I am thinking of a number between 1 and 20.") 
    print("Take guess.") 
 
    while True: 
        user_answer = int(input()) 
 
        if user_answer > number: 
            print("Your guess is biger.") 
            print("Take guess.") 
             
            number_gusses += 1 
 
        elif user_answer < number: 
            print("Your guess is to low.") 
            print("Take guess.") 
             
            number_gusses += 1 
 
        elif user_answer == number: 
            print(f"Good job, {user_name}! You guessed my number in {number_gusses} guesses!") 
 
            break


