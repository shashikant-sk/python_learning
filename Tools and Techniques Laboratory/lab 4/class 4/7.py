# Original - Write a Python program to count the occurrence of elements in a list
# Edited - WAP to find the most frequently occurring element in a list using dictionary
lis = list(map(int, input('Enter list elements: ').split()))
freq = {}
for i in lis:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
max_el = 0
max_freq = 0
for f in freq:
    if max_freq <= freq[f]:
        max_freq = freq[f]
        max_el = f
print(f'Most frequent element (frequency = {max_freq}) -> {max_el}')