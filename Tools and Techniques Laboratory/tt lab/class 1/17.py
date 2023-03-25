# # Input 2 numbers and make a calculator menu to add subtract divide multiply. Use switch case
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter a operator to perform (+, -, *, /): ")
match op:
    case '+':
        print(f"{a} + {b} = {a + b}")
    case '-':
        print(f"{a} - {b} = {a - b}")
    case '*':
        print(f"{a} * {b} = {a * b}")
    case '/':
        if b == 0:
            print("Divide by 0 error.")
        else:
            print(f"{a} / {b} = {a / b}")
    case default:
        print("Incorrect operator.")
    
    
    # WAP which takes two integer operands and one operator from the user, performs the operation and then prints the result. Consider the operators +,-,*, /, % etc). Use switch cse. : python program

    
    