# WAP to print all odd and even numbers separately within a given range. The range is input through user by funvtion

def oddEven(n):
    if n == 0:
        return 0
    oddEven(n - 1)
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
  
n = int(input("Enter number to check odd or even: "))
oddEven(n)
     
        