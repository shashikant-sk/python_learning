# Original - Write a Python program to remove all tuples from a list of tuples whose length is k
# Edited - WAP to remove all tuples from a list of tuples whose length is greater than equal to k
listOfTuples = []
n = int(input('Enter number of tuples: '))
k = int(input('Enter k: '))
for i in range(n):
    listOfTuples.append(
        tuple(map(int, input(f'Enter elements of tuple {i + 1}: ').split())))
newListOfTuples = []
for tup in listOfTuples:
    if len(tup) < k:
        newListOfTuples.append(tup)
print(f'Old list of tuples -> {listOfTuples}')
print(f'New list of tuples -> {newListOfTuples}')
