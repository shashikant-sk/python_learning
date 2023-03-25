# WAP to find distance between 2 coordinates
from math import sqrt, pow

c1 = list(map(int, input("Enter coordinate 1: ").split()))
c2 = list(map(int, input("Enter coordinate 2: ").split()))
dist = sqrt(pow(c1[0] - c2[0], 2) + pow(c1[1] - c2[1], 2))
print(f"Distance = {dist}")