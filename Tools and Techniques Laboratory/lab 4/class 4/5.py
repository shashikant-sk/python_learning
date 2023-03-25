# Original -  Write a Python program to find the maximum and minimum values in a set
# Edited - WAP to find the difference between max and min element in a set
set1 = set(map(int, input('Enter elements of set: ').split()))
print(f'Difference between max and min element = {list(set1)[-1] - list(set1)[0]}')