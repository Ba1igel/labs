from functools import reduce

numbs = list(map(int, input().split()))

result = reduce(lambda x, y:x*y, numbs)

print = ("The result: ", result)


