# WAP to find gcd of two numbers 
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a) 

print(f"gcd({a}, {b}) = {gcd(a, b)}")
