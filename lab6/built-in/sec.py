import time
import math

n = int(input())
milisec = int(input())

time.sleep(milisec/1000)
sqrtr = lambda x: math.sqrt(n)

print(f"Square root of {n} after {milisec} miliseconds is {sqrtr}")