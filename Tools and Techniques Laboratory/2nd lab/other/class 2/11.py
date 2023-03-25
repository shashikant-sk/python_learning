# WAP to find the first n numbers of a Fibonacci sequence.
n = int(input("Enter n: "))
f = 1
s = 1
if n == 1:
    print('1')
elif n == 2:
    print('1 1')
else:
    n -= 2
    print('1 1', end=' ')
    while n != 0:
        print(f'{f + s}', end=' ')
        sum = f + s
        s = f
        f = sum
        n -= 1