# Original - Write a Python program to remove the intersection of a second set with a first set
# Edited - WAP to find the intersection of 2 sets
set1 = set(map(int, input('Enter elements in first set: ').split()))
set2 = set(map(int, input('Enter elements in first set: ').split()))
ans = set([])
for i in set1:
    if i in set2:
        ans.add(i)
print(f'Intersection of {set1} and {set2} => {ans}')