# WAP to display reverse of a number by function call
def reverse(n):
    if n == 0:
        return 0
    return (n % 10) * 10 ** (len(str(n)) - 1) + reverse(n // 10)
n = int(input("Enter number to reverse: "))
print(f"Reverse of {n} is {reverse(n)}")


 