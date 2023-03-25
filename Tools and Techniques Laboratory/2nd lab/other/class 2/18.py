# WAP to print the following pattern for n rows. Ex. for n=5 rows
# A
# B A
# C B A
# D C B	A
# E D C	B A
n = int(input("Enter n: "))
for i in range(1, n + 1):
    num = chr(ord('A') + i - 1)
    for j in range(1, i + 1):
        print(f'{num}', end=' ')
        num = chr(ord(num) - 1)
    print('')