# WAP to find out the prime factors of a number entered through keyboard (distinct).
from math import sqrt

n = int(input("Enter n: "))

facs = []

def isPrime(n):
    num = 2
    for num in range(2, int(sqrt(n)) + 1):
        if n % num == 0:
            return False
    return True

for num in range(1, n + 1):
    if isPrime(num) and n % num == 0:
        if num in facs:
            continue
        else:
            facs.append(num)

print(f"Prime factors of {n} -> {facs}")