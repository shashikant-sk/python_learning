# WAP to print the series as 1 3 7 15 31 ........, where n is given by user.
n = int(input("Enter n: "))
print("n terms of the series: ", end='')
for num in range(1, n):
    print(f"{2 ** num - 1}", end=' ')