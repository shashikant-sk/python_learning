# Original - Write a Python program to count frequency of elements in a list
# Edited - WAP to print elements and their frequencies in a given tuple
tup = tuple(map(int, input('Enter tuple elements: ').split()))
freq = {}
for i in tup:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(f'Frequency table of given tuple -> {freq}')