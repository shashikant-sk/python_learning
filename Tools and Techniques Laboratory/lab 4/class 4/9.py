# Original - Write a Python program to print elements with frequency more than k
# Edited - WAP to remove all elements from a list having frequency more than equal to k and print the final list
lis = list(map(int, input('Enter list elements: ').split()))
k = int(input('Enter k: '))
freq = {}
for i in lis:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
ans = []
for i in lis:
    if freq[i] >= k:
        continue
    ans.append(i)
print(f'Element with frequency < {k}: {ans}')
