# WAP to swap 2 variables without 3rd variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swap: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After swap: a = {a}, b = {b}")