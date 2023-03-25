# WAP to calculate the factorial of a given  by function call
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1) 
n = int(input("Enter number to calculate factorial: "))
 
print(f"Factorial of {n} is {factorial(n)}")
     
