# WAP to print the following pattern for n rows. Ex. for n=6 rows
# 1
# 0	1
# 1	0 1
# 0	1 0	1
# 1	0 1	0 1
# 0	1 0	1 0	1
n = int(input("Enter n: "))
for i in range(1, n + 1):
    num = 1
    if i & 1:
        num = 1
    else:
        num = 0
    for j in range(1, i + 1):
        print(f'{num}', end=' ')
        num += 1
        num %= 2
    print('')