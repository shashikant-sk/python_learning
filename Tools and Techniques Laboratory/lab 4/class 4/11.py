# Original - Write a Python program to change each tuple element by adding 1 to them
# Edited - WAP to print tuple elements after changing them to square of themselves
tup = tuple(map(int, input('Enter tuple elements: ').split()))
newTup = ()
for i in tup:
    newTup = newTup + tuple([i ** 2])
print(f'Old Tuple -> {tup}')
print(f'New Tuple -> {newTup}')
