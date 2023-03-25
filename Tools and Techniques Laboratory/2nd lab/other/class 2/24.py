# WAP to convert a number with base b into its equivalent decimal number. Number with base b & b are the user input.
b = int(input("Enter base: "))
n = input(f"Enter number in base {b}: ")
n = ''.join(reversed(n))
num = 0
pow = 1
for dig in n:
    num += pow * int(dig)
    pow *= b
n = ''.join(reversed(n))
print(f"({n}){b} = ({num})10")
