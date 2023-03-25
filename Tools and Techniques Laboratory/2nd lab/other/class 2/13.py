# WAP to print the series as 3 5 7 11 13 17..........n, where n is given by user
from math import sqrt
n = int(input("Enter n: "))
series = []
def isPrime(n):
    num = 2
    for num in range(2, int(sqrt(n)) + 1):
        if n % num == 0:
            return False
    return True
for i in range(2, 1000):
    if (i & 1) and isPrime(i):
        series.append(i)
print("n terms of the series: ", end='')
for i in range(n):
    print(f"{series[i]}", end=' ')