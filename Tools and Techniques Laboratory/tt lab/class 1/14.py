# Input 2 numbers and make a calculator menu to add subtract divide multiply
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter a operator to perform (+, -, *, /): ")
if op == '+':
    print(f"{a} + {b} = {a + b}")
elif op == '-':
    print(f"{a} - {b} = {a - b}")
elif op == '*':
    print(f"{a} * {b} = {a * b}")
elif op == '/':
    if b == 0:
        print("Divide by 0 error.")
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print("Incorrect operator.")