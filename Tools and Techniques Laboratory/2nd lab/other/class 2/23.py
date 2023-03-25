# WAP to convert a decimal number into its equivalent number with base b. Decimal number and b are the user input
# Assuming 2 <= b <= 9
b = int(input("Enter base: "))
n = int(input(f"Enter number in decimal: "))
tempn = n
rem = []
while n:
    rem.append(n % b)
    n //= b
rem.reverse()
num = ''.join(map(str, rem))
print(f"({tempn})10 = ({num}){b}")