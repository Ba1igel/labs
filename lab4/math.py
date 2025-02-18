import math
def degree_to_radian(degrees):
    return degrees * (math.pi / 180)

degrees  = float(input("Input degree: "))
radians = degree_to_radian(degrees)
print(f"Output radian: {radians}")


# Task 2
def trapezoid_s(height, value1, value2):
    return height * (value1 + value2)/2

height = int(input("height"))
value1 = int(input("Base, first value: "))
value2 = int(input("Base, second value: "))
area = trapezoid_s(height, value1, value2)
print(f"Expected Output: {area}")


# Task 3
def polygon_a(n, length):
    return (n * length**2) / (4 * math.tan(math.radians(180 / n)))

n = int(input("Input number of sides: "))
lenght = int(input("Input the length of a side: "))
area_trapez = polygon_a(n, lenght)
print(f"Expected Output: {area_trapez}")

# Task 4
def parallelogram(heightp, value):
    return heightp * (value)

heightp = int(input("height of the parallelogram "))
value = int(input("Base, value: "))
area_p = parallelogram(heightp, value)
print(f"Expected Output: {area_p}")
