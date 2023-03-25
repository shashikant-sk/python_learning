# WAP to evaluate the equation y=x^n where n is a non-negative integer by defining a function
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
x = int(input("Enter x: "))
n = int(input("Enter n: "))
print(f"{x}^{n} = {power(x, n)}")
 