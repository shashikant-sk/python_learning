# Original - Write a Python program to print elements in ascending order of their frequency
# Edited - WAP to print elements in descending order of their frequency
lis = list(map(int, input('Enter list elements: ').split()))
freq = {}
for i in lis:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
revFreq = {}
ans = []
for f in freq:
    if freq[f] not in revFreq:
        revFreq[freq[f]] = [f]
    else:
        revFreq[freq[f]].append(f)
set1 = set()
for f in revFreq:
    set1.add(f)
for i in set1:
    for j in revFreq[i]:
        ans.append(j)
ans = list(reversed(ans))
print(f'Element in descending order of frequency: {ans}')