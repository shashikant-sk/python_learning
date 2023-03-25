# WAP to check if number is prime
from math import sqrt

def isPrime(n):
    num = 2
    for num in range(2, int(sqrt(n)) + 1):
        if n % num == 0:
            return False 
    return True

n = int(input("Enter number to check primality: "))
if isPrime(n):
    print(f"{n} is Prime!")
else:
    print(f"{n} is not prime!")