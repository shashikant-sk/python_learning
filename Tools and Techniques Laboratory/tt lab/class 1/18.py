# Find roots of quadratic equation ax^2 + bx + c = 0
from math import sqrt

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
D = (b * b - 4 * a * c)
if D < 0:
    print("Imaginary roots")
    print(f"Root1: {(-b) / (2 * a)} + {sqrt(-D) / (2 * a)}i")
    print(f"Root2: {(-b) / (2 * a)} + {sqrt(-D) / (2 * a)}i")
else:
    print("Real roots")
    print(f"Root1: {(-b + sqrt(D)) / (2 * a)}")
    print(f"Root2: {(-b - sqrt(D)) / (2 * a)}")
