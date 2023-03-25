# WAP to print the Following pattern for n rows. Ex. for n=5 rows
#     *
#    * *
#   * * *
#  * * * *
# *	* *	* *
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(n - i + 1):
        print('', end=' ')
    for j in range(1, i + 1):
        print('*', end=' ')
    print('')