# WAP to check whether an input integer is strong number or not. 
n = int(input("Enter n: "))

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)

sum = 0
temp = n
while temp != 0:
    sum += fac(temp % 10)
    temp //= 10

if sum == n:
    print(f"{n} is strong!")
else:
    print(f"{n} is not strong!")