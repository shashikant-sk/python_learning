# Original - Python program to print even and odd numbers in a list
# Edited - WAP to print all the prime numbers in a list
lis = list(map(int, input('Enter list elements: ').split()))
print(f"Initial list -> {lis}")
primes = []


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in lis:
    if isPrime(i):
        primes.append(i)


print(f"Prime numbers in list -> {primes}")
