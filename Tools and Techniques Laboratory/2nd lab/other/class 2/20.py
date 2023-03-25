# WAP to form reverse pyramid of numbers for a given number Ex: n = 4 
# 1 2 3 4 3 2 1
# 1 2 3 2 1
# 1 2 1
# 1
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        print(f'{j}', end=' ')
    j = n - i
    while j > 0:
        print(f'{j}', end=' ')
        j -= 1
    print('')