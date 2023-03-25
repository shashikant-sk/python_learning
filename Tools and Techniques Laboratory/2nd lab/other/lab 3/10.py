# WAP to convert a decimal number into its equivalent number with base b. Decimal number and b are the user input using function deference
# Assuming 2 <= b <= 9
def convert(n, b):
    rem = []
    while n:
        rem.append(n % b)
        n //= b
    rem.reverse()
    num = ''.join(map(str, rem))
    return num        
b = int(input("Enter base: "))
n = int(input(f"Enter number in decimal: "))
tempn = n
print(f"({tempn})10 = ({convert(n, b)}){b}")
    
