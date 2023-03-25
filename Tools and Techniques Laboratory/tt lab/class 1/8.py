# WAP to swap 2 variable using a third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a = {a}, b = {b}")
c = a
a = b
b = c
print(f"After swap: a = {a}, b = {b}")