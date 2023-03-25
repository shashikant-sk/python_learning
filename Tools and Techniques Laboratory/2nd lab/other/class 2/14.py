# WAP to sum the following series S=1+(1+2)+(1+2+3)+...+(1+2+3+...+n)
n = int(input("Enter n: "))
print("n terms of the series: ", end='')
for num in range(1, n + 1):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(f"{sum}", end=' ')