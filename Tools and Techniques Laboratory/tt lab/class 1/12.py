# Test whether number is odd or even
a = int(input("Enter number: "))
if a & 1:
    print(f"{a} is odd.")
else:
    print(f"{a} is even.")