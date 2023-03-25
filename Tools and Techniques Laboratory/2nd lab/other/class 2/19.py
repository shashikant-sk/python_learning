# 19.WAP to print the following pattern for n rows. Ex. for n=5 rows
# 1
# 2	1		
# 1	2 3	
# 4	3 2	1	
# 1	2 3	4 5
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i & 1 == 0:
        num = i
        for j in range(1, i + 1):
            print(f'{num}', end=' ')
            num -= 1
    else:
        num = 1
        for j in range(1, i + 1):
            print(f'{num}', end=' ')
            num += 1
    print('')