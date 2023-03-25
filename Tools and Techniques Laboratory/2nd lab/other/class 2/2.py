# WAP to calculate sum of digits of a number by function
def sumOfDigits(n):
    if n == 0:
        return 0
    return n % 10 + sumOfDigits(n // 10)
n = int(input("Enter number to calculate sum of digits: "))
print(f"Sum of digits of {n} is {sumOfDigits(n)}")
 
 
    