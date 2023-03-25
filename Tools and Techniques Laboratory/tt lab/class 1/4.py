# WAP to calculate area of triangle given 3 sides
from math import sqrt

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))
print(f"Area of triangle: {area}")